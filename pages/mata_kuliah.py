import flet as ft

from components.card import section_card
from components.theme import Colors, FontSize, Spacing
from data.dummy_data import MATA_KULIAH, STUDENT


def mata_kuliah_page() -> ft.Control:
    mata_kuliah_semester = [
        item
        for item in MATA_KULIAH
        if item["semester"] == STUDENT["semester_aktif"]
    ]

    total_sks = sum(item["sks"] for item in mata_kuliah_semester)

    daftar_mata_kuliah = []

    for item in mata_kuliah_semester:
        daftar_mata_kuliah.append(
            ft.Container(
                content=ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.Text(
                                    item["kode"],
                                    size=FontSize.CAPTION,
                                    weight=ft.FontWeight.W_600,
                                    color=Colors.PRIMARY,
                                ),
                                ft.Text(
                                    f"{item['sks']} SKS",
                                    size=FontSize.CAPTION,
                                    color=Colors.TEXT_SECONDARY,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        ft.Text(
                            item["nama"],
                            size=FontSize.BODY,
                            weight=ft.FontWeight.W_600,
                            color=Colors.TEXT_PRIMARY,
                        ),
                        ft.Text(
                            item["dosen"],
                            size=FontSize.CAPTION,
                            color=Colors.TEXT_SECONDARY,
                        ),
                    ],
                    spacing=Spacing.XS,
                ),
                padding=Spacing.MD,
                border=ft.Border.all(1, Colors.BORDER),
                border_radius=8,
            )
        )

    return ft.Column(
        controls=[
            ft.Text(
                "Mata Kuliah",
                size=FontSize.HEADLINE,
                weight=ft.FontWeight.BOLD,
                color=Colors.TEXT_PRIMARY,
            ),
            ft.Text(
                f"Daftar mata kuliah semester {STUDENT['semester_aktif']}.",
                size=FontSize.BODY,
                color=Colors.TEXT_SECONDARY,
            ),
            ft.Text(
                f"{len(mata_kuliah_semester)} mata kuliah • {total_sks} SKS",
                size=FontSize.BODY,
                weight=ft.FontWeight.W_600,
                color=Colors.TEXT_PRIMARY,
            ),
            section_card(
                "Daftar Mata Kuliah",
                ft.Column(
                    controls=daftar_mata_kuliah,
                    spacing=Spacing.SM,
                ),
            ),
        ],
        spacing=Spacing.LG,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
    )