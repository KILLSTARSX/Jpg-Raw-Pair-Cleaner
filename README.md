# JPG-RAW Pair Cleaner

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Latest release](https://img.shields.io/github/v/release/KILLSTARSX/Jpg-Raw-Pair-Cleaner)](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/KILLSTARSX/Jpg-Raw-Pair-Cleaner/total)](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/releases)
[![Platform](https://img.shields.io/badge/platform-Windows%2010%2F11-brightgreen)](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/releases/latest)
[![Size](https://img.shields.io/badge/size-11.6%20MB-brightgreen)](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/releases/latest)
[![Stars](https://img.shields.io/github/stars/KILLSTARSX/Jpg-Raw-Pair-Cleaner?style=social)](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/stargazers)


JPG without RAW? RAW without JPG?  
This **11.6 MB** tool is built for exactly that — the “half photo” left behind.  
It pairs by base name, lists every orphan, and shows missing sides side by side.  
Confirmed files go to the **Windows Recycle Bin** — recoverable, never permanently deleted.  
Small enough to fit on an SD card. Plug it into any Windows PC, double-click, and go.  
Supports 15+ camera brands, 10 languages, dark/light themes.


有 JPG，没 RAW？有 RAW，没 JPG？  
这个 **11.6 MB** 的小工具，专治这种“半张照片”。  
按基础名自动配对，孤立文件左右对比，一眼看清缺哪边。  
确认后移入 **Windows 回收站**，可恢复，不永久删除。  
轻到能塞进 SD 卡，插到任何 Windows 电脑，双击就能用。  
支持 15+ 相机品牌、10 种语言、深浅主题。


> **Keywords**: orphaned jpg · orphaned raw · jpg raw pair · camera raw cleanup · photo culling leftovers · 孤立文件清理 · JPG RAW 配对

---

## 📖 目录 / Table of Contents

- [什么算“孤立文件” / What is an orphan file](#what-is-an-orphan-file)
- [功能亮点 / Features](#功能亮点)
- [快速开始 / Quick Start](#快速开始)
- [界面预览 / Screenshots](#界面预览)
- [支持的相机品牌与 RAW 格式](#支持的相机品牌与-raw-格式)
- [性能测试数据 / Performance](#性能测试数据)
- [安全说明 / Safety](#安全说明)
- [常见问题 / FAQ](#常见问题)
- [更新日志 / Changelog](#更新日志)
- [作者 / Author](#作者)

---

## <a id="what-is-an-orphan-file"></a> 🤔 什么算“孤立文件”？ / What is an orphan file?

同一张照片通常会存成一对文件：IMG_0001.JPG + IMG_0001.CR3。删掉其中一侧（相机里挑片、只导入了一半、以前手工清理过）之后，另一侧就成了**孤立文件**。

| 情况 | 结果 | 本工具的处理 |
| :--- | :--- | :--- |
| 有 JPG，没有 RAW | 孤立 JPG | 列出来，确认后移入回收站 |
| 有 RAW，没有 JPG | 孤立 RAW | 列出来，确认后移入回收站 |
| 两侧都在 | 正常配对 | 不会被选中，不会被删除 |

扫描文件夹（可递归子文件夹），按**基础名**配对，只把“多出来的那一半”列给你确认。

One photo usually exists as a pair — IMG_0001.JPG + IMG_0001.CR3. Delete one side (in-camera culling, a half-finished import, a past manual cleanup) and the other becomes an **orphan file**. JPG-RAW Pair Cleaner scans a folder (recursively if you want), pairs files by base name, lists exactly what is left over, and cleans only what you confirm.

---

## <a id="功能亮点"></a> ✨ 功能亮点 / Features

| 中文 | English |
| :--- | :--- |
| 📦 **极致轻量**：11.6 MB —— 比一张 JPG 照片还小，功能却堪比一套完整的照片管理工具 | 📦 **Ultra-Light**：11.6 MB – smaller than a single JPG photo, yet packed with full photo management capabilities |
| 🖥️ **两种界面可选**：经典界面（只列出孤立文件）与对比界面（JPG / RAW 左右并排，缺哪边一目了然），选择会被记住 | 🖥️ **Two UI Modes**：Classic (orphans only) and Comparison (JPG/RAW side by side, missing side highlighted); choice is remembered |
| 🌐 **十种语言**：English / 简体中文 / 繁體中文 / 日本語 / 한국어 / Français / Deutsch / Español / Русский / Português，首次启动自动检测系统语言 | 🌐 **10 Languages**：English / 简体中文 / 繁體中文 / 日本語 / 한국어 / Français / Deutsch / Español / Русский / Português, auto-detects system language on first launch |
| 🎨 **深浅色主题**：一键切换浅色 / 深色，默认跟随系统，所有控件整体换色无残留 | 🎨 **Dark/Light Theme**：One-click toggle, follows system by default, all controls re-color cleanly |
| ☑️ **勾选式选择**：列表勾选框 / 缩略图角标 / 空格键三种方式，删除数量只统计勾选文件 | ☑️ **Checkbox Selection**：List checkboxes / thumbnail badges / spacebar – deletion count only includes checked files |
| 🔗 **列表预览联动**：单击列表行自动滚动到对应缩略图并高亮；单击缩略图反向定位列表行 | 🔗 **List-Preview Sync**：Click a list row to scroll to and highlight its thumbnail; click a thumbnail to locate its list row |
| 🧠 **智能识别**：自动检测文件夹内的 RAW 格式，支持 15+ 相机品牌，品牌名随语言本地化 | 🧠 **Smart Detection**：Auto-detects RAW format, supports 15+ brands with localized brand names |
| 📂 **递归扫描**：支持扫描子文件夹（可选层级），跨文件夹配对 | 📂 **Recursive Scan**：Scans subfolders with configurable depth, cross-folder pairing |
| 🖼️ **缩略图预览**：JPG 显示缩略图，RAW 显示后缀占位框，三档大小可调 | 🖼️ **Thumbnail Preview**：JPG shows thumbnails, RAW shows suffix placeholders, 3 size presets |
| 📷 **EXIF 信息显示**：单击查看 EXIF，支持简略 / 详细模式切换与一键复制 | 📷 **EXIF Display**：Click to view EXIF, compact/detailed mode toggle with one-click copy |
| 🗑️ **安全删除**：所有文件移入 Windows 回收站，可恢复 | 🗑️ **Safe Deletion**：All files moved to Windows Recycle Bin, fully recoverable |
| 🛡️ **防误触确认**：自绘确认窗口，无“×”关闭按钮，默认焦点在“取消”上 | 🛡️ **Mis-touch Protection**：Custom dialog with no “×” button, focus defaults to “Cancel” |
| ⚡ **多核并行**：扫描与缩略图生成利用多核 CPU，流畅不卡顿 | ⚡ **Multi-core Parallel**：Scanning & thumbnail generation utilize multi-core CPU |
| ⚙️ **配置记忆**：自动记住文件夹、格式、主题、语言、界面模式、勾选状态等设置 | ⚙️ **Settings Memory**：Remembers folder, format, theme, language, UI mode, checkbox states, etc. |

---

## <a id="快速开始"></a> 🚀 快速开始 / Quick Start

### 1. 下载安装 / Download & Install

| 步骤 | 中文 | English |
| :--- | :--- | :--- |
| ① | 前往 **[Releases 页面](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/releases/latest)** 下载最新版本（适用于 Windows 10 / 11） | Download the latest build from the **[Releases page](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/releases/latest)** (Windows 10 / 11) |
| ② | 双击运行，无需安装任何额外软件 | Double-click to run – no installer and no runtime required |

> ⚠️ 本程序未购买代码签名证书，首次运行 Windows SmartScreen 可能提示“Windows 已保护你的电脑”：点击 **更多信息 → 仍要运行** 即可。发布页给出 SHA256 可自行校验，源码全部公开，也可以自己打包（见下方 FAQ）。

### 2. 三步上手 / Three Steps

| 步骤 | 中文 | English |
| :--- | :--- | :--- |
| ① | 点击“浏览…”选择照片文件夹 → 自动开始扫描 | Click “Browse…” to select folder → scanning starts automatically |
| ② | 在孤立文件列表或对比界面中检查要删除的文件（不需要删的取消勾选） | Review files in the orphan list or comparison view (uncheck any you want to keep) |
| ③ | 点击“删除”→ 在确认窗口中点圆形“删除”按钮 → 完成 | Click “Delete” → click the round “Delete” button in the dialog → done |

> 📖 详细使用说明见 [User_Manual.txt](User_Manual.txt) / [使用说明书.txt](使用说明书.txt)。 / For detailed instructions, see [User_Manual.txt](User_Manual.txt) or [使用说明书.txt](使用说明书.txt).

---

## <a id="界面预览"></a> 🖼️ 界面预览 / Screenshots

<img width="1437" height="1353" alt="JPG-RAW Pair Cleaner 界面 / UI" src="https://github.com/user-attachments/assets/6872ee45-132b-431d-b612-24e041bc0896" />

---

## <a id="支持的相机品牌与-raw-格式"></a> 📸 支持的相机品牌与 RAW 格式 / Supported Camera Brands & RAW Formats

内置 15 个品牌，品牌名随界面语言本地化显示（如简体中文显示“松下 Panasonic”，英文显示“Panasonic”，日文显示“パナソニック Panasonic”）。

15 built-in brands with localized display names per UI language (e.g. “松下 Panasonic” in Simplified Chinese, “Panasonic” in English, “パナソニック Panasonic” in Japanese).

| 品牌 / Brand | RAW 后缀 / RAW Suffix(es) |
| :--- | :--- |
| 松下 Panasonic | .RW2 |
| 佳能 Canon | .CR3 / .CR2 / .CRW |
| 尼康 Nikon | .NEF / .NRW |
| 索尼 Sony | .ARW / .SR2 / .SRF |
| 富士 Fujifilm | .RAF |
| 奥林巴斯 Olympus | .ORF |
| 宾得 Pentax | .PEF |
| 适马 Sigma | .X3F |
| 三星 Samsung | .SRW |
| 理光 Ricoh | .DNG |
| 徕卡 Leica | .DNG |
| 哈苏 Hasselblad | .3FR |
| 飞思 Phase One | .IIQ |
| 玛米亚 Mamiya | .MEF |
| 利图 Leaf | .MOS |

---

## <a id="性能测试数据"></a> 🧪 性能测试数据 / Performance Test Data

以下为极限性能场景下的实测数据，所有测试项 **全部通过**：

The following data was measured under extreme performance scenarios. **All tests passed**:

| 测试项 / Test Item | 结果 / Result |
| :--- | :--- |
| 配对 / Pairing | ✅ 全部通过 / Passed |
| 勾选 / Checkbox selection | ✅ 1000 次勾选 1.3s / 1000 checks in 1.3s |
| 联动 / List-preview sync | ✅ 66ms |
| 2000 文件性能 / 2000-file performance | ✅ 扫描 11.7s，1200 缩略图 / Scan 11.7s, 1200 thumbnails |

<small>此数据基于极限性能场景，具体性能差异因用户电脑配置不同而异。 / This data is based on extreme performance scenarios; actual performance may vary depending on your computer configuration.</small>

---

## <a id="安全说明"></a> ⚠️ 安全说明 / Safety Notes

| 中文 | English |
| :--- | :--- |
| 所有删除操作均移入 **Windows 回收站**，可从回收站还原 | All deletions go to **Windows Recycle Bin** – restorable at any time |
| **不存在任何永久删除调用**，绝不永久删除文件 | **No permanent deletion calls** – files are never permanently deleted |
| 格式不符时强制二次确认，即使取消勾选也不会跳过 | Force re-confirmation on format mismatch, even if checkbox is unchecked |
| 单个文件失败不中断流程，失败原因明确列出；文件被占用时自动等待后重试一次 | Individual file failure won’t interrupt the process; reasons are clearly listed; auto-retry once if file is in use |
| 删除前确认窗口无“×”按钮，默认焦点在“取消”，按 Esc / 回车均为取消 | Confirmation dialog has no “×” button, focus defaults to “Cancel”, Esc/Enter both cancel |

---

## <a id="常见问题"></a> ❓ 常见问题 / FAQ

| 问题 / Question | 回答 / Answer |
| :--- | :--- |
| **Windows 提示“已保护你的电脑”怎么办？ / SmartScreen warning?** | 程序没有购买代码签名证书（个人开源项目通常不买），点击 **更多信息 → 仍要运行** 即可。可先核对 Release 页面给出的 SHA256，源码完全公开，也可以自己重新打包。 |
| **会永久删除我的照片吗？ / Is deletion permanent?** | 不会。所有删除都走 Windows 回收站，随时可以还原；程序中没有永久删除的调用。 |
| **会动到已经配好对的文件吗？ / Will it touch matched pairs?** | 不会。默认只处理孤立文件；对比界面中已配对的行不可勾选。 |
| **支持哪些格式？ / Which formats are supported?** | JPG/JPEG，以及上表 15 个相机品牌的 RAW（RW2、CR3、CR2、NEF、ARW、RAF、ORF、DNG 等）。 |
| **支持 macOS / Linux 吗？ / Other platforms?** | 目前仅提供 Windows 10 / 11 版本。 |
| **怎么切换语言？ / How to change language?** | 应用栏右侧的语言下拉框可切换 10 种语言，首次启动按系统语言自动选择，选择会被记住。 |
| **发现问题怎么反馈？ / How to report a bug?** | 直接开一个 [Issue](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/issues)，附上版本号、语言和截图即可。 |

---

## <a id="更新日志"></a> 📝 更新日志 / Changelog

**v5.1** — 🖥️ 双界面模式 + 🧩 对比视图
- **新增**：配对对比界面（JPG | RAW 左右并排，缺失一侧留空，颜色标记：绿=齐全，黄=缺 JPG，红=缺 RAW）
- **新增**：界面模式可自主切换（应用栏「界面」下拉框），选择会被记住
- **新增**：对比界面「处理」列，明确显示每行是否会删除（删除 / 不删除·已取消勾选 / 不删除·已配对 / 不删除·格式未匹配）
- **新增**：对比界面「用背景色标记」开关（默认开）与「只显示缺失」开关
- **新增**：对比界面顶部图例实时统计（共 N 组：齐全 x · 缺 RAW y · 缺 JPG z）
- **新增**：对比界面支持按 JPG 文件名 / RAW 文件名 / 状态 / 处理排序
- **优化**：删除方式（只删 JPG / 只删 RAW / 全部）的圆点改为自绘大圆环，更醒目
- **优化**：列宽可拖动，最小列宽 = 表头文字宽度，不会遮住表头

**v5.0** — 🌍 全球化 + 🎨 主题系统 + ☑️ 勾选选择
- **新增**：10 种语言支持（English / 简体中文 / 繁體中文 / 日本語 / 한국어 / Français / Deutsch / Español / Русский / Português）
- **新增**：首次启动自动检测系统语言（Windows UI 语言 / 环境变量回退）
- **新增**：相机品牌名本地化（如简体中文“松下 Panasonic”、日文“パナソニック Panasonic”、俄文“Никон Nikon”）
- **新增**：深色 / 浅色主题，默认跟随系统，一键切换实时生效
- **新增**：列表与预览勾选选择（列表勾选框 / 缩略图角标 / 空格键三种方式）
- **新增**：勾选状态记忆，删除数量与总大小只统计仍被勾选的文件
- **新增**：列表 ↔ 预览双向联动定位（单击列表行滚动到缩略图，单击缩略图定位列表行）
- **新增**：自绘圆润滚动条（长方形 + 两端半圆，非椭圆），列表 / 预览 / 结果区样式统一
- **新增**：自绘药丸形按钮、下拉框、滑块、卡片
- **新增**：二次确认防误触弹窗（无“×”按钮，圆形取消 / 删除按钮，默认焦点在取消）
- **修复**：EXIF 信息独占一行右对齐，与按钮永不重叠（窄窗口下也能完整显示）
- **修复**：列表水平滚动（长路径超出宽度时可正常滚动）
- **优化**：软件体积从 16.2 MB 进一步缩减至 **11.6 MB**
- **优化**：打包时排除 numpy、PIL 未用插件、unittest 等无用模块
- **优化**：语言资源外置，任何缺失键自动回退英语

**v4.1**
- **新增**：现代卡片式圆角界面
- **优化**：打包体积精简（16.2 MB）

**v4.0**
- **新增**：回收站删除可恢复（确认弹窗明确提示）
- **新增**：EXIF 九字段对齐显示（相机厂商、型号、光圈、快门、ISO、焦距、拍摄日期、分辨率、镜头）
- **新增**：简略 EXIF 模式（一行紧凑显示：相机 | f值 | 快门 | ISO | 焦距 | 分辨率）
- **新增**：双击 EXIF 区域或右键菜单复制 EXIF 信息
- **新增**：单击缩略图/列表行显示 EXIF
- **新增**：双击缩略图跳转资源管理器定位文件
- **新增**：预览区滚动自动回到顶部（切换文件夹后）
- **修复**：RAW 文件 EXIF 解析（内嵌 TIFF 解析，缺失字段显示 “--”）
- **优化**：缩略图缓存、多核并行处理，提升扫描与加载速度
- **优化**：软件体积缩减 40%（26.7 MB → 16.2 MB）

**v3.6**
- **新增**：状态条固定（不再随滚动移动）
- **新增**：卡片等比缩放（保持图片比例不变形）
- **新增**：模式切换不丢图（切换删除方式后缩略图保留）
- **新增**：EXIF 懒加载（按需加载，减少启动耗时）
- **新增**：RAW EXIF 支持（内嵌 TIFF 解析）

**v3.5**
- **新增**：EXIF 信息显示（单击列表行或缩略图查看）
- **新增**：缩略图缓存与多核并行（大幅提升加载速度）
- **修复**：预览区滚轮卡顿
- **修复**：快速拖动滑块缩略图层叠
- **修复**：上传后文件名变为 default 的问题

**v3.3**
- **新增**：关于窗口加大
- **移除**：手动选择按钮与锁定逻辑

**v3.2**
- **新增**：自动识别显示修正
- **新增**：强制删除
- **新增**：滑块吸附

**v3.1**
- **新增**：网格预览
- **新增**：缩略图三档大小
- **新增**：自动识别锁定

**v3.0**
- **新增**：自动识别
- **新增**：格式不符保护
- **新增**：配置记忆

**v2.0**
- **新增**：多 RAW 格式支持
- **新增**：递归扫描

**v1.0**
- **新增**：基础 RAW / JPG 筛选删除

---

## <a id="作者"></a> 👨‍💻 作者 / Author

- **KILL-STAR SX**
- GitHub: [KILLSTARSX](https://github.com/KILLSTARSX)
- 哔哩哔哩 / bilibili: [KILL-STAR_SX](https://space.bilibili.com/381623593)

---

## 📄 许可证 / License

本项目采用 **MIT License** 开源协议，完全免费开源，完整文本见 [LICENSE](LICENSE)。
This project is licensed under the **MIT License** – completely free and open source, see [LICENSE](LICENSE).

---

## ⭐ 如果觉得有用，欢迎点个 Star！ / If it helped, a star is appreciated!

[![Star History](https://img.shields.io/github/stars/KILLSTARSX/Jpg-Raw-Pair-Cleaner?style=social)](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/stargazers)
[![Fork](https://img.shields.io/github/forks/KILLSTARSX/Jpg-Raw-Pair-Cleaner?style=social)](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/forks)
