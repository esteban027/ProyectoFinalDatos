class Contenedor:

    def __init__(self,iden,tipoMerc,ciudOrigen,ciudDestino):
        self.iden = iden
        self.tipoMerc = tipoMerc
        self.ciudOrigen = ciudOrigen
        self.ciudDestino = ciudDestino

    def verificarDoc(self,tipoMerc,ciudOrigen,ciudDestino):
        if (tipoMerc.isalpha() and ciudOrigen.isalpha() and ciudDestino.isalpha()):
            return True
        else:
            return False
        
    def verificarFormatoId(self,iden):
        if len(iden) == 11:
            if(iden[0:5]).isalpha()  and iden[5] == "-" and (iden[6:]).isdigit():
                return True
            else:
                return False
        else:
            return False
        
        
        
            
        
        


