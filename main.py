import flet as ft

from components.header import header
from components.placeholder import placeholder_page
from components.sidebar import sidebar
from components.theme import Colors, Spacing, app_theme
from data.dummy_data import STUDENT
from pages.dashboard import dashboard_page

# (label menu, icon, function halaman). Tambah menu baru cukup di sini.
# Ganti placeholder_page dengan function halaman asli saat sudah tersedia.
PAGES = [
    ("Dashboard", ft.Icons.DASHBOARD_OUTLINED, dashboard_page),
    ("Mata Kuliah", ft.Icons.MENU_BOOK_OUTLINED, lambda: placeholder_page("Mata Kuliah")),
    ("Nilai", ft.Icons.GRADING_OUTLINED, lambda: placeholder_page("Nilai")),
    ("Profile", ft.Icons.PERSON_OUTLINE, lambda: placeholder_page("Profile")),
]


def main(page: ft.Page):
    page.title = "Student Academic Dashboard"
    page.theme = app_theme()
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = Colors.BACKGROUND
    page.padding = 0
    page.window.width = 1280
    page.window.height = 820
    page.window.min_width = 1024
    page.window.min_height = 640

    menu_items = [(label, icon) for label, icon, _ in PAGES]
    sidebar_slot = ft.Container()
    content_slot = ft.Container(padding=Spacing.XL)

    def navigate(index: int):
        sidebar_slot.content = sidebar(menu_items, index, navigate)
        content_slot.content = PAGES[index][2]()
        page.update()

    page.add(
        ft.Row(
            controls=[
                sidebar_slot,
                ft.Column(
                    controls=[
                        header(STUDENT),
                        ft.Column(
                            controls=[content_slot],
                            scroll=ft.ScrollMode.AUTO,
                            expand=True,
                            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                        ),
                    ],
                    spacing=0,
                    expand=True,
                ),
            ],
            spacing=0,
            expand=True,
            vertical_alignment=ft.CrossAxisAlignment.STRETCH,
        )
    )
    navigate(0)


if __name__ == "__main__":
    ft.run(main)
