"""Design tokens untuk seluruh aplikasi.

Semua warna, ukuran teks, spacing, dan radius diambil dari file ini.
Jika design system kelompok berubah, cukup sesuaikan nilai di sini.
"""

import flet as ft


class Colors:
    PRIMARY = "#2563EB"
    PRIMARY_LIGHT = "#EFF6FF"

    BACKGROUND = "#F8FAFC"
    SURFACE = "#FFFFFF"
    BORDER = "#E2E8F0"

    TEXT_PRIMARY = "#0F172A"
    TEXT_SECONDARY = "#64748B"
    TEXT_ON_PRIMARY = "#FFFFFF"

    SUCCESS = "#16A34A"
    SUCCESS_LIGHT = "#F0FDF4"
    WARNING = "#D97706"
    WARNING_LIGHT = "#FFFBEB"
    DANGER = "#DC2626"
    DANGER_LIGHT = "#FEF2F2"


class FontSize:
    CAPTION = 12
    BODY = 14
    SUBTITLE = 16
    TITLE = 20
    HEADLINE = 24
    DISPLAY = 28


class Spacing:
    XS = 4
    SM = 8
    MD = 16
    LG = 24
    XL = 32


class Radius:
    SM = 6
    MD = 10
    LG = 14
    FULL = 999


SIDEBAR_WIDTH = 240

CARD_SHADOW = ft.BoxShadow(
    blur_radius=12,
    spread_radius=0,
    color=ft.Colors.with_opacity(0.06, "#0F172A"),
    offset=ft.Offset(0, 2),
)


def app_theme() -> ft.Theme:
    return ft.Theme(color_scheme_seed=Colors.PRIMARY, use_material3=True)
