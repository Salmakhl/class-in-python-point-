class point():
    def __init__(self,abscisse=0,ordonne=0):
        self.__abscisse = abscisse
        self.__ordonne = ordonne

    def getabscisse(self):
        return self.__abscisse
    

    def getordonne(self):
        return self.__ordonne 
    

    def set_abscisse(self):
        return self.__abscisse
    
    def set_ordonne(self):
       return self.__ordonne



    
    def norme(self):
        print ("la norme est :",format(((self.getabscisse())**2+(self.getordonne())**2)**1/2))

    #def norme
    
p1=point(5,7)
p1.norme()


    
    
