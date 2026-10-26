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