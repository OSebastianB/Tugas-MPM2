import flet as ft

from components.card import card
from components.theme import Colors, FontSize, Radius, Spacing


def stat_card(icon, label: str, value: str, caption: str = "") -> ft.Container:
    icon_box = ft.Container(
        content=ft.Icon(icon, size=24, color=Colors.PRIMARY),
        width=48,
        height=48,
        bgcolor=Colors.PRIMARY_LIGHT,
        border_radius=Radius.MD,
        alignment=ft.Alignment.CENTER,
    )
    texts = ft.Column(
        controls=[
            ft.Text(label, size=FontSize.BODY, color=Colors.TEXT_SECONDARY),
            ft.Text(value, size=FontSize.DISPLAY, weight=ft.FontWeight.BOLD, color=Colors.TEXT_PRIMARY),
            ft.Text(
                caption,
                size=FontSize.CAPTION,
                color=Colors.TEXT_SECONDARY,
                visible=bool(caption),
                max_lines=1,
                overflow=ft.TextOverflow.ELLIPSIS,
            ),
        ],
        spacing=2,
        expand=True,
    )
    return card(
        ft.Row(controls=[texts, icon_box], vertical_alignment=ft.CrossAxisAlignment.START),
        expand=True,
    )
