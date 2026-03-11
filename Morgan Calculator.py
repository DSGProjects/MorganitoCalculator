import os
import sys
import tkinter as tk
import pygame

# Función para localizar recursos dentro del .exe o en script
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller temporal
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Inicializar mixer
pygame.mixer.init()

# Cargar sonido usando resource_path
sonido_click = pygame.mixer.Sound(resource_path("click.wav"))



def click_boton(valor):
    entrada_actual=entrada_var.get()
    entrada_var.set(entrada_actual+str(valor))
    
def borrar():
    entrada_var.set('')
    
def calcular():
    try:
        resultado = eval(entrada_var.get())
        entrada_var.set(resultado)
        sonido_click.play()
    except:
        entrada_var.set('ERROR')    
        
            
root=tk.Tk()
root.title('Morgan CLI Calculator')
root.geometry('295x420')
root.resizable(False, False)

ruta_base = os.path.dirname(__file__)
ruta_icono = os.path.join(ruta_base, "Morgan.png")

icono = tk.PhotoImage(file=ruta_icono)
root.iconphoto(True, icono)

entrada_var = tk.StringVar()

entrada=tk.Entry(root,
    textvariable=entrada_var,
    font=('Arial', 18),
    justify='right',
    bd=8
)
entrada.grid(row=0,
    column=0,
    columnspan=4,
    ipadx=8,
    ipady=8,
    pady=10
)

botones=[
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('c',4,2), ('+',4,3)
]

for (texto, fila, columna) in botones:
    if texto == 'c':
        boton=tk.Button(root,
        text=texto,
        font=('Arial', 14),
        width=5,
        height=2,
        bg='coral',
        command=borrar)
    else:
        boton=tk.Button(root,
        text=texto,
        font=('Arial', 14),
        width=5,
        height=2,
        command=lambda valor=texto: click_boton(valor))
    
    boton.grid(row=fila, column=columna, padx=2, pady=2)
    
boton_igual=tk.Button(root, text='=', font=('Arial', 14),width=22, height=2, bg='lightgreen', command=calcular)
boton_igual.grid(row=5, column=0, columnspan=4, padx=2, pady=2)
        
            
        
                    
    
    

root.mainloop()
    
    
    