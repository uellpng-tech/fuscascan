from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import ImageTk, Image

def iniciar_interface():

    root = tk.Tk()
    root.title("FuscaScan")
    root.geometry("450x550")
    root.minsize(450, 550)
    root.maxsize(450, 550)

    caixa = tk.Frame(root, bg="#AFAFAF")
    caixa.place(x=80, y=75, relwidth=0.65, relheight=0.55)

    def limpar_img():
        global cam_limpar, img_btnc, btn_select, btn_analisar, cam_edit, btn_edit

        cam_limpar = PhotoImage(file="assets/remover.png")
        btn_limpar = tk.Button(root, image=cam_limpar, bg="#DBDBDB", border=0, activebackground="#DBDBDB", command=limpar_img, state="disabled")
        btn_limpar.place(x=295, y=400, relwidth=0.2, relheight=0.1)

        img_btnc = PhotoImage(file="assets/add_btn.png")
        btn_select = tk.Button(root, text="Clique para selecionar a imagem", image=img_btnc, compound=tk.TOP, bg="#F0F0F0", fg="#868686",activeforeground="#868686" ,cursor="hand2", relief=tk.FLAT, command=carrega_img)
        btn_select.place(x=91.5, y=90, relwidth=0.6, relheight=0.5)
            
        btn_analisar = tk.Button(root, text="Analisar", state="disabled")
        btn_analisar.place(x=155, y=400, relwidth=0.3, relheight=0.1)

        cam_edit = PhotoImage(file="assets/editar.png")
        btn_edit = tk.Button(root, image=cam_edit, bg="#DBDBDB", border=0, activebackground="#DBDBDB", command=carrega_img, state="disabled")
        btn_edit.place(x=65, y=400, relwidth=0.2, relheight=0.1)

    def carrega_img():
        global cam, img_cam, img, btn_analisar, cam_limpar, btn_limpar, cam_edit, btn_edit

        cam = Image.open(filedialog.askopenfilename(title="Selecione uma imagem para analise", filetypes=[("image files", "*.png"), ("image files", "*.jpg"),("image files", "*.jpeg"), ("Todos os arquivos", "*.*")]))
        redimen = cam.resize((270, 275))
        img_cam = ImageTk.PhotoImage(redimen)
        img = tk.Label(root, image=img_cam, cursor="hand2")
        img.place(x=91.5, y=90, relwidth=0.6, relheight=0.5)

        btn_analisar = tk.Button(root, text="Analisar", state="active", cursor="hand2")
        btn_analisar.place(x=155, y=400, relwidth=0.3, relheight=0.1)

        cam_limpar = PhotoImage(file="assets/remover.png")
        btn_limpar = tk.Button(root, image=cam_limpar, bg="#DBDBDB", border=0, activebackground="#DBDBDB", command=limpar_img)
        btn_limpar.place(x=295, y=400, relwidth=0.2, relheight=0.1)

        cam_edit = PhotoImage(file="assets/editar.png")
        btn_edit = tk.Button(root, image=cam_edit, bg="#DBDBDB", border=0, activebackground="#DBDBDB", command=carrega_img)
        btn_edit.place(x=65, y=400, relwidth=0.2, relheight=0.1)

    img_btnc = PhotoImage(file="assets/add_btn.png")
    btn_select = tk.Button(root, text="Clique para selecionar a imagem", image=img_btnc, compound=tk.TOP, bg="#F0F0F0", fg="#868686",activeforeground="#868686" ,cursor="hand2", relief=tk.FLAT, command=carrega_img)
    btn_select.place(x=91.5, y=90, relwidth=0.6, relheight=0.5)

    btn_analisar = tk.Button(root, text="Analisar", state="disabled")
    btn_analisar.place(x=155, y=400, relwidth=0.3, relheight=0.1)

    cam_limpar = PhotoImage(file="assets/remover.png")
    btn_limpar = tk.Button(root, image=cam_limpar, bg="#DBDBDB", border=0, activebackground="#DBDBDB", command=limpar_img, state="disabled")
    btn_limpar.place(x=295, y=400, relwidth=0.2, relheight=0.1)

    cam_edit = PhotoImage(file="assets/editar.png")
    btn_edit = tk.Button(root, image=cam_edit, bg="#DBDBDB", border=0, activebackground="#DBDBDB", command=carrega_img, state="disabled")
    btn_edit.place(x=65, y=400, relwidth=0.2, relheight=0.1)

    root.mainloop()

iniciar_interface()

