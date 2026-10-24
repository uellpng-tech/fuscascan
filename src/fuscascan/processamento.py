from tkinter import *
import tkinter as tk
from tkinter import filedialog

def carrega_img():
    global btn_select
    caminho_img = filedialog.askopenfilename(title="Selecione uma imagem para analise", filetypes=[("image files", "*.png"), ("image files", "*.jpg"),("image files", "*.jpeg"), ("Todos os arquivos", "*.*")])
    img_btnc = PhotoImage(file=caminho_img)
    btn_select['image'] = img_btnc
