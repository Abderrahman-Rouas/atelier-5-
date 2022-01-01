class vecteur2D:

    def __init__(self, x0=0, y0=0): #Constructeur avec parametres par defaut

        self.x = x0  # initialisation de x et y
        self.y = y0

    def display(self): #fonction d'affichage
        print(self.x,self.y)

    def __add__(self, other):  #fonction pour additionner deux vecteurs

        a=self.x+other.x
        b=self.y+other.y
        print("la somme des deux vecteurs est : ",a,b)

v1=vecteur2D(2,3)   #premier vecteur
print("le premier vecteur est ")
v1.display()

v2=vecteur2D(4,6) #deuxieme vecteur
print("le deuxieme vecteur est : " )
v2.display()

v3=v1+v2      #la somme des deux vecteurs



