from tkinter import *
from tkinter.ttk import * #para combobox
from tkinter.messagebox import * #ESTE ES EL QUE SIRVE!!
import PanelPrincipalB

class PanelDespacharContenedor_B:
    
    def __init__(self):
        print("Panel Despachar Contenedor PARTE II")
        
        self.pdcb=PanedWindow()
        self.lblTipoMercancia=Label()
        self.comboTipoMercancia= Spinbox()
        
        self.lblCiudadDestino=Label()
        self.comboCiudadDestino=Spinbox()
        
        self.btnDespachar=Button()
        self.btnAtras=Button()
        
    def atras(self):
        self.pdcb.destroy()
        back=PanelPrincipalB.PanelPrincipalB()
        back.vprb()
        
    def despacharContenedorB(self):
        mensaje= ("Contenedor a Despachar: "+"\n"+"\n"
        + "Tipo de Mercancia: " +self.comboTipoMercancia.get()+"\n"
        + "Ciudad de Destino: " +self.comboCiudadDestino.get())
        showinfo("Despachar Contenedor ", mensaje)
        
        showinfo("Despachar Contenedor ", "se despacho el contenedor")
        showerror("Despachar Contenedor ", "NO se despacho el contendor")
    
    def PanelDCB(self):
        
        self.pdcb.pack(fill=BOTH, expand=1)
        
        self.lblTipoMercancia=Label(self.pdcb, text="Tipo de Mercancia")
        self.lblTipoMercancia.pack(padx=10,pady=10)
        self.comboTipoMercancia=Spinbox(self.pdcb,values=("Televisor", "Juguete ", "Computador"))
        self.comboTipoMercancia.pack(padx=10,pady=10)
        self.lblCiudadDestino=Label(self.pdcb,text="Ciudad de Destino")
        self.lblCiudadDestino.pack(padx=10,pady=10)
        self.comboCiudadDestino=Spinbox(self.pdcb,values=("Bogota", "Cali", "Medellin", "Barranquilla","Cartagena",))
        self.comboCiudadDestino.pack(padx=10,pady=10)
        
        self.btnDespachar=Button(self.pdcb, text="Despachar",command=self.despacharContenedorB)
        self.btnDespachar.pack(padx=10, pady=10)
        
        self.btnAtras=Button(self.pdcb,text="Atras",command=self.atras)
        self.btnAtras.pack(padx=10,pady=10)
        self.pdcb.mainloop()