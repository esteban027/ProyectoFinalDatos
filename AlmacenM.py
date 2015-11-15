import PArchivo
import time
import socket
import Stack
import Contenedor
import Cola
#import Lista

class AlmacenM:
    def __init__(self):
        self.archivo = PArchivo.Archivo()
        self.hInicial = time.strftime("%H:%M:%S")
        self.ip = socket.gethostbyname(socket.gethostname())
        self.pilaJug = Stack.Stack()
        self.pilaTele = Stack.Stack()
        self.pilaPc = Stack.Stack()
        self.colaContenedor = Cola.Cola()
        #listaContenedor
        
    def registrarContenedor(self,iden,tipoMerc,ciudOrigen,ciudDestino):
        contenedor = Contenedor.Contenedor(iden,tipoMerc,ciudOrigen,ciudDestino)
        if self.verificarCola(iden):
            if contenedor.verificarDoc(tipoMerc,ciudOrigen,ciudDestino) and contenedor.verificarFormatoId(iden):          
                self.colaContenedor.encolar(contenedor)
                return True
            else:
                return False
        else:
            return False

    def ubicarContPila(self):
        if not self.colaContenedor.esVacia():
            while len(self.colaContenedor.items) > 0:
                aux = self.colaContenedor.desEncolar()
                if aux.tipoMerc == "Juguete":
                    self.pilaJug.push(aux)
                elif aux.tipoMerc == "Televisor":
                    self.pilaTele.push(aux)
                else:
                    self.pilaPc.push(aux)
                            
            return True
        else:
            return False
        
    def despacharCont(self,tipoMerc,ciudDestino):
        colaAux = Cola.Cola()
        print(tipoMerc)
        if tipoMerc == "Juguete":
            if not self.pilaJug.isEmpty():
                while not self.pilaJug.isEmpty():
                    if self.pilaJug.peek().ciudDestino == ciudDestino:
                        self.pilaJug.pop()
                    else:
                        colaAux.encolar(self.pilaJug.pop())
                while not colaAux.esVacia():
                    self.pilaJug.push(colaAux.desEncolar())
                return True
            else:
                return False
                
        elif tipoMerc == "Televisor":
            if not self.pilaTele.isEmpty():
                while not self.pilaTele.isEmpty():
                    if self.pilaTele.peek().ciudDestino == ciudDestino:
                        self.pilaTele.pop()
                    else:
                        colaAux.encolar(self.pilaTele.pop())
                while not colaAux.esVacia():
                    self.pilaTele.push(colaAux.desEncolar())
                return True
            else:
                return False
        else:
            if not self.pilaPc.isEmpty():
                while not self.pilaPc.isEmpty():
                    if self.pilaPc.peek().ciudDestino == ciudDestino:
                        self.pilaPc.pop()
                    else:
                        colaAux.encolar(self.pilaPc.pop())
                while not colaAux.esVacia():
                    self.pilaPc.push(colaAux.desEncolar())
                return True
            else:
                return False
                       
        
    def escribirArch(self,hFinal):
        self.archivo.escribir(self.hInicial,self.ip,hFinal)

    def verificarCola(self,iden):
        for i in range(0,len(self.colaContenedor.items)):
            if iden == self.colaContenedor.items[i].iden:
                return False
        return True

        
    
                                                                        
        

##almacen = AlmacenM()        
####print(almacen.archivo.leer("insertenombreaqui.txt"))
##almacen.registrarContenedor("asdfg-12345","Juguete","cOuno","cDuno")
##almacen.registrarContenedor("gfdsa-12435","Televisor","cOdos","cDdos")
##almacen.registrarContenedor("asert-12345","Juguete","cOtres","cDtres")
##almacen.registrarContenedor("as34g-12345","Juguete","cOcuatro","cDcuatro")
##almacen.ubicarContPila()
####for i in range(0,len(almacen.colaContenedor.items)):
####    print(almacen.colaContenedor.items[i].iden)
####print(almacen.pilaTele.items[0].iden)
##for i in range(0,len(almacen.pilaJug.items)):
##              print(almacen.pilaJug.items[i].iden)     
####print(almacen.pilaJug)
####print(almacen.pilaTele)


    


    
