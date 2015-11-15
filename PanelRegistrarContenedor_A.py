from tkinter import *
from tkinter.ttk import * #para combobox
from tkinter.messagebox import * #ESTE ES EL QUE SIRVE!!

import PanelPrincipalA
class PanelRegistrarContenedor_A:
    
    def __init__(self,almacen):
        self.almacen = almacen
        print("PanelRegistrarContenedor A")
        self.prc=PanedWindow()
        self.lblCiudadOrigen=Label()
        self.comboCiudadOrigen=Spinbox()   
        
        self.lblCiudadDestino=Label()
        self.comboCiudadestino=Spinbox()
        
        self.lblTipoMercancia=Label()
        self.comboTipoMercancia=Spinbox()
        
        self.lblId=Label()
        self.txtId=Entry()
        
        self.btnRegistrar=Button()
        self.btnAtras=Button()
        
    def regre(self):
        self.prc.destroy()
        ret=PanelPrincipalA.PanelPrincipalA(self.almacen)
        ret.vpr()  
        
    def registrarContenedor(self):
        if(self.txtId.get()==""):
            showerror("FALTAN DATOS", "LLENE TODOS LOS CAMPOS POR FAVOR!")
        else:
            if self.comboCiudadOrigen.get() != self.comboCiudadestino.get():
                if (self.almacen.registrarContenedor(self.txtId.get(),self.comboTipoMercancia.get(),
                    self.comboCiudadOrigen.get(),self.comboCiudadestino.get())):
                    mensaje=("Contenedor a Registrar: "+"\n"+"\n"
                    +"Ciudad de Origen: "+ self.comboCiudadOrigen.get()+"\n"
                    + "Ciudad de Destino:  "+ self.comboCiudadestino.get()+"\n"
                    + "Tipo de Mercancia: "+ self.comboTipoMercancia.get()+"\n"
                    + "Id: "+ self.txtId.get())
                    showinfo(title="Registrar Contenedor ", message=mensaje)
                
                
                    print("bien")
                    showinfo("CORRECTO", "SE REGISTRO EL NUEVO CONTENEDOR")
                    for i in range(0,len(self.almacen.colaContenedor.items)):
                        print(self.almacen.colaContenedor.items[i].iden,self.almacen.colaContenedor.items[i].tipoMerc,self.almacen.colaContenedor.items[i].ciudOrigen,self.almacen.colaContenedor.items[i].ciudDestino)
                
                else:
                    showerror("ERROR", "NO SE AGREGARON LOS DATOS, POR FAVOR INTENTELO DE NUEVO")
                    print("mal")
            else:
                showerror("ERROR", "La ciudad de destino es igual a la ciudad de origen")
    
    def vRegisCont(self):
        
        self.prc.pack(fill=BOTH, expand=1)
        
        
        self.lblCiudadOrigen=Label(self.prc,text="Ciudad de Origen")
        self.lblCiudadOrigen.pack(padx=10,pady=10)
        self.comboCiudadOrigen=Spinbox(self.prc,values=("Bogota", "Cali", "Medellin", "Barranquilla","Cartagena"))
        self.comboCiudadOrigen.pack(padx=10,pady=10)
        
        self.lblCiudadDestino=Label(self.prc,text="Ciudad de Destino")
        self.lblCiudadDestino.pack(padx=10,pady=10)
        self.comboCiudadestino=Spinbox(self.prc,values=("Bogota", "Cali", "Medellin", "Barranquilla","Cartagena"))
        self.comboCiudadestino.pack(padx=10,pady=10)
        
        self.lblTipoMercancia=Label(self.prc,text="Tipo de Mercancia")
        self.lblTipoMercancia.pack(padx=10,pady=10)
        self.comboTipoMercancia=Spinbox(self.prc,values=("Televisor", "Juguete", "Computador"))
        self.comboTipoMercancia.pack(padx=10,pady=10)
        
        self.lblId=Label(self.prc,text="ID")
        self.lblId.pack(padx=10,pady=10)
        self.txtId=Entry(self.prc)
        self.txtId.pack(padx=10,pady=10)
        
        self.btnRegistrar=Button(self.prc,text="Registrar",command=self.registrarContenedor)
        self.btnRegistrar.pack(padx=10,pady=10)
        self.btnAtras=Button(self.prc,text="Atras",command=self.regre)
        self.btnAtras.pack(padx=10,pady=10)
        
        
        self.prc.mainloop()
