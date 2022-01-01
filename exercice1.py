class vecteur2D:


    def __init__(self, x0=0, y0=0): #Constructeur avec parametres par defaut

        self.x = x0  # initialisation de x et y
        self.y = y0

    def display(self):
        print(self.x,self.y)


v1=vecteur2D()
v2=vecteur2D(4,6)
print("Constructeur sans parametres par defaut= ")
v1.display()
print("Constructeur avec parametres par defaut= ")
v2.display()


