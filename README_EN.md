<p align="right">
  <a href="README.md">🇨🇳 简体中文</a> | <b>🇬🇧 English</b>
</p>

# OctPc - High-Performance Point Cloud Octree Indexing Suite & 3D Interactive Viewer

[![GitHub release](https://img.shields.io/github/v/release/HonghuangKongJian/OctPc-Release?color=brightgreen&label=Release%20v3.0.0)](https://github.com/HonghuangKongJian/OctPc-Release/releases)
[![Format](https://img.shields.io/badge/Format-64--bit%20V2-emerald.svg)](https://amw3.eu.org)
[![Capacity](https://img.shields.io/badge/Capacity-Billion--scale-orange.svg)]()
[![Performance](https://img.shields.io/badge/Viewport_Roaming-60_FPS_Smooth-blue.svg)]()
[![Test Data](https://img.shields.io/badge/Test_Dataset-50M_Humanoid_Pts-green.svg)]()
[![SDK](https://img.shields.io/badge/Developer_SDK-Ready-blueviolet.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20x64-lightgrey.svg)]()
[![Sponsor](https://img.shields.io/badge/☕-Sponsor-rose.svg)](#-sponsor--support)

> 🚀 **Single project handles up to Billion-scale points with smooth 60 FPS roaming!**  
> Brand new 64-bit spatial addressing architecture and V2 topology break through the historical 2.1-billion-point limitation, enabling massive point cloud visualization even on ordinary office PCs and laptops.

**OctPc** is a modern, high-performance technology stack for ultra-large-scale LiDAR point clouds (LAS/LAZ). Built upon an in-house linear octree topology and multi-core spatial partitioning, it eliminates long import waits, high GPU memory overhead, and viewport frame drops, delivering blazing-fast spatial conversion and millisecond-level instant 60 FPS streaming rendering.

---

## 🌟 Key Features & Highlights

- 🏆 **Billion-Scale Point Cloud Capacity with 64-bit V2 Format**:
  - Full architectural upgrade to 64-bit file offset addressing, breaking the 2.14-billion-point limit (2^31-1) with native multi-billion point cloud support; backward compatible with V1 format;
  - Front-end streams only visible points dynamically via PagedLOD frustum culling, maintaining a resident memory footprint of just a few hundred megabytes for silky 60 FPS flights.
- 🌐 **Full-Stack Native Bilingual Support (Zh / En)**:
  - Both `octpc_cli` and `octpc_viewer` support Chinese and English with automatic OS locale detection;
  - Command-line flags `--lang en` and `--lang zh` supported;
  - Press `[L]` anytime in the 3D viewport to toggle the HUD language seamlessly.
- ⚡ **Multi-Core High-Speed Conversion (`octpc_cli`)**:
  - Achieves **8~10 Million Points/sec** spatial index throughput using multi-core space partitioning and 16MB contiguous write buffering.
- 📦 **Zero-Dependency Portable Distribution**:
  - Pure green standalone architecture completely free from PCL, Boost, Eigen, or MFC (~2.9 MB total size).
- 🎯 **Seamless File Interaction & Auto-Conversion (`octpc_viewer`)**:
  - Automatically invokes native Windows file dialogs;
  - Seamlessly triggers background conversion when opening raw `.las` files;
  - Press `[F3]` anytime to switch point clouds smoothly.
- 🎨 **Multi-Dimensional Color Rendering**:
  - Instant one-click switching between True Color RGB, Intensity Grayscale, Semantic Classification, and Elevation Color Ramp.

---

## 🔌 Zero-Code Third-Party System Integration Guide

Whether you are developing a new GIS/Digital Twin system or extending massive point cloud browsing in existing 3D software, OctPc provides seamless integration:

### Mode 1: OSG Dynamic Driver Plugin (Zero Recompilation)

For applications based on OpenSceneGraph (OSG):

#### Step 1: Deploy Plugin DLL
Copy `osgdb_octpc.dll` to your application's `osgPlugins-3.x.x/` folder or working directory.

#### Step 2: One-Line Loading via Standard API
```cpp
#include <osgDB/ReadFile>

// 1. Directly load .octpc octree point cloud (PagedLOD auto-scheduled)
osg::ref_ptr<osg::Node> pointCloud = osgDB::readNodeFile("D:/data/survey.octpc");

// 2. Attach node to the root scene graph
rootGroup->addChild(pointCloud.get());
```

#### Step 3 (Optional): Dynamic Options Control
```cpp
osg::ref_ptr<osgDB::ReaderWriter::Options> options = new osgDB::ReaderWriter::Options();
// Render Mode: 0-RGB, 1-Intensity, 2-Classification, 4-Elevation
options->setPluginStringData("TD_PcDisplayMode", "1");
// LOD Distance Multiplier (default: 40.0)
options->setPluginStringData("TD_PcDisplayDistRatio", "40.0");

osg::ref_ptr<osg::Node> pointCloud = osgDB::readNodeFile("D:/data/survey.octpc", options.get());
```

---

### Mode 2: Headless CLI Process Integration

For C# (WPF/WinForm), Qt, Python, or Electron applications, `octpc_cli.exe` can be invoked as a background engine:

#### C# / .NET Example:
```csharp
var process = new Process();
process.StartInfo.FileName = Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "octpc_cli.exe");
process.StartInfo.Arguments = "\"D:\\data\\input.las\" -d 5 --lang en";
process.StartInfo.CreateNoWindow = true;
process.StartInfo.UseShellExecute = false;
process.Start();
process.WaitForExit();
```

#### Python Example:
```python
import subprocess

cmd = ["octpc_cli.exe", "D:/data/input.las", "-d", "5", "--lang", "en"]
subprocess.run(cmd, check=True)
print("Conversion completed: D:/data/input.octpc")
```

---

## 📦 Package Downloads

Please visit 👉 **[Releases](https://github.com/HonghuangKongJian/OctPc-Release/releases)** to download:

| Package | Size | Description |
| :--- | :--- | :--- |
| **`octpc_suite_v3.0.0.zip`** | **~2.9 MB** | **[Recommended] All-in-One Portable Suite**. Contains 3D viewer, converter CLI, complete DLLs and launcher scripts. |
| **`octpc_cli_v3.0.0.zip`** | **~240 KB** | **Standalone CLI Converter**. Ultra-lightweight headless engine for server batching and data pipelines. |

---

## ⌨️ 3D Viewer Interactive Hotkeys

| Hotkey / Action | Description |
| :--- | :--- |
| **Left Drag** | 3D orbital trackball rotation |
| **Mouse Wheel** | Viewport distance zooming |
| **Space** | Reset camera viewpoint to point cloud center |
| **[1] / [2]** | Switch to [Original RGB] / [Intensity Grayscale] |
| **[3] / [4]** | Switch to [Classification Colors] / [Elevation Ramp] |
| **[+] / [-]** | Increase / decrease point rendering size |
| **[ [ ] / [ ] ]** | Adjust LOD distance ratio multiplier |
| **[F3]** | Open file dialog to load another point cloud |
| **[B]** | Cycle background color (Dark / Black / Navy / Light) |
| **[H]** | Toggle HUD overlay status and shortcut panel |
| **[L]** | **Toggle interface language in real time (Chinese ⇄ English)** |
| **[O] or [F1]** | Open official technology homepage |
| **[M] or [F2]** | Send support & feedback email |

---

## 📄 File Format Specifications

Processing an input `filename.las` generates:
1. **`filename.octpc`**: Master 64-bit V2 octree index file (bounding box, global offsets, property flags, node offset map);
2. **`filename.octlod`**: Multi-resolution spatial downsampled LOD preview cache;
3. **`filename_oct.las`**: Geometry data reordered along linear space-filling curve.

---

## 📝 Release History (Changelog)

### v3.0.0 (Latest)
- 🚀 **New 64-bit V2 Topology**: Completely refactored octree index addressing to 64-bit integers, smashing the 2.14-billion-point ceiling with multi-billion point cloud capacity; full backward compatibility with V1 format;
- 🌐 **Full-Stack Native Bilingual Support**: `octpc_cli` and `octpc_viewer` auto-adapt to OS locale; CLI `--lang zh/en` flag, Viewer `[L]` hotkey for instant bilingual toggle;
- ⚡ **Enhanced Viewport Interaction**: Tuned dynamic LOD culling curve and added real-time hotkeys;
- 📦 **Dual Packaging**: All-in-one suite (`octpc_suite_v3.0.0.zip`) & standalone CLI (`octpc_cli_v3.0.0.zip`).

### v2.0.0
- 📦 **All-in-One Portable Suite**: Merged standalone packages into a single zero-dependency suite;
- 🎨 **Multi-Dimensional Coloring & Dialogs**: True Color RGB, Intensity, Classification and Elevation ramp modes.

---

## 🌐 Official Portal & Support

- **Official Portal**: [https://amw3.eu.org](https://amw3.eu.org)
- **Technical Support Email**: [19053936@qq.com](mailto:19053936@qq.com)
- **Feedback & Issues**: Welcome to open tickets on [GitHub Issues](https://github.com/HonghuangKongJian/OctPc-Release/issues).
- **License**: [MIT License](LICENSE)

---

## ☕ Sponsor & Support

If OctPc assists your research, digital twin engineering, or GIS projects, we welcome your sponsorship!

<div align="center">
  <table>
    <tr>
      <td align="center" width="320">
        <a href="https://amw3.eu.org">
          <img src="docs/images/wechat-reward.png" width="220" alt="WeChat Pay Reward" />
        </a>
        <br/>
        <b>🟢 WeChat Pay Sponsor</b>
        <br/>
        <sub>Scan with WeChat app</sub>
      </td>
      <td align="center" width="320">
        <a href="https://amw3.eu.org">
          <img src="docs/images/alipay-reward.png" width="220" alt="Alipay Reward" />
        </a>
        <br/>
        <b>🔵 Alipay Sponsor</b>
        <br/>
        <sub>Scan with Alipay app</sub>
      </td>
    </tr>
  </table>
  <br/>
  <p>
    🌐 <b>Official Portal</b>: <a href="https://amw3.eu.org">https://amw3.eu.org</a><br/>
    📧 <b>Contact & Feedback Email</b>: <a href="mailto:19053936@qq.com">19053936@qq.com</a>
  </p>
</div>
