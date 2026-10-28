import numpy as np
import struct
import time
import os
import argparse

def generate_humanoid_las(output_path, total_points=50_000_000):
    print(f"=========================================================")
    print(f"  OctPc 3D 人形点云生成器")
    print(f"  目标点数: {total_points:,} 点")
    print(f"  输出路径: {output_path}")
    print(f"=========================================================")
    t0 = time.time()
    
    # 人体各部位比例分配
    n_head = int(total_points * 0.14)
    n_torso = int(total_points * 0.30)
    n_arm = int(total_points * 0.10)   # 单臂
    n_leg = int(total_points * 0.16)   # 单腿
    n_foot = int(total_points * 0.02)  # 单脚
    # 动态补偿余数，保证总点数严格等于 total_points
    n_torso = total_points - (n_head + 2 * n_arm + 2 * n_leg + 2 * n_foot)
    
    scale = 0.0001 # 0.1 毫米精度
    
    min_x, max_x = float('inf'), float('-inf')
    min_y, max_y = float('inf'), float('-inf')
    min_z, max_z = float('inf'), float('-inf')

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    f = open(output_path, "wb")
    f.seek(227) # 预留 LAS 1.2 标准头部空间
    
    def write_chunk(x, y, z, r, g, b, intensity=None):
        nonlocal min_x, max_x, min_y, max_y, min_z, max_z
        count = len(x)
        if count == 0:
            return
        min_x = min(min_x, float(np.min(x)))
        max_x = max(max_x, float(np.max(x)))
        min_y = min(min_y, float(np.min(y)))
        max_y = max(max_y, float(np.max(y)))
        min_z = min(min_z, float(np.min(z)))
        max_z = max(max_z, float(np.max(z)))
        
        xi = (x / scale).astype(np.int32)
        yi = (y / scale).astype(np.int32)
        zi = (z / scale).astype(np.int32)
        
        if intensity is None:
            intensity = np.clip((r.astype(np.float32)*0.299 + g.astype(np.float32)*0.587 + b.astype(np.float32)*0.114), 0, 255).astype(np.uint16) * 100
        else:
            intensity = intensity.astype(np.uint16)
            
        r16 = (r.astype(np.uint16) * 257)
        g16 = (g.astype(np.uint16) * 257)
        b16 = (b.astype(np.uint16) * 257)
        
        dtype = np.dtype([
            ('x', '<i4'),
            ('y', '<i4'),
            ('z', '<i4'),
            ('intensity', '<u2'),
            ('flags', 'u1'),
            ('classification', 'u1'),
            ('angle', 'i1'),
            ('user_data', 'u1'),
            ('point_source_id', '<u2'),
            ('red', '<u2'),
            ('green', '<u2'),
            ('blue', '<u2')
        ])
        
        arr = np.empty(count, dtype=dtype)
        arr['x'] = xi
        arr['y'] = yi
        arr['z'] = zi
        arr['intensity'] = intensity
        arr['flags'] = 1
        arr['classification'] = 2
        arr['angle'] = 0
        arr['user_data'] = 0
        arr['point_source_id'] = 1
        arr['red'] = r16
        arr['green'] = g16
        arr['blue'] = b16
        
        f.write(arr.tobytes())

    # 1. 头部与颈部
    print(f"-> 正在生成头部与颈部 ({n_head:,} 点)...")
    is_neck = np.random.rand(n_head) < 0.15
    z_neck = np.random.uniform(1.48, 1.56, np.sum(is_neck))
    theta_neck = np.random.uniform(0, 2*np.pi, np.sum(is_neck))
    r_neck = 0.065 + np.random.uniform(-0.001, 0.001, len(z_neck))
    x_neck = r_neck * np.cos(theta_neck)
    y_neck = r_neck * np.sin(theta_neck)
    write_chunk(x_neck, y_neck, z_neck, 
                np.full(len(z_neck), 235, dtype=np.uint8), 
                np.full(len(z_neck), 190, dtype=np.uint8), 
                np.full(len(z_neck), 165, dtype=np.uint8))

    n_h = n_head - np.sum(is_neck)
    theta_h = np.random.uniform(0, 2*np.pi, n_h)
    phi_h = np.random.uniform(-np.pi/2, np.pi/2, n_h)
    dr_h = 1.0 + np.random.uniform(-0.002, 0.002, n_h)
    xh = 0.095 * np.cos(phi_h) * np.sin(theta_h) * dr_h
    yh = 0.02 + 0.11 * np.cos(phi_h) * np.cos(theta_h) * dr_h
    zh = 1.68 + 0.12 * np.sin(phi_h) * dr_h
    
    is_hair = (zh > 1.69) | (yh < 0.01)
    rc_h = np.where(is_hair, 35, 240).astype(np.uint8)
    gc_h = np.where(is_hair, 28, 195).astype(np.uint8)
    bc_h = np.where(is_hair, 22, 170).astype(np.uint8)
    write_chunk(xh, yh, zh, rc_h, gc_h, bc_h)

    # 2. 躯干（运动夹克）
    print(f"-> 正在生成躯干衣服 ({n_torso:,} 点)...")
    chunk_size = 5_000_000
    torso_rem = n_torso
    while torso_rem > 0:
        cur_n = min(chunk_size, torso_rem)
        zt = np.random.uniform(0.82, 1.48, cur_n)
        theta_t = np.random.uniform(0, 2*np.pi, cur_n)
        dr_t = 1.0 + np.random.uniform(-0.002, 0.002, cur_n)
        
        h_norm = (zt - 0.82) / (1.48 - 0.82)
        wx = 0.17 + 0.08 * (h_norm - 0.3)**2 + 0.03 * h_norm
        wy = 0.11 + 0.02 * np.sin(h_norm * np.pi)
        
        xt = wx * np.cos(theta_t) * dr_t
        yt = wy * np.sin(theta_t) * dr_t
        
        brightness = (0.7 + 0.3 * np.cos(theta_t)).clip(0.5, 1.0)
        rc_t = np.clip(35 * brightness, 0, 255).astype(np.uint8)
        gc_t = np.clip(95 * brightness, 0, 255).astype(np.uint8)
        bc_t = np.clip(185 * brightness, 0, 255).astype(np.uint8)
        
        is_zipper = (np.abs(xt) < 0.006) & (yt > 0.05)
        rc_t[is_zipper] = 220
        gc_t[is_zipper] = 220
        bc_t[is_zipper] = 230
        
        write_chunk(xt, yt, zt, rc_t, gc_t, bc_t)
        torso_rem -= cur_n

    # 3. 双臂双手
    print(f"-> 正在生成双臂双手 ({2 * n_arm:,} 点)...")
    for side in [-1, 1]:
        arm_rem = n_arm
        while arm_rem > 0:
            cur_n = min(chunk_size, arm_rem)
            t = np.random.uniform(0, 1, cur_n)
            theta_a = np.random.uniform(0, 2*np.pi, cur_n)
            dr_a = 1.0 + np.random.uniform(-0.002, 0.002, cur_n)
            
            # 臂部骨骼中心线: 从 (side*0.22, 0, 1.42) 到 (side*0.37, 0, 0.78)
            cx = side * (0.22 + 0.15 * t)
            cy = 0.0 + 0.02 * np.sin(t * np.pi)
            cz = 1.42 - 0.64 * t
            
            r_arm = np.where(t < 0.75, 0.055 - 0.02 * t, 0.035 + 0.015 * np.sin((t-0.75)/0.25 * np.pi))
            xa = cx + r_arm * np.cos(theta_a) * dr_a
            ya = cy + r_arm * np.sin(theta_a) * dr_a
            za = cz
            
            is_sleeve = t < 0.45
            rc_a = np.where(is_sleeve, 35, 235).astype(np.uint8)
            gc_a = np.where(is_sleeve, 95, 190).astype(np.uint8)
            bc_a = np.where(is_sleeve, 185, 165).astype(np.uint8)
            
            write_chunk(xa, ya, za, rc_a, gc_a, bc_a)
            arm_rem -= cur_n

    # 4. 双腿裤子
    print(f"-> 正在生成双腿裤子 ({2 * n_leg:,} 点)...")
    for side in [-1, 1]:
        leg_rem = n_leg
        while leg_rem > 0:
            cur_n = min(chunk_size, leg_rem)
            t = np.random.uniform(0, 1, cur_n)
            theta_l = np.random.uniform(0, 2*np.pi, cur_n)
            dr_l = 1.0 + np.random.uniform(-0.002, 0.002, cur_n)
            
            cx = side * (0.095 - 0.01 * t)
            cy = 0.01 * np.sin(t * np.pi)
            cz = 0.82 - 0.74 * t
            
            r_leg = 0.075 - 0.02 * t
            xl = cx + r_leg * np.cos(theta_l) * dr_l
            yl = cy + r_leg * np.sin(theta_l) * dr_l
            zl = cz
            
            rc_l = np.full(cur_n, 42, dtype=np.uint8)
            gc_l = np.full(cur_n, 50, dtype=np.uint8)
            bc_l = np.full(cur_n, 78, dtype=np.uint8)
            
            write_chunk(xl, yl, zl, rc_l, gc_l, bc_l)
            leg_rem -= cur_n

    # 5. 双脚鞋子
    print(f"-> 正在生成双脚鞋子 ({2 * n_foot:,} 点)...")
    for side in [-1, 1]:
        foot_rem = n_foot
        while foot_rem > 0:
            cur_n = min(chunk_size, foot_rem)
            theta_f = np.random.uniform(0, 2*np.pi, cur_n)
            phi_f = np.random.uniform(-np.pi/2, np.pi/2, cur_n)
            dr_f = 1.0 + np.random.uniform(-0.002, 0.002, cur_n)
            
            xf = side * 0.09 + 0.045 * np.cos(phi_f) * np.sin(theta_f) * dr_f
            yf = 0.035 + 0.12 * np.cos(phi_f) * np.cos(theta_f) * dr_f
            zf = 0.04 + 0.035 * np.sin(phi_f) * dr_f
            
            is_sole = zf < 0.018
            rc_f = np.where(is_sole, 200, 25).astype(np.uint8)
            gc_f = np.where(is_sole, 200, 25).astype(np.uint8)
            bc_f = np.where(is_sole, 205, 30).astype(np.uint8)
            
            write_chunk(xf, yf, zf, rc_f, gc_f, bc_f)
            foot_rem -= cur_n

    # 写入 LAS 1.2 头部信息
    print("-> 正在写入 LAS 1.2 头部元数据...")
    f.seek(0)
    
    header = bytearray(227)
    header[0:4] = b"LASF"
    header[24] = 1
    header[25] = 2
    header[26:58] = "OctPc Humanoid Generator".encode('ascii').ljust(32, b'\x00')
    header[58:90] = "OctPc v2.0".encode('ascii').ljust(32, b'\x00')
    struct.pack_into("<H", header, 94, 227)
    struct.pack_into("<I", header, 96, 227)
    struct.pack_into("<I", header, 100, 0)
    header[104] = 2 # Format 2: RGB + Intensity
    struct.pack_into("<H", header, 105, 26)
    struct.pack_into("<I", header, 107, total_points)
    struct.pack_into("<I", header, 111, total_points)
    struct.pack_into("<ddd", header, 131, scale, scale, scale)
    struct.pack_into("<ddd", header, 155, 0.0, 0.0, 0.0)
    struct.pack_into("<dddddd", header, 179, max_x, min_x, max_y, min_y, max_z, min_z)
    
    f.write(header)
    f.close()
    
    elapsed = time.time() - t0
    filesize_mb = os.path.getsize(output_path) / (1024 * 1024)
    print(f"=========================================================")
    print(f"  生成成功！总耗时: {elapsed:.2f} 秒")
    print(f"  文件路径: {output_path}")
    print(f"  文件大小: {filesize_mb:.2f} MB")
    print(f"  三维空间范围: X[{min_x:.3f}, {max_x:.3f}], Y[{min_y:.3f}, {max_y:.3f}], Z[{min_z:.3f}, {max_z:.3f}]")
    print(f"=========================================================")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OctPc 3D 人形点云批量生成工具")
    parser.add_argument("-n", "--points", type=int, default=50_000_000, help="生成点数 (默认: 50,000,000)")
    parser.add_argument("-o", "--out", type=str, default=r"D:\work\las\humanoid\humanoid_50M.las", help="输出 LAS 文件路径")
    args = parser.parse_args()
    
    generate_humanoid_las(args.out, total_points=args.points)
