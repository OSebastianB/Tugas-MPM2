import flet as ft

from components.theme import Colors, FontSize, Radius, Spacing

GRADE_COLORS = {
    "A": (Colors.SUCCESS, Colors.SUCCESS_LIGHT),
    "AB": (Colors.SUCCESS, Colors.SUCCESS_LIGHT),
    "B": (Colors.PRIMARY, Colors.PRIMARY_LIGHT),
    "BC": (Colors.PRIMARY, Colors.PRIMARY_LIGHT),
    "C": (Colors.WARNING, Colors.WARNING_LIGHT),
    "D": (Colors.DANGER, Colors.DANGER_LIGHT),
    "E": (Colors.DANGER, Colors.DANGER_LIGHT),
}


def badge(text: str, color: str = Colors.PRIMARY, bgcolor: str = Colors.PRIMARY_LIGHT) -> ft.Container:
    return ft.Container(
        content=ft.Text(text, size=FontSize.CAPTION, weight=ft.FontWeight.W_600, color=color),
        padding=ft.Padding.symmetric(horizontal=Spacing.SM + 2, vertical=Spacing.XS),
        bgcolor=bgcolor,
        border_radius=Radius.FULL,
    )


def grade_badge(grade: str) -> ft.Container:
    color, bgcolor = GRADE_COLORS.get(grade, (Colors.TEXT_SECONDARY, Colors.BACKGROUND))
    return badge(grade, color, bgcolor)
