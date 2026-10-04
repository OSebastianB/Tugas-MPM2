import flet as ft

from components.theme import CARD_SHADOW, Colors, FontSize, Radius, Spacing


def card(content: ft.Control, padding: int = Spacing.LG, expand=None) -> ft.Container:
    return ft.Container(
        content=content,
        padding=padding,
        bgcolor=Colors.SURFACE,
        border=ft.Border.all(1, Colors.BORDER),
        border_radius=Radius.LG,
        shadow=CARD_SHADOW,
        expand=expand,
    )


def section_card(title: str, content: ft.Control, icon=None, expand=None) -> ft.Container:
    title_row = ft.Row(
        controls=[
            *([ft.Icon(icon, size=20, color=Colors.PRIMARY)] if icon else []),
            ft.Text(title, size=FontSize.SUBTITLE, weight=ft.FontWeight.W_600, color=Colors.TEXT_PRIMARY),
        ],
        spacing=Spacing.SM,
    )
    return card(
        ft.Column(controls=[title_row, content], spacing=Spacing.MD),
        expand=expand,
    )
