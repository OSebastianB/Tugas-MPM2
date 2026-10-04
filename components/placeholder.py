import flet as ft

from components.card import card
from components.page_title import page_title
from components.theme import Colors, FontSize, Radius, Spacing


def placeholder_page(title: str) -> ft.Column:
    """Halaman sementara untuk menu yang masih dikerjakan anggota lain."""
    message = ft.Column(
        controls=[
            ft.Container(
                content=ft.Icon(ft.Icons.CONSTRUCTION_OUTLINED, size=32, color=Colors.PRIMARY),
                width=64,
                height=64,
                bgcolor=Colors.PRIMARY_LIGHT,
                border_radius=Radius.LG,
                alignment=ft.Alignment.CENTER,
            ),
            ft.Text("Halaman sedang dikembangkan", size=FontSize.SUBTITLE, weight=ft.FontWeight.W_600, color=Colors.TEXT_PRIMARY),
            ft.Text(
                f"Konten halaman {title} akan segera tersedia.",
                size=FontSize.BODY,
                color=Colors.TEXT_SECONDARY,
            ),
        ],
        spacing=Spacing.SM,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
    return ft.Column(
        controls=[
            page_title(title),
            card(ft.Container(content=message, padding=Spacing.XL, alignment=ft.Alignment.CENTER)),
        ],
        spacing=Spacing.LG,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
    )
