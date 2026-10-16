# JPG-RAW Pair Cleaner

[English](README.md) | [简体中文](README.zh-CN.md)

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Latest release](https://img.shields.io/github/v/release/KILLSTARSX/Jpg-Raw-Pair-Cleaner)](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/KILLSTARSX/Jpg-Raw-Pair-Cleaner/total)](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/releases)
[![Platform](https://img.shields.io/badge/platform-Windows%2010%2F11-brightgreen)](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/releases/latest)
[![Size](https://img.shields.io/badge/size-613%20KB-brightgreen)](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/releases/latest)
[![Stars](https://img.shields.io/github/stars/KILLSTARSX/Jpg-Raw-Pair-Cleaner?style=social)](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/stargazers)

Clean orphaned JPG/RAW files, filter and delete JPG & RAW photos in sync. Only 613 KB. Supports 15+ brands, 10 languages, dark/light themes, with Recycle Bin recovery.

💥 **v6.0 C++ rewrite: from 27.4 MB to 613 KB — just 2% of the size, with more features. Starts in 218 ms. Small enough to slip into an SD card without noticing.**

> **Keywords**: orphaned jpg · orphaned raw · jpg raw pair · delete jpg with raw · camera raw cleanup · photo culling leftovers

---

## 📖 Table of Contents

- [What is an orphan file?](#what-is-an-orphan-file)
- [Features](#features)
- [Quick Start](#quick-start)
- [Screenshots](#screenshots)
- [Supported Camera Brands & RAW Formats](#supported-camera-brands--raw-formats)
- [Performance Test Data](#performance-test-data)
- [Safety Notes](#safety-notes)
- [FAQ](#faq)
- [Changelog](#changelog)
- [Author](#author)
- [Development Notes](#development-notes)

---

## <a id="what-is-an-orphan-file"></a> 🤔 What is an orphan file?

One photo usually exists as a pair — IMG_0001.JPG + IMG_0001.CR3. Delete one side (in-camera culling, a half-finished import, a past manual cleanup) and the other becomes an **orphan file**.

| Situation | Result | How this tool handles it |
| :--- | :--- | :--- |
| JPG without RAW | Orphaned JPG | Listed; moved to Recycle Bin after confirmation |
| RAW without JPG | Orphaned RAW | Listed; moved to Recycle Bin after confirmation |
| Both sides present | Normal pair | Never selected, never deleted |

Scans a folder (recursively if you want), pairs files by base name, and lists only the leftover half for you to confirm.

---

## <a id="features"></a> ✨ Features

| English |
| :--- |
| 🧹 **JPG / RAW Synchronized Cleanup**：Delete JPG and RAW together. Auto-pairs by base name; matched files are never touched |
| 📦 **Ultra-Light**：613 KB – only 2% of the original 27.4 MB, 98% of the size optimized away; hundreds of times smaller than a single JPG photo |
| ⚡ **Native C++ Rewrite**：C++17 + Win32 API. No Python, no Qt, no .NET, no third-party libraries. Single exe, 218 ms startup |
| 🖼️ **RAW Embedded Thumbnail Preview (v6.0 new)**：Parses embedded JPG previews from six major camera brands – RAW files now show real photos |
| 🖥️ **Two UI Modes**：Classic (orphans only) and Comparison (JPG/RAW side by side, missing side highlighted); choice is remembered |
| 🌐 **10 Languages**：English / 简体中文 / 繁體中文 / 日本語 / 한국어 / Français / Deutsch / Español / Русский / Português, auto-detects system language on first launch |
| 🎨 **Dark/Light Theme**：One-click toggle, follows system by default, all controls re-color cleanly |
| ☑️ **Checkbox Selection**：List checkboxes / thumbnail badges / spacebar – deletion count only includes checked files |
| 🔗 **List-Preview Sync**：Click a list row to scroll to and highlight its thumbnail; click a thumbnail to locate its list row |
| 🧠 **Smart Detection**：Auto-detects RAW format, supports 15+ brands with localized brand names |
| 📂 **Recursive Scan**：Scans subfolders with configurable depth, cross-folder pairing |
| 📷 **EXIF Display**：Click to view EXIF, compact/detailed mode toggle with one-click copy |
| 🗑️ **Safe Deletion**：All files moved to Windows Recycle Bin, fully recoverable |
| 🛡️ **Mis-touch Protection**：Custom dialog with no “×” button, focus defaults to “Cancel” |
| ⚙️ **Settings Memory**：Remembers folder, format, theme, language, UI mode, checkbox states, etc. |

---

## <a id="quick-start"></a> 🚀 Quick Start

Download the latest build from the **[Releases page](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/releases/latest)** (Windows 10 / 11), double-click to run — no installer and no runtime required.

| Step | English |
| :--- | :--- |
| ① | Click “Browse…” to select folder → scanning starts automatically |
| ② | Review files in the orphan list or comparison view (uncheck any you want to keep) |
| ③ | Click “Delete” → click the round “Delete” button in the dialog → done |

For detailed instructions, see [User_Manual.txt](User_Manual.txt).

---

## <a id="screenshots"></a> 🖼️ Screenshots

<img width="1437" height="1353" alt="JPG-RAW Pair Cleaner UI" src="https://github.com/user-attachments/assets/6872ee45-132b-431d-b612-24e041bc0896" />

---

## <a id="supported-camera-brands--raw-formats"></a> 📸 Supported Camera Brands & RAW Formats

15 built-in brands with localized display names per UI language (e.g. “Panasonic” in English, “松下 Panasonic” in Simplified Chinese, “パナソニック Panasonic” in Japanese).

| Brand | RAW Suffix(es) |
| :--- | :--- |
| Panasonic | .RW2 |
| Canon | .CR3 / .CR2 / .CRW |
| Nikon | .NEF / .NRW |
| Sony | .ARW / .SR2 / .SRF |
| Fujifilm | .RAF |
| Olympus | .ORF |
| Pentax | .PEF |
| Sigma | .X3F |
| Samsung | .SRW |
| Ricoh | .DNG |
| Leica | .DNG |
| Hasselblad | .3FR |
| Phase One | .IIQ |
| Mamiya | .MEF |
| Leaf | .MOS |

---

## <a id="performance-test-data"></a> 🧪 Performance Test Data

Measured under extreme performance scenarios. All tests passed.

| Test Item | Result |
| :--- | :--- |
| Pairing | ✅ Passed |
| Checkbox selection | ✅ 1000 checks in 1.3s |
| List-preview sync | ✅ 66ms |
| 2000-file performance | ✅ Scan 11.7s, 1200 thumbnails |
| v6.0 startup | ✅ 218 ms (150% DPI, 3840×2160) |
| v6.0 memory | ✅ WorkingSet 16.8 MB / Private 4.7 MB |
| v6.0 RAW thumbnails | ✅ Embedded previews parsed from all six major brands |

This data is based on extreme performance scenarios; actual performance may vary depending on your computer configuration.

---

## <a id="safety-notes"></a> ⚠️ Safety Notes

| English |
| :--- |
| All deletions go to **Windows Recycle Bin** – restorable at any time |
| **No permanent deletion calls** – files are never permanently deleted |
| Force re-confirmation on format mismatch, even if checkbox is unchecked |
| Individual file failure won't interrupt the process; reasons are clearly listed; auto-retry once if file is in use |
| Confirmation dialog has no “×” button, focus defaults to “Cancel”, Esc/Enter both cancel |

---

## <a id="faq"></a> ❓ FAQ

| Question | Answer |
| :--- | :--- |
| **Is deletion permanent?** | No. All deletions go through the Windows Recycle Bin and can be restored at any time; there is no permanent-delete call in the program. |
| **Will it touch matched pairs?** | No. Only orphaned files are processed by default; paired rows in the comparison view cannot be checked. |
| **Which formats are supported?** | JPG/JPEG, plus RAW from the 15 camera brands listed above (RW2, CR3, CR2, NEF, ARW, RAF, ORF, DNG, etc.). |
| **Can RAW files show thumbnails?** | Since v6.0, embedded JPG previews from six major camera brands are parsed, so RAW files can show real photos. A few formats (e.g. X3F) fall back to a suffix placeholder. |
| **Other platforms?** | Windows 10 / 11 only. |
| **How to change language?** | Use the language dropdown on the right of the app bar — 10 languages, auto-detected on first launch, and the choice is remembered. |

---

## <a id="changelog"></a> 📝 Changelog

**v6.0** — Native C++ Rewrite + RAW Thumbnail Preview

Rewritten entirely in C++17 + Win32 API. No Python, no Qt, no .NET, no third-party libraries. Single exe, ready to run.

- New: RAW embedded thumbnail preview (parses embedded JPG previews from six major camera brands)
- New: Synchronized deletion of JPG and RAW files (auto-pairs by base name; matched files never touched)
- Rewrite: Native C++17 + Win32 API, no Python / Qt / .NET / any third-party library
- Optimized: Size from 11.6 MB to 613 KB (only 2% of the original 27.4 MB, 98% optimized away)
- Optimized: Startup from 1–2 s to 218 ms
- Optimized: Scanning, thumbnails, EXIF all implemented natively, overall efficiency upgraded
- Kept: All original features (10 languages, themes, checkbox selection, list-preview sync, EXIF, Recycle Bin deletion, mis-touch protection, settings memory)

**v5.1** — Dual UI Modes + Comparison View
- New: Comparison view (JPG | RAW side by side, missing side left blank, color markers: green = paired, yellow = missing JPG, red = missing RAW)
- New: UI mode switchable (app bar “View” dropdown), choice is remembered
- New: “Action” column in comparison view showing whether each row will be deleted
- New: “Mark with background color” and “Missing only” toggles
- New: Live legend at top (Total N: paired x · missing RAW y · missing JPG z)
- New: Sort by JPG filename / RAW filename / Status / Action
- Optimized: Larger custom-drawn radio dots for deletion mode
- Optimized: Draggable column widths; minimum width = header text width

**v5.0** — Globalization + Theme System + Checkbox Selection
- New: 10 languages, auto-detects system language on first launch
- New: Localized camera brand names
- New: Dark / light theme, follows system by default
- New: Checkbox selection in list and preview (list checkbox / thumbnail badge / spacebar)
- New: Checkbox state memory; deletion count only counts checked files
- New: Bidirectional list-preview sync
- New: Custom-drawn rounded scrollbars, pill buttons, dropdowns, sliders, cards
- New: Mis-touch-proof confirmation dialog
- Optimized: Size from 16.2 MB to 11.6 MB

**v4.1**
- New: Modern rounded-card UI
- Optimized: Packed size reduced (16.2 MB)

**v4.0**
- New: Recoverable Recycle Bin deletion (explicit confirmation dialog)
- New: 9-field aligned EXIF display
- New: Compact EXIF mode
- New: Double-click EXIF area or right-click menu to copy EXIF
- New: Click thumbnail / list row to show EXIF
- New: Double-click thumbnail to locate file in Explorer
- New: Preview auto-scrolls to top after folder change
- Fixed: RAW EXIF parsing (missing fields show “--”)
- Optimized: Thumbnail cache, multi-core parallel processing
- Optimized: Size reduced 40% (26.7 MB → 16.2 MB)

**v3.6**
- New: Fixed status bar, proportional card scaling, thumbnails kept on mode switch, EXIF lazy loading, RAW EXIF support

**v3.5**
- New: EXIF display, thumbnail cache, multi-core parallel
- Fixed: Scroll wheel stutter in preview, thumbnail stacking when dragging slider, filename becoming default after upload

**v3.3** — Larger About window, removed manual select button and lock logic
**v3.2** — Auto-detect display fix, force delete, slider snapping
**v3.1** — Grid preview, three thumbnail sizes, auto-detect lock
**v3.0** — Auto-detect, format mismatch protection, settings memory
**v2.0** — Multiple RAW formats, recursive scanning
**v1.0** — Basic RAW / JPG filter deletion

---

## <a id="author"></a> 👨‍💻 Author

- **KILL-STAR SX**
- GitHub: [KILLSTARSX](https://github.com/KILLSTARSX)
- Bilibili: [KILL-STAR_SX](https://space.bilibili.com/381623593)

---

## <a id="development-notes"></a> 🛠️ Development Notes

At first, I built the framework with Python + tkinter. Over time, I added Pillow, multithreading, multilingual support, and a theme system. Surprisingly, the size kept shrinking — from the initial 27.4 MB down to 16.2 MB, and eventually to 11.6 MB. Every update added features while reducing size. But Python packaging has a natural ceiling. The interpreter, Tk runtime, and Pillow decoding modules are unavoidable fixed overheads, and there was very little room left for further optimization. After struggling with this for a long time, I decided to do a complete rewrite — using C++17 + Win32 API to build the entire application from scratch. The process was far from easy. From rounded cards and pill buttons to scrollbars and dropdowns, every part of the UI had to be hand-drawn. Add to that 10-language localization, TIFF/EXIF parsing, WIC image decoding, RAW embedded thumbnail extraction, Recycle Bin deletion, DPI scaling, and dark/light theme switching — all of which are readily available libraries in Python, but had to be written from zero in C++. Before starting the rewrite, I hesitated for quite a while. Fortunately, most of the tedious and repetitive work was handled with AI assistance. Years ago, when AI wasn't this capable, I wouldn't have even dared to imagine such a large-scale rewrite — and it did cost me a fair amount of money. The final result was well worth the effort: the size dropped from 27.4 MB straight down to 613 KB — only 2% of the original. Startup time went from 1–2 seconds to 218 ms, and memory usage fell from 55 MB to 16.7 MB. Features didn't decrease; they increased, and the interface became more polished. This software has been completely free and non-commercial from the very beginning. My goal is to let low-spec computers enjoy a high-quality, handy tool — and I use it myself all the time. If something doesn't exist on the market, I build it from scratch. If it exists but isn't good enough, I make a better one and give it away for free. I've always believed that user experience comes first. Many software products today pile on useless features and ads for profit, becoming more bloated and laggy with every update. I do the opposite: every update should be smaller, faster, and more feature-rich — without sacrificing visual polish for performance. It took a lot of time, energy, and money, but looking back, it was all worth it.

---

## 📄 License

This project is licensed under the **MIT License** – completely free and open source, see [LICENSE](LICENSE).

---

## ⭐ If it helped, a star is appreciated!

[![Star History](https://img.shields.io/github/stars/KILLSTARSX/Jpg-Raw-Pair-Cleaner?style=social)](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/stargazers)
[![Fork](https://img.shields.io/github/forks/KILLSTARSX/Jpg-Raw-Pair-Cleaner?style=social)](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/forks)
