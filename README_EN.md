<p align="right">
  <a href="README.md">🇨🇳 简体中文</a> | <b>🇬🇧 English</b>
</p>

# OctPc - High-Performance Point Cloud Octree Indexer & 3D Interactive Viewer

[![GitHub release](https://img.shields.io/github/v/release/HonghuangKongJian/OctPc-Release?color=brightgreen&label=Latest%20v5.2.0)](https://github.com/HonghuangKongJian/OctPc-Release/releases)
[![Format](https://img.shields.io/badge/Format-4.0%20Single--File-emerald.svg)](https://amw3.eu.org)
[![Capacity](https://img.shields.io/badge/Scale-Billion--Points-orange.svg)]()
[![Performance](https://img.shields.io/badge/Streaming-Sub--Second%20Preview%2060FPS-blue.svg)]()
[![License: Dual](https://img.shields.io/badge/License-MIT%20%7C%20Commercial-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20x64-lightgrey.svg)]()

> 🚀 **Entering the New Era of OctPc 4.0: Self-Contained Single-File Architecture & Two-Stage Progressive Streaming Engine!**  
> Say goodbye to auxiliary companion files! Multi-level LOD spatial pyramid and full leaf points are consolidated into a single `.octpc` file. Enjoy sub-second preview startup on massive point clouds while deep points stream silently in the background with auto hot-reload!

**OctPc** is a state-of-the-art high-performance octree processing and 3D interactive visualization toolchain designed for massive LiDAR point clouds (LAS/LAZ). Powered by proprietary linear octree topology and multi-threaded spatial chunking algorithms, OctPc conquers the challenges of sluggish import, excessive memory footprint, and viewport stutter.

> 📰 **Featured Bilingual Blog Post**: 👉 [50M Points Converted in 10s with 50%+ Size Reduction! Full Feature Guide (Bilingual)](docs/BLOG_V5_RELEASE.md) ｜ [Read Online](https://blog.amw3.eu.org/?p=71)

---

## 🌟 Highlights of v5.2.0

- 🪟 **Panels You Can Rearrange Freely**: the layers, console and runtime log panels are no longer pinned to one side — drag a panel by its title bar to split left/right, stack top/bottom, or dock them as tabs. A tidy default layout is ready on first launch, and your arrangement is remembered next time;
- ⚡ **Faster Opening of Large LAS Files**: uncompressed LAS now converts with multi-core reading, so the bigger the file, the more waiting time you save. Nothing changes in how you open files — the overview appears first and fine details stream in quietly in the background;
- 🕒 **Compile Time Shown in the Status Bar**: the bottom of the window shows when the program was built, so you can tell at a glance whether you are on the latest version and report issues more precisely;
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
- 🎯 **Real-Time 3D Point Coordinate Picker**: Real-time calculation and display of hovered point coordinates (X, Y, Z) with one-click [C] shortcut to copy to clipboard;
- 🗂️ **Multi-Cloud Overlay & Layer Management**: Supports opening multiple point cloud files in one viewport with a dedicated layers management panel (`[M]`), per-layer visibility toggles, Zoom-to-cloud focus, and layer unloading;
- 🔄 **Intuitive Viewport Zoom Experience**: Reversed mouse wheel zoom direction to match industry CAD/GIS standards;
- 🛡️ **Native Chinese & Unicode Path Compatibility**: Full-pipeline Unicode path resolving, eliminating Windows path transcoding errors and crashes;
- 📦 **Zero-Installation Green Portable Suite (~3.45 MB)**.

---

## 📦 Release Assets Download

Please visit the 👉 **[Releases Page](https://github.com/HonghuangKongJian/OctPc-Release/releases)** to download:

| Package | Size | Description |
| :--- | :--- | :--- |
| **`octpc_viewer_v5.2.0.zip`** | **~3.45 MB** | **[Recommended] Pure Viewer Suite**: unzip and run — for everyday inspection, presentations and on-site checks. Overlay several clouds in one viewport, hover to read real-world coordinates; the conversion tool is bundled. |
| **`octpc_cli_v5.2.0.zip`** | **~0.31 MB** | For batch conversion without a GUI: a command-line tool that turns LAS/LAZ into smaller, faster-loading `.octpc` files, easy to plug into automated pipelines. |

### 🔒 SHA-256 Checksums

```text
E31EAC88C92BC4651EE3AEEC500D5E6F4B8D430A223F4587AF480C882D1ACEA1  octpc_viewer_v5.2.0.zip
592E919E26D87954F05AE8D86E425421312DCD7D676FF2BFBAF651AD7DAC6BAF9  octpc_cli_v5.2.0.zip
```

---

- 🌐 **Homepage**: https://amw3.eu.org
- 📧 **Feedback Email**: 19053936@qq.com
- ⚖️ **License**: [MIT License](LICENSE)
