<p align="right">
  <b>🇨🇳 简体中文</b> | <a href="README_EN.md">🇬🇧 English</a>
</p>

# OctPc - 海量点云高性能八叉树转换工具与三维交互浏览器

[![GitHub release](https://img.shields.io/github/v/release/HonghuangKongJian/OctPc-Release?color=brightgreen&label=最新版本%20v4.0.1)](https://github.com/HonghuangKongJian/OctPc-Release/releases)
[![Format](https://img.shields.io/badge/索引格式-4.0%20自包含单文件-emerald.svg)](https://amw3.eu.org)
[![Capacity](https://img.shields.io/badge/单工程承载-千亿级点云-orange.svg)]()
[![Performance](https://img.shields.io/badge/流式引擎-首帧秒开%2060FPS%20丝滑-blue.svg)]()
[![Test Data](https://img.shields.io/badge/配套测试集-5000万点%20人形点云-green.svg)]()
[![License: Dual](https://img.shields.io/badge/License-MIT%20%7C%20Commercial-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20x64-lightgrey.svg)]()
[![Sponsor](https://img.shields.io/badge/☕-赞赏支持-rose.svg)](#-赞赏与支持-sponsor)

> 🚀 **全面进入 OctPc 4.0 自包含单文件架构与两阶段渐进流式（边写边看）新纪元！**  
> 彻底终结原有伴生碎片文件，多级 LOD 空间金字塔与全量点云统合于单一 `.octpc`；首创两阶段流式引擎，亿级海量点云 0.3 秒极速开窗预览，后台静默追加深层细节并自动平滑热重载！

**OctPc** 是一套面向超大规模激光雷达点云（LAS/LAZ）的现代高性能八叉树处理与三维交互可视化技术栈。采用自研高性能线性八叉树拓扑与多核空间分块调度算法，彻底攻克亿级点云导入耗时长、显存开销大、视口顿挫严重的行业难题，实现极速转换与毫秒级秒开满帧渲染。

---

## 🌟 核心特性与亮点 (v4.0.1 Highlights)

- 🏆 **OctPc 4.0 自包含单文件架构 (Single-File Self-Contained)**：
  - 彻底淘汰原有伴生的 `_oct.las`、`.octlod`、`.octdata` 分离碎片文件；
  - 八叉树空间拓扑元数据、多级多分辨率 LOD 空间金字塔索引、紧凑叶子点云全量封装于单一 `.octpc` 文件中；
  - 零外部散落文件，工程迁移或网络分发只需拷贝一个 `.octpc` 单文件即可直接漫游渲染，绝不丢失数据；
- ⚡ **两阶段渐进流式引擎（边写边看，首帧秒开）**：
  - **阶段一（极速粗模）**：输入数千万至数亿点原始点云时，八叉树前 3 层全景粗模在 0.12 ~ 0.35 秒内即可刷盘就绪；
  - **秒级开窗交互**：三维查看器（Viewer）嗅探到粗模就绪即刻拉起三维视口开始全景漫游，用户无需枯坐等待漫长的全量写入；
  - **阶段二（平滑追加与热重载）**：后台静默流式追加深层采样与全量叶子点云，追加完成后查看器自动平滑热重载（Hot-Reload），无缝升级至高清终态全树；
- 🧠 **智能自适应八叉树层数推导**：
  - 内置基于点云总规模的动态自适应层数计算公式；
  - 免除用户手动猜测和调优 `-d` 参数的繁琐心智负担，百亿级点云自动推导匹配最佳深度；
- 🖥️ **Win32 原生 Unicode 纯净视口与状态监控**：
  - 窗口标题栏全面重构为 Win32 原生 `SetWindowTextW` 宽字符管线，杜绝任何 ANSI/GBK 或特殊符号引发的字符乱码与问号；
  - 查看器 HUD 抬头面板与窗口标题栏实时直观呈现当前运行状态（全景粗模预览中 / 完备终态单文件）、采样点数及八叉树层级；
- 🌐 **全栈原生中英双语支持 (Bilingual Ready)**：
  - 全套程序（`octpc_cli` 与 `octpc_viewer`）及文档均已原生支持中英双语，自动识别系统语言，支持随时按 `[L]` 键切换；
- 📦 **免安装绿色便携**：
  - 解压即用，内置轻量运行库与高清中文字体，全套压缩包仅 2.97 MB，无需安装庞杂的第三方 SDK 环境；
- 🎯 **三维点云坐标实时测量与拾取 (Real-Time 3D Coordinate Picker)**：
  - 鼠标在视口滑过时，状态栏毫秒级高灵敏度动态计算并呈现光标附近点云的三维真实空间坐标（X, Y, Z）；
  - 支持快捷键 [C] 极速复制当前测量点坐标到系统剪贴板，极大方便工程复核与点云质检；
- 🔄 **交互手感优化 (Optimized Viewport Zoom Interaction)**：
  - 深度对调优化鼠标滚轮视距缩放方向，滚轮操作体验与主流 CAD/GIS 专业软件全面统一；
- 🛡️ **复杂中文路径彻底兼容与运行日志防护**：
  - 构建全链路原生 Unicode 路径中台，彻底根治 Windows 下中文文件夹或文件名引发的转码异常与闪退崩溃；
  - 内置持久化磁盘运行日志 (octpc_viewer.log) 与系统级崩溃转储拦截机制，工业级稳健；
- 🎨 **多维度科学赋色**：
  - 原始 RGB 真彩色、激光反射强度灰度、语义分类颜色及高程动态渐变色带一键自由切换。

---

## 🔌 第三方客户程序无缝集成指南 (Zero-Code 插件与工具集成)

无论是研发全新的测绘/GIS/数字孪生系统，还是为已有的行业三维软件扩展海量点云浏览功能，OctPc 均提供了极简的直接集成方案，**客户现有主程序无需重新编译即可直接使用**：

### 模式一：三维宿主系统零重编译即插即用 (OSG 插件方式)

若客户已有基于 OpenSceneGraph (OSG) 的三维应用程序：

#### 步骤 1：部署插件动态库
将发布包中的 `osgdb_octpc.dll` 直接拷贝至客户软件运行目录下的 `osgPlugins-3.x.x/` 插件子目录（或与客户主程序 `.exe` 同目录）。

#### 步骤 2：一行代码直接加载渲染 (4.0 自包含单文件)
客户程序无需改动原有渲染管线，直接使用 OSG 标准接口：
```cpp
#include <osgDB/ReadFile>

// 1. 直接加载 .octpc 八叉树点云（OSG 插件自动接管分页多分辨率自包含单文件调度）
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
process.StartInfo.Arguments = ""D:\data\input.las" --lang en"; // 自动自适应最佳层数
process.StartInfo.CreateNoWindow = true;
process.StartInfo.UseShellExecute = false;
process.Start();
process.WaitForExit();

// 转换完成，生成的单个 D:\data\input.octpc 自包含文件即可由渲染器接管
```

#### Python 集成示例：
```python
import subprocess
import os

# 后台静默调用八叉树转换（自适应层数推导）
cmd = ["octpc_cli.exe", "D:/data/input.las", "--lang", "zh"]
subprocess.run(cmd, check=True)
print("转换成功，生成自包含单文件 D:/data/input.octpc")
```

---

## 🧪 测试点云生成工具 (5000 万点高精度人形模型)

如果您手头没有现成的大体量激光点云数据，本项目贴心配套了千万级点云生成脚本 `generate_humanoid.py`：
- 可一键快速生成包含真实 RGB 色彩、反射强度与各部位语义分类的 **5000 万点 3D 彩色人形点云 (`humanoid_50M.las`)**；
- **运行命令**：
  ```bash
  python generate_humanoid.py -n 50000000 -o humanoid_50M.las
  ```
- 生成完成后，直接双击运行 `octpc_viewer.exe` 选择该 `humanoid_50M.las`，即可亲身体验千万级大点云在 0.12 秒内生成粗模开窗秒开与 60fps 满帧浏览！

---

## 🧩 开发者 SDK (开发孵化中) 与双轨授权模式 (Developer SDK & Dual-License)

- 🚀 **底层核心解耦演进中**：正持续对底层八叉树算法与自包含单文件流进行标准化 C++17 API 提炼，成熟完备后将正式推出对外 SDK；
- **典型赋能场景**：
  - 轻松嵌入 GIS 平台、无人机航测后处理软件、数字孪生/BIM 引擎、三维测绘测量系统；
  - 提供海量点云自定义构建、空间索引查询、快速降采样抽稀与定制视口嵌入能力；
- ⚖️ **双轨许可原则**：
  - **社区版 (Community)**：**功能 100% 完全开放**（单工程支持千亿级点云，无任何性能截断），渲染画面保留轻量水印标识，个人学习、科研与内部评估完全免费；
  - **商业版 (Pro)**：**彻底移除画面水印**，支持品牌 OEM/深度嵌入行业测绘/GIS 商业软件系统，并提供官方 24h 优先技术支持服务；
- 🤝 **商业授权咨询**：欢迎通过官方技术邮箱 [19053936@qq.com](mailto:19053936@qq.com) 与作者取得联系。

---

## 📊 数据规模与性能承载规格表

| 点云规模 | 典型数据源 | 阶段一粗模就绪耗时 | 视口漫游帧率 | 内存 / 显存开销 |
| :--- | :--- | :--- | :--- | :--- |
| **1,000 万 ~ 5,000 万点** | 无人机航测、人形点云测试集 | **~0.12 秒 (首帧秒开)** | **60 FPS** 满帧极速 | < 150 MB |
| **1 亿 ~ 3 亿点** | 车载移动测量、城市级倾斜航测 | **~0.35 秒 (首帧秒开)** | **60 FPS** 满帧丝滑 | ~300 MB |
| **5 亿 ~ 10 亿点** | 区域级激光雷达测绘大场景 | **~1 秒内 (首帧秒开)** | **60 FPS** 流畅漫游 | ~500 MB |
| **21 亿 ~ 100 亿点** | 特大型国家级/城市实景三维工程 | **秒级首帧呈现** | **60 FPS** 动态多级调度 | 分页受控按需调度 |
| **千亿级空间点云** | 全流域/全省域宏观地理空间测绘工程 | 4.0 自包含单文件原生支持 | **60 FPS** 边写边看流式调度 | 分页按需动态吞吐 |

---

## 📦 软件包下载 (Release Assets)

请前往 👉 **[Releases 页面](https://github.com/HonghuangKongJian/OctPc-Release/releases)** 下载最新发布版：

| 分发包名称 | 体积 | 推荐适用场景 |
| :--- | :--- | :--- |
| **`octpc_suite_v4.0.1.zip`** | **约 2.97 MB** | **【强烈推荐】一体化完整绿色套件**。内含三维查看器、格式转换工具、完整动态链接库及便捷启动脚本，解压即用。 |
| **`octpc_cli_v4.0.1.zip`** | **约 252 KB** | **独立命令行转换工具精简版**。纯静态自包含，零外部依赖，专供服务器端后台批处理或嵌入数据生产流水线。 |

### 🔒 文件 SHA-256 校验码 (Checksums)

```text
75719F5F7FDFCCDAE59F1069DC4C664003E26D56B8F62C187FEA09104213F1C4  octpc_suite_v4.0.1.zip
8AD7C7CE41E22C5D4467F97EB534C391CC690ACB338CF984A6B2B75C4C91C4C1  octpc_cli_v4.0.1.zip
```

---

## ⌨️ 常用快捷键一览

| 按键 | 说明 |
| :--- | :--- |
| **[Space]** | 视角快速居中至点云中心 |
| **[1] / [2]** | 切换为【原始 RGB 真彩】 / 【激光反射强度】模式 |
| **[3] / [4]** | 切换为【点云分类赋色】 / 【高程动态色带】模式 |
| **[+] / [-]** | 实时放大 / 缩小点渲染尺寸 (Point Size) |
| **[ [ ] / [ ] ]** | 增减 LOD 细化加载距离倍率 |
| **[C]** | **复制当前鼠标悬停点真实三维空间坐标至系统剪贴板** |
| **[F3]** | 弹出文件选择器更换点云 |
| **[B]** | 循环切换视口背景色 (深灰黑 / 纯黑 / 藏青夜空 / 浅灰白) |
| **[H]** | 开启 / 关闭左上角 HUD 抬头显示 |
| **[L]** | **实时无缝切换界面中英双语 (中 ⇄ 英)** |
| **[F1]** | 快捷访问官方主页 |
| **[F2]** | 快捷联系反馈作者 |

---

## ☕ 赞赏与支持 (Sponsor)

如果您觉得本项目对您的工作、学习或商业研发有所帮助，欢迎赞赏支持作者持续迭代！您的每一份认可都是底层架构持续创新的最强动力：

<p align="center">
  <img src="docs/sponsor_wechat.png" alt="微信赞赏" width="260" style="margin-right: 30px; display: inline-block;" />
  <img src="docs/sponsor_alipay.png" alt="支付宝赞赏" width="260" style="display: inline-block;" />
</p>
<p align="center">
  <i>微信赞赏码（左） &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 支付宝收款码（右）</i>
</p>

---

- 🌐 **洪荒空间门户矩阵**：https://amw3.eu.org
- 📧 **技术支持与交流邮箱**：19053936@qq.com
- ⚖️ **开源许可证**：[MIT License](LICENSE)
