import socket
class Archivo:
    def escribir(self,hInicial,ip,hFinal):
        archivo =open("Archivo.txt","a")        
        archivo.write(hInicial+","+ip+","+hFinal+"\n")
        archivo.close()

    def leer(self):
        listaAux = []
        archivo = open("Archivo.txt","r")
        for linea in archivo:
            hInicio, ip, hFinal = linea.rstrip("\n").split(",")
            listaAux.append((hInicio,ip,hFinal))
        archivo.close()
        return listaAux
            
      

        
        
        
