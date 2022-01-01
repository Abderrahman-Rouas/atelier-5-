class Point:


    def __init__(self, x=0.0, y=0.0):     # Initialisation avec valeurs par defaut

        self.a = float(x)
        self.b = float(y)

class Segment:              #declaration class segment
    def __init__(self, x1, y1, x2, y2): #constructeur avec 4 valeurs

        self.orig = Point(x1, y1)   #deux objets de classe point
        self.extrem = Point(x2, y2)
    def display(self):
        print("[(",self.orig.a,",", self.orig.b,")", "(",self.extrem.a,"," ,self.extrem.b,")]")

s = Segment(1, 2, 3, 4)
s.display()