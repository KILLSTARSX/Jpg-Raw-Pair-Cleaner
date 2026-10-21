# -*- coding: utf-8 -*-
# ============================================================================
# Jpg-Raw-Pair-Cleaner 5.1
# Copyright (C) 2026 KILL-STAR SX. All rights reserved.
# Licensed under the KILL-STAR SX Academic Source License 1.0. See LICENSE.
# Original project: https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner
#
# This copyright and license notice is part of the source code and must be
# retained in copies or substantial portions of the Software (KS-ASL-1.0).
# ============================================================================
"""
相机照片筛选工具 v5.1
=====================

功能概述
--------
扫描用户指定的文件夹中的 .jpg 与相机 RAW 文件，按文件名基础名（去掉扩展名）
配对，找出"未配对"的孤立文件：
  - 同一基础名同时存在至少一个 .jpg 与至少一个 RAW -> 已配对，不处理；
  - 只有 .jpg 没有 RAW -> 孤立 JPG 文件；
  - 只有 RAW 没有 .jpg -> 孤立 RAW 文件。
用户可选择只删除孤立 JPG、只删除孤立 RAW，或全部删除。
删除一律移入 Windows 回收站（可恢复），绝不使用永久删除。

v4.0 新特性
-----------
- 删除逻辑：恢复【回收站删除】（移入 Windows 回收站，可从回收站恢复；
  send2trash 或 ctypes SHFileOperationW 双保险），并完全移除 Ctrl+Z
  撤销功能（操作栈 / PowerShell 还原 / UI 提示均删除）；
- 修复 JPG 文件占用：所有图片读取使用 with 上下文管理，缩略图生成后立即
  转为独立内存副本（.copy()）并关闭原对象；EXIF 懒加载读取后立即释放
  句柄；删除失败自动等待 100ms 重试一次；
- EXIF 展示双模式：详细模式固定 9 个字段行（Make/Model/光圈/快门/ISO/
  焦距/拍摄日期/分辨率/镜头型号），JPG 与 RAW 字段数完全一致、缺失显示
  "--"；简略模式仅相机 + 分辨率（固定高度，布局零跳动）；两模式共享
  同一份缓存数据；
- 中英文界面实时切换（无需重启）：语言标签位于选择框左侧；语言资源
  外置于 language.json，便于维护；
- 保留：RAW EXIF 轻量解析器、EXIF 懒加载、缩略图缓存、多核并行、
  状态条固定、卡片等比缩放等 v3.6 已验证成果。

v3.6 新特性
-----------
- 修复：预览区状态提示文字固定显示（不再随缩略图内容滚动）；
- 修复：切换缩略图档位时整个卡片（图片/边框/间距/文件名区）等比缩放，
  文件名始终完整可见；
- 修复：切换删除方式后缩略图保留在内存缓存中，不再出现"加载中"，
  无需重新扫描；
- EXIF 增强：增加镜头型号字段；改为单击照片时才按需解析（懒加载）；
- RAW EXIF：新增轻量 TIFF 结构解析器，支持读取主流 RAW（松下 RW2 /
  佳能 CR3 / 尼康 NEF / 索尼 ARW / 富士 RAF / 奥林巴斯 ORF / 宾得 PEF /
  DNG / 哈苏 3FR / 飞思 IIQ / 玛米亚 MEF / 利图 MOS 等）的内嵌 EXIF，
  无法解析的格式（如适马 X3F）保持友好提示；
- 新增：删除后支持 Ctrl+Z 从回收站撤销最近一次删除（还原到原位置）。

v3.5 新特性
-----------
- 修复：预览区任意位置（含空白区域）滚轮均可流畅滚动；
- 修复：快速拖动缩略图滑块不再出现层叠/变形（拖动中防抖，不重建）；
- 修复：文件名标签不再被遮挡（单元格预留足够高度、单行固定）；
- 新增：双击预览缩略图/占位框，打开资源管理器定位文件（与列表双击一致）；
- 新增：单击缩略图或列表行，在预览区右上角显示照片 EXIF 关键信息
  （相机/光圈/快门/ISO/焦距/拍摄日期/分辨率）；
- 性能：缩略图只解码一次并缓存最小档（120px），切换大小仅等比缩放、
  不重新解码；解码与 EXIF 读取使用 ThreadPoolExecutor 多核并行；
- 体积/内存：单元格持有图片引用、旧图及时释放，降低运行内存。

v3.3 新特性
-----------
- 首次成功删除后固定 2 秒弹出感谢"关于"，同一设备只弹一次；
- 关于对话框显示面积加大；
- 移除"手动选择"按钮与锁定机制：自动识别完成后相机品牌下拉框保持
  显示"自动识别"且可直接操作（选品牌即切换手动模式，无需锁定）；
- 强制删除保护判定扩大：文件夹中没有任何已知 RAW、或检测到的格式
  与所选不符，均视为"未匹配"，删除按钮切换为"强制删除"并强制二次确认。

v3.2 新特性
-----------
- 自动识别扫描完成后：相机品牌下拉框保持显示"自动识别"并锁定，
  识别到的后缀显示在"后缀"输入框内；
- 未匹配到任何 RAW 格式时，删除按钮变为"强制删除"，删除前强制弹出
  二次确认（警告未匹配），防止误删；
- 缩略图大小滑块自动吸附到 小/中/大 三个档位；
- 关于对话框改为自定义窗口（不触发系统提示音、文字可复制、主页与
  哔哩哔哩链接可直接点击）；首次成功删除文件后 1~3 秒自动弹出
  感谢开发者信息，同一台设备只弹出一次。

v3.1 新特性
-----------
- 相片预览改为多列网格布局：每行数量随窗口宽度自动计算，调整窗口大小时
  排列与缩略图自动适应（防抖重建），垂直滚动、无横向滚动条；
- 缩略图大小三档可调（小 120 / 中 200 / 大 320，默认"中"），滑块切换后
  后台异步重新生成，默认尺寸更小、采用低质量抽帧解码，降低内存占用；
- 自动识别模式扫描完成后，RAW 格式下拉框自动显示识别到的后缀（如 RW2）
  并锁定为灰色禁用状态，点击"手动选择"按钮可改为手动选择品牌。

v3.0 新特性
-----------
- RAW 格式"自动识别"：扫描文件夹实际存在的已知 RAW 扩展名，自动参与配对；
  手动选择品牌或自定义后缀时，若文件夹内 RAW 格式与所选不符，状态栏提示
  "检测到文件夹内 RAW 格式为 XXX，与所选格式不符…"，且不匹配格式的 RAW
  文件不会被判定为孤立 RAW（防止误删）。
- 相片预览区：将被删除的文件纵向排列，JPG 缩略图保持原始宽高比、无白边，
  RAW 显示正方形占位框（居中显示后缀名）；垂直滚动；高度可用分隔条拖拽调整。
- 配置记忆：文件夹、RAW 格式选择、扫描层级、二次确认勾选、窗口大小与预览
  高度保存到 %APPDATA%\\相机照片筛选工具\\config.json，下次启动自动恢复。
- 浏览选择文件夹后自动开始扫描。
- 默认窗口加长，主要区域一屏可见。

删除实现
--------
优先使用 send2trash 库；若未安装，自动回退到 ctypes 调用
Windows Shell API SHFileOperationW（带 FOF_ALLOWUNDO 标志）。
两种方式都只会把文件移入回收站。

环境要求
--------
- Windows + Python 3.10 及以上
- Pillow>=9.1（生成缩略图，缺失时仅预览功能不可用）
- send2trash>=1.8.2（可选：未安装时自动使用 ctypes 备用方案）
"""

import ctypes
import json
import os
import queue
import re
import struct
import subprocess
import sys
import threading
import time
import tkinter as tk
import webbrowser
from concurrent.futures import ThreadPoolExecutor, as_completed
from ctypes import wintypes
from dataclasses import dataclass, field
from tkinter import filedialog, messagebox, ttk

# ---------- 基本信息 ----------

APP_NAME = "Jpg-Raw-Pair-Cleaner"
APP_VERSION = "5.1"
APP_AUTHOR = "KILL-STAR SX"
GITHUB_URL = "https://github.com/KILLSTARSX"            # 开发者主页
BILIBILI_URL = "https://space.bilibili.com/381623593"   # 开发者哔哩哔哩
APP_COPYRIGHT = "Copyright (C) 2026 KILL-STAR SX"
APP_LICENSE = "KILL-STAR SX Academic Source License 1.0"
PROJECT_URL = "https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner"

# 模块级开源归属信息（与关于窗口、--version 输出保持一致；请勿删除）
__author__ = APP_AUTHOR
__copyright__ = APP_COPYRIGHT
__license__ = "KS-ASL-1.0"
__project__ = PROJECT_URL

# ---------- 支持的语言（英语为默认回退语言；简体/繁体/英语必备） ----------

LANGUAGES = [
    ("en", "English"),
    ("zh-CN", "简体中文"),
    ("zh-TW", "繁體中文"),
    ("ja", "日本語"),
    ("ko", "한국어"),
    ("fr", "Français"),
    ("de", "Deutsch"),
    ("es", "Español"),
    ("ru", "Русский"),
    ("pt", "Português"),
]
LANG_CODES = [code for code, _name in LANGUAGES]
LANG_NATIVE = dict(LANGUAGES)
FALLBACK_LANG = "en"


def lang_label_text(code: str) -> str:
    """语言下拉框左侧标签：中文界面显示 "Language"，其他语言显示"语言"，
    保证任何语言的用户都能找到语言切换入口。"""
    return "Language" if str(code).lower().startswith("zh") else "语言"


def detect_system_language() -> str:
    """首次启动时按系统 UI 语言选择界面语言：
    中文系统：简体 -> zh-CN，繁体（台湾/香港）-> zh-TW；其余按主要语言匹配；
    未支持的语言一律回退英语。"""
    try:
        if sys.platform == "win32":
            langid = ctypes.windll.kernel32.GetUserDefaultUILanguage()
            primary = langid & 0x03FF
            sub = (langid >> 10) & 0x03FF
            if primary == 0x04:  # 中文
                # Windows 中文子语言：0x01 繁体(台湾) 0x02 简体(大陆)
                # 0x03 繁体(香港) 0x04 简体(新加坡) 0x05 繁体(澳门)
                return "zh-CN" if sub in (0x02, 0x04) else "zh-TW"
            table = {0x09: "en", 0x11: "ja", 0x12: "ko", 0x0C: "fr",
                     0x07: "de", 0x0A: "es", 0x19: "ru", 0x16: "pt"}
            return table.get(primary, FALLBACK_LANG)
    except Exception:
        pass
    # 非 Windows（源码调试）或调用失败：尝试环境变量
    try:
        loc = (os.environ.get("LANG") or os.environ.get("LC_ALL") or "").lower()
        if loc.startswith("zh"):
            return "zh-TW" if ("tw" in loc or "hk" in loc or "hant" in loc) else "zh-CN"
        for code in LANG_CODES:
            if loc.startswith(code):
                return code
    except Exception:
        pass
    return FALLBACK_LANG


def detect_system_dark() -> bool:
    """读取 Windows 应用主题设置：深色返回 True（失败一律浅色）。"""
    try:
        import winreg
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
        value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
        winreg.CloseKey(key)
        return int(value) == 0
    except Exception:
        return False


# ---------- 主题配色（浅色 / 深色，运行时切换并记住选择） ----------

THEME_LIGHT = {
    "bg": "#eef1f6",          # 窗口底色
    "card": "#ffffff",        # 卡片/面板底色
    "card_alt": "#f6f8fc",    # 次级面板底色
    "border": "#d9e0ea",      # 分隔线与卡片描边
    "text": "#1e2733",        # 主文字
    "muted": "#6d7987",       # 次要文字
    "accent": "#2f6bd8",      # 主题色（主按钮/选中）
    "accent_dark": "#2559b8",  # 主题色（悬停/按下）
    "accent_soft": "#e7effc",  # 主题色浅底（选中行/高亮）
    "danger": "#d9453a",      # 危险操作（删除）
    "danger_dark": "#bf3a30",
    "ok": "#2f9e63",          # 正常/成功
    "row_alt": "#f7f9fc",     # 列表隔行底色
    "cell": "#f2f5fa",        # 预览单元底色
    "cell_hover": "#e8eefb",  # 预览单元悬停底色
    "raw_box": "#eaeff7",     # RAW 占位框底色
    "scroll": "#c3ccda",      # 自绘滚动条滑块
    "scroll_hover": "#a6b3c6",
    "trough": "#e8ecf3",      # 自绘滚动条轨道
    "disabled_bg": "#f5f6f9",
    "disabled_fg": "#a8b0bb",
    # 对比视图：齐全 / 缺 RAW / 缺 JPG 的行底色与文字色
    "pair_ok_bg": "#e2f5e8",
    "pair_ok_fg": "#1c6b38",
    "pair_no_raw_bg": "#fde4e1",      # 缺 RAW（红）
    "pair_no_raw_fg": "#b3261e",
    "pair_no_jpg_bg": "#fdf1d2",      # 缺 JPG（黄）
    "pair_no_jpg_fg": "#8a6100",
}

THEME_DARK = {
    "bg": "#14171d",
    "card": "#1e222b",
    "card_alt": "#252a34",
    "border": "#333a46",
    "text": "#e6eaf1",
    "muted": "#98a2b1",
    "accent": "#4c8dff",
    "accent_dark": "#3a76e0",
    "accent_soft": "#26344c",
    "danger": "#e0574c",
    "danger_dark": "#c4473d",
    "ok": "#3fb27a",
    "row_alt": "#222731",
    "cell": "#252b36",
    "cell_hover": "#2f3948",
    "raw_box": "#2a3140",
    "scroll": "#48525f",
    "scroll_hover": "#5d6a7a",
    "trough": "#1a1e26",
    "disabled_bg": "#262b34",
    "disabled_fg": "#6a7382",
    # 对比视图：齐全 / 缺 RAW / 缺 JPG 的行底色与文字色（深色主题用低饱和深底）
    "pair_ok_bg": "#17301f",
    "pair_ok_fg": "#79d39b",
    "pair_no_raw_bg": "#3a1e1c",
    "pair_no_raw_fg": "#ff9c92",
    "pair_no_jpg_bg": "#3a2f14",
    "pair_no_jpg_fg": "#ffd479",
}

THEMES = {"light": THEME_LIGHT, "dark": THEME_DARK}
# 当前主题（运行时按主题开关就地更新；界面控件统一读取 UI[...]）
UI = dict(THEME_LIGHT)


def set_theme(name: str):
    """切换当前主题配色（就地更新 UI 字典，控件无需重新创建）。"""
    UI.clear()
    UI.update(THEMES.get(name, THEME_LIGHT))


def resolve_theme(pref: str) -> str:
    """把配置里的主题偏好（auto/light/dark）解析为实际主题名。"""
    if pref == "dark":
        return "dark"
    if pref == "light":
        return "light"
    return "dark" if detect_system_dark() else "light"


UI_FONT_CANDIDATES = ("Microsoft YaHei UI", "Microsoft YaHei", "Segoe UI", "Tahoma")

# ---------- 第三方库（缺失时降级运行，不影响核心功能） ----------

try:
    import send2trash  # 回收站删除库（Windows 下内部走 IFileOperation）
    SEND2TRASH_AVAILABLE = True
except ImportError:  # 未安装时使用 ctypes 备用方案
    SEND2TRASH_AVAILABLE = False

try:
    from PIL import Image, ImageTk  # 缩略图预览
    PILLOW_AVAILABLE = True
    try:
        RESAMPLE_LANCZOS = Image.Resampling.LANCZOS  # Pillow >= 9.1
    except AttributeError:
        RESAMPLE_LANCZOS = Image.LANCZOS             # 旧版 Pillow 兼容
except ImportError:
    PILLOW_AVAILABLE = False
    RESAMPLE_LANCZOS = None

try:
    import exifread  # 纯 Python EXIF 解析（JPG 与 TIFF-based RAW 优先使用）
    EXIFREAD_AVAILABLE = True
except ImportError:
    EXIFREAD_AVAILABLE = False

# ---------- RAW 品牌与后缀对照表（品牌名按界面语言本地化 + 保留英文原名） ----------
# id：稳定的内部标识（写入配置，不随语言变化）；en：英文原名（回退显示）；
# local：各语言当地通用名（与英文相同或缺失时只显示英文，不重复）
BRANDS = [
    {"id": "panasonic", "en": "Panasonic", "exts": (".rw2",),
     "local": {"zh-CN": "松下", "zh-TW": "松下", "ja": "パナソニック", "ko": "파나소닉"}},
    {"id": "canon", "en": "Canon", "exts": (".cr3", ".cr2", ".crw"),
     "local": {"zh-CN": "佳能", "zh-TW": "佳能", "ja": "キヤノン", "ko": "캐논"}},
    {"id": "nikon", "en": "Nikon", "exts": (".nef", ".nrw"),
     "local": {"zh-CN": "尼康", "zh-TW": "尼康", "ja": "ニコン", "ko": "니콘", "ru": "Никон"}},
    {"id": "sony", "en": "Sony", "exts": (".arw", ".sr2", ".srf"),
     "local": {"zh-CN": "索尼", "zh-TW": "索尼", "ja": "ソニー", "ko": "소니", "ru": "Сони"}},
    {"id": "fujifilm", "en": "Fujifilm", "exts": (".raf",),
     "local": {"zh-CN": "富士", "zh-TW": "富士", "ja": "富士フイルム", "ko": "후지필름",
               "ru": "Фуджифильм"}},
    {"id": "olympus", "en": "Olympus", "exts": (".orf",),
     "local": {"zh-CN": "奥林巴斯", "zh-TW": "奧林巴斯", "ja": "オリンパス", "ko": "올림푸스",
               "ru": "Олимпус"}},
    {"id": "pentax", "en": "Pentax", "exts": (".pef",),
     "local": {"zh-CN": "宾得", "zh-TW": "賓得", "ja": "ペンタックス", "ko": "펜탁스",
               "ru": "Пентакс"}},
    {"id": "sigma", "en": "Sigma", "exts": (".x3f",),
     "local": {"zh-CN": "适马", "zh-TW": "適馬", "ja": "シグマ", "ko": "시그마", "ru": "Сигма"}},
    {"id": "samsung", "en": "Samsung", "exts": (".srw",),
     "local": {"zh-CN": "三星", "zh-TW": "三星", "ja": "サムスン", "ko": "삼성", "ru": "Самсунг"}},
    {"id": "ricoh", "en": "Ricoh", "exts": (".dng",),
     "local": {"zh-CN": "理光", "zh-TW": "理光", "ja": "リコー", "ko": "리코", "ru": "Рико"}},
    {"id": "leica", "en": "Leica", "exts": (".dng",),
     "local": {"zh-CN": "徕卡", "zh-TW": "徠卡", "ja": "ライカ", "ko": "라이카", "ru": "Лейка"}},
    {"id": "hasselblad", "en": "Hasselblad", "exts": (".3fr",),
     "local": {"zh-CN": "哈苏", "zh-TW": "哈蘇", "ja": "ハッセルブラッド", "ko": "핫셀블라드",
               "ru": "Хассельблад"}},
    {"id": "phaseone", "en": "Phase One", "exts": (".iiq",),
     "local": {"zh-CN": "飞思", "zh-TW": "飛思", "ja": "フェーズワン", "ko": "페이즈원"}},
    {"id": "mamiya", "en": "Mamiya", "exts": (".mef",),
     "local": {"zh-CN": "玛米亚", "zh-TW": "瑪米亞", "ja": "マミヤ", "ko": "마미야", "ru": "Мамия"}},
    {"id": "leaf", "en": "Leaf", "exts": (".mos",),
     "local": {"zh-CN": "利图", "zh-TW": "利圖", "ja": "リーフ", "ko": "리프"}},
]
BRAND_BY_ID = {b["id"]: b for b in BRANDS}
RAW_FORMATS = {b["id"]: b["exts"] for b in BRANDS}   # 兼容既有调用：按 id 取后缀
ALL_KNOWN_RAW_EXTS = frozenset(ext for b in BRANDS for ext in b["exts"])

AUTO_ID = "auto"       # 下拉框第一项（默认）
CUSTOM_ID = "custom"   # 手动输入后缀

# 关于窗口与 README 共用的更新日志版本号（只列大功能，顺序为新 -> 旧）
CHANGELOG_VERSIONS = ("51", "50", "41", "40", "36", "35", "30", "20", "10")

# 勾选状态符号（Treeview 单元格与预览角标共用）
CHECK_ON = "☑"
CHECK_OFF = "☐"


def brand_display(brand: dict, lang: str) -> str:
    """品牌显示名：当地通用名 + 英文原名（两者相同或没有当地名时只显示英文）。"""
    local = brand["local"].get(lang) or brand["local"].get(str(lang).split("-")[0]) or ""
    en = brand["en"]
    if not local or local.strip().lower() == en.strip().lower():
        return en
    return f"{local} {en}"


# 旧配置兼容：v4.x 把界面显示名（中文+英文/纯中文）直接存进配置，这里映射回稳定 id
LEGACY_RAW_MODE = {"自动识别": AUTO_ID, "自定义": CUSTOM_ID}
for _b in BRANDS:
    LEGACY_RAW_MODE.setdefault(f"{_b['local'].get('zh-CN', _b['en'])} {_b['en']}", _b["id"])
    LEGACY_RAW_MODE.setdefault(_b["zh-CN"] if "zh-CN" in _b else _b["en"], _b["id"])
    LEGACY_RAW_MODE.setdefault(_b["local"].get("zh-CN", ""), _b["id"])
    LEGACY_RAW_MODE.setdefault(_b["en"], _b["id"])

# ---------- 扫描范围选项（稳定 id 写入配置，界面按语言显示） ----------

SCAN_LEVEL_IDS = ("cur", "l1", "l2", "all")
SCAN_LEVEL_MAX_DEPTH = {
    "cur": 0,     # 只扫第一级
    "l1": 1,      # 第一级 + 下一级
    "l2": 2,      # 第一级 + 下两级
    "all": None,  # 不限层级
}
# 旧配置兼容：v4.x 保存的是界面上的中文选项文本
LEGACY_SCAN_LEVEL = {
    "仅当前文件夹": "cur", "包含一级子文件夹": "l1",
    "包含二级子文件夹": "l2", "包含所有子文件夹": "all",
}

# ---------- 回收站删除模块 ----------


def move_to_recycle_bin(path: str) -> None:
    """把单个文件移入 Windows 回收站（可从回收站恢复）。"""
    if SEND2TRASH_AVAILABLE:
        send2trash.send2trash(path)
    else:
        _recycle_with_shell_api(path)


def _recycle_with_shell_api(path: str) -> None:
    """备用方案：ctypes 调用 SHFileOperationW + FOF_ALLOWUNDO 移入回收站。"""
    if sys.platform != "win32" or not hasattr(ctypes, "windll"):
        raise OSError("回收站删除功能仅支持 Windows 系统。")

    FO_DELETE = 0x0003
    FOF_SILENT = 0x0004          # 不显示进度对话框
    FOF_NOCONFIRMATION = 0x0010  # 不弹系统确认框（程序自身已有二次确认）
    FOF_ALLOWUNDO = 0x0040       # 关键标志：允许撤销 => 移入回收站而非永久删除
    FOF_NOERRORUI = 0x0400       # 出错时不弹系统对话框，由程序自行报告

    class SHFILEOPSTRUCTW(ctypes.Structure):
        _fields_ = [
            ("hwnd", wintypes.HWND),
            ("wFunc", wintypes.UINT),
            ("pFrom", wintypes.LPCWSTR),
            ("pTo", wintypes.LPCWSTR),
            ("fFlags", wintypes.INT),
            ("fAnyOperationsAborted", wintypes.BOOL),
            ("hNameMappings", wintypes.LPVOID),
            ("lpszProgressTitle", wintypes.LPCWSTR),
        ]

    # pFrom 必须是双 \0 结尾的缓冲区（需 cast 成 LPCWSTR 指针类型）
    buf = ctypes.create_unicode_buffer(path + "\0\0")
    op = SHFILEOPSTRUCTW()
    op.hwnd = None
    op.wFunc = FO_DELETE
    op.pFrom = ctypes.cast(buf, wintypes.LPCWSTR)
    op.pTo = None
    op.fFlags = FOF_ALLOWUNDO | FOF_NOCONFIRMATION | FOF_SILENT | FOF_NOERRORUI
    op.fAnyOperationsAborted = 0
    op.hNameMappings = None
    op.lpszProgressTitle = None

    result = ctypes.windll.shell32.SHFileOperationW(ctypes.byref(op))
    if result != 0:
        raise OSError(f"回收站删除失败（错误码 0x{result:X}）")
    if op.fAnyOperationsAborted:
        raise OSError("删除操作被用户取消")


def _recycle_with_retry(path: str) -> None:
    """移入回收站；首次失败（如文件被占用）等待 100ms 后重试一次。"""
    for attempt in range(2):
        try:
            move_to_recycle_bin(path)
            return
        except PermissionError:
            if attempt == 0:
                time.sleep(0.1)  # 等待占用方释放文件句柄
                continue
            raise


def resource_path(rel_path: str) -> str:
    """资源文件路径：兼容源码运行与 PyInstaller 打包（onefile 解压到 _MEIPASS）。"""
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, rel_path)


# ---------- 界面语言（i18n） ----------

# 外置语言资源（language.json）读取失败时的内置兜底（精简版，仅覆盖最常用键）
_BUILTIN_LANG = {
    "en": {
        "app_title": "Jpg-Raw-Pair-Cleaner", "target_folder": "Target folder:",
        "browse": "Browse...", "scan": "Scan", "about": "About", "language": "语言",
        "auto_label": "Auto-detect", "custom_label": "Custom",
        "auto_placeholder": "(Auto-detect)", "field_sep": ": ",
        "confirm_delete": "Delete", "force_delete": "Force Delete",
        "delete_btn_fmt": "Delete ({n}, {size})",
        "force_btn_fmt": "Force Delete ({n}, {size})",
        "status_scanning": "Scanning...", "status_no_orphan": "No unmatched files found.",
        "exif_hint": "Click a photo to view EXIF", "exif_detail": "Detailed EXIF",
        "exif_brief": "Brief EXIF", "exif_make": "Make", "exif_model": "Model",
        "exif_copy_all": "Copy all EXIF", "exif_copied": "EXIF copied to clipboard",
        "loading": "Loading...", "thumb_small": "Small", "thumb_medium": "Medium",
        "thumb_large": "Large", "col_check": "Del", "check_hint": "Checked = delete",
        "select_all": "Select all", "select_none": "Select none",
        "theme": "Theme", "theme_light": "Light", "theme_dark": "Dark",
        "confirm_ok": "Delete", "confirm_cancel": "Cancel",
        "about_author": "Author", "about_copyright": "Copyright", "about_license": "License", "about_project": "Project",
        "view": "View", "view_classic": "Classic list", "view_pair": "Pair compare",
        "pair_frame": "Pair comparison (JPG | RAW)", "pair_col_jpg": "JPG file",
        "pair_col_raw": "RAW file", "pair_col_status": "Status",
        "pair_status_ok": "Complete", "pair_status_no_raw": "Missing RAW",
        "pair_status_no_jpg": "Missing JPG", "pair_status_mismatch": "format not matched",
        "pair_only_missing": "Only missing", "pair_bg_mode": "Mark by background",
        "pair_count_fmt": "Total {total} pairs: complete {ok} \u00b7 missing RAW "
                          "{no_raw} \u00b7 missing JPG {no_jpg}",
        "pair_col_action": "Action", "pair_action_delete": "Delete",
        "pair_action_keep_paired": "Keep - paired",
        "pair_action_keep_unchecked": "Keep - unchecked",
        "pair_action_keep_mismatch": "Keep - format not matched",
    },
    "zh-CN": {
        "app_title": "Jpg-Raw-Pair-Cleaner", "target_folder": "目标文件夹：",
        "browse": "浏览…", "scan": "开始扫描", "about": "关于", "language": "Language",
        "auto_label": "自动识别", "custom_label": "自定义",
        "auto_placeholder": "（自动识别）", "field_sep": "：",
        "confirm_delete": "确认删除", "force_delete": "强制删除",
        "delete_btn_fmt": "确认删除（{n} 个，共 {size}）",
        "force_btn_fmt": "强制删除（{n} 个，共 {size}）",
        "status_scanning": "正在扫描...", "status_no_orphan": "未发现未配对文件。",
        "exif_hint": "单击照片查看 EXIF 信息", "exif_detail": "详细 EXIF",
        "exif_brief": "简略 EXIF", "exif_make": "相机厂商", "exif_model": "相机型号",
        "exif_copy_all": "复制全部 EXIF", "exif_copied": "EXIF 已复制到剪贴板",
        "loading": "加载中…", "thumb_small": "小", "thumb_medium": "中",
        "thumb_large": "大", "col_check": "删除", "check_hint": "勾选＝删除，取消勾选＝保留",
        "select_all": "全选", "select_none": "全不选",
        "theme": "主题", "theme_light": "浅色", "theme_dark": "深色",
        "confirm_ok": "删除", "confirm_cancel": "取消",
        "about_author": "作者", "about_copyright": "版权", "about_license": "开源协议", "about_project": "项目地址",
        "view": "界面", "view_classic": "经典界面", "view_pair": "对比界面",
        "pair_frame": "配对对比（JPG | RAW）", "pair_col_jpg": "JPG 文件",
        "pair_col_raw": "RAW 文件", "pair_col_status": "状态",
        "pair_status_ok": "齐全", "pair_status_no_raw": "缺 RAW",
        "pair_status_no_jpg": "缺 JPG", "pair_status_mismatch": "格式未匹配",
        "pair_only_missing": "只显示缺失", "pair_bg_mode": "用背景色标记",
        "pair_count_fmt": "共 {total} 组：齐全 {ok} \u00b7 缺 RAW {no_raw} \u00b7 "
                          "缺 JPG {no_jpg}",
        "pair_col_action": "处理", "pair_action_delete": "删除",
        "pair_action_keep_paired": "不删除 · 已配对",
        "pair_action_keep_unchecked": "不删除 · 已取消勾选",
        "pair_action_keep_mismatch": "不删除 · 格式未匹配",
    },
}
for _code in LANG_CODES:                      # 其余语言以内置英语兜底
    _BUILTIN_LANG.setdefault(_code, dict(_BUILTIN_LANG["en"]))

# 缩略图档位内部值 -> 语言键（界面显示随语言实时切换）
_THUMB_LEVEL_KEYS = {"小": "thumb_small", "中": "thumb_medium", "大": "thumb_large"}


def _load_lang_data() -> dict:
    """加载语言资源 language.json（10 种语言）；失败时使用内置兜底。
    合并顺序：内置英语 -> 内置对应语言 -> 外置文件：任何缺失键都会回退英语，
    不会出现显示成键名或空白的界面；软件名固定取 APP_NAME 常量。"""
    data = {}
    for code in LANG_CODES:
        merged = dict(_BUILTIN_LANG.get("en", {}))
        merged.update(_BUILTIN_LANG.get(code, {}))
        data[code] = merged
    try:
        with open(resource_path("language.json"), "r", encoding="utf-8") as f:
            loaded = json.load(f)
        if isinstance(loaded, dict):
            for code in LANG_CODES:
                part = loaded.get(code)
                if isinstance(part, dict):
                    data[code].update(
                        {k: v for k, v in part.items() if isinstance(v, str)})
    except Exception:
        pass
    for code in LANG_CODES:
        data[code]["app_title"] = APP_NAME  # 软件名单一来源：代码常量
    return data


# ---------- 配置记忆 ----------

CONFIG_FILENAME = "config.json"

DEFAULT_CONFIG = {
    "folder": "",            # 上次选择的文件夹
    "raw_mode": AUTO_ID,     # auto / 品牌 id / custom（不再保存界面显示名）
    "raw_custom": "",        # 自定义后缀输入内容
    "scan_level": "cur",     # 扫描范围稳定 id：cur / l1 / l2 / all
    "confirm": True,         # 删除前二次确认
    "sash": 0,               # 预览区与列表之间的分隔条位置
    "geometry": "",          # 窗口大小与位置
    "thumb_level": "中",     # 缩略图大小档位（小/中/大）
    "about_shown": False,    # 首次删除后是否已弹出过感谢"关于"（同一设备只弹一次）
    "lang": "",              # 界面语言；空 = 首次启动按系统语言检测后写入
    "theme": "auto",         # 主题：auto（跟随系统）/ light / dark
    "unchecked": [],         # 用户取消勾选（保留不删）的文件完整路径
    "ui_mode": "classic",    # 界面模式：classic（经典孤立列表）/ pair（配对对比）
    "pair_color": "bg",      # 对比视图配色：bg（整行底色，默认）/ fg（仅文字颜色）
    "pair_only_missing": False,  # 对比视图：只显示有缺失的配对行
}


def config_path() -> str:
    """配置文件路径：优先 %APPDATA%（固定目录名，兼容历史配置），失败时退回程序目录。"""
    appdata = os.environ.get("APPDATA")
    base = os.path.join(appdata, "相机照片筛选工具") if appdata else \
        os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, CONFIG_FILENAME)


def load_config() -> dict:
    """读取配置；文件缺失或损坏时返回默认值。
    兼容 v4.x 旧配置：raw_mode / scan_level 当时保存的是界面显示文本，
    这里迁移为稳定 id；本轮新增 lang / theme / unchecked（缺失即用默认值）。"""
    cfg = dict(DEFAULT_CONFIG)
    try:
        with open(config_path(), "r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, dict):
            for key in DEFAULT_CONFIG:
                if key in data:
                    cfg[key] = data[key]
    except Exception:
        pass  # 读取失败一律使用默认值
    # ---- 旧配置值迁移（不影响新配置）----
    raw = str(cfg.get("raw_mode") or "")
    if raw not in (AUTO_ID, CUSTOM_ID) and raw not in RAW_FORMATS:
        cfg["raw_mode"] = LEGACY_RAW_MODE.get(raw, AUTO_ID)
    lvl = str(cfg.get("scan_level") or "")
    if lvl not in SCAN_LEVEL_MAX_DEPTH:
        cfg["scan_level"] = LEGACY_SCAN_LEVEL.get(lvl, "cur")
    if cfg.get("thumb_level") not in ("小", "中", "大"):
        cfg["thumb_level"] = "中"
    if str(cfg.get("lang") or "") not in LANG_CODES:
        cfg["lang"] = ""          # 空 = 首次启动按系统语言自动选择
    if str(cfg.get("theme") or "") not in ("auto", "light", "dark"):
        cfg["theme"] = "auto"
    if not isinstance(cfg.get("unchecked"), list):
        cfg["unchecked"] = []
    return cfg


def save_config(cfg: dict) -> None:
    """保存配置；目录不可写等错误静默忽略，不影响主流程。"""
    try:
        path = config_path()
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(cfg, f, ensure_ascii=False, indent=2)
    except Exception:
        pass


# ---------- RAW 后缀解析 ----------


def parse_raw_exts(text: str) -> set:
    """
    解析用户输入的 RAW 后缀字符串（逗号/分号/空格分隔，可多个）。
    统一转为小写、带点的集合；非法后缀抛出 ValueError。
    例如：".rw2,.dng" -> {".rw2", ".dng"}；"rw2, DNG" 同样有效。
    """
    exts: set[str] = set()
    for part in re.split(r"[,，;；\s]+", text or ""):
        part = part.strip().lower()
        if not part:
            continue
        if not part.startswith("."):
            part = "." + part
        if not re.fullmatch(r"\.[a-z0-9]{1,10}", part):
            raise ValueError(f"无效的 RAW 后缀：{part}（只能包含字母和数字）")
        exts.add(part)
    if not exts:
        raise ValueError("RAW 后缀不能为空，请选择品牌或输入自定义后缀。")
    return exts


# ---------- 扫描与配对逻辑 ----------

@dataclass
class FileInfo:
    """一个孤立文件的显示与删除所需信息。"""
    name: str       # 原始文件名（保留原始大小写，用于显示）
    ext: str        # "JPG" 或 "RAW"
    raw_ext: str    # RAW 文件的实际后缀（小写带点）；JPG 文件为空串
    size: int       # 文件大小（字节）
    folder: str     # 所在文件夹
    full_path: str  # 完整路径（删除时使用，保留原始位置）


@dataclass
class PairRow:
    """对比视图的一行：同一基础名下的 JPG 与 RAW 并排显示。

    status:
      · "ok"     两侧都有（绿色，无需处理）
      · "no_raw" 缺 RAW（红色，JPG 是孤立文件）
      · "no_jpg" 缺 JPG（黄色，RAW 是孤立文件）
    mismatch: RAW 存在但后缀不在本次参与配对的格式内（受保护、不列入删除）。"""
    base: str
    jpg: object = None          # FileInfo 或 None
    raw: object = None          # FileInfo 或 None
    status: str = "ok"
    mismatch: bool = False

    @property
    def primary(self):
        """该行的主文件（优先 JPG）：用于 EXIF / 预览 / 定位。"""
        return self.jpg or self.raw

    @property
    def deletable(self):
        """该行中真正会被删除的孤立文件（配对完整的行为空）。"""
        if self.status == "ok":
            return []
        target = self.jpg if self.status == "no_raw" else self.raw
        if target is None or (self.status == "no_jpg" and self.mismatch):
            return []          # 格式未匹配的 RAW 受保护，不参与删除
        return [target]


@dataclass
class ScanResult:
    """一次扫描的完整结果。"""
    orphans: list
    paired_base_count: int = 0
    skipped: list = field(default_factory=list)        # [(路径, 原因)]
    detected_raw: set = field(default_factory=set)     # 文件夹中实际存在的已知 RAW 后缀
    effective_raw: set = field(default_factory=set)    # 参与孤立判定的 RAW 后缀
    mismatch_raw: set = field(default_factory=set)     # 实际存在但未选择的后缀（需提示）
    auto_detect: bool = False
    pairs: list = field(default_factory=list)          # 配对对比表（PairRow）


def scan_folder(folder: str, auto_detect: bool, selected_raw: set, max_depth) -> ScanResult:
    """
    按层级范围扫描 folder 中的 .jpg / RAW 文件并配对。
      - auto_detect: True 时自动识别文件夹内实际存在的已知 RAW 后缀
      - selected_raw: 手动选择/自定义的 RAW 后缀集合（自动识别时为空集）
      - max_depth: 0 / 1 / 2 / None（None 表示不限层级）

    配对规则：同一基础名同时存在 jpg 与 raw -> 已配对。
    孤立判定：
      - JPG：基础名下没有任何 RAW（任何格式）时才是孤立 JPG；
      - RAW：没有 JPG 且其后缀属于 effective_raw 时才是孤立 RAW。
        —— 与所选格式不符的 RAW（mismatch）不列入孤立文件，防止误删。
    根文件夹不存在 / 不是目录 / 无法读取时抛出 OSError，由调用方友好提示。
    """
    folder = os.path.abspath(folder)
    if not os.path.isdir(folder):
        if os.path.exists(folder):
            raise NotADirectoryError(f"该路径不是文件夹：{folder}")
        raise FileNotFoundError(f"路径不存在：{folder}")

    skipped: list = []
    detected: set = set()

    # groups: {小写基础名: {"jpg": [FileInfo...], "raw": [FileInfo...]}}
    groups: dict = {}

    def _on_walk_error(err: OSError):
        skipped.append((getattr(err, "filename", "未知路径"), f"无法读取（{err}）"))

    for root, dirs, files in os.walk(folder, onerror=_on_walk_error):
        # 计算相对层级并控制扫描深度（不进入超过上限的子文件夹）
        rel = os.path.relpath(root, folder)
        depth = 0 if rel == "." else rel.count(os.sep) + 1
        if max_depth is not None and depth >= max_depth:
            dirs[:] = []  # 已达到最大层级，剪枝：不再进入更深层

        for name in files:
            base, ext = os.path.splitext(name)
            ext = ext.lower()
            if ext == ".jpg":
                kind = "jpg"          # JPG 是固定配对格式
            elif ext in ALL_KNOWN_RAW_EXTS:
                kind = "raw"          # 已知 RAW 格式：参与配对并记录实际存在
                detected.add(ext)
            elif ext in selected_raw:
                kind = "raw"          # 用户自定义的非常规 RAW 后缀
            else:
                continue

            full = os.path.join(root, name)
            try:
                st = os.stat(full)
            except OSError as exc:
                skipped.append((full, f"无法读取文件信息（{exc}）"))
                continue

            # Windows 文件系统不区分大小写：用小写基础名作为分组键近似实现
            key = base.lower()
            groups.setdefault(key, {"jpg": [], "raw": []})[kind].append(
                FileInfo(
                    name=name,
                    ext="JPG" if kind == "jpg" else "RAW",
                    raw_ext=ext if kind == "raw" else "",
                    size=st.st_size,
                    folder=root,
                    full_path=full,
                )
            )

    # 根文件夹本身读取失败（os.walk 不抛异常，通过 onerror 记录）：明确报错
    for item in skipped:
        if item[0] == folder:
            raise PermissionError(item[1])

    # 自动识别：以文件夹中实际存在的已知 RAW 后缀为准；
    # 手动模式：以用户选择/输入的后缀为准，并计算不匹配的格式
    effective_raw = detected if auto_detect else set(selected_raw)
    mismatch_raw = detected - effective_raw

    orphans: list = []
    paired_base_count = 0
    for g in groups.values():
        if g["jpg"] and g["raw"]:
            paired_base_count += 1  # 有 JPG 有 RAW（任何格式）-> 已配对
        else:
            orphans.extend(g["jpg"])  # 无 RAW 的 JPG -> 孤立 JPG
            for f in g["raw"]:
                if f.raw_ext in effective_raw:
                    orphans.append(f)  # 仅所选/所识别格式的 RAW 才列为孤立

    # 配对对比表：同一基础名的 JPG / RAW 并排一行，标注哪一侧缺失
    pairs: list = []
    for g in groups.values():
        jpgs, raws = g["jpg"], g["raw"]
        jpg = jpgs[0] if jpgs else None
        raw = None
        if raws:
            # 有多个同基础名 RAW 时，优先取本次参与配对判定的格式
            raw = next((f for f in raws if f.raw_ext in effective_raw), raws[0])
        anchor = jpg or raw
        if anchor is None:
            continue
        base_name = os.path.splitext(anchor.name)[0]
        if jpg is not None and raw is not None:
            status = "ok"
        elif jpg is not None:
            status = "no_raw"          # 缺 RAW（红）
        else:
            status = "no_jpg"          # 缺 JPG（黄）
        pairs.append(PairRow(
            base=base_name, jpg=jpg, raw=raw, status=status,
            mismatch=bool(status == "no_jpg" and raw is not None
                          and raw.raw_ext not in effective_raw),
        ))
    # 有缺失的排在前面（方便先处理问题），同状态按基础名排序
    pairs.sort(key=lambda p: (p.status == "ok", p.base.lower()))

    orphans.sort(key=lambda f: (f.name.lower(), f.folder.lower()))
    return ScanResult(
        orphans=orphans,
        paired_base_count=paired_base_count,
        skipped=skipped,
        detected_raw=detected,
        effective_raw=effective_raw,
        mismatch_raw=mismatch_raw,
        auto_detect=auto_detect,
        pairs=pairs,
    )


def human_size(num_bytes: int) -> str:
    """把字节数格式化为易读的字符串（B/KB/MB/GB/TB）。

    v6.2（需求1）：改为紧凑格式（"512B"、"1.5KB"、"1GB"），单位前不带空格、
    去掉末尾的 ".0"，与 C++ 版 HumanSize 保持一致；删除按钮会附带容量文本，
    较长的 "1.0 GB" 形式在按钮里显示不全。
    """
    if num_bytes < 1024:
        return f"{num_bytes}B"
    value = float(num_bytes)
    for unit in ("KB", "MB", "GB", "TB"):
        value /= 1024
        if value < 1024 or unit == "TB":
            text = f"{value:.1f}"
            if text.endswith(".0"):
                text = text[:-2]  # 1024*1024*1024 -> "1" + "GB" = "1GB"
            return f"{text}{unit}"
    return f"{num_bytes}B"  # 理论到不了这里


def _exif_float(value):
    """
    EXIF rational 值转浮点，兼容多种表示：
    (分子, 分母) 元组/列表、[单个元素]（递归取首）、Fraction、'9/5'、float。
    """
    if isinstance(value, (tuple, list)):
        if len(value) == 2:
            return value[0] / value[1] if value[1] else 0.0
        if value:
            return _exif_float(value[0])
        return 0.0
    if isinstance(value, str):
        from fractions import Fraction
        return float(Fraction(value))
    return float(value)


def _rat_to_string(value) -> str:
    """
    把 rational 的各种表示转成 '分子/分母' 字符串：
    [18, 10]、[Fraction(18,10)]、Fraction(9,5)、'9/5' 等。
    """
    if isinstance(value, (tuple, list)):
        if len(value) == 2:
            return f"{value[0]}/{value[1]}"
        if value:
            return _rat_to_string(value[0])
        return ""
    return str(value)


def _norm_number(value) -> str:
    """
    渲染层数值归一化：把 "18/10"、"[18, 10]" 等原始表示格式化为 "1.8"；
    已是规范数值则原样返回。防止详细/简略模式显示异常。
    """
    s = str(value).strip()
    if s.startswith("[") and s.endswith("]"):
        import re
        parts = re.findall(r"[\d.]+", s)
        if len(parts) == 2 and float(parts[1]):
            return f"{float(parts[0]) / float(parts[1]):g}"
        return s
    if "/" in s:
        parts = s.split("/")
        if len(parts) == 2:
            try:
                num, den = float(parts[0]), float(parts[1])
                if den:
                    return f"{num / den:g}"
            except ValueError:
                pass
    return s


def _read_exif_exifread(path: str):
    """
    用 exifread 解析 EXIF（JPG 与 TIFF-based RAW 通用），返回 9 字段结构化
    字典（make/model/aperture/shutter/iso/focal/date/resolution/lens）；
    失败返回 None。exifread 会递归解析 ExifIFD，字段识别更完整。
    兼容标签前缀 "EXIF *"（真实相机）与 "Image *"（部分写入器），
    兼容 rational 的 元组/列表/Fraction 多种表示。
    """
    try:
        with open(path, "rb") as f:
            import contextlib
            import io
            # 抑制 exifread 对不支持文件的 stderr 提示噪音
            with contextlib.redirect_stderr(io.StringIO()):
                tags = exifread.process_file(f, details=False)
    except Exception:
        return None
    if not tags:
        return None

    def _val(*names):
        for key in names:
            t = tags.get(key)
            if t is not None:
                v = t.values
                if isinstance(v, str):
                    v = v.strip()
                return v or None
        return None

    def _scalar(v):
        """SHORT 数组类值（如 ISO=[100]）取首元素。"""
        if isinstance(v, (tuple, list)):
            return v[0] if v else None
        return v

    make = _val("Image Make", "EXIF Make")
    model = _val("Image Model", "EXIF Model")
    result = {
        "make": make,
        "model": model,
        "camera": " / ".join(x for x in (make or "", model or "") if x) or None,
    }
    fn = _val("EXIF FNumber", "Image FNumber")
    if fn is not None:
        try:
            result["aperture"] = f"{_exif_float(fn):g}"
        except Exception:
            result["aperture"] = _norm_number(fn)  # 兜底归一化，杜绝 "18/10"/"[...]"
    et = _val("EXIF ExposureTime", "Image ExposureTime")
    if et is not None:
        result["shutter"] = _rat_to_string(et)  # 归一为 "1/200"
    iso = _val("EXIF ISOSpeedRatings", "Image ISOSpeedRatings")
    if iso is not None:
        result["iso"] = str(_scalar(iso))
    fl = _val("EXIF FocalLength", "Image FocalLength")
    if fl is not None:
        try:
            result["focal"] = f"{_exif_float(fl):g}"
        except Exception:
            result["focal"] = _norm_number(fl)
    dt = _val("EXIF DateTimeOriginal", "Image DateTimeOriginal")
    if dt is not None:
        result["date"] = str(dt)
    lm = _val("EXIF LensModel", "Image LensModel")
    if lm is not None:
        result["lens"] = str(lm)
    # 分辨率：优先 ExifIFD 的 ExifImageWidth/PixelXDimension（相机声明的显示尺寸，
    # 索尼/佳能等写入；NEF/DNG 的 IFD0 ImageWidth 可能只是小缩略图，由调用方合并
    # 自研解析结果时按面积甄别替换），最后回退 Image ImageWidth。
    w = _scalar(_val("EXIF ExifImageWidth", "EXIF PixelXDimension",
                     "Image PixelXDimension", "Image ImageWidth"))
    h = _scalar(_val("EXIF ExifImageLength", "EXIF PixelYDimension",
                     "Image PixelYDimension", "Image ImageLength"))
    if w and h:
        result["resolution"] = f"{w} × {h}"
    if not (result.get("camera") or result.get("aperture")
            or result.get("resolution")):
        return None
    return result


def read_exif(path: str):
    """
    读取 JPG 照片的关键 EXIF 信息，返回【结构化字典】（9 个字段项，供详细
    模式固定行渲染；缺失字段在渲染层显示 "--"）；读取失败返回 None。
    字段：make / model / aperture / shutter / iso / focal / date / resolution / lens。
    使用 with 打开：离开作用域即释放文件句柄，不残留占用。
    """
    if not PILLOW_AVAILABLE:
        return None
    try:
        with Image.open(path) as im:
            w, h = im.size
            exif = im.getexif()
    except Exception:
        return None
    make = str(exif.get(0x010F, "") or "").strip()   # Make
    model = str(exif.get(0x0110, "") or "").strip()  # Model
    result = {
        "make": make or None,
        "model": model or None,
        "camera": " / ".join(x for x in (make, model) if x) or None,
        "resolution": f"{w} × {h}",
    }
    fn = exif.get(0x829D)  # FNumber
    if fn is not None:
        try:
            result["aperture"] = f"{_exif_float(fn):g}"
        except Exception:
            pass
    et = exif.get(0x829A)  # ExposureTime
    if et is not None:
        try:
            if isinstance(et, tuple) and len(et) == 2 and et[1]:
                result["shutter"] = f"{et[0]}/{et[1]}"
            else:
                v = _exif_float(et)
                result["shutter"] = f"1/{round(1 / v)}" if v and v < 1 else f"{v:g}"
        except Exception:
            pass
    iso = exif.get(0x8827)  # ISOSpeedRatings
    if iso is not None:
        result["iso"] = str(iso)
    fl = exif.get(0x920A)  # FocalLength
    if fl is not None:
        try:
            result["focal"] = f"{_exif_float(fl):g}"
        except Exception:
            pass
    dt = exif.get(0x9003)  # DateTimeOriginal
    if dt:
        result["date"] = str(dt)
    lm = exif.get(0xA434)  # LensModel
    if lm:
        result["lens"] = str(lm)
    return result


def _read_tiff_exif(data: bytes):
    """
    轻量 TIFF 结构解析：读取 IFD0 与 ExifIFD（0x8769）中的全部标签，
    并跟随 next-IFD / SubIFD（0x014A）指针遍历全部 IFD；同时解析
    松下 MakerNote（0x927C，mini-TIFF 结构）提取图像尺寸。
    不解析缩略图 IFD 的像素数据。返回 (tags, endian, dims)；
    tags: {tag: (type, count, raw_bytes)}；dims: [(宽, 高), ...] 全部候选。
    用于读取 TIFF-based RAW（NEF/ARW/RW2/PEF/DNG/ORF/3FR/IIQ/MEF/MOS 等）
    内嵌的 EXIF 信息，纯 Python 实现、无额外依赖。
    """
    if len(data) < 8:
        return {}, "<", []
    if data[:2] == b"II":
        endian = "<"
    elif data[:2] == b"MM":
        endian = ">"
    else:
        return {}, "<", []

    tags = {}
    dims: list = []  # [(宽, 高)] 全部 IFD/子结构的尺寸候选（取最大面积者）
    size_map = {1: 1, 2: 1, 3: 2, 4: 4, 5: 8, 7: 1, 9: 4, 10: 8}

    def _u16(off):
        return struct.unpack_from(endian + "H", data, off)[0]

    def _u32(off):
        return struct.unpack_from(endian + "I", data, off)[0]

    def _num_from(raw, typ):
        """按标签类型从值字节解析整数：SHORT(3)=2 字节，LONG(4)/SLONG(9)=4 字节。"""
        if typ == 3 and len(raw) >= 2:
            return struct.unpack_from(endian + "H", raw, 0)[0]
        if typ in (4, 9) and len(raw) >= 4:
            return struct.unpack_from(endian + "I", raw, 0)[0]
        return None

    def _parse_panasonic_maker(maker_off):
        """松下 MakerNote：'Panasonic\\0\\0\\0' + mini-IFD（count + 条目）。
        其中的 0x4B/0x4C（LONG）为该 RAW 的真实像素宽/高
        （松下 RW2 不写入标准 ImageWidth/Length，真实尺寸仅存于此）。"""
        if maker_off <= 0 or maker_off + 14 > len(data):
            return
        if not data[maker_off:maker_off + 12].startswith(b"Panasonic\x00\x00\x00"):
            return
        count = _u16(maker_off + 12)
        if not (2 <= count <= 512):
            return
        p = maker_off + 14
        w = h = None
        for _ in range(count):
            if p + 12 > len(data):
                break
            tag = _u16(p)
            typ = _u16(p + 2)
            if tag == 0x4B and typ in (3, 4):
                w = _num_from(data[p + 8:p + 12], typ)
            elif tag == 0x4C and typ in (3, 4):
                h = _num_from(data[p + 8:p + 12], typ)
            p += 12
        if w and h and w > 100 and h > 100:
            dims.append((w, h))

    def _parse_ifd(offset, depth):
        if depth > 5 or offset <= 0 or offset + 2 > len(data):
            return
        count = _u16(offset)
        if count > 512:  # 防御：异常计数（越界/非 IFD 数据）直接放弃
            return
        p = offset + 2
        ifd_dims = {}          # 本 IFD 内 0x0100/0x0101/0xA002/0xA003 的值
        sub_ifds: list = []    # 0x014A 子 IFD 指针（可能多个）
        exif_ifd = 0           # 0x8769 指针
        maker_off = 0          # 0x927C 指针
        for _ in range(count):
            if p + 12 > len(data):
                break
            tag = _u16(p)
            typ = _u16(p + 2)
            cnt = _u32(p + 4)
            size = size_map.get(typ, 1) * cnt
            if size <= 4:
                raw = data[p + 8:p + 12]
                voff = 0
            else:
                voff = _u32(p + 8)
                raw = data[voff:voff + min(size, 512)]
            tags[tag] = (typ, cnt, raw)
            if tag in (0x0100, 0x0101, 0xA002, 0xA003):
                v = _num_from(raw, typ)
                if v:
                    ifd_dims[tag] = v
            elif tag == 0x8769 and size <= 4:
                exif_ifd = struct.unpack_from(endian + "I", raw, 0)[0]
            elif tag == 0x014A:
                if size <= 4:
                    sub_ifds.append(struct.unpack_from(endian + "I", raw, 0)[0])
                else:
                    for j in range(min(cnt, 16)):
                        if voff + j * 4 + 4 <= len(data):
                            sub_ifds.append(
                                struct.unpack_from(endian + "I", data, voff + j * 4)[0])
            elif tag == 0x927C and size > 4:
                maker_off = voff
            p += 12
        # 本 IFD 的尺寸对（ImageWidth/Length 优先，PixelXDimension 次之）
        w = ifd_dims.get(0x0100) or ifd_dims.get(0xA002)
        h = ifd_dims.get(0x0101) or ifd_dims.get(0xA003)
        if w and h:
            dims.append((w, h))
        if maker_off:
            _parse_panasonic_maker(maker_off)
        if exif_ifd:
            _parse_ifd(exif_ifd, depth + 1)
        for so in sub_ifds:
            _parse_ifd(so, depth + 1)
        # 跟随 next IFD 指针：真实 RAW（如松下 RW2）的 RAW 尺寸/参数
        # 分布在后续 IFD（IFD1/IFD2），遍历后统一按面积取最大者
        next_off = _u32(offset + 2 + count * 12) if offset + 2 + count * 12 + 4 <= len(data) else 0
        if next_off and next_off != offset:
            _parse_ifd(next_off, depth + 1)

    _parse_ifd(_u32(4), 0)
    return tags, endian, dims


def _format_tiff_exif(tags: dict, endian: str, dims: list = None):
    """把 TIFF/RAW 解析出的标签格式化为【结构化字典】；无有效数据返回 None。
    dims 为全部 IFD/子结构（含 SubIFD、松下 MakerNote）收集到的 (宽, 高) 候选，
    取【面积最大】者作为分辨率——IFD0 可能是小尺寸预览（NEF/DNG），
    真实像素尺寸位于 SubIFD 或 MakerNote 中。"""
    if not tags:
        return None

    def _ascii(tag):
        t = tags.get(tag)
        if not t:
            return ""
        return t[2].split(b"\x00", 1)[0].decode("utf-8", "ignore").strip()

    def _num(tag):
        """按标签类型解析整数：SHORT(3)=2 字节，LONG(4)/SLONG(9)=4 字节。
        避免固定按 4 字节读取导致大端 SHORT（如 ISO、宽高）解析错误。"""
        t = tags.get(tag)
        if not t or not t[2]:
            return None
        typ, raw = t[0], t[2]
        if typ == 3:  # SHORT
            return struct.unpack_from(endian + "H", raw, 0)[0] if len(raw) >= 2 else None
        if typ in (4, 9):  # LONG / SLONG
            return struct.unpack_from(endian + "I", raw, 0)[0] if len(raw) >= 4 else None
        return None

    def _rat(tag):
        """按标签类型解析 rational：RATIONAL(5)/SRATIONAL(10)=8 字节。"""
        t = tags.get(tag)
        if not t or len(t[2]) < 8:
            return None
        num = struct.unpack_from(endian + "I", t[2], 0)[0]
        den = struct.unpack_from(endian + "I", t[2], 4)[0]
        return num / den if den else 0.0

    make, model = _ascii(0x010F), _ascii(0x0110)
    result = {
        "make": make or None,
        "model": model or None,
        "camera": " / ".join(x for x in (make, model) if x) or None,
    }
    fn = _rat(0x829D)  # FNumber
    if fn:
        result["aperture"] = f"{fn:g}"
    et = tags.get(0x829A)  # ExposureTime
    if et and len(et[2]) >= 8:
        num = struct.unpack_from(endian + "I", et[2], 0)[0]
        den = struct.unpack_from(endian + "I", et[2], 4)[0]
        if den:
            result["shutter"] = f"{num}/{den}"
    iso = _num(0x8827)  # ISOSpeedRatings（部分写入器用 0x8833 ISOSpeedRatings2）
    if iso is None:
        iso = _num(0x8833)
    if iso:
        result["iso"] = str(iso)
    fl = _rat(0x920A)  # FocalLength
    if fl:
        result["focal"] = f"{fl:g}"
    dt = _ascii(0x9003)  # DateTimeOriginal
    if dt:
        result["date"] = dt
    lm = _ascii(0xA434)  # LensModel
    if lm:
        result["lens"] = lm
    w, h = None, None
    if dims:
        # 多 IFD/子结构候选：取面积最大者（预览缩略图尺寸不会误选）
        w, h = max(dims, key=lambda d: d[0] * d[1])
    else:
        w, h = _num(0x0100), _num(0x0101)  # ImageWidth / ImageLength
        if not (w and h):
            # ExifIFD 的 PixelXDimension/PixelYDimension 回退（部分 RAW 仅在此记录尺寸）
            w = w or _num(0xA002)
            h = h or _num(0xA003)
    if w and h:
        result["resolution"] = f"{w} × {h}"
    return result


def read_raw_exif(path: str):
    """
    读取 RAW 文件内嵌的 EXIF 信息（TIFF 结构魔数搜索法）。
    覆盖：TIFF-based RAW（NEF/ARW/RW2/PEF/DNG/ORF/3FR/IIQ/MEF/MOS 等）、
    内嵌 TIFF 的 CR3（佳能）与 RAF（富士）；仅读取文件前 1MB 头部，开销极小。
    无法解析的格式（如适马 X3F）返回 None。
    """
    try:
        with open(path, "rb") as f:
            data = f.read(1024 * 1024)  # 只读头部，避免加载整个 RAW 文件
    except Exception:
        return None
    start = data.find(b"Exif\x00\x00")
    if start >= 0:
        start += 6  # Exif\0\0 之后即为 TIFF 头
    else:
        start = -1
        for magic in (b"II*\x00", b"MM\x00*"):
            idx = data.find(magic)
            if idx >= 0:
                start = idx
                break
    if start < 0:
        return None
    tags, endian, dims = _read_tiff_exif(data[start:])
    return _format_tiff_exif(tags, endian, dims)


def _res_area(res: str) -> int:
    """从 "6000 × 4000" 形式的字符串解析像素面积（用于识别缩略图尺寸）。"""
    nums = re.findall(r"\d+", str(res))
    if len(nums) >= 2:
        try:
            return int(nums[0]) * int(nums[1])
        except ValueError:
            pass
    return 0


def read_photo_exif(path: str):
    """统一入口：JPG 与 TIFF-based RAW 均【优先 exifread】（递归解析 ExifIFD、
    9 字段识别更完整）；RAW 在 exifread 缺失字段（ISO、分辨率）或分辨率仅为
    缩略图尺寸时，用自研 TIFF 解析（多 IFD/SubIFD/松下 MakerNote）补齐。
    JPG 回退 Pillow；RAW 回退自研 TIFF 解析。"""
    ext = os.path.splitext(path)[1].lower()
    if ext == ".jpg":
        if EXIFREAD_AVAILABLE:
            data = _read_exif_exifread(path)
            if data:
                if not data.get("resolution") and PILLOW_AVAILABLE:
                    try:
                        with Image.open(path) as im:
                            w, h = im.size
                        data["resolution"] = f"{w} × {h}"
                    except Exception:
                        pass
                return data
        return read_exif(path)   # JPG 回退：Pillow
    # ---- RAW ----
    data = _read_exif_exifread(path) if EXIFREAD_AVAILABLE else None
    mine = read_raw_exif(path)   # 自研轻量 TIFF 解析（多 IFD/SubIFD/MakerNote）
    if data is None:
        return mine
    if mine:
        # 缺失字段用自研解析补齐（如松下 RW2 的 ISO）
        for k, v in mine.items():
            if k == "resolution" or not v or data.get(k):
                continue
            data[k] = v
        # 分辨率：exifread 的结果缺失，或仅为小尺寸缩略图（<100 万像素，
        # 如 NEF/DNG 的 IFD0 预览）时，采用自研解析的真实像素尺寸
        ex = data.get("resolution")
        mr = mine.get("resolution")
        if mr and (not ex or _res_area(ex) < 1_000_000):
            data["resolution"] = mr
    return data


# ---------- 图形界面 ----------

# ---------- 自绘控件：圆润滚动条 / 圆形按钮 / 药丸按钮 / 圆形开关 / 药丸滑块 ----------

_FONT_FAMILY_CACHE: list = []   # 界面字体族缓存（首次探测后复用）
_BADGE_MASK_CACHE: dict = {}


def _rounded_mask(size: int, radius: int):
    """生成圆角正方形遮罩（纯 PIL 逐像素计算，结果缓存，替代 ImageDraw）。"""
    key = ("r", size, radius)
    mask = _BADGE_MASK_CACHE.get(key)
    if mask is not None:
        return mask
    mask = Image.new("L", (size, size), 0)
    px = mask.load()
    r = max(1, min(radius, size // 2))
    for y in range(size):
        for x in range(size):
            cx, cy = x, y
            if x < r:
                cx = r
            elif x > size - 1 - r:
                cx = size - 1 - r
            if y < r:
                cy = r
            elif y > size - 1 - r:
                cy = size - 1 - r
            if (x - cx) ** 2 + (y - cy) ** 2 <= r * r:
                px[x, y] = 255
    _BADGE_MASK_CACHE[key] = mask
    return mask


def _check_mask(size: int, width: int = 3):
    """生成"勾"形遮罩（两段粗线段，逐像素按点到线段距离判定，结果缓存）。"""
    key = ("c", size, width)
    mask = _BADGE_MASK_CACHE.get(key)
    if mask is not None:
        return mask
    mask = Image.new("L", (size, size), 0)
    px = mask.load()
    s = size
    p1 = (s * 0.26, s * 0.52)
    p2 = (s * 0.44, s * 0.70)
    p3 = (s * 0.76, s * 0.30)
    half = max(1.2, width / 2.0)

    def _dist(ax, ay, bx, by, x, y):
        dx, dy = bx - ax, by - ay
        length2 = dx * dx + dy * dy
        if length2 == 0:
            return ((x - ax) ** 2 + (y - ay) ** 2) ** 0.5
        t = max(0.0, min(1.0, ((x - ax) * dx + (y - ay) * dy) / length2))
        return ((x - (ax + t * dx)) ** 2 + (y - (ay + t * dy)) ** 2) ** 0.5

    for y in range(s):
        for x in range(s):
            xc, yc = x + 0.5, y + 0.5
            if (_dist(p1[0], p1[1], p2[0], p2[1], xc, yc) <= half
                    or _dist(p2[0], p2[1], p3[0], p3[1], xc, yc) <= half):
                px[x, y] = 255
    _BADGE_MASK_CACHE[key] = mask
    return mask


def ui_font_family() -> str:
    """界面字体族（模块级缓存，自绘控件也可使用）。"""
    return _FONT_FAMILY_CACHE[0] if _FONT_FAMILY_CACHE else "TkDefaultFont"


def set_ui_font_family(name: str):
    _FONT_FAMILY_CACHE.clear()
    _FONT_FAMILY_CACHE.append(name or "TkDefaultFont")


def _measure_text(text: str, size: int = 10, bold: bool = False) -> int:
    """测量文本像素宽度（用于自绘按钮自适应宽度）。"""
    try:
        from tkinter import font as tkfont
        f = tkfont.Font(family=ui_font_family(), size=size,
                        weight="bold" if bold else "normal")
        return f.measure(text or "")
    except Exception:
        return max(1, len(text or "")) * (size // 2 + 2)


def draw_rounded_outline(canvas, x0, y0, x1, y1, radius, color, width=1, tags=()):
    """只描边的圆角矩形（4 段直线 + 4 段圆弧）。
    注意：不要把 create_rectangle 的 outline 设成异色——那样会在四个角内侧
    留下直角"毛边"，这正是卡片圆角出现小突起的根因。"""
    r = max(1.0, min(float(radius), (x1 - x0) / 2.0, (y1 - y0) / 2.0))
    kw = {"fill": color, "width": width, "capstyle": "round", "tags": tags}
    canvas.create_line(x0 + r, y0, x1 - r, y0, **kw)
    canvas.create_line(x0 + r, y1, x1 - r, y1, **kw)
    canvas.create_line(x0, y0 + r, x0, y1 - r, **kw)
    canvas.create_line(x1, y0 + r, x1, y1 - r, **kw)
    arc = {"style": "arc", "outline": color, "width": width, "tags": tags}
    canvas.create_arc(x0, y0, x0 + 2 * r, y0 + 2 * r, start=90, extent=90, **arc)
    canvas.create_arc(x1 - 2 * r, y0, x1, y0 + 2 * r, start=0, extent=90, **arc)
    canvas.create_arc(x0, y1 - 2 * r, x0 + 2 * r, y1, start=180, extent=90, **arc)
    canvas.create_arc(x1 - 2 * r, y1 - 2 * r, x1, y1, start=270, extent=90, **arc)


def draw_pill(canvas, x0, y0, x1, y1, radius=None, fill="#000000", outline="",
              stipple=None, tags=()):
    """在 Canvas 上绘制圆角矩形（两端为半圆时即"药丸形"）。
    四个角用小圆 + 两条矩形拼成——角圆必须是正圆，否则竖向滚动条/按钮两端会被
    拉成椭圆；内部两条矩形只填充、不描异色边，否则四角会露出直角"毛边"。
    需要边框时另外用 draw_rounded_outline() 描一圈真正的圆角线。"""
    if x1 - x0 < 1 or y1 - y0 < 1:
        return
    if radius is None:
        radius = min(x1 - x0, y1 - y0) / 2.0
    r = max(1.0, min(float(radius), (x1 - x0) / 2.0, (y1 - y0) / 2.0))
    kw = {"fill": fill, "outline": fill, "tags": tags}   # 关键：outline 必须等于 fill
    if stipple:
        kw["stipple"] = stipple
    canvas.create_oval(x0, y0, x0 + 2 * r, y0 + 2 * r, **kw)
    canvas.create_oval(x1 - 2 * r, y0, x1, y0 + 2 * r, **kw)
    canvas.create_oval(x0, y1 - 2 * r, x0 + 2 * r, y1, **kw)
    canvas.create_oval(x1 - 2 * r, y1 - 2 * r, x1, y1, **kw)
    canvas.create_rectangle(x0 + r, y0, x1 - r, y1, **kw)
    canvas.create_rectangle(x0, y0 + r, x1, y1 - r, **kw)
    if outline and str(outline).lower() != str(fill).lower():
        draw_rounded_outline(canvas, x0, y0, x1, y1, r, outline, 1, tags)


class PillButton(tk.Canvas):
    """药丸形按钮（圆角矩形），支持 primary/danger/secondary/ghost 四种样式。

    与 ttk.Button 的常用接口保持兼容：configure(text=/state=/style=)、cget("text")、
    invoke()，因此既有的 i18n 注册表与状态管理代码无需改动。"""

    STYLES = {
        "primary": ("accent", "#ffffff"),
        "danger": ("danger", "#ffffff"),
        "secondary": ("card_alt", "text"),
        "ghost": ("accent_soft", "accent"),
    }

    def __init__(self, master, text="", command=None, style="secondary",
                 font_size=10, bold=False, height=32, pad_x=18, **kw):
        super().__init__(master, highlightthickness=0, bd=0, bg=UI["card"],
                         height=height, **kw)
        self._text = text
        self._command = command
        self._style = style if style in self.STYLES else "secondary"
        self._font_size = font_size
        self._bold = bold
        self._pad_x = pad_x
        self._height = height
        self._state = "normal"
        self._hover = False
        self._pressed = False
        self.bind("<Button-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)
        self.bind("<Enter>", lambda _e: self._set_hover(True))
        self.bind("<Leave>", lambda _e: self._set_hover(False))
        self._resize_to_text()

    # --- 兼容接口 ---
    def configure(self, cnf=None, **kw):
        text = kw.pop("text", None)
        state = kw.pop("state", None)
        style = kw.pop("style", None)
        if style and style in self.STYLES:
            self._style = style
        if state is not None:
            self._state = "normal" if str(state) in ("normal", "active", "readonly") \
                else "disabled"
        if kw.get("bg") in (None, "") and "bg" in kw:
            kw.pop("bg")
        if cnf or kw:
            super().configure(cnf, **kw)
        if text is not None:
            self._text = text
            self._resize_to_text()
        self._draw()
        return self

    config = configure

    def cget(self, key):
        if key == "text":
            return self._text
        if key == "state":
            return self._state
        if key == "style":
            return self._style
        return super().cget(key)

    def invoke(self):
        """以程序方式触发点击（测试/快捷键使用）。"""
        if self._state == "disabled":
            return None
        return self._command() if self._command else None

    def instate(self, spec):
        """兼容 ttk 的 instate()：支持 ["disabled"] / ["!disabled"] 判断。"""
        specs = [spec] if isinstance(spec, str) else list(spec)
        for item in specs:
            item = str(item)
            negate = item.startswith("!")
            key = item.lstrip("!")
            if key != "disabled":
                continue
            is_disabled = (self._state == "disabled")
            if negate and is_disabled:
                return False
            if not negate and not is_disabled:
                return False
        return True

    def set_text(self, text):
        self.configure(text=text)

    def refresh_theme(self):
        try:
            self.configure(bg=UI["card"])
        except tk.TclError:
            return
        self._draw()

    # --- 内部 ---
    def _colors(self):
        bg_key, fg_key = self.STYLES[self._style]
        if self._state == "disabled":
            return UI["disabled_bg"], UI["disabled_fg"]
        bg = UI[bg_key]
        fg = fg_key if fg_key.startswith("#") else UI[fg_key]
        if self._pressed:
            bg = UI["accent_dark"] if self._style in ("primary", "ghost") else UI["border"]
            if self._style == "danger":
                bg = UI["danger_dark"]
        elif self._hover:
            bg = UI["accent_soft"] if self._style in ("secondary", "ghost") else bg
            if self._style == "primary":
                bg = UI["accent_dark"]
            elif self._style == "danger":
                bg = UI["danger_dark"]
        return bg, fg

    def _set_hover(self, value):
        self._hover = value and self._state != "disabled"
        self._draw()

    def _on_press(self, _e=None):
        if self._state == "disabled":
            return
        self._pressed = True
        self._draw()

    def _on_release(self, event=None):
        was = self._pressed
        self._pressed = False
        self._draw()
        if was and self._state != "disabled":
            inside = True
            if event is not None:
                inside = 0 <= event.x <= self.winfo_width() and 0 <= event.y <= self.winfo_height()
            if inside and self._command:
                self._command()

    def _resize_to_text(self):
        w = _measure_text(self._text, self._font_size, self._bold) + 2 * self._pad_x
        self.configure(width=max(56, w), height=self._height)

    def _draw(self):
        self.delete("all")
        w = max(int(self.winfo_reqwidth()), 40)
        h = self._height
        bg, fg = self._colors()
        r = h / 2.0
        self._pill(1, 1, w - 1, h - 1, r, bg)
        self.create_text(w / 2, h / 2 + 1, text=self._text, fill=fg,
                         font=(ui_font_family(), self._font_size,
                               "bold" if self._bold else "normal"))

    def _pill(self, x0, y0, x1, y1, r, color):
        draw_pill(self, x0, y0, x1, y1, radius=r, fill=color)


class RoundToggle(tk.Canvas):
    """圆形开关（删除前二次确认）：圆环 + 内部实心圆点，右侧为文字标签。"""

    def __init__(self, master, text="", variable=None, command=None, height=30, **kw):
        super().__init__(master, highlightthickness=0, bd=0, bg=UI["card"],
                         height=height, **kw)
        self._text = text
        self._var = variable
        self._command = command
        self._height = height
        self.bind("<Button-1>", self._toggle)
        self.bind("<Enter>", lambda _e: self._draw(hover=True))
        self.bind("<Leave>", lambda _e: self._draw(hover=False))
        if variable is not None:
            try:
                variable.trace_add("write", lambda *_: self._draw())
            except Exception:
                pass
        self._resize_to_text()

    def configure(self, cnf=None, **kw):
        text = kw.pop("text", None)
        if cnf or kw:
            super().configure(cnf, **kw)
        if text is not None:
            self._text = text
            self._resize_to_text()
        self._draw()
        return self

    config = configure

    def cget(self, key):
        if key == "text":
            return self._text
        return super().cget(key)

    def refresh_theme(self):
        try:
            self.configure(bg=UI["card"])
        except tk.TclError:
            return
        self._draw()

    def _value(self) -> bool:
        try:
            return bool(self._var.get())
        except Exception:
            return False

    def _toggle(self, _e=None):
        if self._var is None:
            return
        self._var.set(not self._value())
        if self._command:
            self._command()
        self._draw()

    def _resize_to_text(self):
        w = 26 + _measure_text(self._text, 10) + 8
        self.configure(width=max(60, w), height=self._height)

    def _draw(self, hover=False):
        self.delete("all")
        on = self._value()
        cy = self._height / 2
        r = 9
        cx = 12
        ring = UI["accent"] if on else (UI["accent_dark"] if hover else UI["muted"])
        self.create_oval(cx - r, cy - r, cx + r, cy + r, outline=ring,
                         width=2, fill=UI["card"])
        if on:      # 实心圆点
            self.create_oval(cx - r + 4, cy - r + 4, cx + r - 4, cy + r - 4,
                             outline=ring, fill=ring)
        self.create_text(cx + r + 10, cy, text=self._text, anchor="w",
                         fill=UI["text"], font=(ui_font_family(), 10))


class RoundRadio(tk.Canvas):
    """自绘单选按钮：较大的圆环 + 选中时内部实心圆点（替代 ttk.Radiobutton）。

    ttk 在 clam 主题下的单选圆点偏小，这里统一画成 20px 圆环 + 10px 实心点，
    文字在右侧；同一 variable 的按钮通过 trace 自动同步重绘。"""

    def __init__(self, master, text="", variable=None, value=None, command=None,
                 diameter=20, height=32, font_size=10, **kw):
        super().__init__(master, highlightthickness=0, bd=0, bg=UI["card"],
                         height=height, **kw)
        self._text = text
        self._var = variable
        self._value = value
        self._command = command
        self._diameter = diameter
        self._height = height
        self._font_size = font_size
        self._state = "normal"
        self._hover = False
        self.bind("<Button-1>", self._select)
        self.bind("<Enter>", lambda _e: self._set_hover(True))
        self.bind("<Leave>", lambda _e: self._set_hover(False))
        if variable is not None:
            try:
                variable.trace_add("write", lambda *_: self._draw())
            except Exception:
                pass
        self._resize_to_text()

    # ---- 与 ttk 兼容的接口 ----
    def configure(self, cnf=None, **kw):
        text = kw.pop("text", None)
        state = kw.pop("state", None)
        if state is not None:
            self._state = "disabled" if str(state) == "disabled" else "normal"
        if cnf or kw:
            super().configure(cnf, **kw)
        if text is not None:
            self._text = text
            self._resize_to_text()
        self._draw()
        return self

    config = configure

    def cget(self, key):
        if key == "text":
            return self._text
        if key == "state":
            return self._state
        return super().cget(key)

    def invoke(self):
        if self._state != "disabled":
            self._select()

    def instate(self, spec):
        specs = [spec] if isinstance(spec, str) else list(spec)
        for item in specs:
            item = str(item)
            negate = item.startswith("!")
            if item.lstrip("!") != "disabled":
                continue
            is_disabled = self._state == "disabled"
            if negate and is_disabled:
                return False
            if not negate and not is_disabled:
                return False
        return True

    def refresh_theme(self):
        try:
            self.configure(bg=UI["card"])
        except tk.TclError:
            return
        self._draw()

    # ---- 内部 ----
    def _selected(self) -> bool:
        try:
            return str(self._var.get()) == str(self._value)
        except Exception:
            return False

    def _select(self, _e=None):
        if self._state == "disabled" or self._var is None:
            return None
        self._var.set(self._value)
        if self._command:
            self._command()
        self._draw()
        return None

    def _set_hover(self, value):
        self._hover = bool(value) and self._state != "disabled"
        self._draw()

    def _resize_to_text(self):
        w = self._diameter + 10 + _measure_text(self._text, self._font_size) + 6
        self.configure(width=max(70, w), height=self._height)

    def _draw(self):
        self.delete("all")
        on = self._selected()
        cy = self._height / 2
        r = self._diameter / 2.0
        cx = 2 + r
        if self._state == "disabled":
            ring = UI["disabled_fg"]
            fg = UI["disabled_fg"]
        else:
            ring = UI["accent"] if (on or self._hover) else UI["muted"]
            fg = UI["text"]
        self.create_oval(cx - r, cy - r, cx + r, cy + r, outline=ring, width=2,
                         fill=UI["card"])
        if on:                                  # 内部实心圆点（比 ttk 更大更醒目）
            dot = r - 5
            self.create_oval(cx - dot, cy - dot, cx + dot, cy + dot,
                             outline=UI["accent"], fill=UI["accent"])
        self.create_text(cx + r + 10, cy, text=self._text, anchor="w", fill=fg,
                         font=(ui_font_family(), self._font_size))


class PillSlider(tk.Canvas):
    """药丸形滑块（缩略图大小）：圆角轨道 + 药丸形滑块，拖动即时生效。"""

    def __init__(self, master, variable=None, from_=0, to=2, command=None,
                 width=150, height=24, **kw):
        super().__init__(master, highlightthickness=0, bd=0, bg=UI["card"],
                         width=width, height=height, **kw)
        self._var = variable
        self._from, self._to = from_, to
        self._command = command
        self._bar_w, self._bar_h = width, height
        self._bar_hover = False
        self._dragging = False
        self.bind("<Button-1>", self._on_press)
        self.bind("<B1-Motion>", self._on_drag)
        self.bind("<ButtonRelease-1>", self._on_release)
        self.bind("<Enter>", lambda _e: self._set_hover(True))
        self.bind("<Leave>", lambda _e: self._set_hover(False))
        if variable is not None:
            try:
                variable.trace_add("write", lambda *_: self._draw())
            except Exception:
                pass
        self._draw()

    def refresh_theme(self):
        try:
            self.configure(bg=UI["card"])
        except tk.TclError:
            return
        self._draw()

    def _value(self):
        try:
            return float(self._var.get())
        except Exception:
            return float(self._from)

    def configure(self, cnf=None, **kw):
        """兼容 ttk.Scale 的 configure(state=...)：滑块无禁用态，忽略该选项。"""
        kw.pop("state", None)
        if cnf or kw:
            super().configure(cnf, **kw)
        self._draw()
        return self

    config = configure

    def _set_value(self, value, notify=True):
        value = max(self._from, min(self._to, value))
        snapped = round(value)
        if self._var is not None:
            self._var.set(snapped)
        self._draw()
        if notify and self._command:
            self._command(snapped)

    def _x_for(self, value):
        pad = 10
        span = max(1, self._bar_w - 2 * pad)
        ratio = (value - self._from) / max(1e-6, (self._to - self._from))
        return pad + ratio * span

    def _value_for(self, x):
        pad = 10
        span = max(1, self._bar_w - 2 * pad)
        ratio = (x - pad) / span
        return self._from + max(0.0, min(1.0, ratio)) * (self._to - self._from)

    def _on_press(self, event):
        self._dragging = True
        self._set_value(self._value_for(event.x))

    def _on_drag(self, event):
        if self._dragging:
            self._set_value(self._value_for(event.x))

    def _on_release(self, _e=None):
        self._dragging = False
        self._set_value(round(self._value()))
        self._draw()

    def _set_hover(self, value):
        self._bar_hover = value
        self._draw()

    def _draw(self):
        self.delete("all")
        cy = self._bar_h / 2
        trough_h = 8
        # 轨道（药丸形）
        self._pill(6, cy - trough_h / 2, self._bar_w - 6, cy + trough_h / 2,
                   trough_h / 2, UI["trough"])
        # 已选区间（主题色）
        x = self._x_for(self._value())
        if x > 16:
            self._pill(6, cy - trough_h / 2, x, cy + trough_h / 2,
                       trough_h / 2, UI["accent"])
        # 药丸形滑块
        knob_w, knob_h = 20, 18
        color = UI["accent_dark"] if (self._bar_hover or self._dragging) else UI["accent"]
        self._pill(x - knob_w / 2, cy - knob_h / 2, x + knob_w / 2, cy + knob_h / 2,
                   knob_h / 2, color)
        self.create_oval(x - 2.5, cy - 2.5, x + 2.5, cy + 2.5,
                         fill="#ffffff", outline="#ffffff")

    def _pill(self, x0, y0, x1, y1, r, color):
        draw_pill(self, x0, y0, x1, y1, radius=r, fill=color)


class PillSelect(tk.Canvas):
    """自绘药丸形下拉选择框（替代 ttk.Combobox）。

    为什么不用 ttk.Combobox：只读下拉框在切换取值后经常不重绘显示文本
    （浅色主题下点选后表现为"空白"，必须再点别处才显示），而且它的弹出列表
    是首次点开时才创建的独立控件，主题切换后容易残留旧配色。
    自绘控件每次取值变化都直接重画，天然不存在这两个问题。

    兼容接口：get()/set()/configure(values=/state=)/cget("values")/instate()。"""

    def __init__(self, master, variable=None, values=(), command=None,
                 width=150, height=30, font_size=10, pad_x=12, **kw):
        super().__init__(master, highlightthickness=0, bd=0, bg=UI["card"],
                         width=width, height=height, **kw)
        self._var = variable
        self._values = list(values)
        self._command = command
        self._box_w, self._box_h = width, height
        self._font_size = font_size
        self._pad_x = pad_x
        self._state = "normal"
        self._box_hover = False
        self._menu = None
        self.bind("<Button-1>", self._open_menu)
        self.bind("<Enter>", lambda _e: self._set_hover(True))
        self.bind("<Leave>", lambda _e: self._set_hover(False))
        if variable is not None:
            try:
                variable.trace_add("write", lambda *_: self._draw())
            except Exception:
                pass
        self._draw()

    # ---- 兼容接口 ----
    def configure(self, cnf=None, **kw):
        values = kw.pop("values", None)
        state = kw.pop("state", None)
        if values is not None:
            self._values = list(values)
        if state is not None:
            self._state = "disabled" if str(state) == "disabled" else "normal"
        if cnf or kw:
            super().configure(cnf, **kw)
        self._draw()
        return self

    config = configure

    def cget(self, key):
        if key == "values":
            return list(self._values)
        if key == "state":
            return self._state
        return super().cget(key)

    def instate(self, spec):
        specs = [spec] if isinstance(spec, str) else list(spec)
        for item in specs:
            item = str(item)
            negate = item.startswith("!")
            if item.lstrip("!") != "disabled":
                continue
            is_disabled = self._state == "disabled"
            if negate and is_disabled:
                return False
            if not negate and not is_disabled:
                return False
        return True

    def get(self):
        try:
            return self._var.get() if self._var is not None else ""
        except Exception:
            return ""

    def set(self, value):
        if self._var is not None:
            self._var.set(value)
        self._draw()

    def current(self, index=None):
        if index is None:
            try:
                return self._values.index(self.get())
            except ValueError:
                return -1
        if 0 <= index < len(self._values):
            self.set(self._values[index])
        return None

    def refresh_theme(self):
        try:
            self.configure(bg=UI["card"])
        except tk.TclError:
            return
        self._draw()

    # ---- 内部 ----
    def _set_hover(self, value):
        self._box_hover = value and self._state != "disabled"
        self._draw()

    def _open_menu(self, _e=None):
        if self._state == "disabled" or not self._values:
            return
        menu = tk.Menu(self, tearoff=0, bg=UI["card"], fg=UI["text"],
                       activebackground=UI["accent"], activeforeground="#ffffff",
                       bd=0, relief=tk.FLAT,
                       font=(ui_font_family(), self._font_size))
        for value in self._values:
            menu.add_command(label=value, command=lambda v=value: self._choose(v))
        self._menu = menu
        try:
            menu.tk_popup(self.winfo_rootx(),
                          self.winfo_rooty() + self.winfo_height() - 2)
        finally:
            try:
                menu.grab_release()
            except tk.TclError:
                pass

    def _choose(self, value):
        if self._var is not None:
            self._var.set(value)
        self._draw()
        if self._command:
            self._command()

    def _draw(self):
        self.delete("all")
        w, h = self._box_w, self._box_h
        if self._state == "disabled":
            bg, fg = UI["disabled_bg"], UI["disabled_fg"]
        else:
            bg = UI["card_alt"]
            fg = UI["text"]
            if self._box_hover:
                bg = UI["accent_soft"]
        draw_pill(self, 1, 1, w - 1, h - 1, radius=(h - 2) / 2.0, fill=bg,
                  outline=UI["border"])
        # 文本（左对齐，过长自动截断）
        text = self.get()
        avail = w - 2 * self._pad_x - 18
        while text and _measure_text(text, self._font_size) > avail:
            text = text[:-1]
        self.create_text(self._pad_x, h / 2, text=text, anchor="w", fill=fg,
                         font=(ui_font_family(), self._font_size))
        # 右侧小三角
        cx, cy = w - 12, h / 2
        self.create_polygon(cx - 4, cy - 2, cx + 4, cy - 2, cx, cy + 3,
                            fill=UI["muted"] if self._state != "disabled" else fg,
                            outline="")


class CheckBadge(tk.Canvas):
    """缩略图右上角的勾选角标——极简样式：
    · 勾选：圆角方框 + 方框中间一个勾
    · 取消：只留空圆角方框
    方框与勾都采用"深色细描边 + 白色主体"的双色画法：白色在深色照片上清晰，
    深色轮廓在浅色照片上也不会看不见（不做网点填充，避免出现"井字形"花纹）。
    切换勾选只重绘这 26px 小画布（O(1)，批量勾选也不卡）。"""

    PAD = 3
    RADIUS = 6

    def __init__(self, master, checked=True, on_toggle=None, size=26):
        super().__init__(master, width=size, height=size, highlightthickness=0,
                         bd=0, bg=UI["cell"], cursor="hand2")
        self._checked = checked
        self._on_toggle = on_toggle
        self._size = size
        self.bind("<Button-1>", self._click)
        self._draw()

    def set_checked(self, checked: bool):
        if self._checked != checked:
            self._checked = checked
            self._draw()

    def refresh_theme(self):
        try:
            self.configure(bg=UI["cell"])
        except tk.TclError:
            return
        self._draw()

    def _click(self, _e=None):
        if self._on_toggle:
            self._on_toggle()
        return "break"

    def _draw(self):
        self.delete("all")
        s = self._size
        pad = self.PAD
        box = (pad, pad, s - pad, s - pad)
        dark, light = "#1b2028", "#ffffff"
        # 圆角方框：先深色粗线，再用白色覆盖中间 —— 深浅照片上都清晰
        draw_rounded_outline(self, *box, self.RADIUS, dark, 4)
        draw_rounded_outline(self, *box, self.RADIUS, light, 2)
        if self._checked:                       # 方框中间加勾（同样双色）
            cx = cy = s / 2.0
            pts = (cx - 6, cy + 0.5, cx - 1.5, cy + 5, cx + 6, cy - 4.5)
            self.create_line(*pts, fill=dark, width=6, capstyle="round",
                             joinstyle="round")
            self.create_line(*pts, fill=light, width=3, capstyle="round",
                             joinstyle="round")


class RoundedCard(tk.Canvas):
    """圆角卡片容器：自身是 Canvas，圆角矩形背景 + 内部 Frame（承载实际内容）。

    expand=False：卡片高度自适应内容（工具栏/底部/结果区）。
    expand=True ：卡片高度跟随父容器（列表/预览区放在分隔窗格中），
                  内部 Frame 同时被拉伸——否则窗口变小时内容会比窗格高，
                  导致 Treeview 被裁切且滚动位置计算错乱。
    """

    def __init__(self, master, radius=16, pad=(14, 12), expand=False, **kw):
        super().__init__(master, highlightthickness=0, bd=0, bg=UI["bg"], **kw)
        self._radius = radius
        self._pad = pad
        self._expand = expand
        self.inner = tk.Frame(self, bg=UI["card"])
        self._win = self.create_window(pad[0], pad[1], window=self.inner, anchor="nw")
        self.inner.bind("<Configure>", self._on_inner)
        self.bind("<Configure>", self._on_self)

    def _on_inner(self, _e=None):
        if not self._expand:
            want = self.inner.winfo_reqheight() + 2 * self._pad[1]
            if abs(want - self.winfo_height()) > 1:
                self.configure(height=want)
        self._draw()

    def _on_self(self, event):
        width = max(20, event.width - 2 * self._pad[0])
        if self._expand:
            # 拉伸内部内容以填满卡片（内容随之收缩，滚动计算才正确）
            self.itemconfigure(self._win, width=width,
                               height=max(20, event.height - 2 * self._pad[1]))
        else:
            self.itemconfigure(self._win, width=width)
        self._draw()

    def refresh_theme(self):
        try:
            self.configure(bg=UI["bg"])
            self.inner.configure(bg=UI["card"])
        except tk.TclError:
            return
        self._draw()

    def _draw(self):
        # 只清除"背景形状"，绝不能 delete("all")：
        # 卡片内容是通过 create_window 挂在这个 Canvas 上的，
        # 一旦被一起删除，卡片内的全部控件就会消失（界面一片空白）。
        self.delete("cardbg")
        w, h = self.winfo_width(), self.winfo_height()
        if w <= 4 or h <= 4:
            return
        r = min(self._radius, h / 2, w / 2)
        self._rounded(1, 1, w - 1, h - 1, r, UI["card"], UI["border"])

    def _rounded(self, x0, y0, x1, y1, r, fill, outline):
        draw_pill(self, x0, y0, x1, y1, radius=r, fill=fill, outline=outline,
                  tags=("cardbg",))



class RoundScrollbar(tk.Canvas):
    """自绘圆润滚动条：轨道与滑块都是"两头圆润的长方形"（胶囊形），
    支持悬停加深、按住拖动、点击空白翻页，深浅主题自动适配。
    对外接口与 ttk.Scrollbar 一致（set(first, last) + command）。"""

    def __init__(self, master, orient="vertical", command=None, thickness=12, **kw):
        self._vertical = (orient == "vertical")
        super().__init__(master,
                         width=thickness if self._vertical else 1,
                         height=1 if self._vertical else thickness,
                         highlightthickness=0, bd=0, bg=UI["card"], **kw)
        self._command = command
        self._first, self._last = 0.0, 1.0
        self._hover = False
        self._drag_offset = None
        self._thumb_px = (0, 0)
        self.bind("<Configure>", lambda _e: self._redraw())
        self.bind("<Button-1>", self._on_press)
        self.bind("<B1-Motion>", self._on_drag)
        self.bind("<ButtonRelease-1>", self._on_release)
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
        self.bind("<MouseWheel>", self._on_wheel)

    # ----- 与滚动组件对接 -----
    def set(self, first, last):
        try:
            first, last = float(first), float(last)
        except (TypeError, ValueError):
            return
        if (first, last) == (self._first, self._last):
            return  # 无变化不重绘，长列表滚动时零额外开销
        self._first, self._last = first, last
        self._redraw()

    def refresh_theme(self):
        """主题切换后刷新底色与配色。"""
        try:
            self.configure(bg=UI["card"])
        except tk.TclError:
            return
        self._redraw()

    # ----- 交互 -----
    def _on_enter(self, _e=None):
        self._hover = True
        self._redraw()

    def _on_leave(self, _e=None):
        self._hover = False
        self._redraw()

    def _on_press(self, event):
        pos = event.y if self._vertical else event.x
        start, end = self._thumb_px
        if start <= pos <= end:
            self._drag_offset = pos - start
        else:
            self._drag_offset = None
            self._scroll(-1 if pos < start else 1, "pages")
        self._redraw()

    def _on_drag(self, event):
        if self._drag_offset is None or not self._command:
            return
        pos = event.y if self._vertical else event.x
        span = max(1, self._total() - 4)
        frac = (pos - self._drag_offset - 2) / span
        frac = min(max(frac, 0.0), 1.0)
        try:
            self._command("moveto", f"{frac:.4f}")
        except tk.TclError:
            pass

    def _on_release(self, _e=None):
        self._drag_offset = None
        self._redraw()

    def _on_wheel(self, event):
        self._scroll(-1 if event.delta > 0 else 1, "units")
        return "break"

    def _scroll(self, number, what):
        if self._command:
            try:
                self._command("scroll", number, what)
            except tk.TclError:
                pass

    # ----- 绘制 -----
    def _total(self):
        return self.winfo_height() if self._vertical else self.winfo_width()

    def _pill(self, x0, y0, x1, y1, color):
        """两端正圆的圆角胶囊（统一调用 draw_pill，避免被拉成椭圆）。"""
        draw_pill(self, x0, y0, x1, y1,
                  radius=min(x1 - x0, y1 - y0) / 2.0, fill=color)

    def _redraw(self):
        self.delete("all")
        total = self._total()
        if total <= 6:
            return
        pad = 3
        span = max(1, total - 2 * pad)
        # 滑块最小长度保证"长方形 + 两端圆角"的观感（而不是被压成椭圆）
        min_len = 46
        thumb_len = max(min_len, int((self._last - self._first) * span))
        start = pad + int(self._first * span)
        start = max(pad, min(start, total - pad - thumb_len))
        end = min(total - pad, start + thumb_len)
        self._thumb_px = (start, end)
        active = self._hover or self._drag_offset is not None
        thumb = UI["scroll_hover"] if active else UI["scroll"]
        w = self.winfo_width() if self._vertical else self.winfo_height()
        # 轨道（极浅的圆角长条）+ 滑块（药丸形）
        if self._vertical:
            draw_pill(self, pad, pad, w - pad, total - pad,
                      radius=(w - 2 * pad) / 2.0, fill=UI["trough"])
            draw_pill(self, pad + 1, start, w - pad - 1, end,
                      radius=(w - 2 * pad - 2) / 2.0, fill=thumb)
        else:
            draw_pill(self, pad, pad, total - pad, w - pad,
                      radius=(w - 2 * pad) / 2.0, fill=UI["trough"])
            draw_pill(self, start, pad + 1, end, w - pad - 1,
                      radius=(w - 2 * pad - 2) / 2.0, fill=thumb)


class RoundButton(tk.Canvas):
    """圆形操作按钮（二次确认弹窗专用）：默认描边 + 浅色底，
    按下时变为实心填充；使用箭头/对勾等中性符号，不使用"×"避免误触。"""

    def __init__(self, master, glyph, text, style="neutral", command=None):
        super().__init__(master, width=72, height=72, highlightthickness=0, bd=0,
                         bg=UI["card"], cursor="hand2")
        self._glyph = glyph
        self._text = text
        self._style = style          # neutral / danger
        self._command = command
        self._active = False
        self._hover = False
        self.bind("<Button-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)
        self.bind("<Enter>", lambda _e: self._set_hover(True))
        self.bind("<Leave>", lambda _e: self._set_hover(False))
        self._draw()

    def set_text(self, text):
        self._text = text
        self._draw()

    def refresh_theme(self):
        try:
            self.configure(bg=UI["card"])
        except tk.TclError:
            return
        self._draw()

    def _colors(self):
        if self._style == "danger":
            main = UI["danger"]
            soft = UI["danger"]
        else:
            main = UI["muted"]
            soft = UI["muted"]
        return main, soft

    def _set_hover(self, value):
        self._hover = value
        self._draw()

    def _on_press(self, _e=None):
        self._active = True
        self._draw()

    def _on_release(self, event=None):
        was_active = self._active
        self._active = False
        self._draw()
        if was_active and self._command:
            self._command()

    def _draw(self):
        self.delete("all")
        main, _soft = self._colors()
        cx = cy = 36
        r = 26
        if self._active:                      # 按下：实心填充
            fill, outline, fg = main, main, "#ffffff"
        elif self._hover:
            fill, outline, fg = UI["accent_soft"], main, main
        else:
            fill, outline, fg = UI["card"], main, main
        self.create_oval(cx - r, cy - r, cx + r, cy + r,
                         fill=fill, outline=outline, width=2)
        self.create_text(cx, cy, text=self._glyph, fill=fg,
                         font=(ui_font_family(), 18, "bold"))


class App(tk.Tk):
    """主窗口。"""

    MODE_KEYS = {
        "jpg": "mode_jpg",
        "raw": "mode_raw",
        "all": "mode_all",
    }
    # 缩略图大小三档（正方形基准边长），档位由滑块选择
    THUMB_LEVELS = ["小", "中", "大"]
    THUMB_SIZES = {"小": 120, "中": 200, "大": 320}
    CELL_PAD_X = 8   # 网格单元水平内边距
    CELL_PAD_Y = 46  # 网格单元底部预留（文件名单行 + 边距，避免文字被遮挡）
    MIN_CONTENT_W = 940  # 布局最小可用宽度（窄于此值卡片右侧控件会被裁掉）

    def __init__(self):
        super().__init__()
        self.title(f"{APP_NAME}  ·  {APP_AUTHOR}")
        # 默认窗口：现代卡片式布局一屏可见（列表 + 预览 + 结果区）
        self.geometry("1120x1000")
        self.minsize(self.MIN_CONTENT_W, 760)
        # 界面字体（一次性探测，自绘控件也复用）
        self._font_family = self._pick_font_family()
        set_ui_font_family(self._font_family)

        # 上次使用的配置（读取失败时用默认值）
        cfg = load_config()

        # 主题：auto = 跟随系统深浅色；用户手动切换后写入配置
        self._theme_pref = str(cfg.get("theme") or "auto")
        self._dark = resolve_theme(self._theme_pref) == "dark"
        set_theme("dark" if self._dark else "light")
        self._setup_styles()
        self.configure(bg=UI["bg"])

        self.orphans: list = []          # 最近一次扫描得到的孤立文件
        self.busy = False                # 是否正在扫描/删除
        self.current_folder = ""         # 当前列表对应的文件夹
        self._custom_text = str(cfg.get("raw_custom", "") or "")  # 自定义后缀内容
        self._cfg_sash = 0
        self._force_mode = False         # 上次扫描未匹配到 RAW（强制删除模式）
        self._about_shown = bool(cfg.get("about_shown", False))  # 感谢"关于"是否已弹出过

        # 缩略图相关
        self._preview_token = 0                # 生成任务令牌（换列表时旧任务自动作废）
        self._preview_status_label = None      # 预览区提示标签
        self._preview_items: dict = {}         # 完整路径 -> 预览条目控件信息
        self._tree_iid_by_path: dict = {}      # 完整路径 -> 列表行 iid
        self._closing = False
        self._ui_queue = queue.Queue()         # 工作线程 -> 主线程的消息队列
        self._resize_job = None                # 窗口调整后的防抖重建任务
        self._last_canvas_width = 0            # 上次布局时的画布宽度
        self._thumb_cache: dict = {}           # 路径 -> 120px 缩略图（最小档缓存）
        self._exif_cache: dict = {}            # 路径 -> EXIF 结构化字典
        self._size_job = None                  # 滑块档位防抖任务
        self._resize_token = 0                 # 档位缩放任务令牌（旧任务作废）
        self._scan_summary = None              # 最近一次扫描摘要（语言切换时重译状态栏）
        self._preview_status = None            # 预览状态条摘要（语言切换时重译）
        self._result_entries: list = []        # 结果区结构化条目（语言切换时重译）
        self._preview_placeholder = None       # 预览区空状态提示控件（语言切换时重译）
        self._preview_placeholder_key = None   # 该提示对应的语言键
        self._about_window = None              # 关于窗口引用（打开时语言切换同步重译）
        self._about_render = None              # 关于窗口内容渲染函数
        self._checked: set = set()             # 勾选（=将被删除）的文件完整路径
        self._unchecked_saved = {str(p) for p in (cfg.get("unchecked") or [])}
        self._hl_path = None                   # 预览区当前高亮单元路径
        self._picked_iid = None                # 列表当前选中高亮行
        # 界面模式与对比视图设置（用户可自主选择界面，选择写入配置）
        self._ui_mode = str(cfg.get("ui_mode") or "classic")
        if self._ui_mode not in ("classic", "pair"):
            self._ui_mode = "classic"
        self._pair_color = str(cfg.get("pair_color") or "bg")
        if self._pair_color not in ("bg", "fg"):
            self._pair_color = "bg"
        self._pair_only_missing = bool(cfg.get("pair_only_missing"))
        self.scan_result = None                # 最近一次扫描结果（含配对表）
        self._pair_iid_by_path: dict = {}      # 对比视图：路径 -> 行 iid
        self._pair_rows: list = []             # 对比视图当前显示的行
        self._pair_sort = None                 # 对比视图排序：(列, 是否降序)
        self._picked_pair_iid = None           # 对比视图当前选中高亮行
        self._bar_widgets: list = []           # 自绘滚动条（主题切换时刷新）
        self._round_buttons: list = []         # 圆形按钮（主题切换时刷新）
        self._cards: list = []                 # 圆角卡片（主题切换时刷新）
        self._sash_frac = 0.45                 # 列表区高度占比（可按窗口缩放）
        self._sash_inited = False              # 是否已按保存值初始化过比例

        # 界面语言：首次启动按系统语言自动选择并写入配置；之后以用户选择为准
        self._lang_data = _load_lang_data()    # 语言资源（外置 language.json，英语兜底）
        self._lang = str(cfg.get("lang") or "") or detect_system_language()
        if self._lang not in LANG_CODES:
            self._lang = FALLBACK_LANG
        self._exif_detailed = False            # EXIF 简略展示（默认）/ 详细展示
        self._exif_current_path = None         # 当前显示的 EXIF 对应文件
        self._i18n_controls: list = []         # [(控件, 语言键)] 静态文本注册表
        self._raw_map: dict = {}               # RAW 下拉显示文本 -> 内部 id
        self._level_map: dict = {}             # 层级下拉显示文本 -> 内部 id
        self._lang_map: dict = {}              # 语言下拉显示文本 -> 语言代码

        # 缩略图档位（配置记忆，默认"中"）
        thumb_level = cfg.get("thumb_level", "中")
        if thumb_level not in self.THUMB_LEVELS:
            thumb_level = "中"
        self._thumb_level = thumb_level
        # 用 DoubleVar 保存滑块浮点值，便于拖动时吸附到整数档位
        # （IntVar 会直接把 1.6 截断成 1，导致吸附判断失效）
        self.thumb_level_var = tk.DoubleVar(value=self.THUMB_LEVELS.index(thumb_level))

        # 界面变量（应用配置记忆；显示文本在建界面后按语言重设）
        self.path_var = tk.StringVar(value=str(cfg.get("folder", "") or ""))
        raw_mode = str(cfg.get("raw_mode") or AUTO_ID)
        if raw_mode not in RAW_FORMATS and raw_mode not in (AUTO_ID, CUSTOM_ID):
            raw_mode = AUTO_ID
        self._raw_mode_internal = raw_mode     # RAW 模式内部 id（显示文本经下拉框映射）
        self.raw_mode_var = tk.StringVar(value="")
        self.raw_entry_var = tk.StringVar(value="")
        level = str(cfg.get("scan_level") or "cur")
        if level not in SCAN_LEVEL_MAX_DEPTH:
            level = "cur"
        self._level_internal_value = level     # 层级内部 id
        self.level_var = tk.StringVar(value="")
        self.mode_var = tk.StringVar(value="all")     # jpg / raw / all
        self.confirm_var = tk.BooleanVar(value=bool(cfg.get("confirm", True)))
        self.status_var = tk.StringVar(value="")

        self._build_ui()
        self._bind_tree()
        # 跟踪自定义后缀输入框的变化（切换模式后能恢复用户输入的内容）
        self.raw_entry_var.trace_add("write", self._on_raw_entry_edit)
        self.protocol("WM_DELETE_WINDOW", self._on_close)
        # 启动主线程队列轮询器：工作线程一律通过队列回传 UI 更新
        # （tkinter 的 after() 仅当主线程处于事件循环内才能被其他线程安全调用）
        self._poller_after_id = None
        self._schedule_poll()

        # 应用配置：按当前语言刷新界面文本与下拉框显示
        self._apply_language()
        self._apply_raw_mode_ui()
        self._apply_view_mode()      # 按保存的界面模式显示经典列表或配对对比
        try:
            self._cfg_sash = int(cfg.get("sash") or 0)
        except (TypeError, ValueError):
            self._cfg_sash = 0
        geom = str(cfg.get("geometry", "") or "")
        m = re.fullmatch(r"(\d+)x(\d+)([+-]\d+)([+-]\d+)", geom)
        if m:
            # 旧版可能保存过小于当前布局所需尺寸、或超出屏幕的窗口位置：
            # 统一夹取到"不小于内容最小尺寸、且完整落在屏幕内"，避免控件被裁掉
            w = max(int(m.group(1)), self.MIN_CONTENT_W)
            h = max(int(m.group(2)), 700)
            x, y = int(m.group(3)), int(m.group(4))
            try:
                sw, sh = self.winfo_screenwidth(), self.winfo_screenheight()
                w, h = min(w, sw - 40), min(h, sh - 100)
                x = max(0, min(x, sw - w - 20))
                y = max(0, min(y, sh - h - 60))
            except tk.TclError:
                pass
            try:
                self.geometry(f"{w}x{h}+{x}+{y}")
            except tk.TclError:
                pass  # 非法几何信息则保持默认
        self._restore_sash_job = None
        if self._cfg_sash > 0:
            self._restore_sash_job = self.after(300, self._restore_sash)
        else:
            # 首次运行/未保存：延迟设置合理的默认分隔比例
            self._restore_sash_job = self.after(400, self._restore_sash)

        # 首次启动（配置中没有语言）：把系统语言检测结果与主题写入配置，
        # 之后一律以用户手动选择为准，不再每次启动重新检测
        if not str(cfg.get("lang") or ""):
            self._persist_startup_choices()

        # 窗口/任务栏图标（源码运行用同目录图标；打包后从解压目录读取）
        try:
            self.iconbitmap(default=resource_path("camera.ico"))
        except Exception:
            pass  # 图标缺失不影响使用

    def _restore_sash(self):
        """恢复/初始化列表与预览区的分隔条位置（首次布局完成后调用）。"""
        self._restore_sash_job = None
        self._on_paned_configure()

    def _on_paned_configure(self, _event=None):
        """按比例维护列表 / 预览区的高度分配：
        · 首次：用配置里的保存值换算成比例（越界自动夹取），否则用默认比例；
        · 之后每次尺寸变化都按同一比例重算，保证两个区域都有合理高度
          （只按权重分配会把其中一个区域挤成一条，导致看不到内容、也无法滚动）；
        · 用户手动拖动分隔条后沿用其拖出的比例。"""
        if self._closing:
            return
        try:
            total = self.main_paned.winfo_height()
        except tk.TclError:
            return
        if total < 200:
            return
        if not self._sash_inited:
            if self._cfg_sash > 0:
                # 保存值按比例换算，并夹取到合理区间（防止旧配置的异常值把某区域挤没）
                self._sash_frac = min(0.65, max(0.25, self._cfg_sash / float(total)))
            self._sash_inited = True
        target = int(total * self._sash_frac)
        # 列表至少 140px（约 3 行，否则 Treeview 不足一行高、滚动条会退化成零长度），
        # 预览区至少 120px；窗口很矮时优先保证列表可用
        target = max(140, min(target, total - 120))
        try:
            if abs(self.main_paned.sashpos(0) - target) > 2:
                self.main_paned.sashpos(0, target)
        except tk.TclError:
            pass

    def _on_sash_user_drag(self, _event=None):
        """用户拖动分隔条：记录比例，后续窗口缩放沿用该比例。"""
        try:
            total = self.main_paned.winfo_height()
            if total > 0:
                self._sash_frac = min(0.85, max(0.10,
                                                self.main_paned.sashpos(0) / float(total)))
                self._sash_inited = True
        except tk.TclError:
            pass

    # ----- 现代界面：字体与 ttk 样式 -----

    def _pick_font_family(self) -> str:
        """选择界面字体：优先中文渲染最佳的字体，缺失时逐级回退，全部缺失用默认。
        仅启动时探测一次（families() 有开销），运行期不再查询。"""
        try:
            from tkinter import font as tkfont
            families = set(tkfont.families(self))
            for name in UI_FONT_CANDIDATES:
                if name in families:
                    return name
        except Exception:
            pass
        return "TkDefaultFont"

    def _setup_styles(self):
        """配置 ttk 样式：扁平化卡片主题（clam 为基座，最大化可定制性）。
        主题切换时重新调用本方法即可整体换肤，控件无需重建。"""
        style = ttk.Style(self)
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass
        f = self._font_family
        base = (f, 10)
        bold = (f, 10, "bold")
        disabled_bg = UI["disabled_bg"]
        disabled_fg = UI["disabled_fg"]

        # 容器
        style.configure("TFrame", background=UI["bg"])
        style.configure("Card.TFrame", background=UI["card"])
        style.configure("Bar.TFrame", background=UI["card"])
        style.configure("Divider.TFrame", background=UI["border"])

        # 文本
        style.configure("TLabel", background=UI["card"], foreground=UI["text"], font=base)
        style.configure("Bg.TLabel", background=UI["bg"], foreground=UI["text"], font=base)
        style.configure("Title.TLabel", background=UI["card"], foreground=UI["accent"],
                        font=(f, 13, "bold"))
        style.configure("Muted.TLabel", background=UI["card"], foreground=UI["muted"],
                        font=(f, 9))
        style.configure("CardTitle.TLabel", background=UI["card"], foreground=UI["muted"],
                        font=bold)
        style.configure("Status.TLabel", background=UI["card"], foreground=UI["text"],
                        font=base)

        # 按钮：默认次级（浅灰底、深色字）；Accent 主题色；Danger 危险操作
        style.configure("TButton", font=base, padding=(12, 6), relief="flat",
                        borderwidth=0, background=UI["card_alt"], foreground=UI["text"],
                        focuscolor=UI["card"])
        style.map("TButton",
                  background=[("pressed", UI["border"]), ("active", UI["accent_soft"]),
                              ("disabled", disabled_bg)],
                  foreground=[("disabled", disabled_fg)])
        style.configure("Accent.TButton", font=bold, padding=(16, 6), relief="flat",
                        borderwidth=0, background=UI["accent"], foreground="#ffffff",
                        focuscolor=UI["accent"])
        style.map("Accent.TButton",
                  background=[("pressed", UI["accent_dark"]), ("active", UI["accent_dark"]),
                              ("disabled", disabled_bg)],
                  foreground=[("disabled", disabled_fg)])
        style.configure("Danger.TButton", font=bold, padding=(16, 6), relief="flat",
                        borderwidth=0, background=UI["danger"], foreground="#ffffff",
                        focuscolor=UI["danger"])
        style.map("Danger.TButton",
                  background=[("pressed", UI["danger_dark"]), ("active", UI["danger_dark"]),
                              ("disabled", disabled_bg)],
                  foreground=[("disabled", disabled_fg)])
        style.configure("Ghost.TButton", font=base, padding=(12, 5), relief="flat",
                        borderwidth=0, background=UI["card_alt"], foreground=UI["accent"],
                        focuscolor=UI["card"])
        style.map("Ghost.TButton",
                  background=[("pressed", UI["accent_soft"]), ("active", UI["accent_soft"])],
                  foreground=[("disabled", disabled_fg)])
        # 工具条上的小按钮（全选/全不选/主题/EXIF 模式）
        style.configure("Small.TButton", font=(f, 9), padding=(10, 4), relief="flat",
                        borderwidth=0, background=UI["card_alt"], foreground=UI["text"],
                        focuscolor=UI["card"])
        style.map("Small.TButton",
                  background=[("pressed", UI["border"]), ("active", UI["accent_soft"]),
                              ("disabled", disabled_bg)],
                  foreground=[("disabled", disabled_fg)])

        # 输入框与下拉框：卡片底、细描边、统一内边距
        style.configure("TEntry", fieldbackground=UI["card"], background=UI["card"],
                        foreground=UI["text"], bordercolor=UI["border"],
                        lightcolor=UI["border"], darkcolor=UI["border"],
                        insertcolor=UI["text"], padding=5, relief="flat")
        style.map("TEntry", bordercolor=[("focus", UI["accent"])],
                  lightcolor=[("focus", UI["accent"])],
                  darkcolor=[("focus", UI["accent"])])
        style.configure("TCombobox", fieldbackground=UI["card"], background=UI["card"],
                        foreground=UI["text"], bordercolor=UI["border"],
                        lightcolor=UI["border"], darkcolor=UI["border"],
                        arrowcolor=UI["muted"], padding=4, relief="flat")
        style.map("TCombobox",
                  fieldbackground=[("readonly", UI["card"]), ("disabled", UI["card_alt"])],
                  bordercolor=[("focus", UI["accent"]), ("hover", UI["accent"])],
                  arrowcolor=[("disabled", disabled_fg)])
        # 下拉列表（Tk 选项菜单）配色：option_add 只对"之后新建"的控件生效，
        # 而这些 Listbox 是首次弹出时才创建的，所以切换主题时还必须显式重设
        # 已经存在的下拉列表配色（否则浅色模式下弹出框仍是黑底白字 → 看不清）
        self.option_add("*TCombobox*Listbox.background", UI["card"])
        self.option_add("*TCombobox*Listbox.foreground", UI["text"])
        self.option_add("*TCombobox*Listbox.selectBackground", UI["accent"])
        self.option_add("*TCombobox*Listbox.selectForeground", "#ffffff")
        self.option_add("*TCombobox*Listbox.borderWidth", 0)
        self._restyle_combobox_popdowns()

        # 单选/复选：卡片底色、主题色指示器
        for name in ("TRadiobutton", "TCheckbutton"):
            style.configure(name, background=UI["card"], foreground=UI["text"],
                            font=base, focuscolor=UI["card"], padding=(0, 2))
            style.map(name,
                      background=[("active", UI["card"])],
                      foreground=[("disabled", disabled_fg)],
                      indicatorcolor=[("selected", UI["accent"]),
                                      ("!selected", UI["card"])])

        # 列表：行高按字体自适应、无边框、隔行底色、主题色选中
        try:
            from tkinter import font as _tkfont
            row_h = max(22, _tkfont.Font(family=self._font_family, size=10)
                        .metrics("linespace") + 6)
        except Exception:
            row_h = 26
        style.configure("Treeview", background=UI["card"], fieldbackground=UI["card"],
                        foreground=UI["text"], font=base, rowheight=row_h,
                        borderwidth=0, relief="flat")
        style.map("Treeview",
                  background=[("selected", UI["accent_soft"])],
                  foreground=[("selected", UI["accent_dark"])])
        style.configure("Treeview.Heading", background=UI["card_alt"],
                        foreground=UI["muted"], font=bold, relief="flat",
                        borderwidth=0, padding=(8, 7))
        style.map("Treeview.Heading",
                  background=[("active", UI["accent_soft"])],
                  foreground=[("active", UI["accent_dark"])])

        # 缩略图大小滑块
        style.configure("Horizontal.TScale", background=UI["card"],
                        troughcolor=UI["trough"], bordercolor=UI["card"],
                        lightcolor=UI["accent"], darkcolor=UI["accent"])
        style.map("Horizontal.TScale", background=[("active", UI["card"])])

        # 分组卡片（替代老式 LabelFrame 外观）
        style.configure("Card.TLabelframe", background=UI["card"],
                        bordercolor=UI["border"], borderwidth=1, relief="solid")
        style.configure("Card.TLabelframe.Label", background=UI["card"],
                        foreground=UI["muted"], font=bold)
        # 分隔条
        style.configure("Sash", sashthickness=10, gripcount=0,
                        background=UI["bg"], bordercolor=UI["bg"],
                        lightcolor=UI["bg"], darkcolor=UI["bg"])
        style.configure("TPanedwindow", background=UI["bg"])

    def _card(self, parent, title_key=None, padding=(12, 10), action=None,
              expand=False, height=None, title_attr=None):
        """创建圆角卡片容器；title_key 非空时在卡片顶部显示分组标题（注册进 i18n），
        action 为可选的 (控件工厂) 回调，用于在标题行右侧放置操作按钮；
        expand=True 时卡片高度跟随父容器（用于分隔窗格中的列表/预览卡片）；
        title_attr 非空时把标题控件保存为 self.<title_attr>（界面模式切换时要改标题）。
        返回 (卡片控件, 内容容器)。"""
        outer = RoundedCard(parent, pad=(padding[0], padding[1]), expand=expand)
        if height:                      # 供 ttk.PanedWindow 计算初始分隔比例
            outer.configure(height=height)
        self._cards.append(outer)
        if title_key:
            head = tk.Frame(outer.inner, bg=UI["card"])
            head.pack(fill=tk.X, pady=(0, 2))
            lbl = self._add_i18n(
                tk.Label(head, text=self.t(title_key), bg=UI["card"], fg=UI["muted"],
                         font=(self._font_family, 10, "bold")), title_key)
            lbl.pack(side=tk.LEFT)
            if title_attr:
                setattr(self, title_attr, lbl)
            if action is not None:
                action(head)
        inner = tk.Frame(outer.inner, bg=UI["card"])
        inner.pack(fill=tk.BOTH, expand=True)
        return outer, inner

    def _set_i18n_key(self, widget, key: str):
        """把已注册控件的语言键换成新的（界面模式切换时标题文字随之变化）。"""
        for idx, (item, _old) in enumerate(self._i18n_controls):
            if item is widget:
                self._i18n_controls[idx] = (widget, key)
                break
        try:
            widget.configure(text=self.t(key))
        except tk.TclError:
            pass

    # ----- 界面搭建 -----

    def _build_ui(self):
        # 根布局用 grid + 权重：窗口变小时由"列表/预览"区域吸收压缩，
        # 其余卡片保持整宽不错位（pack 在空间不足时会算错后续子控件宽度）
        self.columnconfigure(0, weight=1)
        self.rowconfigure(3, weight=1)

        # ===== 顶部应用栏：软件名 + 语言切换 + 关于 =====
        appbar = ttk.Frame(self, style="Bar.TFrame")
        appbar.grid(row=0, column=0, sticky="ew")
        bar_inner = ttk.Frame(appbar, style="Bar.TFrame")
        bar_inner.pack(fill=tk.X, padx=14, pady=9)
        ttk.Label(bar_inner, text=APP_NAME, style="Title.TLabel").pack(side=tk.LEFT)
        # 语言切换（运行时实时生效，无需重启）：下拉框列出各语言母语名称，
        # 左侧标签中文界面显示 "Language"、英文界面显示"语言"，便于任何用户找到入口
        self.lang_var = tk.StringVar(value=self.lang_display(self._lang))
        self.lang_combo = PillSelect(
            bar_inner, variable=self.lang_var, width=140, height=30,
            values=[name for _code, name in LANGUAGES],
            command=self._on_language_changed,
        )
        self.lang_combo.pack(side=tk.RIGHT)
        self._add_i18n(ttk.Label(bar_inner, text=self.t("language"),
                                 style="Muted.TLabel"), "language")
        self._i18n_controls[-1][0].pack(side=tk.RIGHT, padx=(0, 6))
        self.about_btn = self._add_i18n(
            PillButton(bar_inner, text=self.t("about"), style="secondary",
                       command=self._show_about), "about")
        self.about_btn.pack(side=tk.RIGHT, padx=(0, 12))
        # 主题切换：按钮显示【当前】主题（浅色/深色），点击切到另一种
        self.theme_btn = PillButton(bar_inner, text=self._theme_button_text(),
                                    style="ghost", command=self._toggle_theme)
        self.theme_btn.pack(side=tk.RIGHT, padx=(0, 12))
        self._add_i18n(ttk.Label(bar_inner, text=self.t("theme"),
                                 style="Muted.TLabel"), "theme")
        self._i18n_controls[-1][0].pack(side=tk.RIGHT, padx=(0, 6))
        # 界面模式（用户可自主选择）：经典孤立列表 / 配对对比（JPG | RAW）
        self.view_var = tk.StringVar(value=self._view_display(self._ui_mode))
        self.view_combo = PillSelect(
            bar_inner, variable=self.view_var, width=132, height=30,
            values=[self._view_display("classic"), self._view_display("pair")],
            command=self._on_view_changed,
        )
        self.view_combo.pack(side=tk.RIGHT, padx=(0, 12))
        self._add_i18n(ttk.Label(bar_inner, text=self.t("view"),
                                 style="Muted.TLabel"), "view")
        self._i18n_controls[-1][0].pack(side=tk.RIGHT, padx=(0, 6))
        ttk.Frame(self, style="Divider.TFrame", height=1).grid(row=1, column=0, sticky="ew")

        # ===== 工具栏卡片：文件夹 + RAW 格式 + 扫描范围 + 删除方式 =====
        tool_outer, tool = self._card(self)
        tool_outer.grid(row=2, column=0, sticky="ew", padx=14, pady=(10, 8))

        row1 = ttk.Frame(tool, style="Card.TFrame")
        row1.pack(fill=tk.X)
        self._add_i18n(ttk.Label(row1, text=self.t("target_folder")), "target_folder")
        self._i18n_controls[-1][0].pack(side=tk.LEFT, padx=(0, 6))
        self.path_entry = ttk.Entry(row1, textvariable=self.path_var)
        self.path_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.browse_btn = self._add_i18n(
            PillButton(row1, text=self.t("browse"), command=self._browse_folder), "browse")
        self.browse_btn.pack(side=tk.LEFT, padx=(8, 0))
        self.scan_btn = self._add_i18n(
            PillButton(row1, text=self.t("scan"), style="primary", bold=True,
                       command=self._on_scan_clicked), "scan")
        self.scan_btn.pack(side=tk.LEFT, padx=(8, 0))

        row2 = ttk.Frame(tool, style="Card.TFrame")
        row2.pack(fill=tk.X, pady=(10, 0))
        raw_box = ttk.Frame(row2, style="Card.TFrame")
        raw_box.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self._add_i18n(ttk.Label(raw_box, text=self.t("raw_frame"),
                                 style="CardTitle.TLabel"), "raw_frame")
        self._i18n_controls[-1][0].pack(side=tk.LEFT, padx=(0, 10))
        self._add_i18n(ttk.Label(raw_box, text=self.t("camera_brand")), "camera_brand")
        self._i18n_controls[-1][0].pack(side=tk.LEFT)
        self.raw_combo = PillSelect(
            raw_box, variable=self.raw_mode_var, width=170, height=30,
            values=self._raw_mode_values(), command=self._on_raw_mode_changed,
        )
        self.raw_combo.pack(side=tk.LEFT, padx=(6, 10))
        self._add_i18n(ttk.Label(raw_box, text=self.t("suffixes")), "suffixes")
        self._i18n_controls[-1][0].pack(side=tk.LEFT)
        self.raw_entry = ttk.Entry(raw_box, textvariable=self.raw_entry_var, width=14)
        self.raw_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(6, 0))

        level_box = ttk.Frame(row2, style="Card.TFrame")
        level_box.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(16, 0))
        self._add_i18n(ttk.Label(level_box, text=self.t("scan_frame"),
                                 style="CardTitle.TLabel"), "scan_frame")
        self._i18n_controls[-1][0].pack(side=tk.LEFT, padx=(0, 10))
        self._add_i18n(ttk.Label(level_box, text=self.t("scope")), "scope")
        self._i18n_controls[-1][0].pack(side=tk.LEFT)
        self.level_combo = PillSelect(
            level_box, variable=self.level_var, width=200, height=30,
            values=[self._level_display(i) for i in SCAN_LEVEL_IDS],
            command=self._on_level_changed,
        )
        self.level_combo.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(6, 0))

        row3 = ttk.Frame(tool, style="Card.TFrame")
        row3.pack(fill=tk.X, pady=(10, 0))
        self._add_i18n(ttk.Label(row3, text=self.t("delete_mode_frame"),
                                 style="CardTitle.TLabel"), "delete_mode_frame")
        self._i18n_controls[-1][0].pack(side=tk.LEFT, padx=(0, 12))
        self.mode_btns = []
        for value, key in (("jpg", "mode_jpg"), ("raw", "mode_raw"), ("all", "mode_all")):
            rb = self._add_i18n(
                RoundRadio(row3, text=self.t(key), variable=self.mode_var,
                           value=value, command=self._on_mode_changed,
                           diameter=20, height=32), key)
            rb.pack(side=tk.LEFT, padx=(0, 22))
            self.mode_btns.append(rb)

        # ===== 中部：文件列表 + 相片预览（分隔条可拖拽） =====
        self.main_paned = ttk.PanedWindow(self, orient=tk.VERTICAL)
        self.main_paned.grid(row=3, column=0, sticky="nsew", padx=14, pady=(0, 8))
        # 首次布局完成后设置分隔条（否则会被窗格初始高度夹取成很小的值）
        self.main_paned.bind("<Configure>", self._on_paned_configure, add="+")
        self.main_paned.bind("<ButtonRelease-1>", self._on_sash_user_drag, add="+")

        # --- 文件列表卡片（首列为勾选列：☑ = 删除，☐ = 保留） ---
        # 「全选/全不选」合并为一个按钮，放在卡片标题行右侧与列表同高，
        # 避免占用下方预览区（简略 EXIF 信息）的空间；
        # 同一张卡片里还有"配对对比"视图（JPG | RAW 左右对照），两种界面由用户切换
        def _list_header_action(head):
            self.select_toggle_btn = self._add_i18n(
                PillButton(head, text=self._select_toggle_text(), style="ghost",
                           font_size=9, height=26, pad_x=12,
                           command=self._toggle_all_checked), "toggle_all")
            self.select_toggle_btn.pack(side=tk.RIGHT)

        tree_outer, tree_inner = self._card(self.main_paned, "list_frame",
                                            action=_list_header_action, expand=True,
                                            height=330, title_attr="list_title_label")
        self.tree_host = tree_inner
        columns = ("chk", "name", "type", "size", "folder")
        self.tree = ttk.Treeview(
            tree_inner, columns=columns, show="headings", selectmode="extended", height=8
        )
        # 表头：文件名/类型/文件大小 单击可排序（点击切换升降序）；勾选列不排序
        self.tree.heading("chk", text=self.t("col_check"))
        for col, key in (("name", "col_name"), ("type", "col_type"),
                         ("size", "col_size"), ("folder", "col_folder")):
            if col in ("name", "type", "size"):
                self.tree.heading(col, text=self.t(key),
                                  command=lambda c=col: self._on_sort(c))
            else:
                self.tree.heading(col, text=self.t(key))
        self._heading_keys = {"chk": "col_check", "name": "col_name",
                              "type": "col_type", "size": "col_size",
                              "folder": "col_folder"}
        # 双击文件行：打开资源管理器并定位该照片；单击行：显示 EXIF / 切换勾选
        self.tree.bind("<Double-1>", self._on_tree_double_click)
        self.tree.bind("<Button-1>", self._on_tree_click)
        self.tree.bind("<space>", self._on_tree_space)
        self.tree.bind("<MouseWheel>", self._on_tree_wheel)
        self._sort_col = None      # 当前排序列
        self._sort_reverse = False  # 是否降序
        # 列宽固定不自动伸展：内容超宽时下方水平滚动条才能真正滚动
        self.tree.column("chk", width=54, anchor=tk.CENTER, stretch=False)
        self.tree.column("name", width=270, anchor=tk.W, stretch=False)
        self.tree.column("type", width=70, anchor=tk.CENTER, stretch=False)
        self.tree.column("size", width=110, anchor=tk.E, stretch=False)
        self.tree.column("folder", width=520, anchor=tk.W, stretch=False)
        # 最小列宽 = 表头文字宽度：拖到最窄也只会刚好显示完整表头，不会遮住上方文字
        self._apply_column_minwidths(self.tree, columns)
        # 自绘圆润滚动条（与预览区/结果区风格统一）
        self.tree_bar = self._new_bar(tree_inner, "vertical", self.tree.yview)
        self.tree_bar_h = self._new_bar(tree_inner, "horizontal", self.tree.xview)
        self.tree_bar.bind("<MouseWheel>", self._on_tree_wheel)
        self.tree_bar_h.bind("<MouseWheel>", self._on_tree_wheel)
        self.tree.configure(yscrollcommand=self.tree_bar.set,
                            xscrollcommand=self.tree_bar_h.set)
        self.tree.grid(row=0, column=0, sticky="nsew")
        self.tree_bar.grid(row=0, column=1, sticky="ns", padx=(4, 0))
        self.tree_bar_h.grid(row=1, column=0, sticky="ew", pady=(4, 0))
        tree_inner.rowconfigure(0, weight=1)
        tree_inner.columnconfigure(0, weight=1)
        self.main_paned.add(tree_outer, weight=1)

        # --- 配对对比视图（与经典列表共用同一格，按界面模式切换显示） ---
        self._build_pair_view(tree_inner)

        # --- 相片预览卡片（多列网格、垂直滚动） ---
        prev_outer, prev_inner = self._card(self.main_paned, "preview_frame",
                                            expand=True, height=280)
        # 第一行：缩略图大小（药丸滑块） + EXIF 模式切换按钮
        toolbar = tk.Frame(prev_inner, bg=UI["card"])
        toolbar.pack(side=tk.TOP, fill=tk.X)
        size_box = tk.Frame(toolbar, bg=UI["card"])
        size_box.pack(side=tk.LEFT)
        self._add_i18n(tk.Label(size_box, text=self.t("thumb_size"), bg=UI["card"],
                                fg=UI["text"], font=(self._font_family, 10)),
                       "thumb_size")
        self._i18n_controls[-1][0].pack(side=tk.LEFT)
        self.size_scale = PillSlider(size_box, variable=self.thumb_level_var,
                                     from_=0, to=2, command=self._on_size_slider,
                                     width=150, height=24)
        self.size_scale.pack(side=tk.LEFT, padx=10)
        self.size_label = tk.Label(size_box, text=self._size_label_text(),
                                   bg=UI["card"], fg=UI["text"],
                                   font=(self._font_family, 10), width=14, anchor="w")
        self.size_label.pack(side=tk.LEFT)
        # EXIF 模式切换（简略 / 详细），放在工具栏右侧
        self.exif_mode_btn = PillButton(toolbar, text=self.t("exif_detail"),
                                        style="ghost", font_size=9, height=26,
                                        pad_x=12, command=self._toggle_exif_mode)
        self.exif_mode_btn.pack(side=tk.RIGHT)

        # 第二行：EXIF 信息区（整行宽度、右对齐向右缩进，不会与按钮重叠）
        self.exif_var = tk.StringVar(value=self.t("exif_hint"))
        self.exif_label = tk.Label(
            prev_inner, textvariable=self.exif_var, justify=tk.RIGHT, anchor="e",
            font=(self._font_family, 9), bg=UI["card"], fg=UI["muted"],
            cursor="hand2", height=1,
        )
        self.exif_label.pack(side=tk.TOP, fill=tk.X, pady=(4, 2), padx=(4, 8))
        # EXIF 可复制：双击复制全部；右键菜单可复制全部或单个字段
        self.exif_label.bind("<Double-1>", lambda _e: self._copy_exif_all())
        self.exif_label.bind("<Button-3>", self._popup_exif_menu)

        self.preview_canvas = tk.Canvas(prev_inner, height=170, bg=UI["card"],
                                        highlightthickness=0, bd=0)
        self.preview_scroll = self._new_bar(prev_inner, "vertical",
                                            self.preview_canvas.yview)
        # 固定状态提示条：位于滚动区域之外（底部），不随缩略图内容滚动
        self.preview_status_bar = ttk.Label(prev_inner, text="", anchor="w",
                                            style="Muted.TLabel")
        self.preview_status_bar.pack(side=tk.BOTTOM, fill=tk.X, pady=(4, 0))
        self.preview_inner = tk.Frame(self.preview_canvas, bg=UI["card"])
        self._preview_window = self.preview_canvas.create_window(
            (0, 0), window=self.preview_inner, anchor="nw"
        )
        self.preview_canvas.configure(yscrollcommand=self.preview_scroll.set)
        self.preview_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.preview_scroll.pack(side=tk.RIGHT, fill=tk.Y, padx=(4, 0))
        # 内容变化时更新纵向滚动范围；画布宽度变化时同步内容宽度（无横向滚动）
        self.preview_inner.bind(
            "<Configure>",
            lambda e: self.preview_canvas.configure(
                scrollregion=self.preview_canvas.bbox("all")
            ),
        )
        self.preview_canvas.bind(
            "<Configure>",
            lambda e: self.preview_canvas.itemconfigure(self._preview_window,
                                                        width=e.width),
        )
        # 窗口大小变化时，防抖重建预览网格（排列与缩略图自动适应）
        self.preview_canvas.bind("<Configure>", self._on_preview_canvas_resize, add="+")
        # 滚轮直接绑定到预览区所有控件（含空白/边框区域），不依赖 Enter/Leave
        for widget in (prev_inner, self.preview_canvas, self.preview_scroll,
                       self.preview_inner):
            self._bind_preview_wheel(widget)
        self.main_paned.add(prev_outer, weight=0)

        # ===== 底部：状态栏 + 二次确认（圆形开关） + 删除按钮（药丸形） =====
        bottom_outer, bottom = self._card(self, padding=(12, 8))
        bottom_outer.grid(row=4, column=0, sticky="ew", padx=14, pady=(0, 8))
        bottom.columnconfigure(0, weight=1)
        tk.Label(bottom, textvariable=self.status_var, bg=UI["card"], fg=UI["text"],
                 font=(self._font_family, 10), anchor="w").grid(row=0, column=0,
                                                                sticky="ew")
        self.confirm_check = self._add_i18n(
            RoundToggle(bottom, text=self.t("confirm_check"), variable=self.confirm_var),
            "confirm_check")
        self.confirm_check.grid(row=0, column=1, padx=(12, 0))
        self.delete_btn = PillButton(
            bottom, text=self.t("confirm_delete"), style="danger", bold=True,
            command=self._on_delete_clicked,
        )
        self.delete_btn.configure(state="disabled")
        self.delete_btn.grid(row=0, column=2, padx=(12, 0))

        # ===== 操作结果卡片 =====
        res_outer, res_inner = self._card(self, "result_frame")
        res_outer.grid(row=5, column=0, sticky="ew", padx=14, pady=(0, 14))
        self.result_text = tk.Text(
            res_inner, height=5, wrap=tk.WORD, state=tk.DISABLED,
            bg=UI["card_alt"], fg=UI["text"], relief=tk.FLAT, bd=0,
            font=(self._font_family, 9), padx=8, pady=6,
            highlightthickness=1, highlightbackground=UI["border"],
            highlightcolor=UI["border"], insertbackground=UI["text"],
        )
        r_bar = self._new_bar(res_inner, "vertical", self.result_text.yview)
        self.result_text.configure(yscrollcommand=r_bar.set)
        self.result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        r_bar.pack(side=tk.RIGHT, fill=tk.Y, padx=(4, 0))

    def _new_bar(self, parent, orient, command):
        """创建自绘圆润滚动条并登记（主题切换时统一刷新配色）。"""
        bar = RoundScrollbar(parent, orient, command=command)
        self._bar_widgets.append(bar)
        return bar

    # ----- 配对对比视图（JPG | RAW 左右对照） -----

    def _view_display(self, mode: str) -> str:
        """界面模式 -> 下拉框显示文本。"""
        return self.t("view_pair" if mode == "pair" else "view_classic")

    def _build_pair_view(self, host):
        """在列表卡片内构建"配对对比"视图：一行一组同基础名的 JPG / RAW，
        用颜色标出哪一侧缺失（底色或文字色可选）。"""
        box = tk.Frame(host, bg=UI["card"])
        self.pair_box = box

        # 顶部：图例（含数量统计） + 标记方式开关 + 只显示缺失
        head = tk.Frame(box, bg=UI["card"])
        head.pack(side=tk.TOP, fill=tk.X, pady=(0, 4))
        self.pair_legend = tk.Label(
            head, text="", bg=UI["card"], fg=UI["text"], anchor="w",
            font=(self._font_family, 9), justify=tk.LEFT,
        )
        self.pair_legend.pack(side=tk.LEFT)
        # 图例用彩色小块 + 文字，深浅主题都清晰
        self.pair_swatches = []
        for key, color_key in (("pair_status_ok", "pair_ok_bg"),
                               ("pair_status_no_raw", "pair_no_raw_bg"),
                               ("pair_status_no_jpg", "pair_no_jpg_bg")):
            swatch = tk.Label(head, text="  ", bg=UI[color_key], bd=0,
                              font=(self._font_family, 8))
            swatch.pack(side=tk.LEFT, padx=(8, 2))
            lbl = self._add_i18n(
                tk.Label(head, text=self.t(key), bg=UI["card"], fg=UI["muted"],
                         font=(self._font_family, 9)), key)
            lbl.pack(side=tk.LEFT)
            self.pair_swatches.append((swatch, color_key))
        self.pair_only_toggle = self._add_i18n(
            RoundToggle(head, text=self.t("pair_only_missing"),
                        variable=tk.BooleanVar(value=self._pair_only_missing),
                        command=self._on_pair_only_missing, height=26),
            "pair_only_missing")
        self.pair_only_toggle.pack(side=tk.RIGHT)
        self.pair_color_toggle = self._add_i18n(
            RoundToggle(head, text=self.t("pair_bg_mode"),
                        variable=tk.BooleanVar(value=self._pair_color == "bg"),
                        command=self._on_pair_color_mode, height=26),
            "pair_bg_mode")
        self.pair_color_toggle.pack(side=tk.RIGHT, padx=(0, 10))

        # 表格：勾选 | JPG 文件（左） | RAW 文件（右） | 所在文件夹 | 状态 | 处理
        # 「处理」列明确写出这一行会不会被删除，避免"全部显示却难以分辨"
        grid = tk.Frame(box, bg=UI["card"])
        grid.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        cols = ("chk", "jpg", "raw", "folder", "status", "action")
        self.pair_tree = ttk.Treeview(grid, columns=cols, show="headings",
                                      selectmode="extended", height=8)
        self._pair_heading_keys = {"chk": "col_check", "jpg": "pair_col_jpg",
                                   "raw": "pair_col_raw", "folder": "col_folder",
                                   "status": "pair_col_status",
                                   "action": "pair_col_action"}
        for col, key in self._pair_heading_keys.items():
            if col in ("jpg", "raw", "status", "action"):
                self.pair_tree.heading(col, text=self.t(key),
                                       command=lambda c=col: self._on_pair_sort(c))
            else:
                self.pair_tree.heading(col, text=self.t(key))
        self.pair_tree.column("chk", width=50, anchor=tk.CENTER, stretch=False)
        self.pair_tree.column("jpg", width=235, anchor=tk.W, stretch=False)
        self.pair_tree.column("raw", width=235, anchor=tk.W, stretch=False)
        self.pair_tree.column("folder", width=250, anchor=tk.W, stretch=False)
        self.pair_tree.column("status", width=135, anchor=tk.CENTER, stretch=False)
        self.pair_tree.column("action", width=185, anchor=tk.CENTER, stretch=False)
        # 最小列宽 = 表头文字宽度（拖到最窄也不遮住上方表头文字）
        self._apply_column_minwidths(self.pair_tree, cols)
        # 列宽随窗口自适应：保证"状态 / 处理"两列始终可见（不同 DPI 缩放也不跑偏）
        self.pair_tree.bind("<Configure>", self._fit_pair_columns, add="+")
        self.pair_tree.bind("<Button-1>", self._on_pair_click)
        self.pair_tree.bind("<Double-1>", self._on_pair_double_click)
        self.pair_tree.bind("<space>", self._on_pair_space)
        self.pair_tree.bind("<MouseWheel>", self._on_pair_wheel)
        self.pair_bar = self._new_bar(grid, "vertical", self.pair_tree.yview)
        self.pair_bar_h = self._new_bar(grid, "horizontal", self.pair_tree.xview)
        self.pair_bar.bind("<MouseWheel>", self._on_pair_wheel)
        self.pair_bar_h.bind("<MouseWheel>", self._on_pair_wheel)
        self.pair_tree.configure(yscrollcommand=self.pair_bar.set,
                                 xscrollcommand=self.pair_bar_h.set)
        self.pair_tree.grid(row=0, column=0, sticky="nsew")
        self.pair_bar.grid(row=0, column=1, sticky="ns", padx=(4, 0))
        self.pair_bar_h.grid(row=1, column=0, sticky="ew", pady=(4, 0))
        grid.rowconfigure(0, weight=1)
        grid.columnconfigure(0, weight=1)
        self._bind_pair_tree()

    def _bind_pair_tree(self):
        """对比视图行配色：按"标记方式"决定改底色还是改文字色。"""
        use_bg = self._pair_color == "bg"
        base_bg = {"ok": UI["pair_ok_bg"], "no_raw": UI["pair_no_raw_bg"],
                   "no_jpg": UI["pair_no_jpg_bg"]}
        base_fg = {"ok": UI["pair_ok_fg"], "no_raw": UI["pair_no_raw_fg"],
                   "no_jpg": UI["pair_no_jpg_fg"]}
        for status in ("ok", "no_raw", "no_jpg"):
            if use_bg:
                self.pair_tree.tag_configure(f"p_{status}",
                                             background=base_bg[status],
                                             foreground=UI["text"])
            else:
                self.pair_tree.tag_configure(f"p_{status}",
                                             background=UI["card"],
                                             foreground=base_fg[status])
        self.pair_tree.tag_configure("p_picked", background=UI["accent_soft"],
                                     foreground=UI["accent_dark"])
        if hasattr(self, "pair_only_toggle"):
            try:
                self.pair_only_toggle.configure(bg=UI["card"])
            except tk.TclError:
                pass

    def _pair_color_of(self, status: str) -> str:
        return {"ok": "pair_ok_bg", "no_raw": "pair_no_raw_bg",
                "no_jpg": "pair_no_jpg_bg"}[status]

    def _refresh_pair_legend(self):
        """刷新图例上的数量统计：共 N 组：齐全 x · 缺 RAW y · 缺 JPG z。"""
        if not hasattr(self, "pair_legend"):
            return
        rows = self.scan_result.pairs if self.scan_result is not None else []
        ok = sum(1 for p in rows if p.status == "ok")
        no_raw = sum(1 for p in rows if p.status == "no_raw")
        no_jpg = sum(1 for p in rows if p.status == "no_jpg")
        try:
            self.pair_legend.configure(text=self.t("pair_count_fmt", total=len(rows),
                                                   ok=ok, no_raw=no_raw, no_jpg=no_jpg))
        except tk.TclError:
            pass
        # 图例色块随主题刷新
        for swatch, color_key in getattr(self, "pair_swatches", []):
            try:
                swatch.configure(bg=UI[color_key])
            except tk.TclError:
                pass

    def _pair_visible_rows(self):
        """当前界面下要显示的配对行（可只显示有缺失的）。"""
        if self.scan_result is None:
            return []
        rows = list(self.scan_result.pairs)
        if self._pair_only_missing:
            rows = [p for p in rows if p.status != "ok"]
        if self._pair_sort:
            col, reverse = self._pair_sort

            def key(row):
                if col == "jpg":
                    return (row.jpg.name.lower() if row.jpg else "\uffff")
                if col == "raw":
                    return (row.raw.name.lower() if row.raw else "\uffff")
                if col == "action":
                    # 会删除的排前面，其次按状态
                    return (0 if row.deletable else 1, row.status)
                return row.status
            rows.sort(key=key, reverse=reverse)
        return rows

    def _apply_column_minwidths(self, tree, cols):
        """把每列的最小宽度设为「表头文字宽度 + 排序箭头 + 内边距」。

        这样用户拖动列宽时，最窄只会到"刚好完整显示表头文字"，
        不会再拖到把上方表头文字遮住/截断。语言切换后表头文字变长时
        也会重新计算，避免中文表头被英文宽度限制。"""
        try:
            from tkinter import font as tkfont
            font = tkfont.nametofont("TkHeadingFont")
        except Exception:
            font = None
        for col in cols:
            try:
                text = str(tree.heading(col, "text"))
                for mark in (" ▲", " ▼"):
                    text = text.replace(mark, "")
                need = (font.measure(text) if font is not None else 0) + 30
                tree.column(col, minwidth=max(36, need))
            except tk.TclError:
                pass

    # 对比视图列宽权重与最小宽度（按可用宽度自适应）
    PAIR_COL_LAYOUT = (("chk", 0.05, 46), ("jpg", 0.21, 120), ("raw", 0.21, 120),
                       ("folder", 0.215, 100), ("status", 0.12, 96),
                       ("action", 0.195, 132))

    def _fit_pair_columns(self, _event=None):
        """按表格当前可用宽度分配列宽，保证 6 列（含「处理」）都能看到。"""
        if not hasattr(self, "pair_tree"):
            return
        try:
            total = self.pair_tree.winfo_width()
        except tk.TclError:
            return
        if total < 200:
            return
        minimum = sum(min_w for _c, _w, min_w in self.PAIR_COL_LAYOUT)
        extra = max(0, total - minimum)
        for col, weight, min_w in self.PAIR_COL_LAYOUT:
            width = int(min_w + extra * weight)
            try:
                # 不低于该列"表头文字宽度"下限，避免遮住上方表头
                width = max(width, int(self.pair_tree.column(col, "minwidth")))
                if abs(int(self.pair_tree.column(col, "width")) - width) > 2:
                    self.pair_tree.column(col, width=width)
            except tk.TclError:
                pass

    def _pair_action_text(self, row, checked: bool = None) -> str:
        """「处理」列文案：这一行到底会不会被删除，一眼看清。
        · 会删除 -> "删除"（勾选状态）
        · 用户取消勾选 -> "不删除·已取消勾选"
        · 已配对（两侧都有）-> "不删除·已配对"
        · RAW 格式未匹配（受保护）-> "不删除·格式未匹配" """
        if row.deletable:
            target = row.deletable[0]
            if checked is None:
                checked = target.full_path in self._checked
            return self.t("pair_action_delete" if checked
                          else "pair_action_keep_unchecked")
        if row.status == "ok":
            return self.t("pair_action_keep_paired")
        return self.t("pair_action_keep_mismatch")

    def _refresh_pair_tree(self):
        """重建对比视图表格（行 iid 与孤立文件路径建立映射，便于勾选联动）。"""
        if not hasattr(self, "pair_tree"):
            return
        for iid in self.pair_tree.get_children():
            self.pair_tree.delete(iid)
        self._pair_iid_by_path = {}
        self._pair_rows = []
        status_text = {"ok": "pair_status_ok", "no_raw": "pair_status_no_raw",
                       "no_jpg": "pair_status_no_jpg"}
        for row in self._pair_visible_rows():
            deletable = row.deletable
            target = deletable[0] if deletable else None
            checked = bool(target and target.full_path in self._checked)
            if target is None:
                chk = ""            # 不参与删除：无需勾选
            else:
                chk = CHECK_ON if checked else CHECK_OFF
            status = self.t(status_text[row.status])
            folder = ""
            primary = row.primary
            if primary is not None:
                folder = primary.folder
            iid = self.pair_tree.insert(
                "", tk.END,
                values=(chk,
                        row.jpg.name if row.jpg else "",
                        row.raw.name if row.raw else "",
                        folder, status,
                        self._pair_action_text(row, checked)),
                tags=(f"p_{row.status}",),
            )
            self._pair_rows.append((iid, row))
            if target is not None:
                self._pair_iid_by_path[target.full_path] = iid
        self._refresh_pair_legend()
        self._paint_pair_rows()
        self.after_idle(self._fit_pair_columns)   # 表格可见后按可用宽度重排列宽

    def _paint_pair_rows(self):
        """按当前选中/勾选状态刷新对比视图行：配色标签 + 勾选格 + 「处理」列文案。"""
        picked = self._picked_pair_iid
        for iid, row in getattr(self, "_pair_rows", []):
            tags = [f"p_{row.status}"]
            if iid == picked:
                tags = ["p_picked"]
            try:
                self.pair_tree.item(iid, tags=tuple(tags))
                target = (row.deletable or [None])[0]
                if target is not None and iid in self.pair_tree.get_children():
                    checked = target.full_path in self._checked
                    self.pair_tree.set(iid, "chk", CHECK_ON if checked else CHECK_OFF)
                    self.pair_tree.set(iid, "action",
                                       self._pair_action_text(row, checked))
            except tk.TclError:
                pass

    def _pair_row_path(self, iid):
        """行 iid -> 该行可删除文件的路径（配对完整的行为主文件路径）。"""
        for row_iid, row in getattr(self, "_pair_rows", []):
            if row_iid == iid:
                target = (row.deletable or [None])[0]
                if target is not None:
                    return target.full_path
                return row.primary.full_path if row.primary else None
        return None

    def _pair_target_path(self, iid):
        """行 iid -> 可切换勾选的文件路径（配对完整的行返回 None）。"""
        for row_iid, row in getattr(self, "_pair_rows", []):
            if row_iid == iid:
                target = (row.deletable or [None])[0]
                return target.full_path if target is not None else None
        return None

    def _on_pair_click(self, event):
        """对比视图单击：点勾选列切换勾选；其它位置显示 EXIF 并联动预览。"""
        iid = self.pair_tree.identify_row(event.y)
        if not iid:
            return None
        self._picked_pair_iid = iid
        self._paint_pair_rows()
        if self.pair_tree.identify_column(event.x) == "#1":
            path = self._pair_target_path(iid)
            if path:
                self._toggle_checked(path)
                return "break"
            return None
        path = self._pair_row_path(iid)
        if path:
            self._on_thumb_click(path)      # 高亮列表 + 预览滚动 + 显示 EXIF
        return None

    def _on_pair_double_click(self, event):
        iid = self.pair_tree.identify_row(event.y)
        if iid:
            path = self._pair_row_path(iid)
            if path:
                self._reveal_in_explorer(path)
        return "break"

    def _on_pair_space(self, _event=None):
        """空格：切换对比视图选中行的勾选。"""
        for iid in self.pair_tree.selection():
            path = self._pair_target_path(iid)
            if path:
                self._toggle_checked(path)
        return "break"

    def _on_pair_wheel(self, event):
        """对比视图滚轮滚动。"""
        try:
            self.pair_tree.yview_scroll(-1 if event.delta > 0 else 1, "units")
        except tk.TclError:
            pass
        return "break"

    def _on_pair_sort(self, col):
        """点击表头排序（再次点击切换升降序）。"""
        if self._pair_sort and self._pair_sort[0] == col:
            self._pair_sort = (col, not self._pair_sort[1])
        else:
            self._pair_sort = (col, False)
        for key, heading_key in self._pair_heading_keys.items():
            text = self.t(heading_key)
            if key == self._pair_sort[0]:
                text += " ▼" if self._pair_sort[1] else " ▲"
            self.pair_tree.heading(key, text=text)
        self._refresh_pair_tree()

    def _on_pair_color_mode(self):
        """切换"用背景色 / 用文字颜色"标记缺失。"""
        self._pair_color = "bg" if self.pair_color_toggle._value() else "fg"
        self._bind_pair_tree()
        self._refresh_pair_tree()
        self._save_config_now()

    def _on_pair_only_missing(self):
        """只显示有缺失的配对行。"""
        self._pair_only_missing = bool(self.pair_only_toggle._value())
        self._refresh_pair_tree()
        self._save_config_now()

    def _on_view_changed(self):
        """用户在应用栏切换界面模式：切换视图并写入配置。"""
        mode = "pair" if self.view_var.get() == self._view_display("pair") \
            else "classic"
        if mode == self._ui_mode:
            return
        self._ui_mode = mode
        self._apply_view_mode()
        self._save_config_now()

    def _apply_view_mode(self):
        """按当前界面模式显示经典列表或配对对比视图（标题同步变化）。"""
        if not hasattr(self, "pair_box"):
            return
        pair = self._ui_mode == "pair"
        try:
            if pair:
                self.tree.grid_remove()
                self.tree_bar.grid_remove()
                self.tree_bar_h.grid_remove()
                self.pair_box.grid(row=0, column=0, sticky="nsew")
            else:
                self.pair_box.grid_remove()
                self.tree.grid(row=0, column=0, sticky="nsew")
                self.tree_bar.grid(row=0, column=1, sticky="ns", padx=(4, 0))
                self.tree_bar_h.grid(row=1, column=0, sticky="ew", pady=(4, 0))
        except tk.TclError:
            return
        # 标题：经典 -> 孤立文件列表；对比 -> 配对对比（JPG | RAW）
        if getattr(self, "list_title_label", None) is not None:
            self._set_i18n_key(self.list_title_label,
                               "pair_frame" if pair else "list_frame")
        # 全选/全不选按钮文字保持一致语义
        try:
            self.select_toggle_btn.configure(text=self._select_toggle_text())
        except tk.TclError:
            pass
        if pair:
            self._refresh_pair_tree()
            self.after_idle(self._fit_pair_columns)
        self._update_delete_btn()

    def _bind_tree(self):
        """列表行样式：隔行底色 + 选中高亮 + 未勾选（保留）行的弱化配色。"""
        self.tree.tag_configure("odd", background=UI["row_alt"])
        self.tree.tag_configure("even", background=UI["card"])
        self.tree.tag_configure("picked", background=UI["accent_soft"],
                                foreground=UI["accent_dark"])
        self.tree.tag_configure("off", foreground=UI["muted"])
        if hasattr(self, "pair_tree"):
            self._bind_pair_tree()
            self._refresh_pair_legend()

    # ----- 语言 / 主题 -----

    def lang_display(self, code: str) -> str:
        """语言代码 -> 下拉框显示名（母语写法）。"""
        return LANG_NATIVE.get(code, LANG_NATIVE[FALLBACK_LANG])

    def _theme_button_text(self) -> str:
        """主题按钮显示【当前】主题（浅色/深色），点击切换到另一种。"""
        return self.t("theme_dark") if self._dark else self.t("theme_light")

    def _select_toggle_text(self) -> str:
        """「全选/全不选」合并按钮文字。"""
        return self.t("toggle_all")

    def _toggle_all_checked(self):
        """合并按钮：按当前状态自动在全选 / 全不选之间切换。"""
        targets = self._preview_targets()
        if not targets:
            return
        all_checked = all(f.full_path in self._checked for f in targets)
        self._set_all_checked(not all_checked)

    def _toggle_theme(self):
        """浅色 / 深色主题切换：立即生效并写入配置。"""
        old_palette = dict(UI)          # 记录切换前配色，用于整体换色
        self._dark = not self._dark
        self._theme_pref = "dark" if self._dark else "light"
        set_theme("dark" if self._dark else "light")
        self._apply_theme(old_palette)
        self._save_config_now()

    def _apply_theme(self, old_palette: dict = None):
        """主题切换后重新套用配色：ttk 样式 + 全部 tk 控件换色 + 自绘控件重绘 +
        预览卡片重建。old_palette 非空时把"旧配色"整体映射为新配色，
        避免出现残留旧主题色的方块（这是浅色/深色切换不彻底的根因）。"""
        if old_palette:
            self._recolor_tk_widgets(old_palette, UI)
        self._setup_styles()
        try:
            self.configure(bg=UI["bg"])
        except tk.TclError:
            return
        # 所有自绘控件（卡片/按钮/开关/滑块/滚动条/角标）统一刷新
        self._refresh_widget_tree(self)
        # 显式兜底：几处关键控件与文本颜色
        for widget, key in ((self.preview_canvas, "card"),
                            (self.preview_inner, "card"),
                            (self.exif_label, "card"),
                            (self.result_text, "card_alt")):
            try:
                widget.configure(bg=UI[key])
            except tk.TclError:
                pass
        try:
            self.result_text.configure(fg=UI["text"], insertbackground=UI["text"],
                                       highlightbackground=UI["border"],
                                       highlightcolor=UI["border"])
        except tk.TclError:
            pass
        try:
            self.exif_label.configure(fg=UI["muted"])
        except tk.TclError:
            pass
        self._bind_tree()          # 列表行标签配色
        if self.orphans:
            self._refresh_preview()   # 预览卡片底色随主题变化（用缓存，不重新解码）
        try:
            self.theme_btn.configure(text=self._theme_button_text())
        except tk.TclError:
            pass
        self._relabel_about_window()

    def _recolor_tk_widgets(self, old: dict, new: dict):
        """把 tk 控件的旧主题色整体替换为新主题色（按颜色值映射，覆盖所有控件）。"""
        mapping = {}
        for key, value in old.items():
            if key in new and isinstance(value, str) and value.startswith("#") \
                    and str(new[key]).lower() != value.lower():
                mapping[value.lower()] = new[key]
        if not mapping:
            return

        def walk(widget):
            for child in widget.winfo_children():
                self._recolor_one(child, mapping)
                walk(child)

        walk(self)

    @staticmethod
    def _recolor_one(widget, mapping: dict):
        for opt in ("bg", "background", "fg", "foreground", "highlightbackground",
                    "highlightcolor", "insertbackground", "selectbackground",
                    "selectforeground", "troughcolor", "activebackground"):
            try:
                current = widget.cget(opt)
            except Exception:
                continue          # ttk 控件多数不支持这些选项，直接跳过
            if not isinstance(current, str):
                continue
            target = mapping.get(current.strip().lower())
            if target:
                try:
                    widget.configure(**{opt: target})
                except tk.TclError:
                    pass

    def _restyle_combobox_popdowns(self):
        """让下拉弹出列表的颜色跟随主题。

        ttk.Combobox 的弹出列表（内部 Listbox）**首次点开时才创建**，创建后不再受
        option_add 影响——所以切换主题后弹出框会停留在旧主题（浅色模式下仍是
        黑底白字，看不清）。这里双管齐下：
        ① 已存在的 Listbox 直接重设配色；
        ② 销毁缓存的弹出框控件，下次点开时按新的 option_add 重新创建。"""
        for combo in (getattr(self, "lang_combo", None),
                      getattr(self, "raw_combo", None),
                      getattr(self, "level_combo", None)):
            if combo is None:
                continue
            try:
                path = str(combo)
            except tk.TclError:
                continue
            # ① 已存在的下拉列表直接换色
            try:
                for child in combo.winfo_children():
                    for target in (child, *child.winfo_children()):
                        if target.winfo_class() == "Listbox":
                            target.configure(background=UI["card"],
                                             foreground=UI["text"],
                                             selectbackground=UI["accent"],
                                             selectforeground="#ffffff",
                                             borderwidth=0, highlightthickness=0)
            except tk.TclError:
                pass
            # ② 丢弃缓存的弹出框，保证下次按新配色重建
            try:
                popdown = path + ".popdown"
                if self.tk.call("winfo", "exists", popdown):
                    self.tk.call("destroy", popdown)
            except tk.TclError:
                pass

    def _refresh_widget_tree(self, widget):
        """递归刷新所有带 refresh_theme() 的自绘控件（卡片/按钮/开关/滑块/滚动条/角标）。"""
        for child in widget.winfo_children():
            refresh = getattr(child, "refresh_theme", None)
            if callable(refresh):
                try:
                    refresh()
                except tk.TclError:
                    pass
            self._refresh_widget_tree(child)

    def _thumb_level_text(self) -> str:
        """缩略图档位的【当前语言】显示文本（内部值仍为 小/中/大，配置记忆不变）。"""
        return self.t(_THUMB_LEVEL_KEYS.get(self._thumb_level, "thumb_medium"))

    def _size_label_text(self) -> str:
        """缩略图大小标签文本（"当前：中" / "Current: Medium"，随语言切换）。"""
        return f"{self.t('current')}{self._thumb_level_text()}"

    def t(self, key: str, **fmt) -> str:
        """按当前语言取界面文本；缺失键回退英语（默认回退语言），再回退键名。"""
        data = self._lang_data.get(self._lang) or {}
        text = data.get(key)
        if text is None:
            text = (self._lang_data.get(FALLBACK_LANG) or {}).get(key, key)
        if fmt:
            try:
                text = text.format(**fmt)
            except Exception:
                pass
        return text

    def _add_i18n(self, widget, key: str):
        """注册静态文本控件（切换语言时自动刷新文本）。"""
        self._i18n_controls.append((widget, key))
        return widget

    def _raw_display(self, internal: str) -> str:
        """RAW 模式内部 id -> 当前语言显示文本（品牌名本地化 + 英文原名）。"""
        if internal == AUTO_ID:
            return self.t("auto_label")
        if internal == CUSTOM_ID:
            return self.t("custom_label")
        brand = BRAND_BY_ID.get(internal)
        return brand_display(brand, self._lang) if brand else str(internal)

    def _raw_internal(self) -> str:
        """RAW 下拉框显示文本 -> 内部 id（映射重建后选择/读取均走此函数）。"""
        return self._raw_map.get(self.raw_mode_var.get(), self.raw_mode_var.get())

    def _level_display(self, internal: str) -> str:
        """扫描范围内部 id -> 当前语言显示文本。"""
        try:
            idx = SCAN_LEVEL_IDS.index(internal)
        except ValueError:
            idx = 0
        return self.t(f"level_{idx}")

    def _level_internal(self) -> str:
        """层级下拉框显示文本 -> 内部 id。"""
        return self._level_map.get(self.level_var.get(), self.level_var.get())

    def _rebuild_combo_maps(self):
        """按当前语言重建下拉框的 显示文本<->内部 id 映射与选项列表。"""
        self._raw_map = {}
        for internal in [AUTO_ID] + [b["id"] for b in BRANDS] + [CUSTOM_ID]:
            self._raw_map[self._raw_display(internal)] = internal
        self._level_map = {self._level_display(i): i for i in SCAN_LEVEL_IDS}
        self._lang_map = {LANG_NATIVE[c]: c for c in LANG_CODES}
        self.raw_combo.configure(values=list(self._raw_map))
        self.level_combo.configure(values=list(self._level_map))
        self.lang_combo.configure(values=list(self._lang_map))

    def _apply_language(self):
        """按当前语言刷新全部界面文本（运行时实时切换，无需重启）。
        覆盖：注册控件、表头、下拉框、动态标签、EXIF、状态栏、预览状态条、
        缩略图档位名、预览占位提示与结果区日志——保证切换后无残留旧语言。"""
        for widget, key in self._i18n_controls:
            try:
                widget.configure(text=self.t(key))
            except Exception:
                pass
        # 表头（保留排序方向标记）
        for col, key in self._heading_keys.items():
            text = self.t(key)
            if self._sort_col == col:
                text += " ▼" if self._sort_reverse else " ▲"
            self.tree.heading(col, text=text)
        self._apply_column_minwidths(self.tree, tuple(self._heading_keys))
        # 下拉框：重建显示选项，并把当前值切换到新语言显示（品牌名本地化）
        self._rebuild_combo_maps()
        self.raw_mode_var.set(self._raw_display(self._raw_mode_internal))
        self.level_var.set(self._level_display(self._level_internal_value))
        self.lang_var.set(self.lang_display(self._lang))
        self.lang_combo.configure(values=list(self._lang_map))
        # 界面模式下拉框（经典 / 对比）显示名随语言变化
        try:
            self.view_var.set(self._view_display(self._ui_mode))
            self.view_combo.configure(values=[self._view_display("classic"),
                                              self._view_display("pair")])
        except tk.TclError:
            pass
        # 对比视图表头与图例统计
        if hasattr(self, "pair_tree"):
            for col, key in self._pair_heading_keys.items():
                text = self.t(key)
                if self._pair_sort and self._pair_sort[0] == col:
                    text += " ▼" if self._pair_sort[1] else " ▲"
                try:
                    self.pair_tree.heading(col, text=text)
                except tk.TclError:
                    pass
            self._apply_column_minwidths(self.pair_tree,
                                         tuple(self._pair_heading_keys))
            status_text = {"ok": "pair_status_ok", "no_raw": "pair_status_no_raw",
                           "no_jpg": "pair_status_no_jpg"}
            for iid, row in getattr(self, "_pair_rows", []):
                try:
                    self.pair_tree.set(iid, "status", self.t(status_text[row.status]))
                    self.pair_tree.set(iid, "action", self._pair_action_text(row))
                except tk.TclError:
                    pass
            self._refresh_pair_legend()
        # 主题按钮显示"切换到"的目标主题
        try:
            self.theme_btn.configure(text=self._theme_button_text())
        except tk.TclError:
            pass
        # 后缀输入框内容/占位（自动识别时显示"（自动识别）"/"(Auto-detect)"）
        self._apply_raw_mode_ui()
        # 动态文本
        self.size_label.configure(text=self._size_label_text())
        self.exif_mode_btn.configure(
            text=self.t("exif_brief") if self._exif_detailed else self.t("exif_detail"))
        self.exif_label.configure(height=0 if self._exif_detailed else 1)
        self._render_exif_current()
        # EXIF 信息区在"未选中照片"时显示提示语：同样需要随语言切换
        if not self._exif_current_path:
            self.exif_var.set(self.t("exif_hint"))
        # 预览区"加载中/无内容/缺少 Pillow"等占位文本
        self._relabel_preview_placeholders()
        # 状态栏按当前语言重译（扫描完成/未发现/格式不符等历史状态）
        if self.busy:
            self.status_var.set(self.t("status_scanning"))
        elif self._scan_summary:
            s = self._scan_summary
            if s.get("mismatch"):
                self.status_var.set(self.t("warn_mismatch_status", list=s["mismatch"]))
            elif s.get("has_orphans"):
                self.status_var.set(
                    self.t("status_scan_done_orphans",
                           n=s["count"], j=s["jpg"], r=s["raw"]))
            else:
                self.status_var.set(self.t("status_no_orphan"))
        else:
            self.status_var.set(self.t("status_initial"))
        # 预览状态条按当前语言重译（"每行 N 张…" / "共 N 张缩略图…"）
        if self._preview_status:
            kind = self._preview_status[0]
            if kind == "gen":
                _, cols, level, size = self._preview_status
                self.preview_status_bar.configure(
                    text=self.t("preview_status_gen", cols=cols,
                                level=self.t(_THUMB_LEVEL_KEYS.get(level, "thumb_medium")),
                                size=size))
            else:
                _, ok, fail = self._preview_status
                self.preview_status_bar.configure(
                    text=self.t("preview_status_done", ok=ok,
                                fail=self.t("preview_status_fail", n=fail) if fail else ""))
        # 结果区日志按当前语言重译（结构化条目）
        self.result_text.configure(state=tk.NORMAL)
        self.result_text.delete("1.0", tk.END)
        for entry in self._result_entries:
            self._render_result_entry(entry)
        self.result_text.configure(state=tk.DISABLED)
        self._update_delete_btn()
        # 关于窗口若正开着：同步重译（避免模态窗口残留旧语言）
        self._relabel_about_window()

    def _relabel_preview_placeholders(self):
        """重译预览区占位文本：空状态提示 + 尚未加载完成的"加载中…"标签。"""
        if self._preview_placeholder is not None:
            try:
                self._preview_placeholder.configure(
                    text=self.t(self._preview_placeholder_key))
            except tk.TclError:
                self._preview_placeholder = None
        for item in self._preview_items.values():
            label = item.get("img_label")
            if label is not None and item.get("photo") is None:
                try:
                    label.configure(text=self.t("loading"))
                except tk.TclError:
                    pass

    def _on_language_changed(self, _event=None):
        """语言切换：10 种语言实时生效，无需重启；选择写入配置。"""
        new = self._lang_map.get(self.lang_var.get())
        if new is None or new == self._lang:
            self.lang_var.set(self.lang_display(self._lang))
            return
        self._lang = new
        self.title(f"{self.t('app_title')}  ·  {APP_AUTHOR}")
        self.lang_var.set(self.lang_display(self._lang))
        self._refresh_combo(self.lang_combo)
        self._apply_language()
        self._save_config_now()   # 记住用户手动选择的语言

    def _on_level_changed(self, _event=None):
        """层级下拉框选择：刷新删除按钮（范围在扫描时生效）并强制重绘下拉框。"""
        self.level_var.set(self._level_display(self._level_internal()))
        self._refresh_combo(self.level_combo)
        self._update_delete_btn()

    @staticmethod
    def _refresh_combo(combo):
        """兼容用：自绘下拉框（PillSelect）取值一变就重画，不需要额外刷新；
        若传入的是 ttk.Combobox 则按老办法强制重绘（只读框切换后常不刷新）。"""
        try:
            if hasattr(combo, "selection_clear"):
                combo.selection_clear()
                combo.configure(state="readonly")
            combo.update_idletasks()
        except tk.TclError:
            pass

    def _raw_mode_values(self):
        """相机品牌下拉框的选项（随语言本地化）。"""
        return ([self.t("auto_label")]
                + [brand_display(b, self._lang) for b in BRANDS]
                + [self.t("custom_label")])

    def _toggle_exif_mode(self):
        """EXIF 展示模式切换：简略展示（单行紧凑、固定高度）<-> 详细展示（9 字段自适应）。"""
        self._exif_detailed = not self._exif_detailed
        self.exif_mode_btn.configure(
            text=self.t("exif_brief") if self._exif_detailed else self.t("exif_detail"))
        self.exif_label.configure(height=0 if self._exif_detailed else 1)
        self._render_exif_current()

    _EXIF_FIELDS = [
        ("exif_make", "make", ""),
        ("exif_model", "model", ""),
        ("exif_aperture", "aperture", "f/"),
        ("exif_shutter", "shutter", ""),
        ("exif_iso", "iso", ""),
        ("exif_focal", "focal", ""),
        ("exif_date", "date", ""),
        ("exif_resolution", "resolution", ""),
        ("exif_lens", "lens", ""),
    ]

    @staticmethod
    def _fmt_exif_value(key: str, value) -> str:
        """EXIF 字段值格式化（详细模式显示用；与底层存储解耦）。
        数值字段先归一化，确保显示 f1.8 而非 18/10 或 [18, 10]。"""
        if key == "exif_aperture":
            return f"f/{_norm_number(value)}"
        if key == "exif_shutter":
            return f"{value}s"
        if key == "exif_focal":
            return f"{_norm_number(value)} mm"
        return str(value)

    def _render_exif(self, data: dict) -> str:
        """按当前模式渲染 EXIF。
        详细模式：固定 9 个字段行（Make/Model/光圈/快门/ISO/焦距/拍摄日期/
        分辨率/镜头型号），缺失字段显示 "--"，JPG 与 RAW 视觉结构完全一致；
        简略模式：单行紧凑排列——相机 | f值 | 快门 | ISO | 焦距 | 分辨率，
        用 " | " 分隔，固定单行高度。"""
        if self._exif_detailed:
            lines = []
            for key, field, _prefix in self._EXIF_FIELDS:
                value = data.get(field)
                if value is None:
                    value = "--"  # 字段缺失占位，保证 9 行结构一致
                else:
                    value = self._fmt_exif_value(key, value)
                lines.append(f"{self.t(key)}{self.t('field_sep')}{value}")
            return "\n".join(lines)
        # 简略：单行紧凑格式（缩短文案，固定高度内展示更多常用信息）
        parts = []
        if data.get("camera"):
            parts.append(data["camera"])              # 相机完整型号
        if data.get("aperture"):
            parts.append(f"f{_norm_number(data['aperture'])}")  # f1.8
        if data.get("shutter"):
            parts.append(data["shutter"])             # 1/200
        if data.get("iso"):
            parts.append(f"ISO{data['iso']}")         # ISO100
        if data.get("focal"):
            parts.append(f"{_norm_number(data['focal'])}mm")  # 50mm
        if data.get("resolution"):
            parts.append(data["resolution"])          # 6000×4000
        return " | ".join(parts) if parts else "--"

    def _copy_exif_all(self):
        """双击 EXIF 区域：复制全部 EXIF 文本到剪贴板。"""
        text = self.exif_var.get()
        if text and text != self.t("exif_hint"):
            self.clipboard_clear()
            self.clipboard_append(text)
            self.status_var.set(self.t("exif_copied"))

    def _copy_exif_value(self, value):
        """右键菜单：复制单个字段值到剪贴板。"""
        if value is not None:
            self.clipboard_clear()
            self.clipboard_append(str(value))
            self.status_var.set(self.t("exif_copied"))

    def _popup_exif_menu(self, event):
        """右键菜单：复制全部 EXIF / 复制单个字段值。"""
        menu = tk.Menu(self, tearoff=0)
        menu.add_command(label=self.t("exif_copy_all"), command=self._copy_exif_all)
        data = self._exif_cache.get(self._exif_current_path or "")
        if data:
            menu.add_separator()
            for key, field, _prefix in self._EXIF_FIELDS:
                value = data.get(field)
                label = (
                    f"{self.t(key)}{self.t('field_sep')}"
                    f"{self._fmt_exif_value(key, value) if value is not None else '--'}"
                )
                menu.add_command(label=label,
                                 command=lambda v=value: self._copy_exif_value(v))
        try:
            menu.tk_popup(event.x_root, event.y_root)
        finally:
            menu.grab_release()

    def _render_exif_current(self):
        """重新渲染当前照片的 EXIF（语言切换/模式切换后调用）。"""
        if not self._exif_current_path:
            return
        data = self._exif_cache.get(self._exif_current_path)
        if data:
            self.exif_var.set(self._render_exif(data))
        else:
            self.exif_var.set(self.t("exif_fail"))

    # ----- 配置与通用辅助 -----

    def _apply_raw_mode_ui(self):
        """根据 RAW 下拉框当前值设置后缀输入框的状态与内容。"""
        mode = self._raw_internal()
        auto_text = self.t("auto_placeholder")
        if mode == AUTO_ID:
            self.raw_entry.configure(state="disabled")
            self.raw_entry_var.set(auto_text)
        elif mode == CUSTOM_ID:
            self.raw_entry.configure(state="normal")
            self.raw_entry_var.set(self._custom_text or "")
        elif mode in RAW_FORMATS:
            self.raw_entry.configure(state="readonly")
            self.raw_entry_var.set(", ".join(RAW_FORMATS[mode]))
        else:  # 防御：未知值一律回退自动识别
            self.raw_mode_var.set(self._raw_display(AUTO_ID))
            self.raw_entry.configure(state="disabled")
            self.raw_entry_var.set(auto_text)

    def _on_raw_mode_changed(self, _event=None):
        """下拉框切换 RAW 模式：记录内部 id 并刷新后缀输入框状态。"""
        self._raw_mode_internal = self._raw_internal()
        self.raw_mode_var.set(self._raw_display(self._raw_mode_internal))
        self._refresh_combo(self.raw_combo)
        self._apply_raw_mode_ui()
        if self._raw_mode_internal == CUSTOM_ID:
            # 切到"自定义"时把焦点给后缀输入框，用户可直接输入
            try:
                self.raw_entry.focus_set()
            except tk.TclError:
                pass

    def _on_raw_entry_edit(self, *_args):
        """自定义后缀输入变化时记录，供切换模式后恢复。"""
        if self._raw_internal() == CUSTOM_ID:
            self._custom_text = self.raw_entry_var.get()

    def _resolve_raw_config(self):
        """返回 (auto_detect, selected_raw)；自定义后缀非法时抛 ValueError。"""
        mode = self._raw_internal()
        if mode == AUTO_ID:
            return True, set()
        if mode == CUSTOM_ID:
            return False, parse_raw_exts(self.raw_entry_var.get())
        return False, set(RAW_FORMATS.get(mode, ()))

    def _save_config_now(self):
        """把当前界面状态写入配置文件（关闭窗口与扫描完成时调用）。"""
        try:
            sash = self.main_paned.sashpos(0)
        except tk.TclError:
            sash = self._cfg_sash or 0
        save_config({
            "folder": self.current_folder or self.path_var.get().strip(),
            "raw_mode": self._raw_internal(),
            "raw_custom": self._custom_text,
            "scan_level": self._level_internal(),
            "confirm": bool(self.confirm_var.get()),
            "sash": sash,
            "geometry": self.winfo_geometry(),
            "thumb_level": self._thumb_level,
            "about_shown": self._about_shown,
            "lang": self._lang,                      # 界面语言（首次自动检测后写入）
            "theme": self._theme_pref,               # auto / light / dark
            "unchecked": sorted(self._unchecked_paths())[:5000],  # 勾选状态记忆
            "ui_mode": self._ui_mode,                # classic / pair（用户选择的界面）
            "pair_color": self._pair_color,          # bg / fg
            "pair_only_missing": bool(self._pair_only_missing),
        })

    def _unchecked_paths(self):
        """当前未被勾选（保留不删）的文件路径集合。"""
        return {f.full_path for f in self.orphans if f.full_path not in self._checked}

    def _persist_startup_choices(self):
        """首次启动：把系统语言检测结果与主题偏好写入配置（只改这两项，
        避免在窗口尚未映射时覆盖用户保存的窗口几何与分隔条位置）。"""
        try:
            cfg = load_config()
            cfg["lang"] = self._lang
            cfg["theme"] = self._theme_pref
            save_config(cfg)
        except Exception:
            pass

    def _set_controls_state(self, disabled: bool):
        """操作进行中禁用输入控件，防止重复触发（自绘控件同样支持 state=）。"""
        state = "disabled" if disabled else "normal"
        combo_state = "disabled" if disabled else "readonly"
        for widget in (self.browse_btn, self.scan_btn, self.size_scale,
                       self.select_toggle_btn):
            try:
                widget.configure(state=state)
            except tk.TclError:
                pass
        self.path_entry.configure(state=state)
        for widget in self.mode_btns:
            widget.configure(state=state)
        self.level_combo.configure(state=combo_state)
        self.raw_combo.configure(state=combo_state)
        if disabled:
            self.raw_entry.configure(state=tk.DISABLED)
        else:
            # 恢复后缀输入框应有的状态（自动=禁用 / 品牌=只读 / 自定义=可编辑）
            self._apply_raw_mode_ui()
        if disabled:
            self.delete_btn.configure(state="disabled")
        else:
            self._update_delete_btn()

    def _update_delete_btn(self):
        """刷新删除按钮：数量与总大小只统计【仍被勾选】的文件；
        未匹配 RAW 时改为"强制删除"（强制二次确认）。语言切换时同步刷新。"""
        targets = self._targets_for_mode()
        if targets and not self.busy:
            total_size = sum(f.size for f in targets)
            key = "force_btn_fmt" if self._force_mode else "delete_btn_fmt"
            self.delete_btn.configure(
                text=self.t(key, n=len(targets), size=human_size(total_size)),
                style="primary" if self._force_mode else "danger",
                state="normal",
            )
        else:
            self.delete_btn.configure(state="disabled", style="danger",
                                      text=self.t("confirm_delete"))

    @staticmethod
    def _escape_fmt(text: str) -> str:
        """转义格式化占位符括号，避免文件名/错误信息里的 { } 干扰 .format。"""
        return str(text).replace("{", "{{").replace("}", "}}")

    def _append_result(self, text: str):
        """向"操作结果"区域追加一行普通文本（语言切换时保持原文）。"""
        self._result_entries.append(("text", text))
        self._render_result_entry(("text", text))

    def _append_result_key(self, key: str, **data):
        """追加一行【可重译】的结果条目（语言切换时按当前语言重新渲染）。"""
        self._result_entries.append(("key", key, data))
        self._render_result_entry(("key", key, data))

    def _render_result_entry(self, entry):
        if entry[0] == "text":
            text = entry[1]
        else:
            # 数据值若是 ("t", key) 元组，则渲染时按当前语言翻译（用于模式名等）
            data = {
                k: (self.t(v[1]) if isinstance(v, tuple) and v and v[0] == "t" else v)
                for k, v in entry[2].items()
            }
            text = self.t(entry[1], **data)
        self.result_text.configure(state=tk.NORMAL)
        self.result_text.insert(tk.END, text + "\n")
        self.result_text.see(tk.END)
        self.result_text.configure(state=tk.DISABLED)

    def _refresh_tree(self):
        """用 self.orphans 重建列表（首列为勾选状态），并记录 路径 <-> 行 iid 映射。"""
        for iid in self.tree.get_children():
            self.tree.delete(iid)
        self._tree_iid_by_path = {}
        self._iid_to_path = {}
        for idx, f in enumerate(self.orphans):
            checked = f.full_path in self._checked
            tags = ["odd" if idx % 2 else "even"]
            if not checked:
                tags.append("off")   # 未勾选（保留）的行弱化显示
            iid = self.tree.insert(
                "", tk.END,
                values=(CHECK_ON if checked else CHECK_OFF, f.name, f.ext,
                        human_size(f.size), f.folder),
                tags=tuple(tags),
            )
            self._tree_iid_by_path[f.full_path] = iid
            self._iid_to_path[iid] = f.full_path

    # ----- 勾选（删除 / 保留） -----

    def _sync_checked_from_config(self):
        """扫描完成后初始化勾选状态：默认全选，配置里记录的"保留"项不勾选。"""
        self._checked = {f.full_path for f in self.orphans}
        if self._unchecked_saved:
            for f in self.orphans:
                if f.full_path in self._unchecked_saved:
                    self._checked.discard(f.full_path)

    def _set_checked(self, path: str, checked: bool):
        """设置单个文件的勾选状态，并同步列表单元格与预览角标。"""
        if checked:
            self._checked.add(path)
        else:
            self._checked.discard(path)
        iid = self._tree_iid_by_path.get(path)
        if iid:
            try:
                self.tree.set(iid, "chk", CHECK_ON if checked else CHECK_OFF)
                self._refresh_row_tags(iid)
            except tk.TclError:
                pass
        pair_iid = self._pair_iid_by_path.get(path)
        if pair_iid:
            try:
                self.pair_tree.set(pair_iid, "chk",
                                   CHECK_ON if checked else CHECK_OFF)
                row = next((r for i, r in self._pair_rows if i == pair_iid), None)
                if row is not None:      # 「处理」列同步：删除 / 不删除·已取消勾选
                    self.pair_tree.set(pair_iid, "action",
                                       self._pair_action_text(row, checked))
            except tk.TclError:
                pass
        item = self._preview_items.get(path)
        if item:
            self._apply_check_style(path, item, checked)
        self._update_delete_btn()

    def _toggle_checked(self, path: str):
        self._set_checked(path, path not in self._checked)

    def _set_all_checked(self, checked: bool):
        """全选 / 全不选（只影响当前删除方式下会显示的文件）。"""
        for f in self._preview_targets():
            if checked:
                self._checked.add(f.full_path)
            else:
                self._checked.discard(f.full_path)
        for f in self.orphans:
            iid = self._tree_iid_by_path.get(f.full_path)
            if not iid:
                continue
            try:
                self.tree.set(iid, "chk",
                              CHECK_ON if f.full_path in self._checked else CHECK_OFF)
                self._refresh_row_tags(iid)
            except tk.TclError:
                pass
        for path, item in self._preview_items.items():
            self._apply_check_style(path, item, path in self._checked)
        self._paint_pair_rows()
        self._update_delete_btn()

    def _on_tree_space(self, _event=None):
        """空格键：切换当前选中行的勾选状态。"""
        for iid in self.tree.selection():
            path = self._iid_to_path.get(iid)
            if path:
                self._toggle_checked(path)
        return "break"

    def _on_tree_wheel(self, event):
        """鼠标滚轮滚动列表（含滚动条上滚动）。"""
        try:
            self.tree.yview_scroll(-1 if event.delta > 0 else 1, "units")
        except tk.TclError:
            pass
        return "break"

    def _on_sort(self, col: str):
        """单击表头排序：文件名/类型/文件大小，再次点击切换升降序。"""
        if self._sort_col == col:
            self._sort_reverse = not self._sort_reverse
        else:
            self._sort_col = col
            self._sort_reverse = False
        key = {
            "name": lambda f: f.name.lower(),      # 按 Windows 规则不区分大小写
            "type": lambda f: (f.ext, f.name.lower()),
            "size": lambda f: f.size,              # 按字节数数值排序
        }[col]
        self.orphans.sort(key=key, reverse=self._sort_reverse)
        self._refresh_tree()
        self._refresh_preview()  # 预览顺序与列表保持一致
        # 表头显示排序方向标记
        mark = " ▼" if self._sort_reverse else " ▲"
        for c, key in self._heading_keys.items():
            text = self.t(key) + (mark if c == col else "")
            self.tree.heading(c, text=text)

    def _reset_sort(self):
        """新扫描结果就绪后：恢复默认排序并清除表头标记。"""
        self._sort_col = None
        self._sort_reverse = False
        for c, key in self._heading_keys.items():
            self.tree.heading(c, text=self.t(key))

    def _on_tree_click(self, event):
        """单击列表行：显示 EXIF，并把预览区滚动/高亮到对应缩略图；
        单击首列（勾选列）则切换该行的勾选状态。"""
        iid = self.tree.identify_row(event.y)
        if not iid:
            return
        path = self._iid_to_path.get(iid)
        if not path:
            return
        if self.tree.identify_column(event.x) == "#1":   # 勾选列
            self._toggle_checked(path)
            return
        try:
            self.tree.selection_set(iid)
        except tk.TclError:
            pass
        self._show_exif(path)
        self._focus_preview(path)

    def _focus_preview(self, path: str):
        """把预览区滚动到指定缩略图并高亮（列表 -> 预览联动，长列表也流畅）。"""
        item = self._preview_items.get(path)
        if item is None:
            return
        cell = item["cell"]
        try:
            total = max(1, self.preview_inner.winfo_height())
            canvas_h = max(1, self.preview_canvas.winfo_height())
            y = cell.winfo_y()
            # 让目标单元尽量靠近可视区顶端（留 8px 余量）
            frac = max(0.0, (y - 8) / total) if total > canvas_h else 0.0
            self.preview_canvas.yview_moveto(min(frac, 1.0))
        except tk.TclError:
            pass
        self._highlight_preview(path)

    def _highlight_preview(self, path: str):
        """高亮预览区指定单元：只改上一个与当前单元，O(1) 开销。"""
        if self._hl_path == path:
            return
        prev = self._preview_items.get(self._hl_path or "")
        if prev:
            try:
                prev["cell"].configure(highlightbackground=UI["border"],
                                       highlightthickness=1)
            except tk.TclError:
                pass
        self._hl_path = path
        cur = self._preview_items.get(path)
        if cur:
            try:
                cur["cell"].configure(highlightbackground=UI["accent"],
                                      highlightthickness=2)
            except tk.TclError:
                pass

    def _on_tree_double_click(self, event):
        """双击文件行：在资源管理器中打开并定位对应照片。"""
        iid = self.tree.identify_row(event.y)
        if not iid:
            return
        path = self._iid_to_path.get(iid)
        if path:
            self._reveal_in_explorer(path)

    def _reveal_in_explorer(self, path: str):
        """
        调用 Windows 资源管理器并选中指定文件。

        不直接使用 explorer /select, 命令行：explorer.exe 按系统 ANSI
        代码页解析命令行参数，中文路径会解析错误导致打开位置不对。
        这里改用 Shell API（SHParseDisplayName + SHOpenFolderAndSelectItems），
        全程 Unicode，中文/空格/逗号路径均可正确定位。
        """
        shell32 = ctypes.windll.shell32
        ole32 = ctypes.windll.ole32
        # 设置参数类型，避免 64 位下指针截断、str 被当作 ANSI 字符串
        shell32.SHParseDisplayName.argtypes = [
            wintypes.LPCWSTR,                    # pszName
            ctypes.c_void_p,                     # pbc
            ctypes.POINTER(ctypes.c_void_p),     # ppidl
            ctypes.c_uint,                       # sfgaoIn
            ctypes.c_void_p,                     # psfgaoOut
        ]
        shell32.SHParseDisplayName.restype = ctypes.c_long
        shell32.SHOpenFolderAndSelectItems.argtypes = [
            ctypes.c_void_p,                     # pidlFolder
            ctypes.c_uint,                       # cidl
            ctypes.c_void_p,                     # apidl
            ctypes.c_uint,                       # dwFlags
        ]
        shell32.SHOpenFolderAndSelectItems.restype = ctypes.c_long
        try:
            ole32.CoInitialize(None)  # 需要 COM 初始化
            try:
                pidl = ctypes.c_void_p()
                # 把路径字符串解析为 PIDL（绝对定位，支持 Unicode）
                hr = shell32.SHParseDisplayName(path, None, ctypes.byref(pidl), 0, None)
                if hr == 0 and pidl.value:
                    try:
                        # 打开所在文件夹并选中该文件
                        shell32.SHOpenFolderAndSelectItems(pidl, 0, None, 0)
                    finally:
                        ole32.CoTaskMemFree(pidl)  # 释放 PIDL
                    return
                raise OSError(f"SHParseDisplayName 失败（HRESULT=0x{hr & 0xFFFFFFFF:08X}）")
            finally:
                ole32.CoUninitialize()
        except Exception as exc:
            # 兜底：直接打开所在文件夹（不做选中定位）
            try:
                subprocess.Popen(["explorer", os.path.dirname(path)])
            except Exception:
                messagebox.showerror(
                    "无法打开资源管理器",
                    f"打开文件所在位置失败：\n{path}\n\n原因：{exc}",
                    parent=self,
                )

    def _schedule_poll(self):
        """安排下一次队列轮询，并记录句柄以便关闭窗口时取消。"""
        self._poller_after_id = self.after(100, self._poll_queue)

    def _poll_queue(self):
        """主线程定期取出并执行工作线程放入队列的 UI 更新（线程安全）。"""
        try:
            while True:
                func, args = self._ui_queue.get_nowait()
                try:
                    func(*args)
                except Exception:
                    # 单个 UI 更新失败（如窗口已关闭）不影响轮询器；
                    # 但若 _on_scan_done 等主流程回调出错，必须解除忙碌状态，
                    # 否则状态栏会永远卡在"正在扫描"，界面无法继续操作
                    if not self._closing and self.busy:
                        self.busy = False
                        try:
                            self._set_controls_state(disabled=False)
                        except Exception:
                            pass
        except queue.Empty:
            pass
        if not self._closing:
            self._schedule_poll()

    # ----- 事件处理 -----

    def _browse_folder(self):
        """浏览选择文件夹：选择后自动开始扫描。"""
        initial = self.path_var.get().strip() or os.path.expanduser("~")
        chosen = filedialog.askdirectory(initialdir=initial, title=self.t("browse"))
        if chosen:
            self.path_var.set(os.path.normpath(chosen))
            self._begin_scan_from_ui()

    def _on_scan_clicked(self):
        self._begin_scan_from_ui()

    def _begin_scan_from_ui(self):
        """校验路径与 RAW 配置后开始扫描（扫描按钮与浏览选择共用）。"""
        if self.busy:
            return
        path = self.path_var.get().strip().strip('"')
        if not path:
            messagebox.showwarning(self.t("scan"), self.t("msg_path_empty"), parent=self)
            return
        if not os.path.exists(path):
            messagebox.showerror(self.t("scan"),
                                 self.t("msg_path_not_exist", path=path), parent=self)
            return
        if not os.path.isdir(path):
            messagebox.showerror(self.t("scan"),
                                 self.t("msg_path_not_dir", path=path), parent=self)
            return
        try:
            auto_detect, selected_raw = self._resolve_raw_config()
        except ValueError as exc:
            messagebox.showerror(self.t("scan"), str(exc), parent=self)
            return
        # 手动重新扫描时清空旧的结果区（删除后的自动重扫不清空，保留失败详情）
        self._result_entries.clear()
        self.result_text.configure(state=tk.NORMAL)
        self.result_text.delete("1.0", tk.END)
        self.result_text.configure(state=tk.DISABLED)
        self._start_scan(path, auto_detect, selected_raw)

    def _start_scan(self, path: str, auto_detect: bool, selected_raw: set):
        self.busy = True
        self._set_controls_state(disabled=True)
        self.status_var.set(self.t("status_scanning"))
        self.current_folder = path
        self._scan_summary = None  # 扫描开始：清空旧摘要（语言切换时显示扫描中）
        self._clear_preview()
        max_depth = SCAN_LEVEL_MAX_DEPTH.get(self._level_internal(), None)
        threading.Thread(
            target=self._scan_worker,
            args=(path, auto_detect, set(selected_raw), max_depth),
            daemon=True,
        ).start()

    def _scan_worker(self, path, auto_detect, selected_raw, max_depth):
        """后台线程：执行耗时扫描；完成后通过队列回到主线程刷新界面。"""
        try:
            result = scan_folder(path, auto_detect, selected_raw, max_depth)
            error = None
        except Exception as exc:  # 文件夹级错误：统一转成友好提示
            result, error = None, exc
        self._ui_queue.put((self._on_scan_done, (path, result, error)))

    def _on_scan_done(self, path, result, error):
        self.busy = False
        self._set_controls_state(disabled=False)

        if error is not None or result is None:
            # 扫描失败：清空旧数据，避免误删过期列表中的文件
            self.orphans = []
            self.scan_result = None
            self._reset_sort()
            self._refresh_tree()
            self._refresh_pair_tree()
            self._clear_preview()
            self.status_var.set(self.t("status_scan_failed"))
            self._append_result_key(
                "result_scan_failed",
                path=self._escape_fmt(path),
                error=self._escape_fmt(error))
            messagebox.showerror(
                self.t("msg_scan_failed_title"),
                self.t("msg_scan_failed_body", path=path, error=error),
                parent=self,
            )
            self._update_delete_btn()
            return

        self.orphans = result.orphans
        self.scan_result = result          # 配对对比视图的数据来源
        # 新文件夹的扫描结果：旧缩略图/EXIF 缓存不再有用，清空以释放内存
        self._thumb_cache.clear()
        self._exif_cache.clear()
        # 勾选状态：默认全部勾选（加入删除），配置中记录为"保留"的文件不勾选
        self._sync_checked_from_config()
        # 未匹配保护：文件夹中没有任何已知 RAW，或检测到的格式与所选不符，
        # 均视为"未匹配" -> 删除按钮切换为"强制删除"并强制二次确认
        self._force_mode = not result.detected_raw or bool(result.mismatch_raw)
        self._reset_sort()  # 新扫描结果恢复默认排序
        self._pair_sort = None
        self._picked_pair_iid = None
        self._refresh_tree()
        self._refresh_pair_tree()          # 对比视图同步刷新
        self._refresh_preview()

        # 状态栏与结果区信息
        if result.mismatch_raw:
            fmt_list = "、".join(sorted(e.upper() for e in result.mismatch_raw))
            warn = self.t("result_mismatch", list=fmt_list)
            self.status_var.set(warn)
            self._append_result_key("result_mismatch", list=fmt_list)
            self._append_result_key("result_mismatch_tail")
        elif result.auto_detect:
            # 自动识别完成：识别到的后缀显示在"后缀"输入框内；
            # 相机品牌下拉框不锁定，可直接重新选择品牌或切回"自动识别"
            suffix_display = "、".join(
                sorted(e.upper().lstrip(".") for e in result.detected_raw)
            )
            if not suffix_display:
                suffix_display = self.t("auto_label")
            self.raw_mode_var.set(self._raw_display(AUTO_ID))  # 品牌框显示"自动识别"
            self._raw_mode_internal = AUTO_ID
            self.raw_entry.configure(state="disabled")
            self.raw_entry_var.set(
                ", ".join(sorted(e for e in result.detected_raw))
                or self.t("auto_placeholder")
            )
            self._append_result_key("result_auto_detect", list=suffix_display)

        if self._force_mode:
            self._append_result_key("result_force")

        if result.skipped:
            self._append_result_key("result_skipped", n=len(result.skipped))
            for item_path, reason in result.skipped:
                self._append_result(f"  · {item_path} —— {reason}")

        jpg_count = sum(1 for f in result.orphans if f.ext == "JPG")
        raw_count = len(result.orphans) - jpg_count
        # 记录扫描摘要：语言切换时用当前语言重译状态栏（扫描完成/未发现/格式不符）
        self._scan_summary = {
            "mismatch": ("、".join(sorted(e.upper() for e in result.mismatch_raw))
                         if result.mismatch_raw else None),
            "has_orphans": bool(result.orphans),
            "count": len(result.orphans),
            "jpg": jpg_count,
            "raw": raw_count,
        }
        if not result.orphans:
            # 有格式不符警告时，状态栏保留警告信息，不覆盖
            if not result.mismatch_raw:
                self.status_var.set(self.t("status_no_orphan"))
            self._append_result_key(
                "result_scan_done_none", path=self._escape_fmt(path),
                p=result.paired_base_count)
        else:
            if not result.mismatch_raw:
                self.status_var.set(
                    self.t("status_scan_done_orphans", n=len(result.orphans),
                           j=jpg_count, r=raw_count)
                )
            self._append_result_key(
                "result_scan_done", path=self._escape_fmt(path), n=len(result.orphans),
                j=jpg_count, r=raw_count, p=result.paired_base_count)
        self._update_delete_btn()
        self._save_config_now()  # 记忆本次使用的配置

    # ----- 删除 -----

    def _targets_for_mode(self):
        """按当前单选方式取出【已勾选】的待删除文件（取消勾选的保留不删）。"""
        return [f for f in self._preview_targets() if f.full_path in self._checked]

    def _on_mode_changed(self):
        """删除方式变化：刷新删除按钮与相片预览。"""
        self._update_delete_btn()
        self._refresh_preview()

    def _on_delete_clicked(self):
        if self.busy:
            return
        targets = self._targets_for_mode()
        if not targets:
            messagebox.showinfo(self.t("confirm_delete"), self.t("msg_no_target"),
                                parent=self)
            return

        total_size = sum(f.size for f in targets)
        # 已排除（取消勾选、保留不删）的文件数量，二次确认中明确告知
        excluded = len([f for f in self._preview_targets()
                        if f.full_path not in self._checked])
        if self._force_mode or self.confirm_var.get():
            # 强制删除：RAW 格式未匹配，必须弹出强制确认（不可跳过）
            # 普通模式：勾选"删除前二次确认"时弹确认框
            title_key = "msg_force_title" if self._force_mode else "msg_confirm_title"
            body_key = "msg_force_body" if self._force_mode else "msg_confirm_body"
            text = self.t(body_key, count=len(targets), size=human_size(total_size))
            if excluded:
                text += "\n\n" + self.t("msg_confirm_excluded", n=excluded)
            if not self._ask_confirm(self.t(title_key), text):
                return

        self.busy = True
        # 作废旧缩略图任务：避免后台解码线程在删除期间占用文件句柄
        self._preview_token += 1
        self._set_controls_state(disabled=True)
        self.status_var.set(self.t("status_deleting"))
        self._append_result_key(
            "result_deleting", n=len(targets),
            mode=("t", self.MODE_KEYS[self.mode_var.get()])
        )
        threading.Thread(target=self._delete_worker, args=(targets,), daemon=True).start()

    def _ask_confirm(self, title: str, body: str) -> bool:
        """自绘二次确认弹窗（防误触）：
        · 无标题栏、无"×"关闭按钮；Esc / Enter 一律视为取消；
        · 两个圆形按钮：左侧中性"取消"、右侧危险色"删除"，按下时变为实心；
        · 默认焦点在取消，删除必须明确点击，避免回车误删。"""
        dlg = tk.Toplevel(self)
        dlg.withdraw()
        dlg.overrideredirect(True)          # 无系统标题栏（因此没有 × 按钮）
        dlg.configure(bg=UI["border"])
        dlg.transient(self)
        result = {"ok": False}

        outer = tk.Frame(dlg, bg=UI["card"])
        outer.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        tk.Label(outer, text=title, bg=UI["card"], fg=UI["text"],
                 font=(self._font_family, 12, "bold"),
                 anchor="w", justify=tk.LEFT).pack(fill=tk.X, padx=20, pady=(16, 6))
        tk.Label(outer, text=body, bg=UI["card"], fg=UI["text"],
                 font=(self._font_family, 10), anchor="w", justify=tk.LEFT,
                 wraplength=460).pack(fill=tk.X, padx=20)

        def _finish(ok):
            result["ok"] = ok
            try:
                dlg.grab_release()
            except tk.TclError:
                pass
            dlg.destroy()

        btns = tk.Frame(outer, bg=UI["card"])
        btns.pack(fill=tk.X, pady=(14, 16))
        cancel_btn = RoundButton(btns, "✕", self.t("confirm_cancel"),
                                 style="neutral", command=lambda: _finish(False))
        ok_btn = RoundButton(btns, "✓", self.t("confirm_ok"),
                             style="danger", command=lambda: _finish(True))
        self._round_buttons.extend([cancel_btn, ok_btn])
        cancel_btn.pack(side=tk.LEFT, expand=True)
        ok_btn.pack(side=tk.RIGHT, expand=True)
        tip = tk.Frame(outer, bg=UI["card"])
        tip.pack(fill=tk.X, pady=(0, 12))
        tk.Label(tip, text=self.t("confirm_cancel"), bg=UI["card"], fg=UI["muted"],
                 font=(self._font_family, 9)).pack(side=tk.LEFT, expand=True)
        tk.Label(tip, text=self.t("confirm_ok"), bg=UI["card"], fg=UI["danger"],
                 font=(self._font_family, 9)).pack(side=tk.RIGHT, expand=True)

        dlg.bind("<Escape>", lambda _e: _finish(False))
        dlg.bind("<Return>", lambda _e: _finish(False))   # 回车=取消（安全默认）
        dlg.update_idletasks()
        w, h = max(420, dlg.winfo_reqwidth()), dlg.winfo_reqheight()
        self.update_idletasks()
        x = self.winfo_rootx() + max(0, (self.winfo_width() - w) // 2)
        y = self.winfo_rooty() + max(0, (self.winfo_height() - h) // 3)
        dlg.geometry(f"{w}x{h}+{x}+{y}")
        dlg.deiconify()
        try:
            dlg.grab_set()          # 模态
            dlg.focus_force()
            cancel_btn.focus_set()
        except tk.TclError:
            pass
        self.wait_window(dlg)
        for btn in (cancel_btn, ok_btn):
            if btn in self._round_buttons:
                self._round_buttons.remove(btn)
        return bool(result["ok"])

    def _delete_worker(self, targets):
        """后台线程：逐个移入回收站（带重试）；单个失败不中断整个流程。"""
        ok = fail = 0
        failures: list = []  # [(文件名, 原因)]
        total = len(targets)
        for index, f in enumerate(targets, start=1):
            try:
                if not os.path.exists(f.full_path):
                    raise OSError("文件不存在（可能已被移动或删除）")
                _recycle_with_retry(f.full_path)  # 移入回收站，失败重试一次
                ok += 1
            except Exception as exc:  # 单个文件失败不中断，继续处理其余文件
                fail += 1
                failures.append((f.name, str(exc) or exc.__class__.__name__))
            self._ui_queue.put(
                (self.status_var.set,
                 (f"{self.t('status_deleting')} {index}/{total}",))
            )
        self._ui_queue.put((self._on_delete_done, (ok, fail, failures)))

    def _on_delete_done(self, ok, fail, failures):
        self._append_result_key("result_deleted", ok=ok, fail=fail)
        if failures:
            for name, reason in failures:
                self._append_result_key(
                    "result_fail_item",
                    name=self._escape_fmt(name),
                    reason=self._escape_fmt(reason))

        if fail:
            messagebox.showwarning(
                self.t("msg_done_fail"),
                self.t("msg_done_fail_body", ok=ok, fail=fail),
                parent=self,
            )
        else:
            messagebox.showinfo(self.t("msg_done_ok"),
                                self.t("msg_done_ok_body", count=ok), parent=self)

        # 首次使用：成功删除文件后固定 2 秒自动弹出"关于"（感谢开发者），
        # 写入配置后同一台设备只弹出一次
        if ok > 0 and not self._about_shown:
            self._about_shown = True
            self._save_config_now()  # 立即持久化，防止重复弹出
            self.after(2000, self._maybe_show_first_about)

        # 删除完成后自动重新扫描刷新列表与预览；
        # 扫描过程不弹任何提示框，仅更新状态栏（"扫描完成"/"未发现未配对文件"）
        self.busy = False
        try:
            auto_detect, selected_raw = self._resolve_raw_config()
        except ValueError:
            auto_detect, selected_raw = True, set()
        self._start_scan(self.current_folder, auto_detect, selected_raw)

    # ----- 相片预览 -----

    def _preview_targets(self):
        """当前删除方式下将被删除的文件（JPG 显示缩略图，RAW 显示占位框）。"""
        mode = self.mode_var.get()
        if mode == "jpg":
            return [f for f in self.orphans if f.ext == "JPG"]
        if mode == "raw":
            return [f for f in self.orphans if f.ext == "RAW"]
        return list(self.orphans)

    def _clear_preview(self):
        """清空预览区并作废旧任务（缩略图/EXIF 缓存保留，供档位切换与
        删除方式切换复用，避免重复解码与重新加载）。
        切换文件夹/重建时强制滚动条归顶，保证首张照片立即可见。"""
        self._preview_token += 1
        for job in (self._resize_job, self._size_job):
            if job is not None:
                try:
                    self.after_cancel(job)
                except tk.TclError:
                    pass
        self._resize_job = None
        self._size_job = None
        self._preview_placeholder = None
        self._preview_placeholder_key = None
        self._hl_path = None          # 预览高亮状态随重建失效
        for child in self.preview_inner.winfo_children():
            child.destroy()
        self._preview_items.clear()
        try:
            self.preview_canvas.yview_moveto(0)  # 滚动条归顶
            self.preview_canvas.configure(
                scrollregion=self.preview_canvas.bbox("all"))
        except tk.TclError:
            pass

    def _set_preview_placeholder(self, key: str):
        """显示预览区空状态提示（记录控件与语言键，语言切换时自动重译）。"""
        label = tk.Label(self.preview_inner, text=self.t(key), bg=UI["card"],
                         fg=UI["muted"], font=(self._font_family, 10))
        label.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self._preview_placeholder = label
        self._preview_placeholder_key = key

    def _refresh_preview(self):
        """重建预览区：多列网格布局，每行数量随窗口宽度自动计算。
        只对未缓存的 JPG 解码生成 120px 最小档缓存（并行），并一并读取
        EXIF；已缓存的直接按当前档位等比缩放显示，切换档位不重新解码。"""
        self._clear_preview()
        targets = self._preview_targets()

        if not PILLOW_AVAILABLE:
            self._set_preview_placeholder("msg_no_pillow")
            return
        if not targets:
            self._set_preview_placeholder("msg_no_preview")
            return

        size = self.THUMB_SIZES[self._thumb_level]
        # 每行数量 = 画布宽度 / 单元格宽度（grid 布局）
        canvas_w = self.preview_canvas.winfo_width()
        if canvas_w < 100:
            canvas_w = 800
        cols = max(1, (canvas_w - 8) // (size + self.CELL_PAD_X))

        # 固定状态提示行（位于滚动区域外的底部状态条，不随内容滚动）
        self._preview_status = ("gen", cols, self._thumb_level, size)
        self.preview_status_bar.configure(
            text=self.t("preview_status_gen", cols=cols,
                        level=self._thumb_level_text(), size=size)
        )
        # 列等宽：单元格在列内顶部居中，多余空间均匀分布。
        # 先清除上一次布局残留的列权重，避免影响本次列宽分配
        for c in range(64):
            self.preview_inner.grid_columnconfigure(c, weight=0, uniform="")
        for c in range(cols):
            self.preview_inner.grid_columnconfigure(c, weight=1, uniform="thumb")

        # 按列表顺序放入网格（行/列由每行数量自动计算）
        for idx, f in enumerate(targets):
            row, col = divmod(idx, cols)
            self._create_preview_item(f, size, row + 1, col)

        # JPG：未缓存的并行解码生成缓存；已缓存的按当前档位缩放显示
        # （缓存保留在内存中，删除方式切换/档位切换都不会重新解码）
        jpg_targets = [f for f in targets if f.ext == "JPG"]
        token = self._preview_token
        if jpg_targets:
            uncached = [f.full_path for f in jpg_targets
                        if f.full_path not in self._thumb_cache]
            cached = [f.full_path for f in jpg_targets
                      if f.full_path in self._thumb_cache]
            if uncached:
                threading.Thread(target=self._thumb_worker,
                                 args=(uncached, token), daemon=True).start()
            if cached:
                self._resize_token += 1  # 作废旧缩放任务，确保本次结果生效
                threading.Thread(target=self._resize_worker,
                                 args=(cached, self._resize_token, size),
                                 daemon=True).start()
            if not uncached:
                self._preview_finish(token, len(cached), 0)
        else:
            self._preview_finish(token, 0, 0)

    def _create_preview_item(self, f, size, row, col):
        """创建一个网格单元（现代扁平卡片：浅底 + 细描边 + 悬停高亮）；
        JPG 等比居中显示缩略图，RAW 显示正方形占位框（居中大写后缀名）；
        右上角为勾选角标（☑ 删除 / ☐ 保留），点击即可切换。"""
        cell = tk.Frame(self.preview_inner, bd=0, highlightthickness=1,
                        highlightbackground=UI["border"], highlightcolor=UI["border"],
                        bg=UI["cell"], cursor="hand2")
        cell.pack_propagate(False)  # 固定单元格尺寸，不随内容变化
        cell.configure(width=size + self.CELL_PAD_X, height=size + self.CELL_PAD_Y)
        # grid 放入指定行列；sticky="n" 保持请求尺寸并顶部居中（不拉伸变形）
        cell.grid(row=row, column=col, padx=5, pady=5, sticky="n")

        img_label = None
        raw_box = None
        if f.ext == "RAW":
            # RAW：正方形占位框，居中显示大写后缀名
            raw_box = tk.Canvas(
                cell, width=size, height=size,
                bg=UI["raw_box"], highlightthickness=1,
                highlightbackground=UI["border"],
            )
            font_px = max(10, min(32, size // 8))
            raw_box.create_text(
                size // 2, size // 2,
                text=f.raw_ext.upper().lstrip("."),
                font=(self._font_family, font_px, "bold"), fill=UI["accent_dark"],
            )
            raw_box.pack(pady=(5, 0))
        else:
            # JPG：先放"加载中"占位，缩略图生成后替换（文案随语言切换）
            img_label = tk.Label(cell, text=self.t("loading"), foreground=UI["muted"],
                                 bg=UI["cell"], font=(self._font_family, 9))
            img_label.pack(pady=(5, 0))

        # 文件名：固定单行高度、靠底放置（CELL_PAD_Y 已预留足够空间，不会被遮挡）
        name_label = tk.Label(cell, text=self._short_name(f.name, size),
                              font=(self._font_family, 9), bg=UI["cell"],
                              fg=UI["text"], height=1)
        name_label.pack(side=tk.BOTTOM, fill=tk.X, pady=(0, 3))

        # 勾选角标（右上角，极简圆角方框 + 勾）：JPG / RAW 统一使用
        checked = f.full_path in self._checked
        badge = CheckBadge(cell, checked=checked,
                           on_toggle=lambda p=f.full_path: self._toggle_checked(p))
        badge.place(relx=1.0, x=-4, y=3, anchor="ne")

        for widget in (cell, img_label, raw_box, name_label):
            if widget is None:
                continue
            # 单击：高亮列表 + 显示 EXIF；双击：打开资源管理器定位
            widget.bind("<Button-1>", lambda _e, p=f.full_path: self._on_thumb_click(p))
            widget.bind("<Double-1>",
                        lambda _e, p=f.full_path: self._on_thumb_double_click(p))
            # 滚轮直接绑定到每个控件（含空白间隙），保证任何位置都能滚动
            widget.bind("<MouseWheel>", self._on_preview_wheel)
        # 悬停高亮（仅绑定在单元格上，开销极小）
        cell.bind("<Enter>", lambda _e, c=cell: self._hover_cell(c, True))
        cell.bind("<Leave>", lambda _e, c=cell: self._hover_cell(c, False))

        self._preview_items[f.full_path] = {
            "cell": cell, "img_label": img_label, "raw_box": raw_box,
            "photo": None, "badge": badge, "name_label": name_label,
        }

    def _apply_check_style(self, path: str, item: dict, checked: bool):
        """刷新预览单元的勾选外观：角标状态 + 未勾选时弱化文件名。"""
        badge = item.get("badge")
        if badge is not None:
            try:
                badge.set_checked(checked)
            except tk.TclError:
                pass
        name = item.get("name_label")
        if name is not None:
            try:
                name.configure(fg=UI["text"] if checked else UI["muted"])
            except tk.TclError:
                pass
        cell = item.get("cell")
        if cell is not None and self._hl_path != path:
            try:
                cell.configure(highlightbackground=UI["border"], highlightthickness=1)
            except tk.TclError:
                pass

    @staticmethod
    def _hover_cell(cell, on: bool):
        """预览单元悬停高亮：切换底色（子控件同步，避免留白突兀）。"""
        bg = UI["cell_hover"] if on else UI["cell"]
        try:
            cell.configure(bg=bg)
            for child in cell.winfo_children():
                if not isinstance(child, tk.Canvas):  # RAW 占位框保持自身底色
                    child.configure(bg=bg)
        except tk.TclError:
            pass

    @staticmethod
    def _short_name(name: str, size: int = 200) -> str:
        """按单元格宽度截断文件名（网格布局下保持一行显示）。"""
        max_chars = max(6, size // 8)
        if len(name) <= max_chars:
            return name
        return name[:max_chars // 2] + "…" + name[-max_chars // 2:]

    def _on_size_slider(self, _value=None):
        """缩略图大小滑块：自动吸附档位；拖动过程中不重建（防抖 250ms），
        生效时仅对缓存的缩略图等比缩放，不重新解码图片。"""
        idx = max(0, min(len(self.THUMB_LEVELS) - 1,
                         int(round(float(self.thumb_level_var.get())))))
        if float(self.thumb_level_var.get()) != idx:
            # 吸附：把滑块值对齐到最近的整数档位（set 后 command 再次触发，
            # 此时值已相同、档位未变，自然停止，不会递归）
            self.thumb_level_var.set(idx)
        level = self.THUMB_LEVELS[idx]
        if level == self._thumb_level:
            return
        self._thumb_level = level
        self.size_label.configure(text=self._size_label_text())
        # 防抖：快速拖动时只更新档位，停顿 250ms 后才执行一次缩放重绘，
        # 避免频繁重建导致的层叠/变形与卡顿
        if self._size_job is not None:
            try:
                self.after_cancel(self._size_job)
            except tk.TclError:
                pass
        self._size_job = self.after(250, self._apply_size_to_cells)

    def _apply_size_to_cells(self):
        """档位切换生效：整体重建预览网格——卡片（图片/边框/间距/文件名区）
        与 RAW 占位框等比缩放到新档位，文件名始终完整可见。
        图片全部来自缓存等比缩放（并行），不重新解码。"""
        self._size_job = None
        if self._closing or self.busy:
            return
        self._refresh_preview()

    def _on_preview_canvas_resize(self, event):
        """窗口大小变化：防抖后重建网格（排列与缩略图尺寸自动适应）。"""
        if event.width == self._last_canvas_width:
            return
        self._last_canvas_width = event.width
        if self._resize_job is not None:
            try:
                self.after_cancel(self._resize_job)
            except tk.TclError:
                pass
        self._resize_job = self.after(400, self._on_resize_settled)

    def _on_resize_settled(self):
        """窗口尺寸稳定后重建预览网格。"""
        self._resize_job = None
        if self._closing or self.busy:
            return
        if self.orphans and self._preview_targets():
            self._refresh_preview()

    def _thumb_worker(self, paths, token):
        """
        并行解码：ThreadPoolExecutor 多线程解码生成 120px 最小档缩略图并缓存，
        实时回传缩略图（预览区逐张出现即为进度反馈）。
        （PIL 的 libjpeg 解码会释放 GIL，多线程即可利用多核；
        不用进程池——PyInstaller onefile 下子进程启动开销大，且图片需回传
        主线程创建 PhotoImage，进程间序列化开销大。）
        EXIF 不在此阶段读取：改为单击照片时按需懒加载，降低扫描性能开销。
        注意：不得在此更新主状态栏——扫描已完成，状态栏应保持"扫描完成"，
        大批量缩略图生成时用预览状态条显示进度即可。
        """
        ok = fail = 0
        total = len(paths)
        workers = min(16, max(2, int((os.cpu_count() or 4) * 1.5)))  # 自适应并发数
        with ThreadPoolExecutor(max_workers=workers) as pool:
            futures = {pool.submit(self._decode_thumb, p): p for p in paths}
            for fut in as_completed(futures):
                if token != self._preview_token:
                    return  # 列表已刷新，旧任务作废
                path = futures[fut]
                try:
                    im = fut.result()
                except Exception:
                    fail += 1  # 无法解码（损坏或并非有效图片）：跳过
                    continue
                ok += 1
                self._ui_queue.put((self._on_thumb_ready, (path, im, token)))
        self._ui_queue.put((self._preview_finish, (token, ok, fail)))

    def _decode_thumb(self, path):
        """（工作线程）解码并生成 120px 最小档缩略图（EXIF 懒加载，不在此读取）。
        使用 with 打开并在完成后返回【独立内存副本 .copy()】：
        原 Image 对象随 with 退出自动关闭，不残留任何文件句柄，
        避免占用 JPG 文件导致后续删除失败。"""
        with Image.open(path) as src:
            if src.mode not in ("RGB", "L"):
                src = src.convert("RGB")
            small = self.THUMB_SIZES["小"]  # 统一缓存最小档
            try:
                # reducing_gap：JPEG 按缩略比例抽帧解码（低质量、快、省内存）
                src.thumbnail((small, small), RESAMPLE_LANCZOS, reducing_gap=3.0)
            except (TypeError, ValueError):
                src.thumbnail((small, small), RESAMPLE_LANCZOS)
            src.load()  # 确保像素已读入内存
            return src.copy()  # 独立内存副本（无文件句柄），原对象随 with 关闭

    def _on_thumb_ready(self, path, im, token):
        """主线程：缓存 120px 缩略图，并按当前档位等比缩放显示。"""
        if self._closing or token != self._preview_token:
            im.close()
            return
        self._thumb_cache[path] = im  # 最小档缓存（后续切换档位/模式不再解码）
        # 按当前档位等比缩放显示（120px→目标档位，单张主线程缩放开销极小）
        size = self.THUMB_SIZES[self._thumb_level]
        w, h = im.size
        target = (size, max(1, round(size * h / w)))  # 保持原始宽高比
        try:
            resized = im.resize(target, RESAMPLE_LANCZOS)
        except Exception:
            resized = im
        self._display_thumb(path, resized)

    def _resize_worker(self, paths, token, size):
        """（工作线程）并行对已缓存的 120px 缩略图等比缩放，不重新解码图片。"""
        workers = min(16, max(2, int((os.cpu_count() or 4) * 1.5)))

        def _one(path):
            if token != self._resize_token:
                return None  # 档位/模式已再次切换，旧任务作废
            im = self._thumb_cache.get(path)
            if im is None:
                return None
            try:
                w, h = im.size
                target = (size, max(1, round(size * h / w)))  # 保持原始宽高比
                return path, im.resize(target, RESAMPLE_LANCZOS)
            except Exception:
                return None

        with ThreadPoolExecutor(max_workers=workers) as pool:
            for result in pool.map(_one, paths):
                if result is None:
                    continue
                p, im = result
                if token != self._resize_token:
                    im.close()
                    return
                self._ui_queue.put((self._on_thumb_resized, (p, im, token)))

    def _on_thumb_resized(self, path, im, token):
        """主线程：接收档位缩放结果并显示（旧档位结果自动丢弃）。"""
        if self._closing or token != self._resize_token:
            im.close()
            return
        self._display_thumb(path, im)

    def _display_thumb(self, path, im):
        """（主线程）把 PIL 图像转为 tkinter 图片并填入对应单元格。
        勾选角标是独立的小画布（网点半透明底 + 实色勾），不修改图片本身。"""
        item = self._preview_items.get(path)
        if item is None or item["img_label"] is None:
            im.close()
            return
        try:
            photo = ImageTk.PhotoImage(im)
        except Exception:
            im.close()
            return
        im.close()
        item["photo"] = photo  # 单元格持有引用（替换时旧图自动释放，降低内存占用）
        item["img_label"].configure(image=photo, text="")  # 等比居中显示


    def _preview_finish(self, token, ok, fail):
        if self._closing or token != self._preview_token:
            return
        # 固定状态条（不随内容滚动）：显示统计与操作提示
        self._preview_status = ("done", ok, fail)
        text = self.t("preview_status_done", ok=ok,
                      fail=self.t("preview_status_fail", n=fail) if fail else "")
        self.preview_status_bar.configure(text=text)

    def _on_thumb_click(self, full_path: str):
        """预览条目单击：高亮列表对应行并同步显示 EXIF（预览 -> 列表联动）。"""
        iid = self._tree_iid_by_path.get(full_path)
        if iid:
            try:
                self.tree.selection_set(iid)
                self.tree.see(iid)
                self.tree.focus(iid)
            except tk.TclError:
                pass
            self._set_picked_row(iid)
        self._highlight_preview(full_path)
        self._show_exif(full_path)

    def _row_tags(self, iid):
        """行标签：隔行底色 + 未勾选弱化 + 当前选中高亮。"""
        try:
            idx = self.tree.index(iid)
        except tk.TclError:
            return ("even",)
        tags = ["odd" if idx % 2 else "even"]
        path = self._iid_to_path.get(iid)
        if path and path not in self._checked:
            tags.append("off")
        if iid == self._picked_iid:
            tags.append("picked")
        return tuple(tags)

    def _set_picked_row(self, iid):
        """刷新"当前选中行"高亮（只更新上一个与当前行，长列表也零负担）。"""
        prev, self._picked_iid = self._picked_iid, iid
        for target in (prev, iid):
            if target:
                try:
                    self.tree.item(target, tags=self._row_tags(target))
                except tk.TclError:
                    pass

    def _refresh_row_tags(self, iid):
        try:
            self.tree.item(iid, tags=self._row_tags(iid))
        except tk.TclError:
            pass

    def _on_thumb_double_click(self, full_path: str):
        """预览条目双击：打开资源管理器并定位该文件（与列表行双击行为一致）。"""
        self._reveal_in_explorer(full_path)

    def _show_exif(self, path: str):
        """在预览区右上角显示照片 EXIF 信息（懒加载：单击时才按需解析并缓存）。"""
        self._exif_current_path = path
        cached = self._exif_cache.get(path)
        if cached:
            self.exif_var.set(self._render_exif(cached))
            return
        threading.Thread(target=self._exif_worker, args=(path,), daemon=True).start()

    def _exif_worker(self, path):
        """（工作线程）按需读取该文件的 EXIF（JPG 走 Pillow，RAW 走轻量 TIFF 解析）。"""
        data = read_photo_exif(path)
        self._ui_queue.put((self._on_exif_ready, (path, data)))

    def _on_exif_ready(self, path, data):
        if self._closing:
            return
        if data:
            self._exif_cache[path] = data  # 结构化缓存，简略/详细与中英文共用
            if path == self._exif_current_path:
                self.exif_var.set(self._render_exif(data))
        else:
            if path == self._exif_current_path:
                self.exif_var.set(self.t("exif_fail"))

    def _bind_preview_wheel(self, widget):
        """给预览区控件直接绑定滚轮滚动（含空白区域，不依赖 Enter/Leave 切换）。"""
        widget.bind("<MouseWheel>", self._on_preview_wheel)

    def _on_preview_wheel(self, event):
        # 预览区垂直滚动（绑定在预览区所有控件上，任何位置都有效）
        self.preview_canvas.yview_scroll(int(-event.delta / 120), "units")

    # ----- 关于与退出 -----

    def _show_about(self):
        """
        关于对话框：自定义 Toplevel 窗口（不会触发 Windows 系统通知音）。
        文字可选中复制；开发者链接可直接点击打开网页；Esc 或"关闭"按钮可关闭。
        内容渲染集中在 render() 中，语言切换时重新渲染（不留旧语言）。
        """
        if self._about_window is not None:
            try:
                if self._about_window.winfo_exists():
                    self._about_window.lift()
                    return
            except tk.TclError:
                pass
        about = tk.Toplevel(self)
        about.title(f"{self.t('about')} {self.t('app_title')}")
        about.resizable(False, False)
        about.transient(self)
        about.configure(bg=UI["card"])
        about.bind("<Escape>", lambda _e: self._close_about())
        about.protocol("WM_DELETE_WINDOW", self._close_about)
        about.grab_set()  # 模态：关闭前主窗口不可操作

        w, h = 640, 660  # 显示面积加大（含作者/许可/宣传链接）
        self.update_idletasks()
        x = self.winfo_rootx() + max(0, (self.winfo_width() - w) // 2)
        y = self.winfo_rooty() + max(0, (self.winfo_height() - h) // 2)
        about.geometry(f"{w}x{h}+{x}+{y}")

        # 只读文本框：内容可选中、Ctrl+C 复制
        text = tk.Text(about, wrap="word", bg=UI["card"], relief=tk.FLAT,
                       font=(self._font_family, 11), padx=18, pady=14,
                       highlightthickness=0, cursor="arrow", fg=UI["text"],
                       insertbackground=UI["text"])
        text.pack(fill=tk.BOTH, expand=True, padx=16, pady=(18, 8))
        close_btn = PillButton(about, text=self.t("about_close"), style="primary",
                               bold=True, command=self._close_about)
        close_btn.pack(pady=(0, 16))
        close_btn.focus_set()

        def render():
            """（重新）渲染关于内容：语言/主题切换时调用，保持与当前语言一致。"""
            about.title(f"{self.t('about')} {self.t('app_title')}  ·  {APP_AUTHOR}")
            close_btn.configure(text=self.t("about_close"))
            content = (
                f"{self.t('app_title')}  v{APP_VERSION}\n"
                f"{self.t('about_author')}{self.t('field_sep')}{APP_AUTHOR}\n"
                f"{self.t('about_copyright')}{self.t('field_sep')}{APP_COPYRIGHT}\n"
                f"{self.t('about_license')}{self.t('field_sep')}{APP_LICENSE}\n"
                f"GitHub{self.t('field_sep')}{GITHUB_URL}\n"
                f"bilibili{self.t('field_sep')}{BILIBILI_URL}\n"
                f"{self.t('about_project')}{self.t('field_sep')}{PROJECT_URL}\n\n"
                f"{self.t('about_thanks')}\n\n"
                f"{self.t('about_changelog')}{self.t('field_sep')}\n"
                + "\n".join(self.t(f"changelog_{v}") for v in CHANGELOG_VERSIONS)
                + "\n\n"
                + self.t("free_statement") + "\n"
            )
            text.configure(state="normal")
            text.delete("1.0", tk.END)
            text.insert("1.0", content)
            text.configure(state="disabled")  # 只读（仍可选中复制）
            text.configure(bg=UI["card"], fg=UI["text"])
            about.configure(bg=UI["card"])

            # GitHub / bilibili / 项目地址：主题色下划线、手型光标、点击打开
            text.tag_remove("link", "1.0", tk.END)
            for url in (GITHUB_URL, BILIBILI_URL, PROJECT_URL):
                pos = content.find(url)
                if pos >= 0:
                    text.tag_add("link", f"1.0+{pos}c", f"1.0+{pos + len(url)}c")
            text.tag_configure("link", foreground=UI["accent"], underline=True)
            text.tag_bind("link", "<Enter>", lambda _e: text.configure(cursor="hand2"))
            text.tag_bind("link", "<Leave>", lambda _e: text.configure(cursor="arrow"))

            # 免费开源声明：与正文区分（主题色）
            text.tag_remove("free", "1.0", tk.END)
            pos = content.find(self.t("free_statement"))
            if pos >= 0:
                text.tag_add("free", f"1.0+{pos}c",
                             f"1.0+{pos + len(self.t('free_statement'))}c")
            text.tag_configure("free", foreground=UI["accent"])

        def _on_link_click(event):
            index = text.index(f"@{event.x},{event.y}")
            line_start = text.index(f"{index} linestart")
            line = text.get(line_start, f"{line_start} lineend")
            for url in (GITHUB_URL, BILIBILI_URL, PROJECT_URL):
                if url in line:
                    webbrowser.open(url)
                    break

        text.tag_bind("link", "<Button-1>", _on_link_click)
        self._about_window = about
        self._about_render = render
        render()

    def _relabel_about_window(self):
        """关于窗口打开时，语言切换同步重译其内容。"""
        win = self._about_window
        if win is None:
            return
        try:
            if not win.winfo_exists():
                self._about_window = None
                return
            if callable(self._about_render):
                self._about_render()
        except tk.TclError:
            self._about_window = None

    def _close_about(self):
        win = self._about_window
        self._about_window = None
        if win is not None:
            try:
                win.destroy()
            except tk.TclError:
                pass

    def _maybe_show_first_about(self):
        """首次成功删除后延迟弹出的感谢"关于"（窗口已关闭则跳过）。"""
        if not self._closing:
            self._show_about()

    def _on_close(self):
        if self.busy:
            messagebox.showwarning(self.t("about"), self.t("msg_busy"), parent=self)
            return
        self._save_config_now()
        self._closing = True
        # 取消待执行的 after 回调（轮询/防抖/分隔条恢复/滑块防抖），避免销毁后 Tcl 报错
        for job in (self._poller_after_id, self._resize_job, self._size_job,
                    self._restore_sash_job):
            if job is not None:
                try:
                    self.after_cancel(job)
                except Exception:
                    pass
        self.destroy()


    def destroy(self):
        """销毁窗口前统一解除挂起的 after 任务，避免 Tcl 报"invalid command name"
        （无论走 _on_close 还是被程序化销毁都安全）。"""
        self._closing = True
        for job in (getattr(self, "_poller_after_id", None),
                    getattr(self, "_resize_job", None),
                    getattr(self, "_size_job", None),
                    getattr(self, "_restore_sash_job", None)):
            if job is not None:
                try:
                    self.after_cancel(job)
                except Exception:
                    pass
        self._poller_after_id = self._resize_job = self._size_job = None
        self._restore_sash_job = None
        super().destroy()


def _selftest(folder: str, report: str = None) -> int:
    """打包自检（仅诊断用，不影响正常使用）：扫描文件夹并验证依赖是否可用。
    用法：Jpg-Raw-Pair-Cleaner.exe --selftest <文件夹> [报告文件]
    用于确认裁剪打包体积后 JPEG 解码 / EXIF 读取 / RAW 解析仍然正常。"""
    out = []

    def log(msg):
        out.append(str(msg))
        print(msg)

    ok = True
    try:
        log(f"{APP_NAME} {APP_VERSION} | {APP_COPYRIGHT} | {APP_LICENSE}")
        log(f"project: {PROJECT_URL}")
        log(f"PIL: {'ok' if PILLOW_AVAILABLE else 'MISSING'}")
        log(f"exifread: {'ok' if EXIFREAD_AVAILABLE else 'MISSING (fallback used)'}")
        log(f"send2trash: {'ok' if SEND2TRASH_AVAILABLE else 'MISSING (shell API used)'}")
        log(f"languages: {len(LANG_CODES)} ({', '.join(LANG_CODES)})")
        log(f"system language: {detect_system_language()} / system dark: {detect_system_dark()}")
        log(f"brands: {len(BRANDS)} (e.g. zh-CN: {brand_display(BRANDS[0], 'zh-CN')} | "
            f"en: {brand_display(BRANDS[0], 'en')} | ja: {brand_display(BRANDS[0], 'ja')})")
        log(f"ui font: {ui_font_family()}")
        lang_data = _load_lang_data()
        missing = {c: len([k for k in lang_data['en'] if k not in lang_data[c]])
                   for c in LANG_CODES}
        log(f"language.json keys: {len(lang_data['en'])}; missing per language: {missing}")
        if not PILLOW_AVAILABLE:
            ok = False
        if not os.path.isdir(folder):
            log(f"ERROR: not a folder: {folder}")
            ok = False
        else:
            res = scan_folder(folder, True, set(), 0)
            log(f"scan: orphans={len(res.orphans)} paired={res.paired_base_count} "
                f"detected={sorted(res.detected_raw)}")
            names = sorted(os.listdir(folder))
            jpgs = [f.full_path for f in res.orphans if f.ext == "JPG"] or [
                os.path.join(folder, n) for n in names
                if n.lower().endswith((".jpg", ".jpeg"))]
            raws = [f.full_path for f in res.orphans if f.ext == "RAW"] or [
                os.path.join(folder, n) for n in names
                if os.path.splitext(n)[1].lower() in ALL_KNOWN_RAW_EXTS]
            if jpgs and PILLOW_AVAILABLE:
                with Image.open(jpgs[0]) as im:
                    im.thumbnail((120, 120), RESAMPLE_LANCZOS)
                    im.load()
                    log(f"jpeg decode: ok size={im.size} mode={im.mode}")
                data = read_photo_exif(jpgs[0])
                log(f"jpg exif: fields={len(data) if data else 0}")
            if raws:
                data = read_photo_exif(raws[0])
                log(f"raw exif: fields={len(data) if data else 0} "
                    f"resolution={data.get('resolution') if data else None}")
    except Exception as exc:
        ok = False
        log(f"ERROR: {exc!r}")
    log("RESULT: " + ("OK" if ok else "FAIL"))
    if report:
        try:
            with open(report, "w", encoding="utf-8") as f:
                f.write("\n".join(out) + "\n")
        except OSError:
            pass
    return 0 if ok else 1


def main():
    # 打包自检模式（仅诊断用；正常双击运行不带参数，直接进入图形界面）
    argv = sys.argv[1:]
    if argv and argv[0] in ("--version", "-V"):
        print(f"{APP_NAME} {APP_VERSION}")
        print(f"Author: {APP_AUTHOR}")
        print(f"Copyright: {APP_COPYRIGHT}")
        print(f"License: {APP_LICENSE}")
        print(f"Project: {PROJECT_URL}")
        print(f"GitHub: {GITHUB_URL}")
        print(f"bilibili: {BILIBILI_URL}")
        return
    if argv and argv[0] == "--selftest":
        sys.exit(_selftest(argv[1] if len(argv) > 1 else ".",
                          argv[2] if len(argv) > 2 else None))
    if sys.platform == "win32":
        # 启用高 DPI 感知，避免高分屏下界面模糊
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except Exception:
            pass
    else:
        print("[警告] 回收站删除功能仅支持 Windows 系统。")
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()

# ============================================================================
# Watermark / 开源归属标识:
#   KILL-STAR SX · Jpg-Raw-Pair-Cleaner 5.1 · KS-ASL-1.0
#   https://github.com/KILLSTARSX/Jpg-Raw-Pair-Cleaner
# 本标识属于源码的一部分，请勿删除（KS-ASL-1.0 要求保留版权与许可声明）。
# ============================================================================
