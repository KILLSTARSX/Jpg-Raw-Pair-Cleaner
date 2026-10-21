# Jpg-Raw-Pair-Cleaner 5.1 (Python source)

**Author:** KILL-STAR SX  
**Copyright:** Copyright (C) 2026 KILL-STAR SX. All rights reserved.  
**License:** Apache License, Version 2.0 (see [`LICENSE`](LICENSE))  
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
| `LICENSE` | Apache License 2.0 full text |
| `NOTICE` | copyright, attribution and license notice |
| `ADDITIONAL-TERMS.md` | author's supplemental requests (not license conditions) |

## License

This project is licensed under the **Apache License, Version 2.0**.
You may use, modify, distribute and commercialize the Software, including in
closed-source products, provided you comply with Apache 2.0 — in particular:

- keep the copyright, license and NOTICE notices;
- state significant changes in modified files;
- retain the patent grant and patent-retaliation terms of Apache 2.0.

Apache 2.0 already grants a patent license and terminates it if you sue over
patents covering the Software. See [`LICENSE`](LICENSE) for the full text.

## Additional requests (not license conditions)

The author additionally requests attribution to **KILL-STAR SX** and the
original project, advance notice before building a derivative, a separate
written agreement before charging fees, no patenting of the original parts, and
no illegal use. These are recorded in [`ADDITIONAL-TERMS.md`](ADDITIONAL-TERMS.md).

**They are not part of Apache 2.0 and do not modify or restrict the rights
Apache 2.0 grants.** If they conflict with Apache 2.0, Apache 2.0 controls. To
make them legally binding, a separate written agreement is required.

The program also carries a visible attribution in its title bar, the About
window, the source header and the `--version` output.
