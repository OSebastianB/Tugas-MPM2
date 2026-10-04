import flet as ft

from components.badge import badge
from components.card import card
from components.data_table import data_table, table_container, table_row, table_text
from components.page_title import page_title
from components.search_field import filter_dropdown, search_field
from components.theme import Colors, FontSize, Spacing
from data.dummy_data import MATA_KULIAH

SEMUA_SEMESTER = "Semua Semester"


def mata_kuliah_page() -> ft.Control:
    semester_options = [SEMUA_SEMESTER] + [
        f"Semester {s}" for s in sorted({mk["semester"] for mk in MATA_KULIAH})
    ]
    state = {"keyword": "", "semester": SEMUA_SEMESTER}

    table = data_table(["KODE", "NAMA MATA KULIAH", "SKS", "DOSEN", "SEMESTER"])
    result_info = ft.Text(size=FontSize.CAPTION, color=Colors.TEXT_SECONDARY)

    def filtered_mata_kuliah() -> list[dict]:
        keyword = state["keyword"].lower()
        hasil = []
        for mk in MATA_KULIAH:
            cocok_keyword = keyword in mk["kode"].lower() or keyword in mk["nama"].lower() or keyword in mk["dosen"].lower()
            cocok_semester = state["semester"] == SEMUA_SEMESTER or state["semester"] == f"Semester {mk['semester']}"
            if cocok_keyword and cocok_semester:
                hasil.append(mk)
        return hasil

    def render_rows():
        data = filtered_mata_kuliah()
        table.rows = [
            table_row([
                table_text(mk["kode"], weight=ft.FontWeight.W_600),
                mk["nama"],
                mk["sks"],
                table_text(mk["dosen"], color=Colors.TEXT_SECONDARY),
                badge(f"Semester {mk['semester']}"),
            ])
            for mk in data
        ]
        result_info.value = f"Menampilkan {len(data)} dari {len(MATA_KULIAH)} mata kuliah"

    results = ft.Column(controls=[result_info, table_container(table)], spacing=Spacing.MD)

    def on_search(e):
        state["keyword"] = e.control.value
        render_rows()
        results.update()

    def on_filter(e):
        state["semester"] = e.control.value
        render_rows()
        results.update()

    render_rows()

    toolbar = ft.Row(
        controls=[
            search_field("Cari kode, nama mata kuliah, atau dosen...", on_search, expand=True),
            filter_dropdown("Semester", semester_options, SEMUA_SEMESTER, on_filter),
        ],
        spacing=Spacing.MD,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )

    return ft.Column(
        controls=[
            page_title("Mata Kuliah", "Daftar mata kuliah yang diambil selama masa studi"),
            card(
                ft.Column(
                    controls=[toolbar, results],
                    spacing=Spacing.MD,
                )
            ),
        ],
        spacing=Spacing.LG,
        horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
    )
