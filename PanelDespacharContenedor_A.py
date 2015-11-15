from tkinter import *
from tkinter.ttk import * #para combobox
from tkinter.messagebox import * #ESTE ES EL QUE SIRVE!!
import PanelPrincipalA

class PanelDespacharContenedor_A:
    
    def __init__(self,almacen):
        print("Panel Despachar Contenedor PARTE I")
        self.almacen = almacen
        self.pdc=PanedWindow()
        self.lblTipoMercancia=Label()
        self.comboTipoMercancia= Spinbox()
        
        self.lblCiudadDestino=Label()
        self.comboCiudadDestino=Spinbox()
        
        self.btnDespachar=Button()
        self.btnAtras=Button()
        
    def atras(self):
        self.pdc.destroy()
        back=PanelPrincipalA.PanelPrincipalA(self.almacen)
        back.vpr()
        
    def despacharContenedor(self):
        mensaje= ("Contenedores a Despachar: "+"\n"+"\n"
        + "Tipo de Mercancia: " +self.comboTipoMercancia.get()+"\n"
        + "Ciudad de Destino: " +self.comboCiudadDestino.get())
        showinfo("Despachar Contenedor ", mensaje)
        if self.almacen.despacharCont(self.comboTipoMercancia.get(),self.comboCiudadDestino.get()):
            print("no vacia")
            showinfo("Despachar Contenedor ", "se despacharon los contenedores")
        else:
            print("vacia")
            showerror("Despachar Contenedor ", "No hay contenedores con ese tipo de mercancía para despachar")
    
    def PanelDC(self):
        
        self.pdc.pack(fill=BOTH, expand=1)
        
        self.lblTipoMercancia=Label(self.pdc, text="Tipo de Mercancia")
        self.lblTipoMercancia.pack(padx=10,pady=10)
        self.comboTipoMercancia=Spinbox(self.pdc,values=("Televisor", "Juguete", "Computador"))
        self.comboTipoMercancia.pack(padx=10,pady=10)
        self.lblCiudadDestino=Label(self.pdc,text="Ciudad de Destino")
        self.lblCiudadDestino.pack(padx=10,pady=10)
        self.comboCiudadDestino=Spinbox(self.pdc,values=("Bogota", "Cali", "Medellin", "Barranquilla","Cartagena",))
        self.comboCiudadDestino.pack(padx=10,pady=10)
        
        self.btnDespachar=Button(self.pdc, text="Despachar",command=self.despacharContenedor)
        self.btnDespachar.pack(padx=10, pady=10)
        
        self.btnAtras=Button(self.pdc,text="Atras",command=self.atras)
        self.btnAtras.pack(padx=10,pady=10)
        self.pdc.mainloop()
