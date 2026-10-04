import flet as ft

from components.theme import Colors


def initials(name: str) -> str:
    return "".join(part[0] for part in name.split()[:2]).upper()


def avatar(name: str, radius: int = 20) -> ft.CircleAvatar:
    return ft.CircleAvatar(
        content=ft.Text(initials(name), size=radius * 0.7, weight=ft.FontWeight.W_600, color=Colors.TEXT_ON_PRIMARY),
        bgcolor=Colors.PRIMARY,
        radius=radius,
    )
