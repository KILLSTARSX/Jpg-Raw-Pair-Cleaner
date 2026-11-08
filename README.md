# JPG-RAW Pair Cleaner

[English](README.md) | [简体中文](README.zh-CN.md)

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Latest release](https://img.shields.io/github/v/release/KILLSTARSX/Jpg-Raw-Pair-Cleaner)](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/KILLSTARSX/Jpg-Raw-Pair-Cleaner/total)](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/releases)
[![Platform](https://img.shields.io/badge/platform-Windows%2010%2F11-brightgreen)](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/releases/latest)
[![Size](https://img.shields.io/badge/size-623%20KB-brightgreen)](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/releases/latest)
[![Stars](https://img.shields.io/github/stars/KILLSTARSX/Jpg-Raw-Pair-Cleaner?style=social)](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/stargazers)

**Find orphaned JPG/RAW photos, compare pairs side by side, and organize photo folders — in one lightweight Windows app.** Cleanup matches photos by filename and moves the selected files to the Recycle Bin; the Photo Organizer files them away by format, camera brand, photo orientation, or capture date.

> **v6.2 — Four organization modes, plus a visual and interaction pass**  
> The organizer grows from two modes to four: by format (now including VIDEO), by camera brand, **by photo orientation** (landscape / portrait / square), and **by capture date** (year / month / week / day / specific day). Adds a category color system, a photo-to-folder hint strip, eased dropdown and card animations, and standardized date folder names.

> **v6.1 — Photo Organizer + comparison improvements**  
> A dedicated organizer window with live preview, configurable destinations, move/copy modes, and camera-brand RAW subfolders.

> **v6.0 — Native C++ rewrite**  
> Rebuilt with C++17 and the Win32 API. The single-file executable dropped from 27.4 MB to about 623 KB, and measured startup time from 1–2 s to 218 ms.

> **Keywords:** orphaned JPG · orphaned RAW · JPG RAW pair · photo cleanup · photo organizer · sort photos by orientation · sort by capture date · RAW file sorter

---

## 📖 Table of Contents

- [What Is an Orphan File](#what-is-an-orphan-file)
- [Features](#features)
- [Quick Start](#quick-start)
- [Photo Organizer](#photo-organizer)
- [Screenshots](#screenshots)
- [Supported Camera Brands & RAW Formats](#supported-camera-brands--raw-formats)
- [Performance & Safety](#performance--safety)
- [FAQ](#faq)
- [Changelog](#changelog)
- [Author & License](#author--license)

---

## <a id="what-is-an-orphan-file"></a> 🤔 What Is an Orphan File?

Shooting in JPG + RAW saves every photo twice: a JPG for quick viewing and a RAW file for editing.

```text
IMG_0001.JPG
IMG_0001.CR3
```

If one side disappears — in-camera culling, an incomplete import, an earlier manual cleanup — the remaining file becomes an **orphan file**.

| Folder contents | Result | How the cleaner handles it |
| :--- | :--- | :--- |
| JPG exists, matching RAW is missing | Orphaned JPG | Lists it for review; moves it to the Recycle Bin only after confirmation |
| RAW exists, matching JPG is missing | Orphaned RAW | Lists it for review; moves it to the Recycle Bin only after confirmation |
| Both JPG and RAW exist | Complete pair | Never selectable for deletion |

Pairs are matched by **base filename** (the name without its extension). Scans can cover the current folder, a chosen number of subfolder levels, or everything.

---

## <a id="features"></a> ✨ Features

| Feature | Description |
| :--- | :--- |
| 🧹 **JPG / RAW pair cleanup** | Pairs files by base name and finds the orphaned side. Process JPG only, RAW only, or both; complete pairs are never touched. |
| 🗂️ **Photo Organizer (v6.2)** | Four modes: by format (JPG / RAW / VIDEO), by camera brand, **by photo orientation**, and **by capture date**. Move or copy, with a full preview and a confirmation step. |
| 🧭 **Orientation sorting** | Decides landscape / portrait / square from the **display proportions after EXIF orientation is applied**, picked with whole-card buttons. Three folders, or two folders where you choose which one takes the square shots. |
| 📅 **Capture-date sorting** | Group by year, month, week, day, or a single chosen day. Folder names follow `2026`, `2026-11`, `2026-W45`, `2026-11-04`; weeks use ISO 8601, so year boundaries land in the right week-year. |
| 🎨 **Category colors** | Blue for JPG and landscape, amber for RAW and portrait, soft green for square, violet for video. The color shows up on folder icons, folder labels, and proportion bars, so categories are readable without text. |
| 👀 **Live organization preview** | Counts, total size, destination folders, and sample filenames update automatically. Previewing never touches a file. |
| ↔️ **Two cleanup views** | Classic lists only orphans; Comparison puts each JPG and RAW on one row so the missing side is obvious. Your choice is remembered. |
| 🧭 **Sorting and filtering** | Sort by JPG name, RAW name, folder, status, or action; click the status legend to show one category at a time. |
| 🖼️ **RAW embedded thumbnails** | Pulls the embedded JPEG preview out of RAW files from six major brands, so those RAW files show real thumbnails. |
| 📷 **EXIF panel** | Compact and detailed modes covering camera, exposure, ISO, focal length, date, resolution, and lens, with copy-to-clipboard. ARW tag merging and date fallback are fixed. |
| ⚡ **Native C++17 / Win32** | No Python, Qt, .NET, or third-party runtime. One executable, measured startup at 218 ms. |
| 🌐 **10 languages** | English, Simplified Chinese, Traditional Chinese, Japanese, Korean, French, German, Spanish, Russian, Portuguese. Detected from the system language on first launch, English as fallback. |
| 🎨 **Dark / light themes** | Follows the Windows app theme by default; manual choice is remembered. |
| ☑️ **Flexible selection** | Checkboxes, thumbnail badges, or Space on a focused row. Only checked files count toward deletion. |
| 🔗 **List–preview sync** | Selecting a row scrolls to and highlights its thumbnail, and the reverse works too. |
| 🗑️ **Recoverable deletion** | Cleanup only ever sends files to the Windows Recycle Bin. |
| 🛡️ **Misclick protection** | A custom confirmation dialog with no title-bar “×”, focused on Cancel by default. |
| ⚙️ **Settings memory** | Remembers the last folder, RAW mode, scan depth, language, theme, view mode, window layout, and checked rows. |

### The two cleanup views

Switch with the **View** selector in the app bar; the choice is saved.

**Classic** lists only orphaned files (name, type, size, folder) — the fastest way to skim what will go.

**Comparison** puts each JPG and its RAW on the same row:

| Pair status | Row marker | Meaning |
| :--- | :--- | :--- |
| Both sides present | **Green** | Complete pair, not selectable |
| RAW present, JPG missing | **Yellow** | Missing JPG; the RAW file is orphaned |
| JPG present, RAW missing | **Red** | Missing RAW; the JPG file is orphaned |

The comparison view also provides:

- **Action column** — states outright whether the row will be deleted (Delete / Keep · unchecked / Keep · paired / Keep · format unmatched).
- **Clickable status legend** — filter by Complete, Missing RAW, or Missing JPG; click again to clear. Counts are live.
- **Missing-only toggle** — hides complete pairs.
- **Sortable headers** — all five columns, click again to reverse, ▲/▼ shows the direction. Default order: Missing RAW → Missing JPG → Complete.
- **Marker style** — full-row background color, or text color only.

---

## <a id="quick-start"></a> 🚀 Quick Start

Download the latest build from the **[Releases page](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/releases/latest)**. Windows 10 / 11, portable single executable, no installer and no runtime.

> **Seeing “Unknown publisher” on first run?** That is normal for a self-signed certificate. Unzip [证书.7z](证书.7z) and run `安装证书.bat` once — it installs and removes the certificate, and one install covers all future updates. The app still runs without it; Windows just shows an extra warning.

### Clean orphaned JPG / RAW

1. Click **Browse…** and pick a folder — scanning starts automatically.
2. Review the results in either view and uncheck anything you want to keep.
3. Choose the scope (JPG only / RAW only / both) and click **Delete**.
4. Confirm in the dialog; only then are the files moved to the Recycle Bin.

### Organize JPG / RAW

1. Click **Photo Organizer** in the app bar.
2. Choose the source folder, destination root, and organization mode (the source defaults to the folder open in the main window).
3. Review the folder cards and statistics, and adjust options until the preview matches what you expect.
4. Click **Start Organizing** and check the summary before it runs.

Full instructions: [User_Manual.txt](User_Manual.txt).

---

## <a id="photo-organizer"></a> 🗂️ Photo Organizer (v6.2)

The organizer is a separate archiving tool: it **does not pair, clean, or delete anything**. It only moves or copies files according to your rules.

### Four organization modes

| Mode | Rule | Folders created |
| :--- | :--- | :--- |
| **By format** | JPG, RAW, and VIDEO each go to their own folder | `JPG`, `RAW`, `VIDEO` |
| **By camera brand** | RAW is split into brand/extension subfolders; video stays separate | `JPG`, `RAW(RW2Panasonic)`, …, `VIDEO` |
| **By orientation** | Landscape, portrait, and square, judged on displayed proportions | `Landscape`, `Portrait`, `Square` |
| **By capture date** | Year, month, week, day, or one specific day | `2026`, `2026-11`, `2026-W45`, `2026-11-04` |

Folder names are editable, and you can enter a full path to send one category somewhere else. The default destination is the source folder itself.

### By orientation

The decision uses the **proportions after EXIF orientation is applied** — a 4:3 photo shot vertically is not mistaken for landscape just because of pixel order.

- **Three folders**: landscape, portrait, and square each get one.
- **Two folders**: only landscape and portrait exist, and you pick which one takes the square shots by clicking the corresponding card. **Start is disabled until you choose** — the app never decides for you.

The three shapes are drawn at fixed ratios (3:2, 2:3, 1:1) with the caption below the shape, so the portrait silhouette can never be squashed into a square to fit text.

### By capture date

| Grouping | Folder name |
| :--- | :--- |
| By year | `2026` |
| By month | `2026-11` |
| By week | `2026-W45` |
| By day | `2026-11-04` |
| Specific day | `2026-11-04` (only that day is organized; everything else stays put) |

Weeks follow **ISO 8601**: Monday is the first day, week 1 contains January 4, and dates near a year boundary belong to their ISO week-year (`2027-01-01 → 2026-W53`, `2024-12-30 → 2025-W01`). There is only one week algorithm in the app, and selecting “By week” shows a one-line note explaining it.

Dates are read in the existing priority order: photo EXIF → video container creation time (MP4 / MOV / MKV headers, AVI ICRD, UTC converted to local) → file timestamp. Files with no readable date can either go to a separate “unknown date” folder or be skipped; the preview marks where each date came from.

### Colors and hints

Blue for JPG and landscape, amber for RAW and portrait, soft green for square, violet for video — applied to folder icons, folder labels, and proportion bars, with separate palettes for light and dark themes. In orientation mode a hint strip under the cards spells out the mapping (“Landscape photos → Landscape folder”); in two-folder mode the square entry takes the color of the folder you picked, and shows a warning color until you pick one.

### Safeguards

- **No silent overwrites** — an existing different file with the same name gets a numbered suffix, e.g. `IMG_0001 (1).JPG`.
- **Already-organized files are skipped**, so re-running the same organize task is safe.
- **Nested destinations are excluded from the scan**, so freshly organized files are not picked up again.
- **DNG is grouped as `RAW(DNG)`** in brand mode, because several brands share the extension.
- **Failures don’t abort the run** — each failed file is reported with its reason.

---

## <a id="screenshots"></a> 🖼️ Screenshots

<img width="670" height="696" alt="Photo Organizer" src="https://github.com/user-attachments/assets/d532f88e-582b-478a-8943-94b68e226f28" />
<img width="695" height="852" alt="Comparison view" src="https://github.com/user-attachments/assets/6f78c095-77ad-4632-b292-b93cbcebe952" />

---

## <a id="supported-camera-brands--raw-formats"></a> 📸 Supported Camera Brands & RAW Formats

**15 built-in brand profiles.** Brand names are localized to the interface language (Panasonic may read `Panasonic`, `松下 Panasonic`, or `パナソニック Panasonic`).

| Camera brand | Recognized RAW suffixes |
| :--- | :--- |
| Panasonic | `.RW2` |
| Canon | `.CR3` / `.CR2` / `.CRW` |
| Nikon | `.NEF` / `.NRW` |
| Sony | `.ARW` / `.SR2` / `.SRF` |
| Fujifilm | `.RAF` |
| Olympus | `.ORF` |
| Pentax | `.PEF` |
| Sigma | `.X3F` |
| Samsung | `.SRW` |
| Ricoh | `.DNG` |
| Leica | `.DNG` |
| Hasselblad | `.3FR` |
| Phase One | `.IIQ` |
| Mamiya | `.MEF` |
| Leaf | `.MOS` |

Other rules:

- **Auto-detect** — detects which RAW suffixes actually exist in the selected folder.
- **Custom formats** — enter several suffixes separated by commas, e.g. `.rw2,.dng`.
- **Case-insensitive**; both `.jpg` and `.jpeg` count as JPG.
- **Format-mismatch protection** — files whose suffix does not match the selected brand are protected and never treated as orphans.
- **UNKNOWN EXIF FIELDS show `--`** — the app does not guess.

---

## <a id="performance--safety"></a> 🧪 Performance & Safety

| Item | Measured result |
| :--- | :--- |
| Startup | about **218 ms** at 150% scaling, 3840 × 2160 |
| Executable size | **623 KB** (2% of the original 27.4 MB) |
| Memory (v6.0 record) | Working set 16.8 MB / private bytes 4.7 MB |
| 2000-file scan | about **11.7 s**, including 1200 thumbnails |
| 1000 checkbox toggles | about **1.3 s** |
| List–preview sync | about **66 ms** |

| Safety mechanism | Detail |
| :--- | :--- |
| **Cleanup deletion** | Moves files to the Recycle Bin only; permanent delete is never called. |
| **Complete pairs** | Not selectable; in the comparison view only orphan rows can be checked. |
| **Format mismatch** | Protected; forced deletion requires a separate confirmation. |
| **Misclick protection** | The confirmation dialog has no “×” and focuses Cancel by default. |
| **Organizer** | Moves by default — enable **Copy** to keep originals, and always check the preview and summary first. |

> Cleanup and organizing are separate operations: one sends selected orphans to the Recycle Bin, the other moves or copies files between folders and **deletes nothing**.

---

## <a id="faq"></a> ❓ FAQ

| Question | Answer |
| :--- | :--- |
| **Is cleanup permanent?** | No — files go to the Recycle Bin and can normally be restored. |
| **Can complete pairs be deleted by accident?** | No, they are not selectable. |
| **Does the organizer delete files?** | No, it only moves or copies. |
| **How do I keep the originals while organizing?** | Enable **Copy (keep originals)**. |
| **What if a file with the same name already exists at the destination?** | It is renamed with a numbered suffix instead of overwritten; files already in place are skipped. |
| **Where do square photos go in two-folder mode?** | Into the folder you picked. Until you pick one, **Start Organizing** stays disabled. |
| **Why does a week number belong to the previous year?** | That is ISO 8601: the date belongs to its ISO week-year, which may differ from the calendar year. |
| **Can RAW files show thumbnails?** | Six major brands expose an embedded preview; other formats show a suffix placeholder. |
| **Which formats are supported?** | JPG / JPEG plus the RAW suffixes above, and custom extensions. |
| **How do I change language or theme?** | The **Language** and **Theme** selectors in the app bar; the language is detected once, then your manual choice wins. |
| **Which systems are supported?** | Windows 10 / 11. |
| **My antivirus flags the app — what now?** | Installing the certificate cannot guarantee a clean verdict; if it is a false positive, whitelist it or report it to the vendor. |

---

## <a id="changelog"></a> 📝 Changelog

### **v6.2 — Four organization modes + visual and interaction pass**

- **New: organize by photo orientation.** Landscape / portrait / square, judged from the display proportions after EXIF orientation correction. Whole-card buttons, three-folder or two-folder mode, and in two-folder mode the square destination is your choice — Start is disabled until you make it.
- **New: organize by capture date.** Year / month / week / day / specific day, with standardized folder names `YYYY`, `YYYY-MM`, `YYYY-Www`, `YYYY-MM-DD`. Weeks are ISO 8601 and correct across year boundaries; the misleading “ISO week” jargon is gone from the UI.
- **New: VIDEO support in format mode** — video files get their own folder, dated from the container creation time.
- **New: category color system.** Blue for JPG / landscape, amber for RAW / portrait, soft green for square, violet for video, applied consistently to icons, labels, and bars.
- **New: orientation hint strip** that states the photo-to-folder mapping outright, and follows your choice in two-folder mode.
- **New: lightweight eased animations.** Dropdowns fade in over 150 ms with a small upward shift and fade out over 110 ms; buttons, cards, and the slider share the same curves. Skipped entirely when Windows “Show animations” is off.
- **Fixed: black nubs on rounded corners** of the calendar and dropdowns — they now use true per-pixel transparency on layered windows.
- **Fixed: empty EXIF on ARW files** — all-zero thumbnail-IFD tags no longer overwrite the main IFD, and the date falls back from original → digitized → modified.
- **Fixed: truncated button captions at 1080p** — widths are now measured in device pixels with a safety margin.
- **Fixed: neutral Chinese being detected as Traditional**, and “specific day” reverting to “by year” after the year mode was added.

### **v6.1 — Photo Organization + Pair Comparison Improvements**

- **New: Photo Organizer** — organize JPG and RAW files into separate destinations, or sort RAW files into camera-brand/extension subfolders.
- **New: Two organization modes** — organize by format (JPG / RAW) or by camera brand. Brand mode offers five RAW folder-naming patterns, including extension + brand, extension only, brand in parentheses, brand only, and suffix-only folder names.
- **New: Configurable destinations** — source folder defaults to the main window's selected folder; destination root defaults to the source folder. JPG/RAW folder names can be customized, or replaced with full paths.
- **New: Move or copy** — moving is the default; Copy mode preserves the original files. Optional recursive organization includes subfolders.
- **New: Automatic visual plan preview** — live summary of file count, total size, and destination-folder count, followed by a card for each destination with its path, file breakdown, sample filenames, and size. The preview updates automatically and does not modify files.
- **New: Confirmation and result summary** — review the planned folders and file count before execution; afterward, see moved/copied totals and any individual failures.
- **Safety: Collision handling** — never silently overwrites a different file; conflicting names receive a numbered suffix. Files already in their destination are skipped, and destination folders nested under the source are excluded from scanning. Shared `.DNG` files are grouped under `RAW(DNG)` in brand mode.
- **Optimized: Comparison sorting** — all five text columns (JPG, RAW, folder, status, and action) can be sorted in either direction. The default status order is Missing RAW → Missing JPG → Complete.
- **New: Clickable status filters** — select Complete, Missing RAW, or Missing JPG from the legend to filter the comparison list; click again to clear the filter.
- **Improved: First-launch language detection** — Simplified Chinese system locales map to Simplified Chinese; Traditional Chinese locales, including Taiwan, Hong Kong, and Macau, map to Traditional Chinese. Unsupported languages fall back to English, and the detected choice is saved.
- **Fixed: About-window flicker** — buffered drawing removes visual flicker when hovering over links.
- **Fixed: Organizer preview spacing** — removed the unnecessary divider and adjusted the spacing between the summary area and folder cards.

### **v6.0 — Native C++ Rewrite + RAW Thumbnail Preview**

- **New:** RAW embedded thumbnail preview.
- **Rewrite:** Native C++17 + Win32 API; no Python / Qt / .NET / third-party runtime or library dependencies.
- **Optimized:** Executable size reduced from 11.6 MB to 623 KB — approximately 2% of the original 27.4 MB build.
- **Optimized:** Startup time reduced from 1–2 seconds to 218 ms in the recorded test.
- **Optimized:** Scanning, thumbnail handling, and EXIF reading implemented natively.
- **Kept:** Existing features, including 10 languages, light/dark themes, checkbox selection, list–preview synchronization, EXIF, Recycle Bin deletion, mis-touch protection, and settings memory.

### **v5.1 — Dual UI Modes + Comparison View**

- **New:** Comparison view with JPG and RAW displayed side by side. Missing sides are left blank; green indicates a complete pair, yellow indicates Missing JPG, and red indicates Missing RAW.
- **New:** Switch between Classic and Comparison views from the app-bar View selector; the selection is remembered.
- **New:** Action column explains whether a row will be deleted and why it may be kept.
- **New:** Background-color marking and Missing-only options.
- **New:** Live status legend showing total pairs, complete pairs, Missing RAW, and Missing JPG.
- **New:** Sorting by JPG filename, RAW filename, status, and action.
- **Optimized:** Larger custom-drawn radio controls for the deletion mode.
- **Optimized:** Resizable columns with a minimum width based on the header text.

### **v5.0 — Localization + Themes + Checkbox Selection**

- **New:** 10 languages with first-launch system-language detection.
- **New:** Localized camera-brand names.
- **New:** Light and Dark themes, following the system by default.
- **New:** Selection controls in both the file list and thumbnail preview (list checkbox, thumbnail badge, and Space key).
- **New:** Remembered checkbox state; deletion totals include checked files only.
- **New:** Bidirectional list–preview synchronization.
- **New:** Custom-drawn rounded scrollbars, pill buttons, dropdowns, sliders, and cards.
- **New:** Custom confirmation dialog designed to reduce accidental deletion.
- **Optimized:** Package size reduced from 16.2 MB to 11.6 MB.

### **v4.1**

- **New:** Modern rounded-card interface.
- **Optimized:** Package size reduced to approximately 16.2 MB.

### **v4.0**

- **New:** Recoverable deletion through the Windows Recycle Bin, with an explicit confirmation dialog.
- **New:** Aligned nine-field detailed EXIF display and a compact EXIF mode.
- **New:** Copy EXIF by double-clicking the EXIF area or using the right-click menu.
- **New:** Click a thumbnail or list row to display the photo's EXIF information.
- **New:** Double-click a thumbnail to locate the file in Windows Explorer.
- **New:** Preview automatically scrolls to the top after changing folders.
- **Fixed:** RAW EXIF parsing; unavailable fields display `--`.
- **Optimized:** Thumbnail caching and multi-core parallel processing.
- **Optimized:** Package size reduced by approximately 40% (26.7 MB → 16.2 MB).

### **v3.6**

- **New:** Fixed status bar, proportional card scaling, thumbnails retained when switching modes, lazy EXIF loading, and RAW EXIF support.

### **v3.5**

- **New:** EXIF display, thumbnail cache, and multi-core parallel processing.
- **Fixed:** Preview scroll-wheel stutter, thumbnail stacking while dragging the size slider, and filename reset after folder selection.

### **v3.3**

- **New:** Larger About window.
- **Removed:** Manual-select button and its associated locking logic.

### **v3.2**

- **New:** Automatic-detection display fix, force-delete option, and slider snapping.

### **v3.1**

- **New:** Grid preview, three thumbnail sizes, and automatic-detection lock.

### **v3.0**

- **New:** Automatic RAW detection, format-mismatch protection, and settings memory.

### **v2.0**

- **New:** Multiple RAW format support and recursive scanning.

### **v1.0**

- **New:** Basic JPG / RAW filtering and deletion.

---

## <a id="author--license"></a> 👨‍💻 Author & License

- **KILL-STAR SX** · [GitHub](https://github.com/KILLSTARSX) · [bilibili](https://space.bilibili.com/381623593)

Released under the **Apache License 2.0**: commercial and closed-source use is fine, provided you keep the copyright notice, LICENSE, NOTICE and attribution, state your changes, and preserve the patent grant and patent-litigation termination terms. See [LICENSE](LICENSE).

[ADDITIONAL-TERMS.md](ADDITIONAL-TERMS.md) records a few **additional requests** (advance notice for derivatives, a conversation before commercializing, no patenting of the original parts, no unlawful use). They are **not additional conditions of Apache 2.0** and do not change or limit the rights it grants; if anything conflicts, Apache 2.0 wins.

### Development notes

The project started as Python + tkinter, then grew Pillow, threading, localization and themes while shrinking from 27.4 MB to 11.6 MB. Python packaging has an irreducible baseline cost, though, so v6.0 was a full rewrite in C++17 + Win32: rounded cards, pill buttons, scrollbars, sliders and dropdowns all redrawn, with localization, DPI scaling, image decoding, RAW thumbnails, EXIF, and Recycle Bin handling rebuilt on native APIs.

v6.1 extended the scope from cleaning to organizing; v6.2 turned organizing into four combinable modes and brought the UI details — colors, corners, animation, date naming — up to the same standard as the cleanup side.

The app stays free and non-commercial. The principle hasn’t changed: **features can grow, the program shouldn’t bloat; speed matters, and so does the experience.**

---

## ⭐ If this project helped, a star is appreciated!

<details>
<summary>Click to support the author (buy me a coffee ☕)</summary>

<br>

<img src="assets/wechat-sponsor.jpg" alt="WeChat sponsor QR code" width="240">

WeChat sponsor QR code
</details>

[![Star History](https://img.shields.io/github/stars/KILLSTARSX/Jpg-Raw-Pair-Cleaner?style=social)](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/stargazers)
[![Fork](https://img.shields.io/github/forks/KILLSTARSX/Jpg-Raw-Pair-Cleaner?style=social)](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/forks)
