from datetime import date

import flet as ft

from components.avatar import avatar
from components.theme import Colors, FontSize, Spacing

HARI = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
BULAN = [
    "Januari", "Februari", "Maret", "April", "Mei", "Juni",
    "Juli", "Agustus", "September", "Oktober", "November", "Desember",
]


def format_tanggal(value: date) -> str:
    return f"{HARI[value.weekday()]}, {value.day} {BULAN[value.month - 1]} {value.year}"


def header(student: dict) -> ft.Container:
    left = ft.Column(
        controls=[
            ft.Text(student["periode"], size=FontSize.SUBTITLE, weight=ft.FontWeight.W_600, color=Colors.TEXT_PRIMARY),
            ft.Text(format_tanggal(date.today()), size=FontSize.CAPTION, color=Colors.TEXT_SECONDARY),
        ],
        spacing=2,
    )
    user = ft.Row(
        controls=[
            ft.IconButton(icon=ft.Icons.NOTIFICATIONS_OUTLINED, icon_color=Colors.TEXT_SECONDARY, tooltip="Notifikasi"),
            ft.Container(width=1, height=32, bgcolor=Colors.BORDER),
            avatar(student["nama"], radius=18),
            ft.Column(
                controls=[
                    ft.Text(student["nama"], size=FontSize.BODY, weight=ft.FontWeight.W_600, color=Colors.TEXT_PRIMARY),
                    ft.Text(student["nim"], size=FontSize.CAPTION, color=Colors.TEXT_SECONDARY),
                ],
                spacing=0,
            ),
        ],
        spacing=Spacing.SM + 4,
    )
    return ft.Container(
        content=ft.Row(
            controls=[left, user],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=ft.Padding.symmetric(horizontal=Spacing.XL, vertical=Spacing.MD),
        bgcolor=Colors.SURFACE,
        border=ft.Border.only(bottom=ft.BorderSide(1, Colors.BORDER)),
    )
