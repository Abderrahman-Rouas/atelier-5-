#class utilisateur  #class utilisateur  #class utilisateur

class utilisateur:
    def set_nom_utilisateur(self, nom_utilisateur):
        self.__nom_utilisateur = nom_utilisateur
    def get_nom_utilisateur(self):
        return self.__nom_utilisateur

    def set_email_utilisateur(self, nom_email):
        self.__email_utilisateur = nom_email
    def get_email_utilisateur(self):
        return self.__email_utilisateur

    def set_mdp(self, mdp):
        self.__mdp = mdp

    def get_mdp(self):
        return self.__mdp

    def set_genre_utilisateur(self, genre_utilisateur):
        self.__genre_utilisateur = genre_utilisateur
        return self.__genre_utilisateur
    def get_genre_utilisateur(self):
        return self.__genre_utilisateur

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

#class professeur  #class professeur  #class professeur  #class professeur

class professeur(utilisateur) :

   def __init__(self,ppr,grade):
       self.__p=ppr
       self.__g=grade
   def get_ppr(self):
       return self.__p
   def set_ppr(self,new_ppr):
       self.__p=new_ppr

   def display(self):
       print("le ppr du professeur est: ", self.__p, "le grade est : ", self.__g)


#classe module #classe module #classe module #classe module #classe module
class module:
    def __init__(self,nom,volume_horaire,semsetre):
        self.__nom=nom
        self.__volume_horaire=volume_horaire
        self.__semstre=semsetre

    def set_nom(self, new_nom):
        self.__nom = new_nom

    def get_nom(self):
        return self.__nom

    def set_volume(self, new_volume):
        self.__volume_horaire = new_volume
    def get_volume(self):
        return self.__volume_horaire

    def set_semstre(self, new_semestre):
        self.__semstre = new_semestre
    def get_semestre(self):
        return self.__semstre
    def display(self):
        print("le nom du module est ",self.__nom,"le volume_horaire est ",self.__volume_horaire,"le semsetre est ",self.__semstre)

#class matiere  #class matiere  #class matiere  #class matiere
class matiere:
    def set_nom_matiere(self, nom_matiere):
        self.__nom_matiere = nom_matiere

    def get_nom_matiere(self):
        return self.__nom_matiere
    def set_peurcentage(self, peurcentage):
        self.__peurcetage = peurcentage

    def get_peurcentage(self):
        return self.__peurcetage

#class année_academique #class année_academique #class année_academique
class anne_academique:
    def set_annee(self, annee):
        self.__annee = annee

    def get_anne(self):
        return self.__annee

#class evaluation  #class evaluation  #class evaluation  #class evaluation  #class evaluation

class evaluation :
    def set_note(self, note):
        self.__note = note
    def get_note(self):
        return self.__note
#class etudiant
class etudiant (utilisateur):
    def set_code(self, code):
        self.__code = code

    def get_code(self):
        return self.__code

m=matiere()
m.set_nom_matiere("algebre")
print("le nom de la matiere est ",m.get_nom_matiere())
m.set_peurcentage(6)
print("le peurcentage est ",m.get_peurcentage())


print("----------------------------------------")

p=professeur(2,"cordinateur")
p.display()

print("----------------------------------------")

m=module("algebre",5,"s3")
m.display()
print("----------------------------------------")
a=anne_academique()
a.set_annee(2020)
print("l'année academique est ",a.get_anne())