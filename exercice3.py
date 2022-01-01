class rectangle:
    def __init__(self,longueur=2,largeur=6):  #initialisation par des valeurs par defauts
        self.lo=longueur
        self.la=largeur
        self.nom="rectangle"
    def display(self):
      print("la surface de ",self.nom,"est : ",self.lo*self.la) #affichage des donnés

class carre(rectangle):   #class carre heritant de class rectangle
    def __init__(self,num=6):  #initialisation du constructeur par defaut
        self.n=num
        rectangle.__init__(self, num, num) #surchage du constructeur
        self.nom = "carre"
    def display(self):       #fonction d'affichage pour la classe carre
        print("le  ", self.nom, "est : ", self.n * self.n)

r=rectangle(3,3)
r.display()
c=carre()
c.display()