from datetime import datetime

import flet as ft

from components.badge import badge
from components.card import section_card
from components.stat_card import stat_card
from components.theme import Colors, FontSize, Radius, Spacing
from data.dummy_data import JADWAL_HARI_INI, MATA_KULIAH, PENGUMUMAN, STUDENT, hitung_ipk, total_sks_lulus

STAT_CARD_COLUMNS = {"xs": 12, "md": 6, "xl": 3}


def _sapaan(jam: int) -> str:
    if jam < 11:
        return "Selamat pagi"
    if jam < 15:
        return "Selamat siang"
    if jam < 18:
        return "Selamat sore"
    return "Selamat malam"


def _mata_kuliah_semester_ini() -> list[dict]:
    return [mk for mk in MATA_KULIAH if mk["semester"] == STUDENT["semester_aktif"]]


def _welcome_badge(text: str) -> ft.Container:
    return badge(text, Colors.TEXT_ON_PRIMARY, ft.Colors.with_opacity(0.18, Colors.TEXT_ON_PRIMARY))


def _welcome_section() -> ft.Container:
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(
                    f"{_sapaan(datetime.now().hour)},",
                    size=FontSize.SUBTITLE,
                    color=ft.Colors.with_opacity(0.85, Colors.TEXT_ON_PRIMARY),
                ),
                ft.Text(
                    STUDENT["nama"],
                    size=FontSize.HEADLINE,
                    weight=ft.FontWeight.BOLD,
                    color=Colors.TEXT_ON_PRIMARY,
                ),
                ft.Text(
                    "Selamat datang kembali! Pantau jadwal, nilai, dan informasi akademik kamu di sini.",
                    size=FontSize.BODY,
                    color=ft.Colors.with_opacity(0.85, Colors.TEXT_ON_PRIMARY),
                ),
                ft.Container(height=Spacing.XS),
                ft.Row(
                    controls=[
                        _welcome_badge(f"NIM {STUDENT['nim']}"),
                        _welcome_badge(STUDENT["program_studi"]),
                    ],
                    spacing=Spacing.SM,
                    wrap=True,
                ),
            ],
            spacing=Spacing.XS,
        ),
        padding=Spacing.LG,
        bgcolor=Colors.PRIMARY,
        border_radius=Radius.LG,
    )


def _summary_card(icon, label: str, value: str, caption: str) -> ft.Container:
    card = stat_card(icon, label, value, caption)
    card.col = STAT_CARD_COLUMNS
    return card


def _academic_summary() -> ft.ResponsiveRow:
    return ft.ResponsiveRow(
        controls=[
            _summary_card(ft.Icons.AUTO_GRAPH, "IPK", f"{hitung_ipk():.2f}", "Skala 4.00"),
            _summary_card(ft.Icons.LIBRARY_BOOKS_OUTLINED, "Total SKS", str(total_sks_lulus()), "SKS telah ditempuh"),
            _summary_card(ft.Icons.CALENDAR_MONTH_OUTLINED, "Semester", str(STUDENT["semester_aktif"]), "Semester aktif"),
            _summary_card(
                ft.Icons.MENU_BOOK_OUTLINED,
                "Mata Kuliah",
                str(len(_mata_kuliah_semester_ini())),
                "Diambil semester ini",
            ),
        ],
        spacing=Spacing.MD,
        run_spacing=Spacing.MD,
    )


def _jadwal_meta(icon, text: str) -> ft.Row:
    return ft.Row(
        controls=[
            ft.Icon(icon, size=14, color=Colors.TEXT_SECONDARY),
            ft.Text(
                text,
                size=FontSize.CAPTION,
                color=Colors.TEXT_SECONDARY,
                max_lines=1,
                overflow=ft.TextOverflow.ELLIPSIS,
                expand=True,
            ),
        ],
        spacing=Spacing.XS,
    )


def _jadwal_item(item: dict) -> ft.Container:
    info = ft.Column(
        controls=[
            ft.Text(item["mata_kuliah"], size=FontSize.BODY, weight=ft.FontWeight.W_600, color=Colors.TEXT_PRIMARY),
            _jadwal_meta(ft.Icons.ROOM_OUTLINED, item["ruang"]),
            _jadwal_meta(ft.Icons.PERSON_OUTLINE, item["dosen"]),
        ],
        spacing=Spacing.XS,
        expand=True,
    )
    return ft.Container(
        content=ft.Row(
            controls=[
                ft.Container(
                    content=ft.Text(item["jam"], size=FontSize.CAPTION, weight=ft.FontWeight.W_600, color=Colors.PRIMARY),
                    width=110,
                ),
                info,
                badge(item["kode"]),
            ],
            spacing=Spacing.MD,
        ),
        padding=Spacing.MD,
        border=ft.Border.all(1, Colors.BORDER),
        border_radius=Radius.MD,
    )


def _pengumuman_item(item: dict) -> ft.Container:
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(item["judul"], size=FontSize.BODY, weight=ft.FontWeight.W_600, color=Colors.TEXT_PRIMARY),
                ft.Text(item["isi"], size=FontSize.CAPTION, color=Colors.TEXT_SECONDARY),
                ft.Text(item["tanggal"], size=FontSize.CAPTION, color=Colors.PRIMARY),
            ],
            spacing=Spacing.XS,
        ),
        padding=ft.Padding.only(left=Spacing.MD, top=Spacing.XS, bottom=Spacing.XS),
        border=ft.Border.only(left=ft.BorderSide(3, Colors.PRIMARY)),
    )


def _jadwal_list() -> ft.Control:
    if not JADWAL_HARI_INI:
        return ft.Text("Tidak ada jadwal kuliah hari ini.", size=FontSize.BODY, color=Colors.TEXT_SECONDARY)
    return ft.Column(controls=[_jadwal_item(item) for item in JADWAL_HARI_INI], spacing=Spacing.SM)


def dashboard_page() -> ft.Control:
    jadwal = section_card(
        "Jadwal Kuliah Hari Ini",
        _jadwal_list(),
        icon=ft.Icons.EVENT_NOTE_OUTLINED,
        expand=3,
    )
    pengumuman = section_card(
        "Pengumuman Akademik",
        ft.Column(controls=[_pengumuman_item(item) for item in PENGUMUMAN], spacing=Spacing.MD),
        icon=ft.Icons.CAMPAIGN_OUTLINED,
        expand=2,
    )
    return ft.Column(
        controls=[
            _welcome_section(),
            _academic_summary(),
            ft.Row(
                controls=[jadwal, pengumuman],
                spacing=Spacing.MD,
                vertical_alignment=ft.CrossAxisAlignment.START,
            ),
        ],
        spacing=Spacing.LG,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
    )
