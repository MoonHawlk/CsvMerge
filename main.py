import tkinter as tk
import customtkinter
import pandas as pd
from tkinter import filedialog
import tkinter.messagebox as messagebox
import os
import codecs
import chardet
from func import *

csv_files = []

# Configuração básica do Tkinter
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Frame Config
app = customtkinter.CTk()
app.geometry("480x480")
app.title("CSVMerge")

# Title Label
title = customtkinter.CTkLabel(app, text="Choose the .csv files")
title.pack(padx=10, pady=10)

# Botão para acionar a Seleção de arquivos
select_files_button = customtkinter.CTkButton(app, text="Select Files", command=lambda: select_files(csv_files))
select_files_button.pack(padx=10, pady=10)

# Lista com todos os diretorios de arquivos descobertos no csv_files
exibir_csv_files_button = customtkinter.CTkButton(app, text="Exibir CSV Files", command=lambda: show_csv_files(csv_files))
exibir_csv_files_button.pack(padx=10, pady=10)

# Botão para Converter e Concatenar CSVs
merge_files_button = customtkinter.CTkButton(app, text="Merge Files", command=lambda: convert_csvs(csv_files))
merge_files_button.pack(padx=10, pady=10)

# Run Application
app.mainloop()
