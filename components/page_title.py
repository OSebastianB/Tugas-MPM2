import flet as ft

from components.theme import Colors, FontSize


def page_title(title: str, subtitle: str = "") -> ft.Column:
    return ft.Column(
        controls=[
            ft.Text(title, size=FontSize.HEADLINE, weight=ft.FontWeight.BOLD, color=Colors.TEXT_PRIMARY),
            ft.Text(subtitle, size=FontSize.BODY, color=Colors.TEXT_SECONDARY, visible=bool(subtitle)),
        ],
        spacing=4,
    )
