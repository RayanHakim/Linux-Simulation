🐧 Linux Terminal Simulator: Interactive GUI Sandbox
Linux Terminal Simulator adalah aplikasi desktop berbasis Python yang mereplikasi antarmuka dan logika shell Linux dalam lingkungan virtual yang aman. Proyek ini menggabungkan struktur data tingkat lanjut (N-ary Tree) dengan antarmuka grafis (GUI) untuk memberikan pengalaman belajar navigasi terminal yang interaktif tanpa risiko merusak sistem operasi asli.

🎮 Fitur Utama & Perintah (Commands)
Simulator ini dibangun dengan logika Backend yang kuat untuk memproses perintah secara real-time:

🖥️ Custom Hacker GUI: Antarmuka grafis menggunakan Tkinter dengan tema High-Contrast (Teks Hijau di atas Background Hitam) ala terminal profesional.

⛓️ Advanced Virtual File System (VFS): Simulasi struktur folder dan file yang kompleks menggunakan algoritma Tree, mendukung navigasi Parent-Child (cd ..).

📂 Core Linux Commands:

ls: Melihat isi direktori virtual.

mkdir: Membuat folder baru secara dinamis.

touch: Membuat file teks baru.

cat: Membaca konten di dalam file virtual.

cd: Navigasi antar direktori (Mendukung Absolute & Relative Path).

💾 Smart Persistence (Auto-Save/Load): * Auto-Load: Mengembalikan struktur folder terakhir saat aplikasi dibuka.

Auto-Save: Otomatis menyimpan perubahan ke file vfs_data.json saat aplikasi ditutup (Klik 'X' atau ketik exit).

🧹 Utility Commands: Dukungan perintah clear untuk membersihkan layar dan whoami untuk identitas user.

📚 Integrated Manual: File manual.txt otomatis tersedia di folder Root sebagai panduan cepat bagi pengguna baru.

🧪 Arsitektur Proyek (Modular Structure)
Proyek ini menerapkan prinsip Separation of Concerns, memisahkan logika data dengan logika tampilan:

📜 main.py (GUI Engine): Mengelola Window Tkinter, menangkap event keyboard, dan menjembatani input pengguna ke mesin filesystem.

🌳 filesystem.py (Core Logic): Berisi definisi kelas Folder dan File. Ini adalah otak dari simulasi yang mengatur hubungan antar objek dalam memori.

💾 storage.py (Data Handler): Bertanggung jawab atas konversi struktur data Tree ke format JSON (Serialisasi) dan sebaliknya (Deserialisasi).

🛠️ Tech Stack
Language: Python 3.x

GUI Framework: Tkinter (Native Python Library)

Data Format: JSON (JavaScript Object Notation)

Algorithms: Recursive Tree Traversal & Persistence Logic.

📂 Struktur Proyek
Plaintext
/Linux-Terminal-Sim
  ├── main.py          <-- Terminal GUI & Input Controller
  ├── filesystem.py    <-- Virtual File System Logic (Tree)
  ├── storage.py       <-- Persistence Manager (Save/Load)
  ├── vfs_data.json    <-- Database Virtual (JSON Format)
  └── README.md        <-- Dokumentasi Proyek
🚀 Panduan Instalasi & Penggunaan
Persiapan: Pastikan Python 3 sudah terinstal. Tidak perlu instalasi library tambahan (Zero Dependencies).

Jalankan Aplikasi:
python main.py

Tips: Gunakan perintah save secara manual jika ingin memastikan data aman, atau cukup tutup aplikasi untuk fitur Auto-Save.
