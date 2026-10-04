import flet as ft

from components.theme import Colors, FontSize


def table_text(value, weight=None, color: str = Colors.TEXT_PRIMARY) -> ft.Text:
    return ft.Text(str(value), size=FontSize.BODY, weight=weight, color=color)


def data_table(columns: list[str], numeric_columns: tuple[int, ...] = ()) -> ft.DataTable:
    """Tabel kosong dengan style standar. Isi `table.rows` dengan `table_row(...)`."""
    return ft.DataTable(
        columns=[
            ft.DataColumn(
                label=ft.Text(name, size=FontSize.CAPTION, weight=ft.FontWeight.W_600, color=Colors.TEXT_SECONDARY),
                numeric=index in numeric_columns,
            )
            for index, name in enumerate(columns)
        ],
        rows=[],
        heading_row_color=Colors.BACKGROUND,
        heading_row_height=44,
        data_row_min_height=48,
        data_row_max_height=56,
        divider_thickness=1,
        horizontal_lines=ft.BorderSide(1, Colors.BORDER),
        column_spacing=32,
        expand=True,
    )


def table_row(cells: list) -> ft.DataRow:
    """`cells` boleh berisi string/angka atau Control (misalnya badge)."""
    return ft.DataRow(
        cells=[ft.DataCell(cell if isinstance(cell, ft.Control) else table_text(cell)) for cell in cells]
    )


def table_container(table: ft.DataTable) -> ft.Row:
    """Membuat tabel memenuhi lebar card."""
    return ft.Row(controls=[table])
