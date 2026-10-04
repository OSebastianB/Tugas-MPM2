# Student Academic Dashboard

Aplikasi desktop dashboard akademik mahasiswa yang dibuat dengan **Python + [Flet](https://flet.dev)**.

> Project ini **front-end only**: tidak ada backend, database, API, maupun autentikasi. Semua data berasal dari `data/dummy_data.py`.

## Fitur

| Halaman | Isi |
| --- | --- |
| Dashboard | Sapaan, ringkasan akademik (IPK, SKS, semester, jumlah MK), jadwal hari ini, pengumuman |
| Mata Kuliah | Daftar mata kuliah semester aktif beserta total SKS dan dosen pengampu |
| Nilai | Ringkasan IPK, total SKS, jumlah MK, semester terakhir; tabel nilai dengan pencarian dan filter semester |
| Profile | Data diri mahasiswa (avatar, nama, NIM, program studi, fakultas, angkatan, email) |

## Pembagian Tugas

| Bagian | Lokasi | Dikerjakan oleh | Status |
| --- | --- | --- | --- |
| Dashboard | `pages/dashboard.py` | @OSebastianB | Selesai |
| Sidebar & Navbar | `components/sidebar.py`, `components/header.py`, `main.py` | @OSebastianB | Selesai |
| Design System / styling | `components/theme.py` | @OSebastianB | Selesai |
| Reusable UI components | `components/` | @OSebastianB | Selesai |
| Halaman Mata Kuliah | `pages/mata_kuliah.py` | @shintaprillia | Selesai |
| Halaman Nilai & Profile | `pages/nilai.py`, `pages/profile.py` | @dzaky15-glitch | Selesai |
| Data dummy & perhitungan IPK | `data/dummy_data.py` | @dzaky15-glitch | Selesai |

## Menjalankan Aplikasi

Membutuhkan **Python 3.10+** dan **Flet 1.x** (API Flet 0.x tidak kompatibel).

```bash
pip install -r requirements.txt
python main.py
```

### Versi web (opsional)

```bash
flet run --web main.py
```

Lalu buka alamat yang tampil di terminal (misalnya `http://localhost:8550`).

> **Windows:** jika muncul error `'flet' is not recognized`, folder `Scripts` milik Python belum ada di PATH.
> Tambahkan folder tersebut ke PATH (lokasinya bisa dilihat dengan
> `python -c "import sysconfig; print(sysconfig.get_path('scripts'))"`), lalu buka ulang terminal.

## Struktur Folder

```
main.py                 # entry point, layout utama, daftar menu (PAGES)
pages/
├── dashboard.py        # dashboard_page()
├── mata_kuliah.py      # mata_kuliah_page()
├── nilai.py            # nilai_page()
└── profile.py          # profile_page()
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
data/
└── dummy_data.py       # seluruh data dummy + fungsi perhitungan IPK
```

## Kontrak Data

UI membaca data dari `data/dummy_data.py`. File tersebut menyediakan:

| Nama | Tipe | Field / keterangan | Dipakai di |
| --- | --- | --- | --- |
| `STUDENT` | `dict` | `nama`, `nim`, `program_studi`, `fakultas`, `email`, `angkatan`, `semester_aktif` (int), `periode` | Header, Dashboard, Mata Kuliah, Profile |
| `JADWAL_HARI_INI` | `list[dict]` | `jam`, `kode`, `mata_kuliah`, `ruang`, `dosen` | Dashboard |
| `PENGUMUMAN` | `list[dict]` | `judul`, `tanggal`, `isi` | Dashboard |
| `MATA_KULIAH` | `list[dict]` | `kode`, `nama`, `sks`, `dosen`, `semester` (int) | Dashboard, Mata Kuliah |
| `NILAI` | `list[dict]` | `kode`, `nama`, `sks`, `nilai` (huruf), `semester` (int) | Nilai |
| `BOBOT_NILAI` | `dict[str, float]` | bobot per nilai huruf (`A` = 4.0 … `E` = 0.0) | Nilai |
| `hitung_ipk()` | `-> float` | IPK kumulatif | Dashboard, Nilai |
| `total_sks_lulus()` | `-> int` | total SKS yang sudah dinilai | Dashboard, Nilai |
| `semester_terakhir()` | `-> int` | semester terakhir yang sudah memiliki nilai | Nilai |

### Perhitungan IPK

```
IPK = Σ (SKS × bobot nilai) / Σ SKS
```

| Nilai | A | AB | B | BC | C | D | E |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Bobot | 4.0 | 3.5 | 3.0 | 2.5 | 2.0 | 1.0 | 0.0 |

IPK ditampilkan dengan 2 angka desimal.

## Panduan Pengembangan

- **Warna, font, spacing, radius** hanya diubah di `components/theme.py`. Jangan hard-code nilai baru di halaman.
- **Halaman baru**: buat file di `pages/` berisi function `nama_page()` yang mengembalikan control Flet, lalu daftarkan di `PAGES` pada `main.py`. Selama halaman belum selesai, pakai `placeholder_page("Judul")` dari `components/placeholder.py`.
- Gunakan komponen dari `components/` (card, stat_card, data_table, search_field, badge, page_title) agar tampilan konsisten.
- Perubahan struktur data di `data/dummy_data.py` harus tetap memenuhi [Kontrak Data](#kontrak-data) karena dipakai beberapa halaman.

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

- Sebelum mulai kerja, selalu ambil update terbaru: `git checkout main && git pull`.
- Sebelum membuat PR, gabungkan update terbaru `main` ke branch kamu agar tidak conflict:
  `git fetch origin && git merge origin/main`.
