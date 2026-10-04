"""Dummy data untuk seluruh halaman front-end.

Tidak ada backend/database/API. Jika nanti data asli tersedia,
cukup ganti isi variabel di file ini dengan format yang sama.
"""

STUDENT = {
    "nama": "Andi Pratama",
    "nim": "21060123130001",
    "program_studi": "S1 Teknik Komputer",
    "fakultas": "Fakultas Teknik",
    "email": "andi.pratama@students.univ.ac.id",
    "angkatan": "2023",
    "semester_aktif": 5,
    "periode": "Semester Ganjil 2026/2027",
}

JADWAL_HARI_INI = [
    {
        "jam": "07:00 - 08:40",
        "kode": "TKK301",
        "mata_kuliah": "Sistem Operasi",
        "ruang": "Gedung A - 301",
        "dosen": "Dr. Budi Santoso, M.T.",
    },
    {
        "jam": "09:30 - 11:10",
        "kode": "TKK305",
        "mata_kuliah": "Jaringan Komputer",
        "ruang": "Lab Jaringan",
        "dosen": "Rina Wulandari, S.T., M.Kom.",
    },
    {
        "jam": "13:00 - 14:40",
        "kode": "TKK307",
        "mata_kuliah": "Rekayasa Perangkat Lunak",
        "ruang": "Gedung B - 204",
        "dosen": "Ir. Agus Setiawan, M.Eng.",
    },
]

PENGUMUMAN = [
    {
        "judul": "Batas Pengisian IRS Semester Ganjil",
        "tanggal": "6 Okt 2026",
        "isi": "Pengisian IRS ditutup pukul 23.59 WIB. Pastikan sudah disetujui dosen wali.",
    },
    {
        "judul": "Jadwal Ujian Tengah Semester",
        "tanggal": "3 Okt 2026",
        "isi": "UTS dilaksanakan 26 Okt - 6 Nov 2026. Jadwal lengkap tersedia di bagian akademik.",
    },
    {
        "judul": "Pendaftaran Beasiswa Prestasi",
        "tanggal": "1 Okt 2026",
        "isi": "Mahasiswa dengan IPK minimal 3.50 dapat mendaftar hingga 20 Oktober 2026.",
    },
]

MATA_KULIAH = [
    {"kode": "TKK101", "nama": "Dasar Pemrograman", "sks": 3, "dosen": "Dr. Budi Santoso, M.T.", "semester": 1},
    {"kode": "TKK103", "nama": "Matematika Diskrit", "sks": 3, "dosen": "Dewi Lestari, S.Si., M.Sc.", "semester": 1},
    {"kode": "TKK105", "nama": "Pengantar Teknik Komputer", "sks": 2, "dosen": "Ir. Agus Setiawan, M.Eng.", "semester": 1},
    {"kode": "TKK201", "nama": "Struktur Data", "sks": 3, "dosen": "Rina Wulandari, S.T., M.Kom.", "semester": 2},
    {"kode": "TKK203", "nama": "Sistem Digital", "sks": 3, "dosen": "Dr. Hendra Gunawan, M.T.", "semester": 2},
    {"kode": "TKK205", "nama": "Basis Data", "sks": 3, "dosen": "Dewi Lestari, S.Si., M.Sc.", "semester": 3},
    {"kode": "TKK207", "nama": "Pemrograman Berorientasi Objek", "sks": 3, "dosen": "Dr. Budi Santoso, M.T.", "semester": 3},
    {"kode": "TKK209", "nama": "Organisasi dan Arsitektur Komputer", "sks": 3, "dosen": "Dr. Hendra Gunawan, M.T.", "semester": 4},
    {"kode": "TKK211", "nama": "Pemrograman Web", "sks": 3, "dosen": "Rina Wulandari, S.T., M.Kom.", "semester": 4},
    {"kode": "TKK301", "nama": "Sistem Operasi", "sks": 3, "dosen": "Dr. Budi Santoso, M.T.", "semester": 5},
    {"kode": "TKK305", "nama": "Jaringan Komputer", "sks": 3, "dosen": "Rina Wulandari, S.T., M.Kom.", "semester": 5},
    {"kode": "TKK307", "nama": "Rekayasa Perangkat Lunak", "sks": 3, "dosen": "Ir. Agus Setiawan, M.Eng.", "semester": 5},
]

NILAI = [
    {"kode": "TKK101", "nama": "Dasar Pemrograman", "sks": 3, "nilai": "A", "semester": 1},
    {"kode": "TKK103", "nama": "Matematika Diskrit", "sks": 3, "nilai": "B", "semester": 1},
    {"kode": "TKK105", "nama": "Pengantar Teknik Komputer", "sks": 2, "nilai": "A", "semester": 1},
    {"kode": "TKK201", "nama": "Struktur Data", "sks": 3, "nilai": "A", "semester": 2},
    {"kode": "TKK203", "nama": "Sistem Digital", "sks": 3, "nilai": "BC", "semester": 2},
    {"kode": "TKK205", "nama": "Basis Data", "sks": 3, "nilai": "AB", "semester": 3},
    {"kode": "TKK207", "nama": "Pemrograman Berorientasi Objek", "sks": 3, "nilai": "A", "semester": 3},
    {"kode": "TKK209", "nama": "Organisasi dan Arsitektur Komputer", "sks": 3, "nilai": "B", "semester": 4},
    {"kode": "TKK211", "nama": "Pemrograman Web", "sks": 3, "nilai": "AB", "semester": 4},
]

BOBOT_NILAI = {
    "A": 4.0,
    "AB": 3.5,
    "B": 3.0,
    "BC": 2.5,
    "C": 2.0,
    "D": 1.0,
    "E": 0.0,
}


def total_sks_lulus() -> int:
    return sum(item["sks"] for item in NILAI)


def hitung_ipk() -> float:
    total_sks = total_sks_lulus()
    if total_sks == 0:
        return 0.0
    total_mutu = sum(item["sks"] * BOBOT_NILAI[item["nilai"]] for item in NILAI)
    return round(total_mutu / total_sks, 2)
