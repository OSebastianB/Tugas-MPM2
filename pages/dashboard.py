import flet as ft

from components.badge import badge
from components.card import section_card
from components.stat_card import stat_card
from components.theme import Colors, FontSize, Radius, Spacing
from data.dummy_data import JADWAL_HARI_INI, PENGUMUMAN, STUDENT, hitung_ipk, total_sks_lulus


def _welcome_section() -> ft.Container:
    nama_depan = STUDENT["nama"].split()[0]
    return ft.Container(
        content=ft.Column(
            controls=[
                ft.Text(
                    f"Selamat datang kembali, {nama_depan}!",
                    size=FontSize.HEADLINE,
                    weight=ft.FontWeight.BOLD,
                    color=Colors.TEXT_ON_PRIMARY,
                ),
                ft.Text(
                    f"{STUDENT['program_studi']} - {STUDENT['fakultas']}. "
                    "Pantau jadwal, nilai, dan informasi akademik kamu di sini.",
                    size=FontSize.BODY,
                    color=ft.Colors.with_opacity(0.85, Colors.TEXT_ON_PRIMARY),
                ),
            ],
            spacing=Spacing.XS,
        ),
        padding=Spacing.LG,
        bgcolor=Colors.PRIMARY,
        border_radius=Radius.LG,
    )


def _stat_cards() -> ft.Row:
    return ft.Row(
        controls=[
            stat_card(ft.Icons.AUTO_GRAPH, "IPK", f"{hitung_ipk():.2f}", "Skala 4.00"),
            stat_card(ft.Icons.LIBRARY_BOOKS_OUTLINED, "Total SKS", str(total_sks_lulus()), "SKS telah ditempuh"),
            stat_card(ft.Icons.CALENDAR_MONTH_OUTLINED, "Semester", str(STUDENT["semester_aktif"]), "Semester aktif"),
        ],
        spacing=Spacing.MD,
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


def dashboard_page() -> ft.Control:
    jadwal = section_card(
        "Jadwal Kuliah Hari Ini",
        ft.Column(controls=[_jadwal_item(item) for item in JADWAL_HARI_INI], spacing=Spacing.SM),
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
            _stat_cards(),
            ft.Row(
                controls=[jadwal, pengumuman],
                spacing=Spacing.MD,
                vertical_alignment=ft.CrossAxisAlignment.START,
            ),
        ],
        spacing=Spacing.LG,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
    )
