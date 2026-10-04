# Student Academic Dashboard

Aplikasi desktop dashboard akademik mahasiswa yang dibuat dengan **Python + [Flet](https://flet.dev)**.

> Project ini **front-end only**: tidak ada backend, database, API, maupun autentikasi.

## Pembagian Tugas

| Bagian | Lokasi | Status |
| --- | --- | --- |
| Dashboard | `pages/dashboard.py` | Selesai |
| Sidebar & Navbar | `components/sidebar.py`, `components/header.py`, `main.py` | Selesai |
| Design System / styling | `components/theme.py` | Selesai |
| Reusable UI components | `components/` | Selesai |
| Data dummy | `data/dummy_data.py` | Dikerjakan anggota lain |
| Halaman Mata Kuliah, Nilai, Profile | `pages/` | Dikerjakan anggota lain (saat ini placeholder) |

## Menjalankan Aplikasi

Membutuhkan **Python 3.10+** dan **Flet 1.x** (API Flet 0.x tidak kompatibel).

```bash
pip install -r requirements.txt
python main.py
```

Aplikasi membutuhkan file `data/dummy_data.py` (lihat [Kontrak Data](#kontrak-data)).

## Struktur Folder

```
main.py                 # entry point, layout utama, daftar menu (PAGES)
pages/
└── dashboard.py        # dashboard_page()
components/             # komponen UI reusable
├── theme.py            #   design tokens: warna, ukuran font, spacing, radius
├── sidebar.py          #   sidebar navigasi
├── header.py           #   navbar atas
├── placeholder.py      #   halaman sementara untuk menu yang belum selesai
├── stat_card.py        #   kartu statistik (ikon + angka)
├── card.py             #   card() dan section_card()
├── badge.py            #   badge() dan grade_badge()
├── avatar.py           #   avatar inisial
├── data_table.py       #   tabel standar: data_table(), table_row(), table_container()
├── search_field.py     #   search_field() dan filter_dropdown()
└── page_title.py       #   judul + subjudul halaman
```

## Kontrak Data

UI membaca data dari `data/dummy_data.py`. File tersebut harus menyediakan:

| Nama | Tipe | Field / keterangan | Dipakai di |
| --- | --- | --- | --- |
| `STUDENT` | `dict` | `nama`, `nim`, `program_studi`, `semester_aktif` (int), `periode` | Header, Dashboard |
| `JADWAL_HARI_INI` | `list[dict]` | `jam`, `kode`, `mata_kuliah`, `ruang`, `dosen` | Dashboard |
| `PENGUMUMAN` | `list[dict]` | `judul`, `tanggal`, `isi` | Dashboard |
| `MATA_KULIAH` | `list[dict]` | minimal `semester` (int) | Dashboard (jumlah MK semester ini) |
| `hitung_ipk()` | `-> float` | IPK kumulatif | Dashboard |
| `total_sks_lulus()` | `-> int` | total SKS yang sudah dinilai | Dashboard |

## Panduan Pengembangan

- **Warna, font, spacing, radius** hanya diubah di `components/theme.py`. Jangan hard-code nilai baru di halaman.
- **Halaman baru**: buat file di `pages/` berisi function `nama_page()` yang mengembalikan control Flet, lalu ganti `placeholder_page(...)` pada `PAGES` di `main.py` dengan function tersebut.
- Gunakan komponen dari `components/` (card, stat_card, data_table, search_field, badge, page_title) agar tampilan konsisten.

## Alur Kerja Git (Kelompok)

Branch `main` diproteksi, perubahan masuk lewat Pull Request.

```bash
git clone https://github.com/OSebastianB/Tugas-MPM2.git
cd Tugas-MPM2
git checkout -b nama-fitur          # contoh: feature/halaman-nilai

# ... edit kode ...
git add .
git commit -m "feat: deskripsi singkat perubahan"
git push -u origin nama-fitur
```

Lalu buka repo di GitHub dan buat **Pull Request** ke `main`.
Sebelum mulai kerja, selalu ambil update terbaru: `git checkout main && git pull`.
