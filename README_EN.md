<p align="right">
  <a href="README.md">🇨🇳 简体中文</a> | <b>🇬🇧 English</b>
</p>

# OctPc - High-Performance Point Cloud Octree Indexer & 3D Interactive Viewer

[![GitHub release](https://img.shields.io/github/v/release/HonghuangKongJian/OctPc-Release?color=brightgreen&label=Latest%20v4.0.0)](https://github.com/HonghuangKongJian/OctPc-Release/releases)
[![Format](https://img.shields.io/badge/Format-4.0%20Single--File-emerald.svg)](https://amw3.eu.org)
[![Capacity](https://img.shields.io/badge/Scale-Billion--Points-orange.svg)]()
[![Performance](https://img.shields.io/badge/Streaming-Sub--Second%20Preview%2060FPS-blue.svg)]()
[![SDK](https://img.shields.io/badge/SDK-v4.0.0%20Available-blueviolet.svg)](https://amw3.eu.org)
[![License: Dual](https://img.shields.io/badge/License-MIT%20%7C%20Commercial-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20x64-lightgrey.svg)]()

> 🚀 **Entering the New Era of OctPc 4.0: Self-Contained Single-File Architecture & Two-Stage Progressive Streaming Engine!**  
> Say goodbye to auxiliary companion files! Multi-level LOD spatial pyramid and full leaf points are consolidated into a single `.octpc` file. Enjoy sub-second preview startup on massive point clouds while deep points stream silently in the background with auto hot-reload!

**OctPc** is a state-of-the-art high-performance octree processing and 3D interactive visualization toolchain designed for massive LiDAR point clouds (LAS/LAZ). Powered by proprietary linear octree topology and multi-threaded spatial chunking algorithms, OctPc conquers the challenges of sluggish import, excessive memory footprint, and viewport stutter.

---

## 🌟 Highlights of v4.0.0

- 🏆 **OctPc 4.0 Self-Contained Single-File Architecture**:
  - Eliminates auxiliary companion files (`_oct.las`, `.octlod`, `.octdata`);
  - Octree metadata, multi-resolution LOD spatial pyramid, and compact leaf points are packaged into a single `.octpc` file;
  - Zero scattered files. Migration and sharing require only a single `.octpc` file;
- ⚡ **Two-Stage Progressive Streaming Engine (Preview while Writing)**:
  - **Stage 1 (Instant Overview)**: Generates the top overview rough model in 0.12 ~ 0.35s for tens to hundreds of millions of points;
  - **Sub-Second Viewport Launch**: OctPc Viewer sniffs the Stage 1 signal and launches the 3D interactive viewport immediately;
  - **Stage 2 (Smooth Streaming & Hot-Reload)**: Streams deep LOD levels and leaf points in the background, automatically performing a smooth hot-reload when finished to upgrade to full resolution;
- 🧠 **Automatic Depth Deduction**:
  - Automatically calculates optimal octree depth based on input point count;
- 🖥️ **Native Win32 Unicode Viewport & Real-Time Status HUD**:
  - Fully migrated window title bar to Win32 native `SetWindowTextW` wide-string API;
  - Real-time status display in HUD and title bar;
- 🌐 **Native Bilingual Support (Chinese & English)**;
- 📦 **Zero-Installation Green Portable Suite (2.97 MB)**.

---

## 📦 Release Assets Download

Please visit the 👉 **[Releases Page](https://github.com/HonghuangKongJian/OctPc-Release/releases)** to download:

| Package | Size | Description |
| :--- | :--- | :--- |
| **`octpc_suite_v4.0.0.zip`** | **~2.97 MB** | **[Recommended] All-in-One Portable Suite**. Contains 3D Viewer, CLI tool, DLL dependencies, and start scripts. |
| **`octpc_cli_v4.0.0.zip`** | **~252 KB** | **Standalone CLI Indexer Tool**. Pure static self-contained, zero external dependencies, perfect for server batch pipelines. |
| **`octpc_sdk_v4.0.0.zip`** | **~180 KB** | **C++ Developer SDK**. Includes headers, import libs, CMake config, and example projects. |

### 🔒 SHA-256 Checksums

```text
0FA120C23984A7A3BCECE5173660060D927D5A74ED1BD3E3D4B8B16524AA86E2  octpc_suite_v4.0.0.zip
9E231E984A9836645B5AA5D7AD7FB3A5C99677BED9374D44E97AEF19D3304CAE  octpc_cli_v4.0.0.zip
5BCF124E271ED409CFEC5EECBF6E9668BBE68DAC8B43E11403D828D05C46086E  octpc_sdk_v4.0.0.zip
```

---

- 🌐 **Homepage**: https://amw3.eu.org
- 📧 **Feedback Email**: 19053936@qq.com
- ⚖️ **License**: [MIT License](LICENSE)
