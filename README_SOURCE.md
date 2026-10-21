# Jpg-Raw-Pair-Cleaner 5.1 (Python source)

**Author:** KILL-STAR SX  
**Copyright:** Copyright (C) 2026 KILL-STAR SX. All rights reserved.  
**License:** KILL-STAR SX Academic Source License 1.0 (KS-ASL-1.0) — source-available, **not** OSI open source, **not** MIT. Full text: [`LICENSE`](LICENSE).  
**Project:** https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner  
**GitHub:** https://github.com/KILLSTARSX  
**bilibili:** https://space.bilibili.com/381623593

A Windows desktop tool for photographers who shoot RAW+JPG: it pairs files by
base name, lists the orphans, and moves only the confirmed files to the Windows
Recycle Bin (recoverable). 10 languages, light/dark themes, JPG preview and EXIF.
It is provided primarily for **academic discussion and research**; commercial use
is permitted under the license conditions below.

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
| `LICENSE` | full license text (KS-ASL-1.0) |
| `NOTICE` | attribution / license notice |

## License summary

This is a **source-available** license, not an open-source license. You may
view, study, compile and use the Software, including for commercial purposes,
provided you keep the attribution to **KILL-STAR SX** and the original project.

- **Derivative works:** notify the Author in advance and obtain written consent.
  With consent, a derivative may be closed-source, but it must retain
  attribution and comply with the commercial/fee, patent and lawful-use rules.
- **Commercial use** is permitted. **Charging fees**, paid distribution,
  paywalls, advertising monetization or similar revenue requires a separate
  written license and a revenue-sharing agreement with the Author.
- **No patenting** the Software, any part of it, or a derivative work.
- **No illegal use**; the user bears all consequences.
- The Software is provided **AS IS**, without warranty; the Author is not liable
  for damages.

For derivative permission, commercial licensing or revenue sharing, contact the
Author via the repository Issues, GitHub profile or bilibili link above.

## Attribution

Any permitted use or derivative work must display:

> Based on Jpg-Raw-Pair-Cleaner by KILL-STAR SX  
> https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner

and retain the copyright, license and disclaimer notices.

The program also carries a visible attribution in its title bar, the About
window, the source header and the `--version` output.
