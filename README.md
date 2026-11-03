# JPG-RAW Pair Cleaner

[English](README.md) | [简体中文](README.zh-CN.md)

[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)
[![Latest release](https://img.shields.io/github/v/release/KILLSTARSX/Jpg-Raw-Pair-Cleaner)](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/KILLSTARSX/Jpg-Raw-Pair-Cleaner/total)](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/releases)
[![Platform](https://img.shields.io/badge/platform-Windows%2010%2F11-brightgreen)](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/releases/latest)
[![Size](https://img.shields.io/badge/size-623%20KB-brightgreen)](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/releases/latest)
[![Stars](https://img.shields.io/github/stars/KILLSTARSX/Jpg-Raw-Pair-Cleaner?style=social)](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/stargazers)

**Find orphaned JPG/RAW photos, compare pairs side by side, and organize photo folders — all in one lightweight Windows application.** The cleanup tools identify unmatched photos by filename and move selected files to the Windows Recycle Bin. The v6.1 Photo Organizer can also sort JPG and RAW files into configurable folders by format or camera brand.

> **v6.1 — Photo Organization + Pair Comparison Improvements**  
> Adds a dedicated Photo Organizer with live previews, configurable destinations, move/copy modes, and camera-brand-based RAW folders. Pair-comparison sorting and status filtering have also been improved.

> **v6.0 — Native C++ Rewrite**  
> Rebuilt with C++17 and the Win32 API. The single-file executable dropped from 27.4 MB to approximately 623 KB, and measured startup time dropped from 1–2 seconds to 218 ms.

> **Keywords:** orphaned JPG · orphaned RAW · JPG RAW pair · camera RAW cleanup · photo organization · photo culling · RAW file sorter

---

## 📖 Table of Contents

- [What Is an Orphan File?](#what-is-an-orphan-file)
- [Features](#features)
- [Quick Start](#quick-start)
- [Photo Organizer (v6.1)](#photo-organizer-v61)
- [Screenshots](#screenshots)
- [Supported Camera Brands & RAW Formats](#supported-camera-brands--raw-formats)
- [Performance Test Data](#performance-test-data)
- [Safety Notes](#safety-notes)
- [FAQ](#faq)
- [Changelog](#changelog)
- [Author](#author)
- [Development Notes](#development-notes)
- [License](#license)

---

## <a id="what-is-an-orphan-file"></a> 🤔 What Is an Orphan File?

A photo is often stored in two formats: a JPG for quick viewing and a camera RAW file for editing. For example:

```text
IMG_0001.JPG
IMG_0001.CR3
```

If one side is removed — during in-camera culling, an incomplete import, or manual cleanup — the remaining file becomes an **orphan file**.

| Folder contents | Result | How the cleaner handles it |
| :--- | :--- | :--- |
| JPG exists, matching RAW is missing | Orphaned JPG | Lists the JPG for review; moves it to the Recycle Bin only after confirmation |
| RAW exists, matching JPG is missing | Orphaned RAW | Lists the RAW file for review; moves it to the Recycle Bin only after confirmation |
| Both JPG and RAW exist | Complete pair | Not selected for deletion |

The application scans the selected folder, pairs files by **base filename** (the filename without its extension), and identifies the unmatched side. You can scan only the current folder or include subfolders, with configurable scan depth.

---

## <a id="features"></a> ✨ Features

| Feature | Description |
| :--- | :--- |
| 🧹 **JPG / RAW Pair Cleanup** | Finds orphaned JPG or RAW files by base filename. Choose whether to process JPG, RAW, or both; complete pairs are protected from ordinary cleanup. |
| 🗂️ **Photo Organizer (v6.1)** | Sorts JPG and RAW files into separate folders, or creates RAW subfolders by camera brand and file extension. Supports moving or copying. |
| 👀 **Live Organization Preview** | Recalculates the proposed organization automatically and displays file counts, total size, destination folders, sample filenames, and per-folder breakdowns before anything is changed. |
| ↔️ **Two Comparison Modes** | Use the Classic view to see only orphaned files, or the Comparison view to see JPG and RAW side by side. The selected view is remembered. |
| 🧭 **Comparison Sorting & Filtering** | Sort by JPG name, RAW name, folder, status, or action. Click the status legend to filter rows by Complete, Missing RAW, or Missing JPG. |
| 🖼️ **RAW Embedded Thumbnail Preview** | Extracts embedded JPEG previews from RAW files for six major camera brands, allowing supported RAW files to display real thumbnails. |
| ⚡ **Native C++17 / Win32 App** | Native Windows implementation with no Python, Qt, .NET, or third-party runtime/library dependency. Single executable; measured startup time is 218 ms. |
| 📦 **Ultra-Lightweight** | Approximately 623 KB — about 2% of the original 27.4 MB package. |
| 🌐 **10 Languages** | English, Simplified Chinese, Traditional Chinese, Japanese, Korean, French, German, Spanish, Russian, and Portuguese. Detects the system language on first launch; English is the fallback. |
| 🎨 **Dark / Light Themes** | Follows the Windows app theme by default. You can switch themes manually, and your choice is remembered. |
| ☑️ **Flexible Selection** | Select or unselect files in the list, use thumbnail badges, or press Space on a selected row. Only checked files are included in the deletion count. |
| 🔗 **List–Preview Synchronization** | Selecting a list row scrolls to and highlights its thumbnail; selecting a thumbnail locates the corresponding list row. |
| 📷 **EXIF Information** | View compact or detailed EXIF data, including camera, exposure, ISO, focal length, date, resolution, and lens information when available. Copy EXIF data from the interface. |
| 🧠 **RAW Format Detection** | Automatically detects RAW extensions present in the selected folder. Includes 15 camera-brand profiles and supports custom extensions. |
| 📂 **Recursive Scanning** | Scan the current folder, selected subfolder levels, or all subfolders. Files in different subfolders can be paired when included in the same scan. |
| 🗑️ **Recoverable Deletion** | Cleanup operations send files to the Windows Recycle Bin instead of permanently deleting them. |
| 🛡️ **Deletion Confirmation** | Uses a custom confirmation dialog designed to reduce accidental deletion. The Cancel action is the default. |
| ⚙️ **Settings Memory** | Remembers the last folder, RAW mode, scan depth, language, theme, interface mode, window layout, and checkbox selections. |

### The Two Cleanup Views

The application offers two ways to inspect JPG/RAW pairs. Switch between them using the **View** selector in the app bar; the choice is saved for the next launch.

#### 1. Classic View

Displays only files identified as orphans, with filename, file type, size, and folder information. Use it when you want a focused list of files that may need cleanup.

#### 2. Comparison View

Displays each JPG/RAW pair on the same row, making missing files immediately visible.

| Pair status | Row marker | Meaning |
| :--- | :--- | :--- |
| JPG and RAW both exist | **Green** | Complete pair; not eligible for deletion |
| RAW exists, JPG is missing | **Yellow** | Missing JPG; the RAW file is orphaned |
| JPG exists, RAW is missing | **Red** | Missing RAW; the JPG file is orphaned |

Additional comparison-view features:

- **Action column:** Explains whether a row will be deleted. It distinguishes selected orphan files from unchecked files, complete pairs, and files protected because their RAW format is not part of the current matching scope.
- **Clickable status legend:** Click Complete, Missing RAW, or Missing JPG to show only that status. Click the active status again to restore all rows. The legend also displays live counts.
- **Missing-only toggle:** Hides complete pairs so you can focus on unmatched files.
- **Sortable columns:** Click JPG filename, RAW filename, folder, status, or action. Click the same header again to reverse the sort direction; ▲/▼ indicates the current direction.
- **Useful default order:** Missing RAW first, Missing JPG second, and complete pairs last. Rows with the same status are ordered by filename.
- **Consistent selection:** Only rows containing orphaned files can be checked. Complete pairs and format-protected rows cannot be selected for ordinary deletion.
- **Display options:** Choose row-background coloring or text-color marking. The background-color mode preserves the normal text color for readability.

---

## <a id="quick-start"></a> 🚀 Quick Start

Download the latest release from the **[Releases page](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/releases/latest)**. The application supports Windows 10 and Windows 11. The released executable is portable: no installer or separate runtime is required.

### Clean orphaned JPG / RAW files

1. Click **Browse…** and select a photo folder. The application starts scanning automatically.
2. Review the results in Classic View or Comparison View. Uncheck any file you want to keep.
3. Choose the deletion scope (JPG, RAW, or both) as needed, then click **Delete**.
4. Review the confirmation dialog and choose the explicit Delete action. Selected files are moved to the Windows Recycle Bin.

### Organize JPG / RAW files

1. Click **Photo Organizer** in the app bar.
2. Choose the source folder, destination root, and organization mode. The source defaults to the folder selected in the main window.
3. Review the automatically generated folder cards and file statistics. Adjust the options until the preview matches your intended folder structure.
4. Click **Start Organizing** and review the confirmation summary before proceeding.

For more detailed operating instructions, see [User_Manual.txt](User_Manual.txt).

---

## <a id="photo-organizer-v61"></a> 🗂️ Photo Organizer (v6.1)

The Photo Organizer is a separate tool for arranging photo files into folders. It **does not pair, clean, or delete photos**. It only moves or copies JPG and RAW files to the destinations you specify.

### Organization options

| Option | Description |
| :--- | :--- |
| **Source folder** | The folder to organize. Defaults to the folder selected in the main window, but can be changed. |
| **Destination root** | The parent location for the new category folders. Leave it blank to create them inside the source folder; choose another location to organize elsewhere. |
| **JPG / RAW destinations** | Defaults to folders named `JPG` and `RAW`. You can rename these folders or enter full paths to send a category to a specific location. |
| **Organization mode** | **By format** (default): JPG files go to the JPG destination and RAW files go to the RAW destination. **By camera brand:** RAW files are separated into brand/extension-specific subfolders. |
| **RAW folder naming** | In brand mode, choose one of five naming patterns: extension + brand (default), extension only, brand in parentheses, brand only, or extension only as the folder name. The example beside the option updates to show the resulting name. |
| **Copy (keep originals)** | Off by default: files are moved. Turn it on to copy files and leave the originals in place. |
| **Include subfolders** | Off by default: only the selected source folder is processed. Turn it on to include supported photos in its subfolders. |

Examples of RAW subfolder naming patterns:

| Pattern | Example |
| :--- | :--- |
| Extension + brand (default) | `RAW(RW2Panasonic)` |
| Extension only | `RAW(RW2)` |
| Brand in parentheses | `RAW(Panasonic)` |
| Brand only | `Panasonic` |
| Extension only as folder name | `RW2` |

Brand names are localized according to the selected application language. The exact folder name therefore depends on the language and naming option you choose.

### Live preview and workflow

The preview is generated automatically; there is no separate Preview button.

1. **Choose the options.** The preview updates when you change the source, destination, organization mode, naming pattern, or other settings. If no source folder has been selected, the preview explains what is needed.
2. **Review the proposed structure.** The top summary shows the number of files, total size, and number of destination folders. Each destination folder is represented by a card showing its path, file count, size, JPG/RAW breakdown, example filenames, and proportion bar. Previewing does not move or modify files.
3. **Confirm the operation.** Click **Start Organizing**. A confirmation dialog summarizes the folders to be created and the number of files to process.
4. **Check the result.** The preview area becomes a result card showing how many files were moved or copied. Any failures are listed individually. Returning to the main window triggers a fresh scan.

### File-handling safeguards

- **No silent overwrites:** If a different file with the same name already exists at the destination, the incoming file is renamed, for example `IMG_0001 (1).JPG`.
- **Already-organized files are skipped:** Files already in their intended destination are not processed again.
- **Nested destinations are excluded from scanning:** If a destination folder is inside the source folder, the organizer skips that destination while scanning, preventing files it just organized from being picked up again.
- **DNG handling:** `.DNG` is shared by multiple camera brands and cannot always be attributed reliably, so it is grouped into `RAW(DNG)` in brand-based organization.
- **Supported photo extensions:** JPG includes `.jpg` and `.jpeg`; RAW includes the extensions recognized by the application.

---

## <a id="screenshots"></a> 🖼️ Screenshots

<img width="670" height="696" alt="PixPin_2026-11-04_01-27-20" src="https://github.com/user-attachments/assets/d532f88e-582b-478a-8943-94b68e226f28" />
<img width="695" height="852" alt="PixPin_2026-10-25_20-25-14" src="https://github.com/user-attachments/assets/6f78c095-77ad-4632-b292-b93cbcebe952" />


---

## <a id="supported-camera-brands--raw-formats"></a> 📸 Supported Camera Brands & RAW Formats

The application includes **15 built-in camera-brand profiles**. Brand names are localized according to the interface language; for example, Panasonic may appear as `Panasonic`, `松下 Panasonic`, or `パナソニック Panasonic`.

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

Additional format behavior:

- **Automatic detection** identifies RAW suffixes actually present in the selected folder.
- **Custom formats** can be entered as a comma-separated list, for example `.rw2,.dng`.
- Extension matching is case-insensitive.
- If a manually selected brand does not match the RAW files found, those files are protected from ordinary matching/deletion rather than being treated as valid matches by mistake.
- RAW embedded-thumbnail extraction is available for six major camera brands. Other RAW formats may use an extension placeholder in the preview; EXIF fields that cannot be read are shown as `--`.

---

## <a id="performance-test-data"></a> 🧪 Performance Test Data

The following figures come from recorded test scenarios, not a promise of identical results on every computer.

| Test | Recorded result |
| :--- | :--- |
| Native app startup | **218 ms** at 150% display scaling and 3840 × 2160 resolution |
| Executable size | **623 KB**, compared with the original 27.4 MB build |
| Memory usage | Working Set: **16.8 MB** / Private Bytes: **4.7 MB** in the recorded v6.0 test |
| 2,000-file scan scenario | **11.7 seconds**, with 1,200 thumbnails |
| Checkbox interaction | 1,000 selection changes in approximately **1.3 seconds** |
| List–preview synchronization | Approximately **66 ms** in the recorded test |
| RAW thumbnails | Embedded previews successfully parsed from the six supported major-brand groups tested |
| Automated checks | Pairing, selection, organizer rules, and other self-tests passed in the recorded test runs |

Actual performance depends on the computer, storage device, file formats, image sizes, and folder structure.

---

## <a id="safety-notes"></a> ⚠️ Safety Notes

| Area | Safeguard |
| :--- | :--- |
| **Cleanup deletion** | Files selected for cleanup are sent to the **Windows Recycle Bin** and can normally be restored from there. |
| **Permanent deletion** | The cleanup workflow does not call a permanent-delete operation. |
| **Matched pairs** | Complete JPG/RAW pairs are not eligible for ordinary cleanup. In Comparison View, only orphan rows can be checked. |
| **Format mismatch** | RAW files outside the selected matching format are protected. Any force-delete path requires a separate confirmation. |
| **Accidental clicks** | The custom confirmation dialog has no window-close “×” button. Cancel is the default action; Esc and Enter both cancel. |
| **File-level errors** | A failure on one file does not stop the remaining operation. Failed items and their reasons are listed; a file-in-use operation is retried once. |
| **Organizer collisions** | Existing destination files are not silently overwritten; conflicting filenames are automatically renamed. |
| **Move vs. copy** | The Photo Organizer defaults to moving files. Enable **Copy (keep originals)** when you want the source files left untouched. Review the preview and confirmation summary before starting. |

> **Important distinction:** Cleanup sends selected orphan files to the Recycle Bin. The Photo Organizer is a separate operation: it moves or copies files to the destinations you choose. Always review the organizer preview and confirmation summary before proceeding.

---

## <a id="faq"></a> ❓ FAQ

| Question | Answer |
| :--- | :--- |
| **Is cleanup deletion permanent?** | No. Cleanup sends selected files to the Windows Recycle Bin. They can normally be restored from the Recycle Bin. |
| **Will it delete complete JPG/RAW pairs?** | Not during ordinary cleanup. Complete pairs are not selectable for deletion. |
| **Does the Photo Organizer delete files?** | No. It moves or copies JPG/RAW files into the destinations you configure. It does not send files to the Recycle Bin or perform orphan cleanup. |
| **How do I keep the original files when organizing?** | Open Photo Organizer and enable **Copy (keep originals)**. Copy mode leaves the source files in place. |
| **What happens if a destination already contains a file with the same name?** | The organizer does not overwrite a different existing file. It automatically adds a numbered suffix, such as ` (1)`, to the incoming filename. Files already in their intended destination are skipped. |
| **Does organization include subfolders?** | Not by default. Enable **Include subfolders** to include photos in the source folder's subfolders. |
| **Can RAW files be previewed?** | v6.0 added embedded JPEG preview extraction for six major camera-brand groups. Some RAW formats, such as Sigma X3F, may show an extension placeholder instead. |
| **Which formats are supported?** | JPG/JPEG and the RAW extensions listed in [Supported Camera Brands & RAW Formats](#supported-camera-brands--raw-formats). Custom RAW extensions are also supported. |
| **Why is a RAW file marked as a format mismatch?** | The file's extension does not match the currently selected camera brand or custom format. Switch to Automatic Detection or select the correct brand/extension. Mismatched files are protected from ordinary cleanup. |
| **How do I change the language?** | Use the Language selector in the app bar. The application detects the system language on first launch, then remembers your manual selection. Unsupported system languages fall back to English. |
| **How do I change the theme?** | Use the Theme control in the app bar to switch between Light and Dark. The default setting follows the Windows app theme. |
| **Which operating systems are supported?** | Windows 10 and Windows 11. |

---

## <a id="changelog"></a> 📝 Changelog

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

## <a id="author"></a> 👨‍💻 Author

- **KILL-STAR SX**
- GitHub: [KILLSTARSX](https://github.com/KILLSTARSX)
- Bilibili: [KILL-STAR_SX](https://space.bilibili.com/381623593)

---

## <a id="development-notes"></a> 🛠️ Development Notes

This project started as a Python + tkinter application. Over time, I added Pillow-based image handling, multithreading, multilingual support, and a theme system. The executable became progressively smaller — from an initial 27.4 MB to 16.2 MB, and then 11.6 MB — even as features were added. Eventually, however, Python packaging reached a point where the interpreter, GUI runtime, and image-processing modules created a fixed size and startup overhead that was difficult to reduce further.

That led to the v6.0 rewrite: rebuilding the application with **C++17 and the native Win32 API**. It was a substantial undertaking. The interface includes custom-drawn rounded cards, pill-shaped buttons, scrollbars, sliders, and dropdowns, alongside localization, DPI scaling, light/dark themes, image decoding, RAW embedded-thumbnail extraction, EXIF reading, and Recycle Bin integration. Components that had previously been available through Python libraries now had to be integrated through native Windows APIs and application code.

The rewrite reduced the executable from 27.4 MB to approximately 623 KB — around 2% of its original size — while measured startup time fell from 1–2 seconds to 218 ms. The goal was not to remove features to make the application smaller; it was to make the application smaller **without giving up functionality or visual polish**.

With v6.1, development moved beyond cleanup and comparison into everyday photo organization. The new organizer was designed around a practical workflow: choose a source and destinations, inspect a live visual plan, confirm the operation, and then review the result. The intention is to make useful file operations clear before they happen, while protecting existing files from accidental overwrites.

This software has been free and non-commercial from the beginning. I build it to solve a practical problem I encounter myself, and to make a useful, polished tool available even on lower-spec computers. I believe every update should improve the experience — adding useful capabilities while keeping the application compact, responsive, and free of unnecessary clutter or advertisements. AI assistance helped with parts of the rewrite and repetitive development work, but the goal remained the same throughout: put the user's experience first.

---

## <a id="license"></a> 📄 License

This project is licensed under the **Apache License 2.0**. You may use, modify, redistribute, and commercially use the software, including in closed-source products, subject to the terms of Apache 2.0. These include preserving applicable copyright, license, NOTICE, and attribution notices, identifying significant changes, and retaining the license's patent grant and patent-litigation termination provisions. See [LICENSE](LICENSE) for the complete license text.

The author also lists several **additional requests** in [ADDITIONAL-TERMS.md](ADDITIONAL-TERMS.md), including advance notice for derivative projects, discussion before commercializing a derivative, avoiding patents on the original parts, and no illegal use. These are requests only: **they are not additional conditions of the Apache License 2.0 and do not modify or restrict the rights granted by that license**. Where there is any conflict, Apache 2.0 governs.

---

## ⭐ If It Helped, a Star Is Appreciated!

Sponsorship: [Ko-fi](https://ko-fi.com/killstarsx)

[![Star History](https://img.shields.io/github/stars/KILLSTARSX/Jpg-Raw-Pair-Cleaner?style=social)](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/stargazers)
[![Fork](https://img.shields.io/github/forks/KILLSTARSX/Jpg-Raw-Pair-Cleaner?style=social)](https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner/forks)
