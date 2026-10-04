"""Dummy data untuk seluruh halaman front-end.

Tidak ada backend/database/API. Jika nanti data asli tersedia,
cukup ganti isi variabel di file ini dengan format yang sama.
"""

STUDENT = {
    "nama": "Muhammad Rizky Ramadhan",
    "nim": "21060123130045",
    "program_studi": "S1 Teknik Elektro",
    "fakultas": "Fakultas Teknik",
    "email": "rizkyramadhan@students.undip.ac.id",
    "angkatan": "2023",
    "semester_aktif": 5,
    "periode": "Semester Ganjil 2026/2027",
}

JADWAL_HARI_INI = [
    {
        "jam": "07:00 - 09:30",
        "kode": "TEL301",
        "mata_kuliah": "Sistem Tenaga Listrik",
        "ruang": "Gedung E - 201",
        "dosen": "Dr. Ir. Hadi Susanto, M.T.",
    },
    {
        "jam": "10:00 - 12:30",
        "kode": "TEL303",
        "mata_kuliah": "Elektronika Daya",
        "ruang": "Lab Elektronika Daya",
        "dosen": "Rina Kusumawati, S.T., M.Eng.",
    },
    {
        "jam": "13:00 - 15:30",
        "kode": "TEL307",
        "mata_kuliah": "Instrumentasi dan Pengukuran",
        "ruang": "Gedung E - 304",
        "dosen": "Ir. Bambang Wicaksono, M.T.",
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
    {"kode": "TEL101", "nama": "Kalkulus I", "sks": 3, "dosen": "Dr. Sri Handayani, M.Si.", "semester": 1},
    {"kode": "TEL103", "nama": "Fisika Dasar I", "sks": 3, "dosen": "Dr. Agus Prasetyo, M.Si.", "semester": 1},
    {"kode": "TEL105", "nama": "Pengantar Teknik Elektro", "sks": 2, "dosen": "Ir. Bambang Wicaksono, M.T.", "semester": 1},
    {"kode": "TEL107", "nama": "Dasar Pemrograman", "sks": 3, "dosen": "Dimas Aditya, S.T., M.Kom.", "semester": 1},
    {"kode": "TEL201", "nama": "Kalkulus II", "sks": 3, "dosen": "Dr. Sri Handayani, M.Si.", "semester": 2},
    {"kode": "TEL203", "nama": "Fisika Dasar II", "sks": 3, "dosen": "Dr. Agus Prasetyo, M.Si.", "semester": 2},
    {"kode": "TEL205", "nama": "Rangkaian Listrik I", "sks": 3, "dosen": "Dr. Ir. Hadi Susanto, M.T.", "semester": 2},
    {"kode": "TEL207", "nama": "Sistem Digital", "sks": 3, "dosen": "Dimas Aditya, S.T., M.Kom.", "semester": 2},
    {"kode": "TEL211", "nama": "Rangkaian Listrik II", "sks": 3, "dosen": "Dr. Ir. Hadi Susanto, M.T.", "semester": 3},
    {"kode": "TEL213", "nama": "Elektronika I", "sks": 3, "dosen": "Rina Kusumawati, S.T., M.Eng.", "semester": 3},
    {"kode": "TEL215", "nama": "Medan Elektromagnetik", "sks": 3, "dosen": "Prof. Dr. Wahyu Nugroho, M.Sc.", "semester": 3},
    {"kode": "TEL217", "nama": "Probabilitas dan Statistika", "sks": 2, "dosen": "Dr. Sri Handayani, M.Si.", "semester": 3},
    {"kode": "TEL221", "nama": "Elektronika II", "sks": 3, "dosen": "Rina Kusumawati, S.T., M.Eng.", "semester": 4},
    {"kode": "TEL223", "nama": "Sinyal dan Sistem", "sks": 3, "dosen": "Prof. Dr. Wahyu Nugroho, M.Sc.", "semester": 4},
    {"kode": "TEL225", "nama": "Sistem Kendali", "sks": 3, "dosen": "Dr. Fajar Hidayat, S.T., M.T.", "semester": 4},
    {"kode": "TEL227", "nama": "Mikroprosesor dan Mikrokontroler", "sks": 3, "dosen": "Dimas Aditya, S.T., M.Kom.", "semester": 4},
    {"kode": "TEL301", "nama": "Sistem Tenaga Listrik", "sks": 3, "dosen": "Dr. Ir. Hadi Susanto, M.T.", "semester": 5},
    {"kode": "TEL303", "nama": "Elektronika Daya", "sks": 3, "dosen": "Rina Kusumawati, S.T., M.Eng.", "semester": 5},
    {"kode": "TEL305", "nama": "Pengolahan Sinyal Digital", "sks": 3, "dosen": "Prof. Dr. Wahyu Nugroho, M.Sc.", "semester": 5},
    {"kode": "TEL307", "nama": "Instrumentasi dan Pengukuran", "sks": 3, "dosen": "Ir. Bambang Wicaksono, M.T.", "semester": 5},
]

NILAI = [
    {"kode": "TEL101", "nama": "Kalkulus I", "sks": 3, "nilai": "AB", "semester": 1},
    {"kode": "TEL103", "nama": "Fisika Dasar I", "sks": 3, "nilai": "B", "semester": 1},
    {"kode": "TEL105", "nama": "Pengantar Teknik Elektro", "sks": 2, "nilai": "A", "semester": 1},
    {"kode": "TEL107", "nama": "Dasar Pemrograman", "sks": 3, "nilai": "A", "semester": 1},
    {"kode": "TEL201", "nama": "Kalkulus II", "sks": 3, "nilai": "B", "semester": 2},
    {"kode": "TEL203", "nama": "Fisika Dasar II", "sks": 3, "nilai": "BC", "semester": 2},
    {"kode": "TEL205", "nama": "Rangkaian Listrik I", "sks": 3, "nilai": "AB", "semester": 2},
    {"kode": "TEL207", "nama": "Sistem Digital", "sks": 3, "nilai": "A", "semester": 2},
    {"kode": "TEL211", "nama": "Rangkaian Listrik II", "sks": 3, "nilai": "B", "semester": 3},
    {"kode": "TEL213", "nama": "Elektronika I", "sks": 3, "nilai": "AB", "semester": 3},
    {"kode": "TEL215", "nama": "Medan Elektromagnetik", "sks": 3, "nilai": "C", "semester": 3},
    {"kode": "TEL217", "nama": "Probabilitas dan Statistika", "sks": 2, "nilai": "A", "semester": 3},
    {"kode": "TEL221", "nama": "Elektronika II", "sks": 3, "nilai": "AB", "semester": 4},
    {"kode": "TEL223", "nama": "Sinyal dan Sistem", "sks": 3, "nilai": "BC", "semester": 4},
    {"kode": "TEL225", "nama": "Sistem Kendali", "sks": 3, "nilai": "B", "semester": 4},
    {"kode": "TEL227", "nama": "Mikroprosesor dan Mikrokontroler", "sks": 3, "nilai": "A", "semester": 4},
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


def semester_terakhir() -> int:
    """Semester terakhir yang sudah memiliki nilai."""
    return max((item["semester"] for item in NILAI), default=0)
