# Optimasi Parameter PI pada Electronic Load Controller (ELC) PLTMH 100 kW Menggunakan PSO + Quantum LSTM

Repo ini berisi implementasi lengkap skripsi/tesis dengan judul di atas. Pendekatan yang digunakan adalah Skenario A: Quantum LSTM (QLSTM) dilatih sebagai *surrogate model* plant PLTMH untuk mempercepat proses optimasi parameter PI menggunakan Particle Swarm Optimization (PSO).

## 1. Latar Belakang Singkat
ELC konvensional pada PLTMH menggunakan kontrol PI dengan *tuning* manual yang menghasilkan deviasi frekuensi >2% saat lepas beban. Optimasi metaheuristik seperti PSO butuh ribuan kali simulasi yang berat jika menggunakan Simulink/ODE. QLSTM dipakai untuk menggantikan model numerik plant sehingga evaluasi fungsi objektif 100x lebih cepat.

## 2. Fitur Utama
1. **Pembangkitan Dataset**: Model numerik swing equation PLTMH 100 kW untuk menghasilkan data training.
2. **Training QLSTM**: Arsitektur 4 qubit, 4 layer, StronglyEntanglingLayers menggunakan PennyLane.
3. **Optimasi PSO**: Pencarian Kp, Ki optimal dengan fungsi objektif ITAE + penalti energi dump.
4. **Validasi**: Perbandingan respon frekuensi Tanpa ELC vs PI Ziegler-Nichols vs PI PSO+QLSTM.
5. **Analisis Lanjut**: Surface J(Kp,Ki) untuk bukti konvergensi dan Uji Robustness pada variasi H ±20%.

## 3. Struktur File
📁 ELC-QLSTM-100kW
├── 📁 code
│   ├── generate_dataset_100kW.py
│   ├── train_qlstm_100kW.py
│   ├── optimasi_pi_100kW.py
│   ├── validasi_plot_100kW.py
│   ├── surface_plot_100kW.py
│   └── uji_robust_100kW.py
├── 📁 data
│   └── data_pltmh_100kW.csv
├── 📁 results
│   ├── hasil_komparasi_100kW.png
│   ├── surface_J_100kW.png
│   ├── uji_robust_100kW.png
│   ├── tabel_performansi_100kW.csv
│   └── tabel_robust_100kW.csv
├── ELC_100kW_Colab.ipynb
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
   
   [![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
   [![PennyLane](https://img.shields.io/badge/PennyLane-0.33.1-yellow)](https://pennylane.ai/)
