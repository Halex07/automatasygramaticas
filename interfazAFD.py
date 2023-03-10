from tkinter import *
from tkinter import ttk
from distutils.cmd import Command
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from automatas import *
from gramaticas import *
from ayudaafd import *
import functools 

class bienvenida2():
    def __init__(self):
        self.win2 = Tk()
        self.win2.resizable(True,False) # Redimensionar la ventana
        self.win2.title('..::ADF::..') # Titulo de la ventana
        self.win2.geometry('1000x700') # Tamaño de la ventana
        self.Centrar2(self.win2, 1000, 700) # Centrar la ventana
        self.win2.config(bg='#102027')
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
        self.cont1 = Frame(height=1000, width=700) # Se coloca sobre la ventana
        self.cont1.config(bg='#37474f')
        self.cont1.pack(padx=10, pady=10)
        Label(self.cont1, text="...:::...Creación de Automatas...:::...", font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=52).place(x=200, y=20)
        Label(self.cont1, text="Ingrese el nombre del automata:", font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=52).place(x=90, y=50)
        Label(self.cont1, text="Ingrese los estados del automata separados por una coma: ", font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=52).place(x=90, y=80)
        Label(self.cont1, text="Ingrese el alfabeto del automata separados por una coma: ", font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=52).place(x=90, y=110)
        Label(self.cont1, text="Ingrese el estado inicial del automata: ", font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=52).place(x=90, y=140)
        Label(self.cont1, text="Ingrese los estados de aceptacion del automata separados por una coma: ", font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=52).place(x=90, y=170)
        Label(self.cont1, text="Ingrese las transiciones del automata separados por una coma: ", font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=52).place(x=90, y=200)
        
        

        self.entrada1 = StringVar()
        Entry(self.cont1, textvariable=self.entrada1, font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=20).place(x=720, y=50)
        self.content2 = StringVar()
        Entry(self.cont1, textvariable=self.content2, font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=20).place(x=720, y=80)
        self.content3 = StringVar()
        Entry(self.cont1, textvariable=self.content3,font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=20).place(x=720, y=110)
        self.content4 = StringVar()
        Entry(self.cont1, textvariable=self.content4,font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=20).place(x=720, y=140)
        self.content5 = StringVar()
        Entry(self.cont1, textvariable=self.content5,font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=20).place(x=720, y=170)
        self.content6 = StringVar()
        Entry(self.cont1, textvariable=self.content6,font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=20).place(x=720, y=200)

       
        Button(self.cont1, text="Calcular",command=self.calc, font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=15).place(x=420, y=280)
        Button(self.cont1, text="Cargar Archivo",command=helpafd, font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=15).place(x=420, y=320)
        Button(self.cont1, text="Regresar",command=lambda:self.win2.destroy(), font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=15).place(x=420, y=360)


        
        self.win2.mainloop(self.cont1.mainloop())
        

        
    
        
        

    

        
       

        
        

        
    def calc (self):

        n1=self.entrada1.get()
        print(n1)
        
         #labels
        Label(self.frame, text=self.entrada1.get(), font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=20).place(x=250, y=440)
        Label(self.frame, text="", font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=50).place(x=75, y=470)
        Label(self.frame, text="", font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=50).place(x=75, y=500)
        Label(self.frame, text="", font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=50).place(x=75, y=530)
        Label(self.frame, text="self.txt5", font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=50).place(x=75, y=560)
        Label(self.frame, text="self.txt6", font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=50).place(x=75, y=590)



    

       
        
        

    

        #fin labels
        



      
        lista_automatas = [] # Vacia inicialmente
        
        while(True):
            #print("CrAeacion de un automata")
            nombre = "A"
            estados = "A,B,C"
            alfabeto = "0,1"
            estado_inicial = "A"
            estados_aceptacion = "C"
            transiciones = "A,0,B;B,1,C"

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
            Label(self.win2, text=self.txt6, font=('Times New Roman',15), fg='#000000', bg='#ff6f00', width=50).place(x=75, y=620)





    

    


    
        
    