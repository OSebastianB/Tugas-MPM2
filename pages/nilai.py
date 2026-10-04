import flet as ft

from components.badge import badge, grade_badge
from components.card import section_card
from components.data_table import data_table, table_container, table_row, table_text
from components.page_title import page_title
from components.search_field import filter_dropdown, search_field
from components.stat_card import stat_card
from components.theme import Colors, FontSize, Spacing
from data.dummy_data import BOBOT_NILAI, NILAI, hitung_ipk, semester_terakhir, total_sks_lulus

STAT_CARD_COLUMNS = {"xs": 12, "md": 6, "xl": 3}
SEMUA_SEMESTER = "Semua Semester"


def _summary_card(icon, label: str, value: str, caption: str) -> ft.Container:
    card = stat_card(icon, label, value, caption)
    card.col = STAT_CARD_COLUMNS
    return card


def _academic_summary() -> ft.ResponsiveRow:
    return ft.ResponsiveRow(
        controls=[
            _summary_card(ft.Icons.AUTO_GRAPH, "IPK", f"{hitung_ipk():.2f}", "Skala 4.00"),
            _summary_card(ft.Icons.LIBRARY_BOOKS_OUTLINED, "Total SKS", str(total_sks_lulus()), "SKS telah dinilai"),
            _summary_card(ft.Icons.WORKSPACE_PREMIUM_OUTLINED, "Mata Kuliah", str(len(NILAI)), "Telah dinilai"),
            _summary_card(
                ft.Icons.CALENDAR_MONTH_OUTLINED,
                "Semester Terakhir",
                str(semester_terakhir()),
                "Semester dengan nilai terbaru",
            ),
        ],
        spacing=Spacing.MD,
        run_spacing=Spacing.MD,
    )


def _nilai_row(item: dict) -> ft.DataRow:
    return table_row([
        table_text(item["kode"], weight=ft.FontWeight.W_600),
        item["nama"],
        item["sks"],
        grade_badge(item["nilai"]),
        f"{BOBOT_NILAI[item['nilai']]:.2f}",
        badge(f"Semester {item['semester']}"),
    ])


def _daftar_nilai() -> ft.Container:
    semester_options = [SEMUA_SEMESTER] + [f"Semester {s}" for s in sorted({item["semester"] for item in NILAI})]
    state = {"keyword": "", "semester": SEMUA_SEMESTER}

    table = data_table(["KODE", "NAMA MATA KULIAH", "SKS", "NILAI", "BOBOT", "SEMESTER"], numeric_columns=(2, 4))
    result_info = ft.Text(size=FontSize.CAPTION, color=Colors.TEXT_SECONDARY)
    empty_info = ft.Text(
        "Tidak ada mata kuliah yang sesuai dengan pencarian.",
        size=FontSize.BODY,
        color=Colors.TEXT_SECONDARY,
    )

    def filtered_nilai() -> list[dict]:
        keyword = state["keyword"].strip().lower()
        return [
            item
            for item in NILAI
            if (keyword in item["kode"].lower() or keyword in item["nama"].lower())
            and (state["semester"] == SEMUA_SEMESTER or state["semester"] == f"Semester {item['semester']}")
        ]

    def render_rows():
        data = filtered_nilai()
        table.rows = [_nilai_row(item) for item in data]
        result_info.value = f"Menampilkan {len(data)} dari {len(NILAI)} mata kuliah"
        empty_info.visible = not data

    results = ft.Column(controls=[result_info, table_container(table), empty_info], spacing=Spacing.MD)

    def on_search(e):
        state["keyword"] = e.control.value or ""
        render_rows()
        results.update()

    def on_filter(e):
        state["semester"] = e.control.value or SEMUA_SEMESTER
        render_rows()
        results.update()

    render_rows()

    toolbar = ft.Row(
        controls=[
            search_field("Cari kode atau nama mata kuliah...", on_search, expand=True),
            filter_dropdown("Semester", semester_options, SEMUA_SEMESTER, on_filter),
        ],
        spacing=Spacing.MD,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    return section_card(
        "Daftar Nilai",
        ft.Column(controls=[toolbar, results], spacing=Spacing.MD),
        icon=ft.Icons.GRADING_OUTLINED,
    )


def nilai_page() -> ft.Control:
    return ft.Column(
        controls=[
            page_title("Nilai", "Rekap nilai dan indeks prestasi kumulatif"),
            _academic_summary(),
            _daftar_nilai(),
        ],
        spacing=Spacing.LG,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
    )
