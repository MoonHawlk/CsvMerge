import tkinter as tk
import customtkinter
import pandas as pd
from tkinter import filedialog
import tkinter.messagebox as messagebox
import os
import codecs
import chardet

def detect_cod(arquivo):
    with open(arquivo, 'rb') as file:
        result = chardet.detect(file.read())
    return result['encoding']

def convert_to_utf8(file_in, file_out):
    original_decode = detect_cod(file_in)
    
    with codecs.open(file_in, 'r', encoding=original_decode, errors='replace') as file:
        content = file.read()

    with codecs.open(file_out, 'w', encoding='utf-8') as file:
        file.write(content)

def convert_csvs(lista_de_arquivos):
    exit_file = "MergedCSV.csv"
    df_concat = pd.DataFrame()
    
    for arquivo in lista_de_arquivos:
        # Criar uma versão UTF-8 do arquivo
        arquivo_utf8 = f"{os.path.splitext(arquivo)[0]}_utf8.csv"
        convert_to_utf8(arquivo, arquivo_utf8)
        
        # Ler o arquivo UTF-8
        df_temp = pd.read_csv(arquivo_utf8)

        # Concatenar horizontalmente (colunas) mantendo todas as colunas
        df_concat = pd.concat([df_concat, df_temp], axis=1)

        # Excluir o arquivo temporário UTF-8
        os.remove(arquivo_utf8)

    # Remover duplicatas de colunas (se existirem)
    df_concat = df_concat.loc[:,~df_concat.columns.duplicated()]

    df_concat.to_csv(exit_file, index=False)
    messagebox.showinfo("Conclusão", "Processo de concatenação finalizado.")

def select_files(csv_files):

    arquivos_selecionados = filedialog.askopenfilenames(
        title="Selecione Arquivos",
        filetypes=[("Arquivos CSV", "*.csv"), ("Todos os arquivos", "*.*")],
        initialdir=os.getcwd()
    )

    if arquivos_selecionados:
        for arquivo in arquivos_selecionados:
            csv_files.append(arquivo)
    
    messagebox.showinfo("Select files", "Files Uploaded")
            
def show_csv_files(csv_files):
    if csv_files:
        content = "\n".join(csv_files)
        messagebox.showinfo("Arquivos CSV", content)
    else:
        messagebox.showinfo("CSV Files", "Nenhum arquivo CSV selecionado.")
