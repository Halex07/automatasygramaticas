from tkinter import *
from tkinter import ttk
from distutils.cmd import Command
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from automatas import *
from gramaticas import * 
from interfazAFD import *
from interfazGR import *



class bienvenida():
    def __init__(self):
        self.win = Tk()
        self.win.resizable(True,False) # Redimensionar la ventana
        self.win.title('..::BIENVENIDO::..') # Titulo de la ventana
        self.win.geometry('1000x700') # Tamaño de la ventana
        self.Centrar(self.win, 1000, 700) # Centrar la ventana
        self.win.config(bg='#102027')
        self.Ventana() # Llamar a la ventana

    def Centrar(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight() # Altura de la pantalla
        ancho_pantalla = r.winfo_screenwidth() # Ancho de la pantalla

        print("Altura de la pantalla: ", altura_pantalla)
        print("Ancho de la pantalla: ", ancho_pantalla)

        x = (ancho_pantalla // 2) - (ancho // 2) # Posicion de la ventana
        y = (altura_pantalla // 2) - (alto // 2) # Posicion de la ventana
        r.geometry(f'+{x}+{y}') # Posicion de la ventana

    def Ventana(self):
        self.frame = Frame(height=1000, width=700) # Se coloca sobre la ventana
        self.frame.config(bg='#37474f')
        self.frame.pack(padx=10, pady=10)
        Label(self.frame, text="Bienvenidos 2", font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=20).place(x=250, y=50)
        Label(self.frame, text="Lenguajes Formales y de Programación N", font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=50).place(x=75, y=80)
        Label(self.frame, text="Henry Alexander García Montúfar", font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=50).place(x=75, y=110)
        Label(self.frame, text="Carnet:201407049", font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=50).place(x=75, y=140)

    


        self.content = StringVar()
        self.content1 = StringVar()
        self.content2 = StringVar()
        self.content3 = StringVar()
        self.content4 = StringVar()
        self.content5 = StringVar()
        self.content6 = StringVar()


        Entry(self.frame, textvariable=self.content,font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=20).place(x=250, y=180)

        Button(self.frame, text="ADF",command=bienvenida2, font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=15).place(x=275, y=240)
        Button(self.frame, text="GR",command=bienvenida3, font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=15).place(x=275, y=280)
        Button(self.frame, text="Cargar Archivo",command=self.cargar, font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=15).place(x=275, y=320)
        Button(self.frame, text="Exit",command=lambda:self.win.destroy(), font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=15).place(x=275, y=360)
    
        
        
        self.frame.mainloop()

    def decir_hola(self):
        print("Hola mundo de python y de lenguajes")
        var = self.content.get()
        print("Nuestro entry contiene: ", var)                                                   
    
    def cargar (self):
        arch = filedialog.askopenfilename(title = "Seleccionar Archivo",filetypes = ((".* Files","*.*"),))
        #Buffer.cargar_buffer(import_file_path)
        with open(arch,"r+") as doc:
            texto1=doc.readline()
            Label(self.frame, text="Automata: "+texto1, font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=20).place(x=250, y=440)
            texto2=doc.readline()
            Label(self.frame, text=texto2, font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=50).place(x=75, y=470)
            texto3=doc.readline()
            Label(self.frame, text=texto3, font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=50).place(x=75, y=500)
            texto3=doc.readline()
            Label(self.frame, text=texto3, font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=50).place(x=75, y=530)

            texto4=doc.readline()
            Label(self.frame, text=texto4, font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=50).place(x=75, y=560)
            texto5=doc.readline()
            Label(self.frame, text=texto5, font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=50).place(x=75, y=590)
            texto6=doc.readline()
        

        texto1 = self.content1.get()
        texto2 = self.content2.get()
        texto3 = self.content3.get()
        texto4 = self.content4.get()
        texto5 = self.content5.get()
        texto6 = self.content6.get()

   
        lista_automatas = [] # Vacia inicialmente
        
        while(True):
            #print("Creacion de un automata")
            nombre = texto1
            estados = texto2
            alfabeto = texto3
            estado_inicial = texto4
            estados_aceptacion = texto5
            transiciones = texto6

            estados_ = estados.split(",") # "A,B,C" -> ["A", "B", "C"]
            alfabeto_ = alfabeto.split(",")
            estados_aceptacion_ = estados_aceptacion.split(",")
            transiciones_ = transiciones.split(";") # A,0,B ; A,1,B ; A,1,C -> ["A,0,B", "A,1,B", "A,1,C"]

            

            if(not estado_inicial in estados_ and not estados_aceptacion_ in estados_):
                print("El estado inicial o los estados de aceptacion no estan en el conjunto de estados")
                continue
    
    # verificar que el alfabeto no sea parte de los estados
            salir = False
            for estado in estados:
                if(estado in alfabeto_):
                    print("El alfabeto no puede ser parte de los estados")
                    salir = True
                    break
            if(salir):
                continue
    
    # creacion de transiciones por separado
            transiciones__ = []
            for t in transiciones_:
                t = t.split(",") # ["A,0,B", "A,1,B", "A,1,C"] -> [ ["A", "0", "B"], ["A", "1", "B"], ["A", "1", "C"]
                if(not t[0] in estados_ or not t[2] in estados_):
                    print("El origen o el destino de una transicion no esta en el conjunto de estados")
                    salir = True
                    break
            transiciones__.append(Transicion(t[0], t[1], t[2]))
        # FORMA DE INGRESO DE TRANSICIONES
        # Manual
        # origen, alfabeto, destino ; origen, alfabeto, destino ; origen, alfabeto, destino

        # Archivo de entrada
        # origen, alfabeto; destino
        # origen, alfabeto; destino
        # origen, alfabeto; destino
    
            if(salir):
                continue

         # Creacion del automata
            automata = Automata(nombre, estados_, alfabeto_, estado_inicial, estados_aceptacion_, transiciones__)
            lista_automatas.append(automata)

        # Preguntar si desea agregar otro automata
            
            opcion = "n"
            if(opcion == "n"):
                break

        print("Automatas ingresados: ")
        for automata in lista_automatas:
            print(automata.__str__())
            


            

        
        

        

    


    

    


    
        
a = bienvenida()
