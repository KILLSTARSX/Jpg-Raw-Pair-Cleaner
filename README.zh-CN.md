# JPG-RAW Pair Cleaner

[English](README.md) | [简体中文](README.zh-CN.md)

[![License: KS-ASL-1.0](https://img.shields.io/badge/license-KS--ASL--1.0-orange.svg)](LICENSE)
[![Latest release](https://img.shields.io/github/v/release/KILLSTARSX/Jpg-Raw-Pair-Cleaner)](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/KILLSTARSX/Jpg-Raw-Pair-Cleaner/total)](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/releases)
[![Platform](https://img.shields.io/badge/platform-Windows%2010%2F11-brightgreen)](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/releases/latest)
[![Size](https://img.shields.io/badge/size-623%20KB-brightgreen)](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/releases/latest)
[![Stars](https://img.shields.io/github/stars/KILLSTARSX/Jpg-Raw-Pair-Cleaner?style=social)](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/stargazers)

自动清理 JPG+RAW 孤立文件，筛选并同步删除 JPG/RAW 照片。软件仅 623 KB，支持 15+ 品牌、10 种语言、深浅主题，回收站可恢复。

💥 **v6.0 C++ 重写：从 27.4 MB 降至 623 KB，体积仅剩 2%，功能却更多。启动 218 ms，轻到无感塞进 SD 卡。**

> **Keywords**: 孤立文件清理 · JPG RAW 配对 · 同步删除 JPG 和 RAW · 相机照片清理 · 照片筛选

---

## 📖 目录

- [什么算“孤立文件”？](#what-is-an-orphan-file)
- [功能亮点](#features)
- [快速开始](#quick-start)
- [界面预览](#screenshots)
- [支持的相机品牌与 RAW 格式](#supported-camera-brands--raw-formats)
- [性能测试数据](#performance-test-data)
- [安全说明](#safety-notes)
- [常见问题](#faq)
- [更新日志](#changelog)
- [作者](#author)
- [开发历程与心得](#development-notes)

---

## <a id="what-is-an-orphan-file"></a> 🤔 什么算“孤立文件”？

同一张照片通常会存成一对文件：IMG_0001.JPG + IMG_0001.CR3。删掉其中一侧（相机里挑片、只导入了一半、以前手工清理过）之后，另一侧就成了**孤立文件**。

| 情况 | 结果 | 本工具的处理 |
| :--- | :--- | :--- |
| 有 JPG，没有 RAW | 孤立 JPG | 列出来，确认后移入回收站 |
| 有 RAW，没有 JPG | 孤立 RAW | 列出来，确认后移入回收站 |
| 两侧都在 | 正常配对 | 不会被选中，不会被删除 |

扫描文件夹（可递归子文件夹），按**基础名**配对，只把“多出来的那一半”列给你确认。

---

## <a id="features"></a> ✨ 功能亮点

| 中文 |
| :--- |
| 🧹 **JPG / RAW 同步清理**：同步删除 JPG 和 RAW 文件，按基础名自动配对，绝不误删已配对文件 |
| 📦 **极致轻量**：623 KB —— 只有初版 27.4 MB 的 2%，优化掉了 98% 的体积，比一张 JPG 照片还小几百倍 |
| ⚡ **原生 C++ 重构**：C++17 + Win32 API，无 Python、无 Qt、无 .NET、无第三方库依赖，单文件 exe，启动仅 218 ms |
| 🖼️ **RAW 内嵌缩略图预览（v6.0 新增）**：解析六大厂商品牌 RAW 内嵌的 JPG 缩略图，RAW 文件也能直接看到照片 |
| 🖥️ **两种界面可选**：经典界面（只列出孤立文件）与对比界面（JPG / RAW 左右并排，缺哪边一目了然），选择会被记住 |
| 🌐 **十种语言**：English / 简体中文 / 繁體中文 / 日本語 / 한국어 / Français / Deutsch / Español / Русский / Português，首次启动自动检测系统语言 |
| 🎨 **深浅色主题**：一键切换浅色 / 深色，默认跟随系统，所有控件整体换色无残留 |
| ☑️ **勾选式选择**：列表勾选框 / 缩略图角标 / 空格键三种方式，删除数量只统计勾选文件 |
| 🔗 **列表预览联动**：单击列表行自动滚动到对应缩略图并高亮；单击缩略图反向定位列表行 |
| 🧠 **智能识别**：自动检测文件夹内的 RAW 格式，支持 15+ 相机品牌，品牌名随语言本地化 |
| 📂 **递归扫描**：支持扫描子文件夹（可选层级），跨文件夹配对 |
| 📷 **EXIF 信息显示**：单击查看 EXIF，支持简略 / 详细模式切换与一键复制 |
| 🗑️ **安全删除**：所有文件移入 Windows 回收站，可恢复 |
| 🛡️ **防误触确认**：自绘确认窗口，无“×”关闭按钮，默认焦点在“取消”上 |
| ⚙️ **配置记忆**：自动记住文件夹、格式、主题、语言、界面模式、勾选状态等设置 |

---

## <a id="quick-start"></a> 🚀 快速开始

前往 **[Releases 页面](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/releases/latest)** 下载最新版本（适用于 Windows 10 / 11），双击运行，无需安装任何额外软件。

| 步骤 | 中文 |
| :--- | :--- |
| ① | 点击“浏览…”选择照片文件夹 → 自动开始扫描 |
| ② | 在孤立文件列表或对比界面中检查要删除的文件（不需要删的取消勾选） |
| ③ | 点击“删除”→ 在确认窗口中点圆形“删除”按钮 → 完成 |

详细使用说明见 [使用说明书.txt](使用说明书.txt)。

---

## <a id="screenshots"></a> 🖼️ 界面预览

<img width="1390" height="1609" alt="image" src="https://github.com/user-attachments/assets/82ccc61e-86a8-4bd2-baf5-7b2d1b531018" />


---

## <a id="supported-camera-brands--raw-formats"></a> 📸 支持的相机品牌与 RAW 格式

内置 15 个品牌，品牌名随界面语言本地化显示（如简体中文显示“松下 Panasonic”，英文显示“Panasonic”，日文显示“パナソニック Panasonic”）。

| 品牌 | RAW 后缀 |
| :--- | :--- |
| 松下 | .RW2 |
| 佳能 | .CR3 / .CR2 / .CRW |
| 尼康 | .NEF / .NRW |
| 索尼 | .ARW / .SR2 / .SRF |
| 富士 | .RAF |
| 奥林巴斯 | .ORF |
| 宾得 | .PEF |
| 适马 | .X3F |
| 三星 | .SRW |
| 理光 | .DNG |
| 徕卡 | .DNG |
| 哈苏 | .3FR |
| 飞思 | .IIQ |
| 玛米亚 | .MEF |
| 利图 | .MOS |

---

## <a id="performance-test-data"></a> 🧪 性能测试数据

以下为极限性能场景下的实测数据，所有测试项全部通过：

| 测试项 | 结果 |
| :--- | :--- |
| 配对 | ✅ 全部通过 |
| 勾选 | ✅ 1000 次勾选 1.3s |
| 联动 | ✅ 66ms |
| 2000 文件性能 | ✅ 扫描 11.7s，1200 缩略图 |
| v6.0 启动速度 | ✅ 218 ms (150% DPI, 3840×2160) |
| v6.0 内存占用 | ✅ WorkingSet 16.8 MB / Private 4.7 MB |
| v6.0 RAW 缩略图 | ✅ 六大厂商品牌 RAW 成功解析内嵌预览 |

此数据基于极限性能场景，具体性能差异因用户电脑配置不同而异。

---

## <a id="safety-notes"></a> ⚠️ 安全说明

| 中文 |
| :--- |
| 所有删除操作均移入 **Windows 回收站**，可从回收站还原 |
| **不存在任何永久删除调用**，绝不永久删除文件 |
| 格式不符时强制二次确认，即使取消勾选也不会跳过 |
| 单个文件失败不中断流程，失败原因明确列出；文件被占用时自动等待后重试一次 |
| 删除前确认窗口无“×”按钮，默认焦点在“取消”，按 Esc / 回车均为取消 |

---

## <a id="faq"></a> ❓ 常见问题

| 问题 | 回答 |
| :--- | :--- |
| **会永久删除我的照片吗？** | 不会。所有删除都走 Windows 回收站，随时可以还原；程序中没有永久删除的调用。 |
| **会动到已经配好对的文件吗？** | 不会。默认只处理孤立文件；对比界面中已配对的行不可勾选。 |
| **支持哪些格式？** | JPG/JPEG，以及上表 15 个相机品牌的 RAW（RW2、CR3、CR2、NEF、ARW、RAF、ORF、DNG 等）。 |
| **RAW 文件能看到缩略图吗？** | v6.0 起支持解析六大厂商品牌 RAW 内嵌的 JPG 缩略图，RAW 文件也能直接看到照片。个别格式（如 X3F）无法解析时显示后缀占位框。 |
| **支持 macOS / Linux 吗？** | 目前仅提供 Windows 10 / 11 版本。 |
| **怎么切换语言？** | 应用栏右侧的语言下拉框可切换 10 种语言，首次启动按系统语言自动选择，选择会被记住。 |

---

## <a id="changelog"></a> 📝 更新日志

**v6.0** — 原生 C++ 重构 + RAW 缩略图预览
- 新增：RAW 内嵌缩略图预览
- 重构：C++17 + Win32 API 原生实现，不依赖 Python / Qt / .NET / 任何第三方库
- 优化：体积从 11.6 MB 降至 623 KB（只有初版 27.4 MB 的 2%，优化掉了 98%）
- 优化：启动速度从 1–2 s 降至 218 ms
- 优化：扫描、缩略图、EXIF 全部由原生代码实现，运行效率全面升级
- 保持：全部原有功能不变（10 种语言、深浅主题、勾选选择、列表预览联动、EXIF、回收站删除、防误触确认、配置记忆）

**v5.1** — 双界面模式 + 对比视图
- 新增：配对对比界面（JPG | RAW 左右并排，缺失一侧留空，颜色标记：绿=齐全，黄=缺 JPG，红=缺 RAW）
- 新增：界面模式可自主切换（应用栏「界面」下拉框），选择会被记住
- 新增：对比界面「处理」列，明确显示每行是否会删除
- 新增：对比界面「用背景色标记」开关与「只显示缺失」开关
- 新增：对比界面顶部图例实时统计（共 N 组：齐全 x · 缺 RAW y · 缺 JPG z）
- 新增：对比界面支持按 JPG 文件名 / RAW 文件名 / 状态 / 处理排序
- 优化：删除方式圆点改为自绘大圆环，更醒目
- 优化：列宽可拖动，最小列宽 = 表头文字宽度

**v5.0** — 全球化 + 主题系统 + 勾选选择
- 新增：10 种语言支持，首次启动自动检测系统语言
- 新增：相机品牌名本地化
- 新增：深色 / 浅色主题，默认跟随系统
- 新增：列表与预览勾选选择（列表勾选框 / 缩略图角标 / 空格键）
- 新增：勾选状态记忆，删除数量与总大小只统计勾选文件
- 新增：列表与预览双向联动定位
- 新增：自绘圆润滚动条、药丸形按钮、下拉框、滑块、卡片
- 新增：二次确认防误触弹窗
- 优化：软件体积从 16.2 MB 缩减至 11.6 MB

**v4.1**
- 新增：现代卡片式圆角界面
- 优化：打包体积精简（16.2 MB）

**v4.0**
- 新增：回收站删除可恢复（确认弹窗明确提示）
- 新增：EXIF 九字段对齐显示
- 新增：简略 EXIF 模式
- 新增：双击 EXIF 区域或右键菜单复制 EXIF 信息
- 新增：单击缩略图/列表行显示 EXIF
- 新增：双击缩略图跳转资源管理器定位文件
- 新增：预览区滚动自动回到顶部
- 修复：RAW 文件 EXIF 解析（缺失字段显示 “--”）
- 优化：缩略图缓存、多核并行处理
- 优化：软件体积缩减 40%（26.7 MB → 16.2 MB）

**v3.6**
- 新增：状态条固定、卡片等比缩放、模式切换不丢图、EXIF 懒加载与 RAW EXIF 支持

**v3.5**
- 新增：EXIF 信息显示、缩略图缓存与多核并行
- 修复：预览区滚轮卡顿、快速拖动滑块缩略图层叠、上传后文件名变为 default 的问题

**v3.3** — 关于窗口加大、移除手动选择按钮与锁定
**v3.2** — 自动识别显示修正、强制删除、滑块吸附
**v3.1** — 网格预览、缩略图三档、自动识别锁定
**v3.0** — 自动识别、格式不符保护、配置记忆
**v2.0** — 多 RAW 格式、递归扫描
**v1.0** — 基础 RAW / JPG 筛选删除

---

## <a id="author"></a> 👨‍💻 作者

- **KILL-STAR SX**
- GitHub: [KILLSTARSX](https://github.com/KILLSTARSX)
- 哔哩哔哩: [KILL-STAR_SX](https://space.bilibili.com/381623593)

---

## <a id="development-notes"></a> 🛠️ 开发历程与心得

最开始用 Python + tkinter 搭的框架，后来陆续加了 Pillow、多线程、多语言、主题系统这些功能，体积反倒从最初的 27.4MB 一路压到 16.2MB，最后到 11.6MB——每次更新都是功能往上加、体积往下降。但 Python 打包的架构天生有天花板，解释器、Tk 运行库、Pillow 解码模块都是躲不开的硬性开销，再往下优化的空间已经很小了。纠结了很久，我干脆决定彻底重构，用 C++17 + Win32 API 从头写整个软件。过程远没那么轻松：从圆角卡片、药丸按钮到滚动条、下拉框，所有界面都得自己画，还有 10 种语言本地化、TIFF/EXIF 解析、WIC 图像解码、RAW 内嵌缩略图提取、回收站删除、DPI 缩放、深浅主题切换……这些在 Python 里都是现成的库，到 C++ 里全得从零敲。重构前我顾虑了挺久，好在大部分繁琐重复的工作都有 AI 帮忙。换作几年前 AI 还没这么厉害的时候，这么大的重构我想都不敢想，当然这次也确实花了不少钱。最终的结果完全对得起这份付出：体积从 27.4MB 直接砍到 623KB，只剩初版的 2%；启动时间从 1-2 秒缩到 218 毫秒，内存占用也从 55MB 降到 16.7MB。功能不减反增，界面也更美观。这款软件从一开始就是纯公益免费的，就是想让低配置电脑也能用上顺手的优质工具，我自己平时也一直在用。市面上没有的软件，我就从零做一个；市面上有的但是不好用，我就做一个比它更强且免费给大家用。一直觉得用户体验才是根本。现在很多软件为了盈利堆一堆没用的功能和广告，越更越臃肿，越用越卡。我刚好反过来：每次更新都要更小、更快、功能更全，也没为了性能丢了界面颜值。虽说搭进去不少时间精力金钱，但回头看，一切都值得。

---

## 📄 许可证

本项目采用 **KILL-STAR SX 学术源码许可协议 1.0（KS-ASL-1.0）**：源码公开，允许学术与商业使用；衍生开发需提前通知作者并取得书面同意（经同意可闭源，须署名）；收费、付费分发、付费墙或广告变现需另行签订书面许可与收益分配协议；禁止专利化与违法使用。完整文本见 [LICENSE](LICENSE)。

---

## ⭐ 如果觉得有用，欢迎点个 Star！

[![Star History](https://img.shields.io/github/stars/KILLSTARSX/Jpg-Raw-Pair-Cleaner?style=social)](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/stargazers)
[![Fork](https://img.shields.io/github/forks/KILLSTARSX/Jpg-Raw-Pair-Cleaner?style=social)](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/forks)
