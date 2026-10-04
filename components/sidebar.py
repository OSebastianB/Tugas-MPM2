import flet as ft

from components.theme import SIDEBAR_WIDTH, Colors, FontSize, Radius, Spacing


def _brand() -> ft.Row:
    logo = ft.Container(
        content=ft.Icon(ft.Icons.SCHOOL, size=22, color=Colors.TEXT_ON_PRIMARY),
        width=40,
        height=40,
        bgcolor=Colors.PRIMARY,
        border_radius=Radius.MD,
        alignment=ft.Alignment.CENTER,
    )
    return ft.Row(
        controls=[
            logo,
            ft.Column(
                controls=[
                    ft.Text("Student", size=FontSize.SUBTITLE, weight=ft.FontWeight.BOLD, color=Colors.TEXT_PRIMARY),
                    ft.Text("Academic Dashboard", size=FontSize.CAPTION, color=Colors.TEXT_SECONDARY),
                ],
                spacing=0,
            ),
        ],
        spacing=Spacing.SM + 4,
    )


def _nav_item(label: str, icon, selected: bool, on_click) -> ft.Container:
    color = Colors.PRIMARY if selected else Colors.TEXT_SECONDARY
    return ft.Container(
        content=ft.Row(
            controls=[
                ft.Icon(icon, size=20, color=color),
                ft.Text(
                    label,
                    size=FontSize.BODY,
                    color=color,
                    weight=ft.FontWeight.W_600 if selected else ft.FontWeight.W_500,
                ),
            ],
            spacing=Spacing.SM + 4,
        ),
        padding=ft.Padding.symmetric(horizontal=Spacing.MD, vertical=Spacing.SM + 4),
        bgcolor=Colors.PRIMARY_LIGHT if selected else None,
        border_radius=Radius.MD,
        ink=True,
        on_click=on_click,
    )


def sidebar(items: list[tuple[str, object]], selected_index: int, on_navigate) -> ft.Container:
    """`items` berisi (label, icon). `on_navigate(index)` dipanggil saat menu diklik."""
    menu = ft.Column(
        controls=[
            _nav_item(label, icon, index == selected_index, lambda e, i=index: on_navigate(i))
            for index, (label, icon) in enumerate(items)
        ],
        spacing=Spacing.XS,
    )
    return ft.Container(
        content=ft.Column(
            controls=[
                _brand(),
                ft.Container(height=Spacing.MD),
                ft.Text("MENU", size=FontSize.CAPTION, weight=ft.FontWeight.W_600, color=Colors.TEXT_SECONDARY),
                menu,
            ],
            spacing=Spacing.SM,
        ),
        width=SIDEBAR_WIDTH,
        padding=Spacing.LG,
        bgcolor=Colors.SURFACE,
        border=ft.Border.only(right=ft.BorderSide(1, Colors.BORDER)),
    )
