import flet as ft

from components.avatar import avatar
from components.badge import badge
from components.card import card, section_card
from components.page_title import page_title
from components.theme import Colors, FontSize, Radius, Spacing
from data.dummy_data import STUDENT


def _profile_summary() -> ft.Container:
    return card(
        ft.Column(
            controls=[
                avatar(STUDENT["nama"], radius=48),
                ft.Text(STUDENT["nama"], size=FontSize.TITLE, weight=ft.FontWeight.BOLD, color=Colors.TEXT_PRIMARY),
                ft.Text(STUDENT["nim"], size=FontSize.BODY, color=Colors.TEXT_SECONDARY),
                badge("Mahasiswa Aktif", Colors.SUCCESS, Colors.SUCCESS_LIGHT),
            ],
            spacing=Spacing.SM,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        expand=1,
    )


def _info_row(icon, label: str, value: str) -> ft.Container:
    return ft.Container(
        content=ft.Row(
            controls=[
                ft.Container(
                    content=ft.Icon(icon, size=20, color=Colors.PRIMARY),
                    width=40,
                    height=40,
                    bgcolor=Colors.PRIMARY_LIGHT,
                    border_radius=Radius.MD,
                    alignment=ft.Alignment.CENTER,
                ),
                ft.Column(
                    controls=[
                        ft.Text(label, size=FontSize.CAPTION, color=Colors.TEXT_SECONDARY),
                        ft.Text(value, size=FontSize.BODY, weight=ft.FontWeight.W_600, color=Colors.TEXT_PRIMARY),
                    ],
                    spacing=2,
                ),
            ],
            spacing=Spacing.MD,
        ),
        padding=ft.Padding.symmetric(vertical=Spacing.SM),
        border=ft.Border.only(bottom=ft.BorderSide(1, Colors.BORDER)),
    )


def profile_page() -> ft.Control:
    info = section_card(
        "Informasi Mahasiswa",
        ft.Column(
            controls=[
                _info_row(ft.Icons.PERSON_OUTLINE, "Nama Lengkap", STUDENT["nama"]),
                _info_row(ft.Icons.BADGE_OUTLINED, "NIM", STUDENT["nim"]),
                _info_row(ft.Icons.SCHOOL_OUTLINED, "Program Studi", STUDENT["program_studi"]),
                _info_row(ft.Icons.APARTMENT_OUTLINED, "Fakultas", STUDENT["fakultas"]),
                _info_row(ft.Icons.EMAIL_OUTLINED, "Email", STUDENT["email"]),
                _info_row(ft.Icons.CALENDAR_TODAY_OUTLINED, "Angkatan", STUDENT["angkatan"]),
            ],
            spacing=0,
        ),
        expand=2,
    )
    return ft.Column(
        controls=[
            page_title("Profile", "Informasi data diri mahasiswa"),
            ft.Row(
                controls=[_profile_summary(), info],
                spacing=Spacing.MD,
                vertical_alignment=ft.CrossAxisAlignment.START,
            ),
        ],
        spacing=Spacing.LG,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
    )
