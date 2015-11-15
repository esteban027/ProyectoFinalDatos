from tkinter import *
import PanelRegistrarContenedor_B
import PanelDespacharContenedor_B

from tkinter.messagebox import * #ESTE ES EL QUE SIRVE!!

class PanelPrincipalB:
    
    def __init__(self):
        print("Panel Principal Parte Dos!! ")
        
        self.pvpd=PanedWindow()
        
        self.lblparteb=Label()
        self.btnRegistrarContenedor=Button()
        self.btnAlmacenarContenedor=Button()
        self.btnDespacharContenedor=Button()
        self.btnSalir=Button()
        self.titulo=Label()
        
    def desCon(self):
        self.pvpd.destroy()
        desp=PanelDespacharContenedor_B.PanelDespacharContenedor_B()
        desp.PanelDCB()
    
    def almaC(self):
        print("ALMACENAR CONTENEDOR")
        showinfo("ALMACENAR CONTENEDOR", "El Contenedor se Ha Almacenado")
        showerror("ALMACENAR CONTENEDOR", "El Contenedor NO se Almaceno")
        
        
    def rConb(self):
        self.pvpd.destroy()
        rcb=PanelRegistrarContenedor_B.PanelRegistrarContenedor_B()
        rcb.vRegisCont()
        
    
    def vprb(self):
        
        self.pvpd.pack(fill=BOTH, expand=1)
        self.pvpd.config(bg="Blue")
        
        self.lblparteb=Label(self.pvpd,text="PARTE II", font=("Comic Sans MS", 14), background="#091DF0")
        self.lblparteb.pack(padx=10,pady=10)
        
        self.btnSalir= Button(self.pvpd, text=" SALIR ", command=self.pvpd.destroy)
        self.btnSalir.pack(side=BOTTOM,padx=10,pady=10)
        self.btnDespacharContenedor= Button(self.pvpd, text=" DESPACHAR CONTENEDOR ",command=self.desCon)# , font=("Comic Sans MS", 10))
        self.btnDespacharContenedor.pack(side=BOTTOM,padx=10,pady=10)
        self.btnAlmacenarContenedor=Button(self.pvpd, text=" ALMACENAR CONTENEDOR ",command= self.almaC)
        self.btnAlmacenarContenedor.pack(side=BOTTOM,padx=10, pady=10)
        self.btnRegistrarContenedor= Button(self.pvpd, text=" REGISTRAR CONTENDOR ", command=self.rConb)
        self.btnRegistrarContenedor.pack(side=BOTTOM,padx=10,pady=10)
        
        self.pvpd.mainloop()
