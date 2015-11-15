from tkinter import *
import PanelRegistrarContenedor_A
import PanelDespacharContenedor_A
import time

from tkinter.messagebox import * #ESTE ES EL QUE SIRVE!!

class PanelPrincipalA:
    
    def __init__(self,almacen):
        print("Panel Principal Parte Uno!! ")
        self.almacen = almacen
        self.pvpu=PanedWindow()
        
        self.lblpartea=Label()
        self.btnRegistrarContenedor=Button()
        self.btnAlmacenarContenedor=Button()
        self.btnDespacharContenedor=Button()
        self.btnSalir=Button()
        self.titulo=Label()
        
    def desCon(self):
        self.pvpu.destroy()
        desp=PanelDespacharContenedor_A.PanelDespacharContenedor_A(self.almacen)
        desp.PanelDC()
    
    def almaC(self):
        print("ALMACENAR CONTENEDOR")
        if self.almacen.ubicarContPila():
            showinfo("ALMACENAR CONTENEDOR", "Se almacenaron todos los contenedores")
        else:
            showerror("ALMACENAR CONTENEDOR", "No hay contenedores para almacenar")
        
        
    def rCon(self):
        self.pvpu.destroy()
        rc=PanelRegistrarContenedor_A.PanelRegistrarContenedor_A(self.almacen)
        rc.vRegisCont()
    def salir(self):
        hFinal = time.strftime("%H:%M:%S")
        self.almacen.escribirArch(hFinal)
        self.pvpu.destroy()       
    
    def vpr(self):
        
        self.pvpu.pack(fill=BOTH, expand=1)
        self.pvpu.config(bg="White")
        
        self.lblpartea=Label(self.pvpu,text="PARTE I", font=("Comic Sans MS", 14), background="#FFFFFF")
        self.lblpartea.pack(padx=10,pady=10)
        
        self.btnSalir= Button(self.pvpu, text=" SALIR ", command=self.salir)
        self.btnSalir.pack(side=BOTTOM,padx=10,pady=10)
        self.btnDespacharContenedor= Button(self.pvpu, text=" DESPACHAR CONTENEDOR ",command=self.desCon)# , font=("Comic Sans MS", 10))
        self.btnDespacharContenedor.pack(side=BOTTOM,padx=10,pady=10)
        self.btnAlmacenarContenedor=Button(self.pvpu, text=" ALMACENAR CONTENEDOR ",command= self.almaC)
        self.btnAlmacenarContenedor.pack(side=BOTTOM,padx=10, pady=10)
        self.btnRegistrarContenedor= Button(self.pvpu, text=" REGISTRAR CONTENDOR ", command=self.rCon)
        self.btnRegistrarContenedor.pack(side=BOTTOM,padx=10,pady=10)
        
        self.pvpu.mainloop()
