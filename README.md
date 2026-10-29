<p align="right">
  <b>🇨🇳 简体中文</b> | <a href="README_EN.md">🇬🇧 English</a>
</p>

# OctPc - 海量点云高性能八叉树转换工具与三维交互浏览器

[![GitHub release](https://img.shields.io/github/v/release/HonghuangKongJian/OctPc-Release?color=brightgreen&label=最新版本)](https://github.com/HonghuangKongJian/OctPc-Release/releases)
[![Capacity](https://img.shields.io/badge/单工程承载-21%20亿点-orange.svg)]()
[![Performance](https://img.shields.io/badge/视口漫游-60%20FPS%20丝滑流畅-blue.svg)]()
[![Test Data](https://img.shields.io/badge/配套测试集-5000万点%20人形点云-green.svg)]()
[![SDK](https://img.shields.io/badge/开发者SDK-即将推出-blueviolet.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20x64-lightgrey.svg)]()
[![Sponsor](https://img.shields.io/badge/☕-赞赏支持-rose.svg)](#-赞赏与支持-sponsor)

> 🚀 **单工程支持高达 21 亿个点（2.1 Billion Points）流畅漫游浏览！**  
> 彻底告别卡顿与崩溃，普通办公电脑与笔记本亦可畅享海量点云极致交互。

**OctPc** 是一套面向超大规模激光雷达点云（LAS/LAZ）的现代高性能八叉树处理与三维交互可视化技术栈。采用自研高性能线性八叉树拓扑与多核空间分块调度算法，彻底攻克亿级点云导入耗时长、显存开销大、视口顿挫严重的行业难题，实现极速转换与毫秒级秒开满帧渲染。

---

## 🌟 核心特性与亮点

- 🏆 **21 亿点超大容量支持，60fps 丝滑漫游**：
  - 底层基于 64 位文件寻址架构与自适应 PagedLOD 多级视锥分块调度技术，**单工程实装承载上限高达 21.47 亿点**；
  - 无论点云总体量多大，前台仅按视距动态吞吐当前可见点，**常驻内存与显存仅需数百兆**，实现 60 帧满帧流畅飞行动作与自由漫游；
- ⚡ **多核并行极速转换 (octpc_cli)**：
  - 基于多核并发空间分块与 16MB 连续写缓冲机制，处理速度相比传统工具提速数倍；
- 📦 **免安装绿色便携**：
  - 解压即用，内置轻量运行库与高清中文字体，无需安装庞杂的第三方 SDK 环境；
- 🎯 **原生文件交互与格式自动联动 (octpc_viewer)**：
  - 启动时自动唤起 Windows 原生文件浏览对话框，首选 `.octpc` 格式；
  - 打开原始 `.las` 文件时自动匹配同级 `.octpc`，未找到时自动调起后台转换并直接呈现；
  - 运行中随时按 `[F3]` 即可选择新点云并平滑无缝切换；
- 🎨 **多维度科学赋色**：
  - 原始 RGB 真彩色、激光反射强度灰度、语义分类颜色及高程动态渐变色带一键自由切换；
- 🌐 **原生中英双语支持 (Bilingual Ready)**：
  - 全套程序（`octpc_cli` 与 `octpc_viewer`）及文档均已原生支持中英双语；
  - 自动根据操作系统语言环境匹配界面与控制台帮助；
  - 支持命令行参数显式指定（`--lang en` / `--lang zh`）；
  - 3D 视口内随时按下 `[L]` 键可在中文与英文 HUD 状态栏之间无缝切换。

---

## 🔌 第三方客户程序无缝集成指南 (Zero-Code 插件与工具集成)

无论是研发全新的测绘/GIS/数字孪生系统，还是为已有的行业三维软件扩展海量点云浏览功能，OctPc 均提供了极简的直接集成方案，**客户现有主程序无需重新编译即可直接使用**：

### 模式一：三维宿主系统零重编译即插即用 (OSG 插件方式)

若客户已有基于 OpenSceneGraph (OSG) 的三维应用程序：

#### 步骤 1：部署插件动态库
将发布包中的 `osgdb_octpc.dll` 直接拷贝至客户软件运行目录下的 `osgPlugins-3.x.x/` 插件子目录（或与客户主程序 `.exe` 同目录）。

#### 步骤 2：一行代码直接加载渲染
客户程序无需改动原有渲染管线，直接使用 OSG 标准接口：
```cpp
#include <osgDB/ReadFile>

// 1. 直接加载 .octpc 八叉树点云（OSG 插件自动接管分页多分辨率调度）
osg::ref_ptr<osg::Node> pointCloud = osgDB::readNodeFile("D:/data/survey.octpc");

// 2. 将节点加入三维场景总根节点
rootGroup->addChild(pointCloud.get());
```

#### 步骤 3（可选）：动态传参控制着色模式与视距
通过 OSG 标准 `ReaderWriter::Options`，主程序可自由控制渲染参数：
```cpp
osg::ref_ptr<osgDB::ReaderWriter::Options> options = new osgDB::ReaderWriter::Options();
// 显示模式：0-原始RGB, 1-激光反射强度, 2-分类颜色, 4-高程动态色带
options->setPluginStringData("TD_PcDisplayMode", "1");
// LOD细化视距灵敏度倍率（默认 40.0）
options->setPluginStringData("TD_PcDisplayDistRatio", "40.0");

osg::ref_ptr<osg::Node> pointCloud = osgDB::readNodeFile("D:/data/survey.octpc", options.get());
```

---

### 模式二：业务系统自动化格式转换 (CLI 进程级集成)

若客户使用的是 C# (WPF/WinForm)、Qt、Python、Electron 等业务软件，可将 `octpc_cli.exe` 放入软件安装目录作为后台无头引擎调用：

#### C# / .NET 集成示例：
```csharp
var process = new Process();
process.StartInfo.FileName = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "octpc_cli.exe");
process.StartInfo.Arguments = "\"D:\\data\\input.las\" -d 5"; // -d 5 指定5层八叉树
process.StartInfo.CreateNoWindow = true;
process.StartInfo.UseShellExecute = false;
process.Start();
process.WaitForExit();

// 转换完成，生成的同名 D:\data\input.octpc 即可由渲染器接管
```

#### Python 集成示例：
```python
import subprocess
import os

# 后台静默调用八叉树转换
cmd = ["octpc_cli.exe", "D:/data/input.las", "-d", "5"]
subprocess.run(cmd, check=True)
print("转换成功，生成 D:/data/input.octpc")
```

---

## 🧪 测试点云生成工具 (5000 万点高精度人形模型)

如果您手头没有现成的大体量激光点云数据，本项目贴心配套了千万级点云生成脚本 `generate_humanoid.py`：
- 可一键快速生成包含真实 RGB 色彩、反射强度与各部位语义分类的 **5000 万点 3D 彩色人形点云 (`humanoid_50M.las`)**；
- **运行命令**：
  ```bash
  python generate_humanoid.py -n 50000000 -o humanoid_50M.las
  ```
- 生成完成后，直接双击 `run_viewer.bat` 选择或拖拽该 `humanoid_50M.las`，即可亲身体验千万级大点云在数秒内自动构建与 60fps 满帧浏览！

---

## 🧩 二次开发与 SDK 支持规划 (Roadmap)

- **开发者 SDK 即将推出**：团队正在对底层核心能力进行标准化抽象封装，**后期将正式面向开发者与行业生态提供标准的 SDK 调用支持**；
- **典型赋能场景**：
  - 轻松嵌入 GIS 平台、无人机航测后处理软件、数字孪生/BIM 引擎、CASS 等三维测绘测量系统；
  - 提供海量点云自定义构建、空间索引查询、快速降采样抽稀与定制视口嵌入能力；
- **早期技术合作**：如有提前试用或深度业务集成需求，欢迎通过下方技术邮箱与作者取得联系。

---

## 📊 数据规模与性能承载规格表

| 点云规模 | 典型数据源 | 转换耗时参考 | 视口漫游帧率 | 内存 / 显存开销 |
| :--- | :--- | :--- | :--- | :--- |
| **1,000 万 ~ 5,000 万点** | 无人机航测、人形点云测试集 | ~3 秒内 | **60 FPS** 满帧极速 | < 150 MB |
| **1 亿 ~ 3 亿点** | 车载移动测量、城市级倾斜航测 | ~20 秒 | **60 FPS** 满帧丝滑 | ~300 MB |
| **5 亿 ~ 10 亿点** | 区域级激光雷达测绘大场景 | ~1~2 分钟 | **60 FPS** 流畅漫游 | ~500 MB |
| **最高 21.47 亿点** | 特大型国家级/全流域空间点云工程 | 支持稳定构建 | **60 FPS** 动态多级调度 | 分页受控按需调度 |

---

## 📦 软件包下载

请前往 👉 **[Releases 页面](https://github.com/HonghuangKongJian/OctPc-Release/releases)** 下载最新发布版：

| 分发包名称 | 体积 | 推荐适用场景 |
| :--- | :--- | :--- |
| **`octpc_suite_vX.X.zip`** | **约 2.9 MB** | **【推荐】一体化完整绿色套件**。内含三维查看器、格式转换工具、完整动态链接库及便捷启动脚本，解压即用。 |
| **`octpc_cli_vX.X.zip`** | **约 230 KB** | **独立命令行转换工具精简版**。极度轻量，专供服务器端后台批处理或嵌入数据生产流水线。 |

---

## 🚀 快速上手使用

### 方式一：三维交互查看器 (OctPc Viewer)
1. 下载解压 `octpc_suite_vX.X.zip`；
2. 双击运行 **`run_viewer.bat`** 或 **`octpc_viewer.exe`**；
3. 在弹出的文件选择器中选中您的 `.octpc` 或 `.las` 文件即可浏览。

### 方式二：命令行格式转换 (OctPc CLI)
在控制台或脚本中执行：
```powershell
# 基础转换（默认 5 层八叉树深度）
octpc_cli.exe D:\data\survey.las

# 指定最大层数并强制覆盖已有文件
octpc_cli.exe D:\data\survey.las -d 6 -f
```

---

## ⌨️ 查看器快捷键操作指南

| 按键 / 操作 | 功能说明 |
| :--- | :--- |
| **鼠标左键拖拽** | 三维轨道球旋转 |
| **鼠标滚轮** | 视角推拉缩放 |
| **空格键 [Space]** | 快速将相机居中对齐到点云中心 |
| **[1] / [2]** | 切换为【原始 RGB 真彩】 / 【激光反射强度】模式 |
| **[3] / [4]** | 切换为【点云分类赋色】 / 【高程动态色带】模式 |
| **[+] / [-]** | 实时放大 / 缩小点渲染尺寸（Point Size） |
| **[ [ ] / [ ] ]** | 增减 LOD 视距加载灵敏度倍率 |
| **[F3]** | 弹出文件选择器，打开新点云文件并无缝切换 |
| **[B]** | 循环切换视口背景色（深灰黑 / 纯黑 / 藏青夜空 / 浅灰白） |
| **[H]** | 开启 / 关闭屏幕左上角帮助与状态 HUD 抬头面板 |
| **[L]** | 实时切换界面中英双语 (中 ⇄ 英) |
| **[O] 或 [F1]** | 打开官方技术主页 |
| **[M] 或 [F2]** | 发送技术支持与反馈邮件 |

---

## 📄 数据格式规范说明

输入 `filename.las` 经转换后将生成规范的标准产物：
1. **`filename.octpc`**：八叉树拓扑主索引文件（包围盒、全局空间偏移、属性标志位与节点位置映射）；
2. **`filename.octlod`**：多级分辨率空间采样快速预览缓存文件；
3. **`filename_oct.las`**：空间局部性优化重排后的点云几何实体文件。

---

## 🌐 官方支持与联系

- **官方技术主页**：[https://amw3.eu.org](https://amw3.eu.org)
- **技术支持邮箱**：[19053936@qq.com](mailto:19053936@qq.com)
- **问题反馈与建议**：欢迎在 [GitHub Issues](https://github.com/HonghuangKongJian/OctPc-Release/issues) 中提交数据格式兼容性反馈。
- **开源许可证**：[MIT License](LICENSE)

---

## ☕ 赞赏与支持 (Sponsor)

如果您觉得 **OctPc** 对您的工作、学习、科学研究或数字孪生/GIS工程开发有所帮助，欢迎赞赏支持作者！您的每一份鼓励都是我们持续演进八叉树算法、提升吞吐性能与坚持开源免费的最大动力！

<div align="center">
  <table>
    <tr>
      <td align="center" width="320">
        <a href="https://amw3.eu.org">
          <img src="docs/images/wechat-reward.png" width="220" alt="微信赞赏码" />
        </a>
        <br/>
        <b>🟢 微信赞赏支持</b>
        <br/>
        <sub>打开手机微信扫一扫</sub>
      </td>
      <td align="center" width="320">
        <a href="https://amw3.eu.org">
          <img src="docs/images/alipay-reward.png" width="220" alt="支付宝收款码" />
        </a>
        <br/>
        <b>🔵 支付宝收款支持</b>
        <br/>
        <sub>打开手机支付宝扫一扫</sub>
      </td>
    </tr>
  </table>
  <br/>
  <p>
    🌐 <b>洪荒空间门户矩阵</b>：<a href="https://amw3.eu.org">https://amw3.eu.org</a><br/>
    📧 <b>联系与技术交流邮箱</b>：<a href="mailto:19053936@qq.com">19053936@qq.com</a>
  </p>
</div>
