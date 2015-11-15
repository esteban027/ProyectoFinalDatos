from tkinter import *
import PanelPrincipalA
import PanelPrincipalB
import PanelDespacharContenedor_A
import AlmacenM

class Principal:
    
    def __init__(self):
        
        self.cuadro=Tk()
        self.panelPricipal=PanedWindow()
        self.almacen = AlmacenM.AlmacenM()
        self.lblGestion=Label()
        self.btnParteA=Button()
        self.btnParteB=Button()
        self.btnSalir=Button()
        
    def parteA(self):
        self.panelPricipal.destroy()
        a=PanelPrincipalA.PanelPrincipalA(self.almacen)
        a.vpr()
    def parteB(self):
        self.panelPricipal.destroy()
        b=PanelPrincipalB.PanelPrincipalB()
        b.vprb()
    
    def venPartes(self):
        
        self.cuadro.title("GESTION DE CONTENEDORES ")
        
    
        self.panelPricipal.pack(fill=BOTH, expand=1)
        self.panelPricipal.config(bg="White")
        
        self.lblGestion=Label(self.panelPricipal,text="GESTION DE CONTENEDORES", font=("Comic Sans MS", 14), background="#FFFFFF")
        self.lblGestion.pack(padx=10,pady=10)
        self.btnParteA=Button(self.panelPricipal,text="Parte I", command=self.parteA)
        self.btnParteA.pack(padx=10, pady=10)
        
        self.btnParteB=Button(self.panelPricipal, text="Parte II", command=self.parteB)
        self.btnParteB.pack(padx=10, pady=10)
        
        self.btnSalir=Button(self.panelPricipal,text="SALIR", command=self.cuadro.destroy)
        self.btnSalir.pack(padx=10, pady=10)
        
        
        self.panelPricipal.mainloop()

a=Principal()
a.venPartes()
