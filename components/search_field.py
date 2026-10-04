import flet as ft

from components.theme import Colors, FontSize, Radius, Spacing

INPUT_BORDER = ft.OutlineInputBorder(side=ft.BorderSide(1, Colors.BORDER), border_radius=Radius.MD)


def search_field(hint: str, on_change, width: int | None = None, expand=None) -> ft.TextField:
    return ft.TextField(
        hint_text=hint,
        prefix_icon=ft.Icons.SEARCH,
        on_change=on_change,
        width=width,
        expand=expand,
        height=44,
        text_size=FontSize.BODY,
        bgcolor=Colors.SURFACE,
        filled=True,
        fill_color=Colors.SURFACE,
        border=INPUT_BORDER,
        content_padding=ft.Padding.symmetric(horizontal=Spacing.MD, vertical=Spacing.SM),
    )


def filter_dropdown(label: str, options: list[str], value: str, on_select, width: int = 200) -> ft.Dropdown:
    return ft.Dropdown(
        label=label,
        value=value,
        options=[ft.DropdownOption(key=option, text=option) for option in options],
        on_select=on_select,
        width=width,
        text_size=FontSize.BODY,
        bgcolor=Colors.SURFACE,
        filled=True,
        fill_color=Colors.SURFACE,
        border=INPUT_BORDER,
        dense=True,
    )
