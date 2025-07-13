# CalcULife: Kalkulator Kalkulus Interaktif

**CalcULife** adalah aplikasi GUI interaktif berbasis Python yang dirancang untuk membantu pelajar dan mahasiswa memahami konsep *turunan* dan *integral* dari fungsi aljabar dengan cara simbolik dan visual. Dibangun menggunakan `customtkinter`, aplikasi ini dapat dijalankan secara lokal di komputer Anda dengan antarmuka modern dan efek suara interaktif.

---

## Fitur Utama

* ✓ Input fungsi aljabar secara simbolik (misal: `x**2 + 3*x + 2`)
* ✓ Perhitungan simbolik **turunan** dan **integral** tak tentu & tertentu
* ✓ Visualisasi grafik fungsi dan turunannya/integralnya
* ✓ Antarmuka interaktif dengan tombol, dropdown, dan opsi tampilan
* ✓ **Mode terang/gelap** dan **efek suara klik**

---

## Teknologi yang Digunakan

* Python 3.10+
* `customtkinter` — antarmuka GUI modern
* `sympy` — perhitungan simbolik matematika
* `numpy` — operasi numerik
* `matplotlib` — visualisasi grafik
* `pygame` — efek suara klik tombol

---

## Struktur Proyek

```
calcULife/
├── app.py                 # Berkas utama GUI
├── click_pop.mp3         # Efek suara tombol klik
├── requirements.txt      # Daftar dependensi Python
├── .replit               # Konfigurasi Replit (opsional)
├── modules/              # Modul terpisah untuk logika
│   ├── logic.py          # Fungsi turunan dan integral (sympy)
│   └── plotter.py        # Fungsi plot matplotlib
└── README.md             # Dokumentasi (file ini)
```

---

## Cara Instalasi dan Menjalankan Secara Lokal

1. **Clone atau download** repositori ini:

   ```bash
   git clone https://github.com/username/calcULife.git
   cd calcULife
   ```

2. (Opsional) **Aktifkan virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate       # Mac/Linux
   venv\Scripts\activate.bat      # Windows
   ```

3. **Install dependensi**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Jalankan aplikasi**:

   ```bash
   python app.py
   ```

---

## Jalankan di Replit (Opsional)

1. Upload semua file (`app.py`, `.replit`, `requirements.txt`, dll.)
2. Pastikan `.replit` berisi:

   ```ini
   run = "python3 app.py"
   ```
3. Klik tombol **Run** di Replit
4. (Opsional) Tambahkan `python==3.10` di baris atas `requirements.txt` jika error

---

## Contoh Soal dan Cara Penulisan Ekspresi

### Penulisan Ekspresi

Ekspresi matematika ditulis dalam format Python (mengikuti aturan `sympy`). Beberapa ketentuan umum:

* Pangkat ditulis dengan `**`, contoh: `x**2`
* Fungsi trigonometri: `sin(x)`, `cos(x)`, `tan(x)`
* Fungsi eksponensial dan logaritma: `exp(x)`, `log(x)`
* Akar kuadrat: `sqrt(...)`

### Soal **TURUNAN (Derivatif)**

Cukup pilih menu **"Turunan"**, lalu salin salah satu ekspresi di bawah ke kolom input:

```python
x**3 + 2*x**2 - x + 5
sin(x) + x*cos(x)
exp(x) * log(x)
1 / (x**2 + 1)
sqrt(x**2 + 4*x + 4)
```

**Hasil**:

* Aplikasi akan menampilkan hasil turunan dalam notasi simbolik
* Grafik fungsi asli dan grafik turunannya akan ditampilkan berdampingan

### Soal **INTEGRAL**

Pilih menu **"Integral"**, isi batas bawah dan atas jika ingin menghitung integral tentu, lalu masukkan salah satu ekspresi berikut:

```python
3*x**2 + 2*x + 1
x**3           # batas bawah = 0, batas atas = 2
sin(x) * cos(x)
1 / (x * log(x))
log(x)         # batas bawah = 1, batas atas = E
```

**Hasil**:

* Integral simbolik ditampilkan (tak tentu)
* Bila batas diisi, akan dihitung nilai numerik integral tentu
* Grafik fungsi dan luas daerah integral divisualisasikan

---

## Identitas Visual

* **Warna latar terang**: `#ffffff`
* **Mode gelap**: `#121212`, teks putih
* **Warna aksen**: `#FFC400` (oranye), `#38b6ff` (biru muda)
* **Font GUI**: Comic Sans MS (friendly)
* **Tata letak**: frame simetris, dropdown, tombol besar, responsive

---

##  Kontribusi

1. Fork repositori ini
2. Buat branch: `feature-nama-fitur`
3. Commit dan push perubahan
4. Buat Pull Request ke repositori utama

---

## Lisensi

Lisensi: **MIT License**

Bebas digunakan, dimodifikasi, dan didistribusikan dengan menyertakan kredit pembuat.

---

##  Pembuat

* **Nama**: Muhamad Aziz Nur Wahid
* **NIM**: 312410040
* **Kelas**: TI.24.C1
* **Instansi**: Universitas Pelita Bangsa
* **Tahun**: 2025

---

**Learn calculus fun with CalcULife By MAzizNurWahid!**