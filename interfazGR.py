from tkinter import *
from tkinter import ttk
from distutils.cmd import Command
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from automatas import *
from gramaticas import *
from ayudagr import *



class bienvenida3:
    def __init__(self):
        self.win3 = Tk()
        self.win3.resizable(True,False) # Redimensionar la ventana
        self.win3.title('..::ADF::..') # Titulo de la ventana
        self.win3.geometry('1000x700') # Tamaño de la ventana
        self.Centrar2(self.win3, 1000, 700) # Centrar la ventana
        self.win3.config(bg='#102027')
        self.Ventana2() # Llamar a la ventana

    def Centrar2(self, r, ancho, alto):
        altura_pantalla = r.winfo_screenheight() # Altura de la pantalla
        ancho_pantalla = r.winfo_screenwidth() # Ancho de la pantalla

        print("Altura de la pantalla: ", altura_pantalla)
        print("Ancho de la pantalla: ", ancho_pantalla)

        x = (ancho_pantalla // 2) - (ancho // 2) # Posicion de la ventana
        y = (altura_pantalla // 2) - (alto // 2) # Posicion de la ventana
        r.geometry(f'+{x}+{y}') # Posicion de la ventana

    def Ventana2(self):
        Label(self.win3, text="...:::...Creación de Automatas...:::...", font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=52).place(x=200, y=20)
        Label(self.win3, text="Ingrese el nombre del automata:", font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=52).place(x=90, y=50)
        Label(self.win3, text="Ingrese los estados del automata separados por una coma: ", font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=52).place(x=90, y=80)
        Label(self.win3, text="Ingrese el alfabeto del automata separados por una coma: ", font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=52).place(x=90, y=110)
        Label(self.win3, text="Ingrese el estado inicial del automata: ", font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=52).place(x=90, y=140)
        Label(self.win3, text="Ingrese los estados de aceptacion del automata separados por una coma: ", font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=52).place(x=90, y=170)
        Label(self.win3, text="Ingrese las transiciones del automata separados por una coma: ", font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=52).place(x=90, y=200)
        
        self.content1 = StringVar()
        self.content2 = StringVar()
        self.content3 = StringVar()
        self.content4 = StringVar()
        self.content5 = StringVar()
        self.content6 = StringVar()
        
        Entry(self.win3, textvariable=self.content1,font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=20).place(x=720, y=50)
        Entry(self.win3, textvariable=self.content2,font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=20).place(x=720, y=80)
        Entry(self.win3, textvariable=self.content3,font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=20).place(x=720, y=110)
        Entry(self.win3, textvariable=self.content4,font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=20).place(x=720, y=140)
        Entry(self.win3, textvariable=self.content5,font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=20).place(x=720, y=170)
        Entry(self.win3, textvariable=self.content6,font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=20).place(x=720, y=200)

       
        Button(self.win3, text="Calcular",command=self.calc, font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=15).place(x=420, y=280)
        Button(self.win3, text="ayuda",command=help, font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=15).place(x=420, y=320)
        Button(self.win3, text="Regresar",command=lambda:self.win3.destroy(), font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=15).place(x=420, y=360)
    
        
        
        self.win3.mainloop()

    
    
    def calc (self):
        txt1 = self.content1.get()
        txt2 = self.content2.get()
        txt3 = self.content3.get()
        txt4 = self.content4.get()
        txt5 = self.content5.get()
        txt6 = self.content6.get()
      
        lista_automatas = [] # Vacia inicialmente
        
        while(True):
            #print("Creacion de un automata")
            nombre = txt1
            estados = txt2
            alfabeto = txt3
            estado_inicial = txt4
            estados_aceptacion = txt5
            transiciones = txt6

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
            fin=print(automata.__str__())
            Label(self.win3, text=txt6, font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=50).place(x=75, y=620)


        

    


    

    


    
        
#b = bienvenida2()