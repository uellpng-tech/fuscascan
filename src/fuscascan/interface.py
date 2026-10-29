import tkinter as tk
import random
import time
from tkinter import *
from tkinter import ttk, filedialog
from PIL import ImageTk, Image
from processamento import analisar, pre_processimg

def iniciar_interface():

    root = tk.Tk()
    root.title("FuscaScan")
    root.geometry("450x550")
    root.minsize(450, 550)
    root.maxsize(450, 550)

    caixa = tk.Frame(root, bg="#AFAFAF")
    caixa.place(x=80, y=50, relwidth=0.65, relheight=0.61)

    cerebroc = PhotoImage(file="assets/cerebro0.png")
    cerebro = tk.Label(root, image=cerebroc, bg="#AFAFAF")
    cerebro.place(x=325, y=50)

    def limpar_img():
        global btn_select, img_btnc

        img_btnc = PhotoImage(file="assets/add_btn.png")
        btn_select = tk.Button(root, text="Clique para selecionar a imagem", image=img_btnc, compound=tk.TOP, bg="#F0F0F0", fg="#868686",activeforeground="#868686" ,cursor="hand2", relief=tk.FLAT, command=carrega_img)
        btn_select.place(x=91.5, y=90, relwidth=0.6, relheight=0.5)

        btn_analisar['state'] = 'disabled'
        btn_edit['state'] = 'disabled'
        btn_limpar['state'] = 'disabled'

    def carrega_img():
        global img_cam, img

        caminho = filedialog.askopenfilename(title="Selecione uma imagem para analise", filetypes=[("image files", "*.png"), ("image files", "*.jpg"),("image files", "*.jpeg"), ("Todos os arquivos", "*.*")])
        cam = Image.open(caminho)
        redimen = cam.resize((270, 275))
        img_cam = ImageTk.PhotoImage(redimen)
        img = tk.Label(root, image=img_cam, cursor="hand2")
        img.place(x=91.5, y=90, relwidth=0.6, relheight=0.5)

        btn_edit['state'] = 'active'

        btn_analisar['state'] = 'active'
        btn_analisar['command'] = analisar

        btn_limpar['state'] = 'active'

        pre_processimg(caminho)


    img_btnc = PhotoImage(file="assets/add_btn.png")
    btn_select = tk.Button(root, text="Clique para selecionar a imagem", image=img_btnc, compound=tk.TOP, bg="#F0F0F0", fg="#868686",activeforeground="#868686" ,cursor="hand2", relief=tk.FLAT, command=carrega_img)
    btn_select.place(x=91.5, y=90, relwidth=0.6, relheight=0.5)

    btn_analisar = tk.Button(root, text="Analisar", state="disabled", command=analisar)
    btn_analisar.place(x=155, y=400, relwidth=0.3, relheight=0.1)

    cam_limpar = PhotoImage(file="assets/remover.png")
    btn_limpar = tk.Button(root, image=cam_limpar, bg="#DBDBDB", border=0, activebackground="#DBDBDB", command=limpar_img, state="disabled")
    btn_limpar.place(x=295, y=400, relwidth=0.2, relheight=0.1)

    cam_edit = PhotoImage(file="assets/editar.png")
    btn_edit = tk.Button(root, image=cam_edit, bg="#DBDBDB", border=0, activebackground="#DBDBDB", command=carrega_img, state="disabled")
    btn_edit.place(x=65, y=400, relwidth=0.2, relheight=0.1)

    root.mainloop()

iniciar_interface()

