import flet as ft

from components.badge import badge, grade_badge
from components.card import card
from components.data_table import data_table, table_container, table_row, table_text
from components.page_title import page_title
from components.stat_card import stat_card
from components.theme import Colors, FontSize, Spacing
from data.dummy_data import BOBOT_NILAI, NILAI, hitung_ipk, total_sks_lulus


def _summary() -> ft.Row:
    return ft.Row(
        controls=[
            stat_card(ft.Icons.AUTO_GRAPH, "IPK Kumulatif", f"{hitung_ipk():.2f}", "Skala 4.00"),
            stat_card(ft.Icons.LIBRARY_BOOKS_OUTLINED, "SKS Lulus", str(total_sks_lulus()), "Total SKS dengan nilai"),
            stat_card(ft.Icons.WORKSPACE_PREMIUM_OUTLINED, "Mata Kuliah", str(len(NILAI)), "Telah dinilai"),
        ],
        spacing=Spacing.MD,
    )


def _nilai_table() -> ft.Row:
    table = data_table(["KODE", "NAMA MATA KULIAH", "SKS", "NILAI", "BOBOT", "SEMESTER"])
    table.rows = [
        table_row([
            table_text(item["kode"], weight=ft.FontWeight.W_600),
            item["nama"],
            item["sks"],
            grade_badge(item["nilai"]),
            f"{BOBOT_NILAI[item['nilai']]:.2f}",
            badge(f"Semester {item['semester']}"),
        ])
        for item in NILAI
    ]
    return table_container(table)


def nilai_page() -> ft.Control:
    return ft.Column(
        controls=[
            page_title("Nilai", "Rekap nilai dan indeks prestasi kumulatif"),
            _summary(),
            card(
                ft.Column(
                    controls=[
                        ft.Text("Daftar Nilai", size=FontSize.SUBTITLE, weight=ft.FontWeight.W_600, color=Colors.TEXT_PRIMARY),
                        _nilai_table(),
                    ],
                    spacing=Spacing.MD,
                )
            ),
        ],
        spacing=Spacing.LG,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
    )
