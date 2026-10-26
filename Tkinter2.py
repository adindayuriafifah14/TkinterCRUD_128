import sqlite3
import tkinter as tk
from tkinter import messagebox

def init_db():
  conn = sqlite3.connect("prediksi_fakultas.db")
  cursor = conn.cursor()
  cursor.execute("""
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_siswa TEXT NOT NULL,
            biologi REAL,
            fisika REAL,
            inggris REAL,
            prediksi_fakultas TEXT
        )
    """)
  conn.commit()
  conn.close()

def submit_data():
  nama = entry_nama.get().strip()
  bio_str = entry_biologi.get().strip()
  fis_str = entry_fisika.get().strip()
  ing_str = entry_inggris.get().strip()

  if not nama or not bio_str or not fis_str or not ing_str:
    messagebox.showwarning(
        "Peringatan", "Semua kolom data dan nilai harus diisi!"
    )
    return

  try:
    biologi = float(bio_str)
    fisika = float(fis_str)
    inggris = float(ing_str)
  except ValueError:
    messagebox.showerror(
        "Error", "Nilai Biologi, Fisika, dan Inggris harus berupa angka!"
    )
    return
  
  nilai_dict = {"Kedokteran": biologi, "Teknik": fisika, "Bahasa": inggris}

  prediksi = max(nilai_dict, key=nilai_dict.get)
  
  try:
    conn = sqlite3.connect("prediksi_fakultas.db")
    cursor = conn.cursor()
    cursor.execute(
        """
            INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
            VALUES (?, ?, ?, ?, ?)
        """,
        (nama, biologi, fisika, inggris, prediksi),
    )
    conn.commit()
    conn.close()

    label_hasil.config(
        text=(
            f"Siswa: {nama}\n Hasil Prediksi Fakultas: {prediksi}\n(Data"
            " berhasil disimpan ke SQLite!)"
        )
    )
    messagebox.showinfo("Sukses", "Data berhasil disimpan ke database!")

    # Kosongkan form input setelah submit
    entry_nama.delete(0, tk.END)
    entry_biologi.delete(0, tk.END)
    entry_fisika.delete(0, tk.END)
    entry_inggris.delete(0, tk.END)

  except Exception as e:
    messagebox.showerror("Error Database", f"Terjadi kesalahan: {e}")

init_db()

root = tk.Tk()
root.title("Aplikasi Prediksi Fakultas Pilihan")
root.geometry("500x550")
root.configure(bg="#f0f4f7")

judul = tk.Label(
    root,
    text="Aplikasi Prediksi Fakultas",
    font=("Helvetica", 18, "bold"),
    bg="#f0f4f7",
    fg="#333",
)
judul.pack(pady=20)

input_frame = tk.Frame(root, bg="#f0f4f7")
input_frame.pack(pady=10)

tk.Label(
    input_frame,
    text="Nama Siswa:",
    font=("Helvetica", 12),
    bg="#f0f4f7",
    anchor="w",
).grid(row=0, column=0, sticky="w", pady=8, padx=10)
entry_nama = tk.Entry(input_frame, width=25, font=("Helvetica", 12))
entry_nama.grid(row=0, column=1, pady=8)

tk.Label(
    input_frame,
    text="Nilai Biologi:",
    font=("Helvetica", 12),
    bg="#f0f4f7",
    anchor="w",
).grid(row=1, column=0, sticky="w", pady=8, padx=10)
entry_biologi = tk.Entry(input_frame, width=25, font=("Helvetica", 12))
entry_biologi.grid(row=1, column=1, pady=8)

tk.Label(
    input_frame,
    text="Nilai Fisika:",
    font=("Helvetica", 12),
    bg="#f0f4f7",
    anchor="w",
).grid(row=2, column=0, sticky="w", pady=8, padx=10)
entry_fisika = tk.Entry(input_frame, width=25, font=("Helvetica", 12))
entry_fisika.grid(row=2, column=1, pady=8)

tk.Label(
    input_frame,
    text="Nilai Inggris:",
    font=("Helvetica", 12),
    bg="#f0f4f7",
    anchor="w",
).grid(row=3, column=0, sticky="w", pady=8, padx=10)
entry_inggris = tk.Entry(input_frame, width=25, font=("Helvetica", 12))
entry_inggris.grid(row=3, column=1, pady=8)

submit_button = tk.Button(
    root,
    text="Submit Nilai",
    command=submit_data,
    font=("Helvetica", 12, "bold"),
    bg="#ff209e",
    fg="white",
    padx=10,
    pady=5,
)
submit_button.pack(pady=15)
