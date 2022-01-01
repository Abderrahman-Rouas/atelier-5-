class etudiant :
    def __init__(self,nom,prenom,age,cne,moyenne):  #constructeur avec 4 parametres
        self.n=nom
        self.p=prenom
        self.a=age
        self.c=cne
        self.m=moyenne
mylist = [                #creation d'une liste de type etudiant
etudiant("ali","bakkali",22,"p1200",16),
etudiant("ahmed","said",19,"p253",12),
etudiant("slim","shady",10,"c235",15),
etudiant("karim","shay",36,"d2365",17)

]


mylist.sort(key=lambda etudiant:etudiant.a )   #fonction pour trier la fonction selon l'age

print("la liste trier selon l'age est : ")
for i in mylist :          #boucle pour afficher la liste trier selon l'age
    print(i.n,i.p,i.a,i.c,i.m)
print("------------------------------------------------")
mylist.sort(key=lambda etudiant:etudiant.m)  #fonction pour trier la fonction selon moyenne
print("la liste trier selon le moyenne est : ")
for i in mylist :           #boucle pour afficher la liste trier selon l'age
    print(i.n,i.p,i.a,i.c,i.m)