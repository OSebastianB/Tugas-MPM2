# Student Academic Dashboard

Aplikasi desktop dashboard akademik mahasiswa yang dibuat dengan **Python + [Flet](https://flet.dev)**.

> Project ini **front-end only**: tidak ada backend, database, API, maupun autentikasi.
> Semua data berasal dari `data/dummy_data.py`.

## Fitur

| Halaman | Isi |
| --- | --- |
| Dashboard | Welcome section, card IPK / total SKS / semester, jadwal kuliah hari ini, pengumuman akademik |
| Mata Kuliah | Pencarian, filter semester, tabel kode / nama / SKS / dosen / semester |
| Nilai | Ringkasan IPK, tabel kode / nama / SKS / nilai huruf / bobot / semester |
| Profile | Avatar, nama, NIM, program studi, fakultas, email, angkatan |

Navigasi lewat sidebar mengganti konten di window yang sama.

## Menjalankan Aplikasi

Membutuhkan **Python 3.10+** dan **Flet 1.x** (API Flet 0.x tidak kompatibel).

```bash
pip install -r requirements.txt
python main.py
```

## Struktur Folder

```
main.py                 # entry point, layout utama, daftar menu (PAGES)
pages/                  # satu file per halaman
├── dashboard.py        #   dashboard_page()
├── mata_kuliah.py      #   mata_kuliah_page()
├── nilai.py            #   nilai_page()
└── profile.py          #   profile_page()
components/             # komponen UI reusable
├── theme.py            #   design tokens: warna, ukuran font, spacing, radius
├── sidebar.py
├── header.py
├── stat_card.py
├── card.py
├── badge.py
├── avatar.py
├── data_table.py
├── search_field.py
└── page_title.py
data/
└── dummy_data.py       # semua data dummy + hitung IPK / total SKS
```

## Panduan Pengembangan

- **Warna, font, spacing, radius** hanya diubah di `components/theme.py`. Jangan hard-code nilai baru di halaman.
- **Halaman baru**: buat file di `pages/` berisi function `nama_page()` yang mengembalikan control Flet, lalu tambahkan satu baris di `PAGES` pada `main.py`.
- **Data**: tambah/ubah data di `data/dummy_data.py`. Jika nanti ada data asli, cukup ganti isi file ini dengan format yang sama.

## Alur Kerja Git (Kelompok)

Branch `main` diproteksi, perubahan masuk lewat Pull Request.

```bash
git clone https://github.com/OSebastianB/Tugas-MPM2.git
cd Tugas-MPM2
git checkout -b nama-fitur          # contoh: fitur-halaman-jadwal

# ... edit kode ...
git add .
git commit -m "feat: deskripsi singkat perubahan"
git push -u origin nama-fitur
```

Lalu buka repo di GitHub dan buat **Pull Request** ke `main`.
Sebelum mulai kerja, selalu ambil update terbaru: `git checkout main && git pull`.
