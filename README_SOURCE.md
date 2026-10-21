# Jpg-Raw-Pair-Cleaner 5.1 (Python source)

**Author:** KILL-STAR SX  
**Copyright:** Copyright (C) 2026 KILL-STAR SX. All rights reserved.  
**License:** MIT License (see the repository `LICENSE`)  
**Project:** https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner  
**GitHub:** https://github.com/KILLSTARSX  
**bilibili:** https://space.bilibili.com/381623593

A Windows desktop tool for photographers who shoot RAW+JPG: it pairs files by
base name, lists the orphans, and moves only the confirmed files to the Windows
Recycle Bin (recoverable). 10 languages, light/dark themes, JPG preview and EXIF.

## Run from source

```bash
python -m pip install -r requirements.txt
python Jpg-Raw-Pair-Cleaner.py
```

Python 3.10+ on Windows. Pillow / send2trash / exifread are optional: the app
still runs without them, with reduced preview / recycle-bin fallback behaviour.

Diagnostics:

```bash
python Jpg-Raw-Pair-Cleaner.py --selftest <folder-with-photos> report.txt
python Jpg-Raw-Pair-Cleaner.py --version
```

## Files

| File | Purpose |
| --- | --- |
| `Jpg-Raw-Pair-Cleaner.py` | main program |
| `language.json` | 10-language UI resources |
| `camera.ico` | window / taskbar icon (loaded automatically) |
| `requirements.txt` | optional Python dependencies |
| `NOTICE` | attribution / license notice |

## Open-source notice

This project is free and open source under the MIT License. You are welcome to
use, modify and redistribute it, **provided that the copyright notice, author
name (`KILL-STAR SX`), `NOTICE` and `LICENSE` are retained**. Removing the
attribution and presenting the original work as your own is not permitted.

The program also carries a visible attribution in its title bar, the About
window, the source header and the `--version` output.
