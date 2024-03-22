"""ensembles de couleurs d’articles
On se place dans le cadre de deux magasins vendant le même type d’article. On suppose que l’on
mémorise dans 2 ensembles coul1 et coul2 les couleurs d’articles disponibles dans chaque magasin.
Chaque couleur est représentée par une chaine de caractères. Définir les fonctions suivantes :
- une fonction afficherCouleurs prenant en paramètre un ensemble de couleurs et permettant
d’afficher les couleurs de l’ensemble.
- une fonction dispo prenant une couleur et un ensemble de couleurs en paramètre et permettant
de savoir si la couleur appartient à l’ensemble de couleurs ou pas.
- une fonction enCommun prenant 2 ensembles de couleurs en paramètres et renvoyant l’ensemble
des couleurs communes aux 2 ensembles.
- une fonction ajouter prenant en paramètres une couleur et un ensemble de couleurs coul et
permettant d’ajouter la couleur à l’ensemble de couleurs coul
- une fonction collection prenant en paramètre deux ensembles de couleurs et renvoyant en
résultat l’ensemble résultant de l’union des deux ensembles
- une fonction diff prenant en paramètres 2 ensembles de couleurs coul1 et coul2 et renvoyant
l’ensemble des couleurs présentes dans coul1 mais pas dans coul2.
En utilisant les fonctions précédentes, le programme doit :
- afficher la liste des couleurs disponibles pour chaque magasins
- afficher si la couleur « vert » est disponible dans chacun des magasins
- afficher les couleurs disponibles dans les deux magasins (chaque couleur en un seul exemplaire)
- saisir une couleur d’un nouvel article et l’ajouter au stock du premier magasin. Afficher le
nouveau stock
- afficher les couleurs disponibles dans le magasin 1 mais pas dans le magasin 2"""





def afficherCouleurs(ensembel: set):

    for col in ensembel:
         print(col)


afficherCouleurs(ensembel={"rouge", "vert", "bleu", "jaune"})

print(50*"=")

def dispo(ensemble2: set ,couleur:str):
          if couleur in ensemble2:
         
               print("la couleur deja exist")
          else:
               print("ya pas ici ") 

dispo(ensemble2={"red", "vert", "bleu", "jaune"},couleur="r")           

print(50*"=")

def dispoà(ens1: set ,ens2:set):
        """
        ensCommun=set()
        for i in ens1:
          for j in ens2:
               if i == j:
                 ensCommun.add(i)
        print(ensCommun)         
        """   
        print(ens1  & ens2)      
         
            

dispoà(ens1={"red", "vert", "bleu", "jaune"},ens2={"red","green"})


print(50*"=")
#####Ajputer
def ajouter(ens: set ,couleur:str) -> set:
         
    ens.add(couleur)
    print(ens)
ajouter(ens={"red", "vert", "bleu", "jaune"},couleur="yellow")

####collction
print(50*"=")

def collection(ens1: set ,ens2:set):
         
        print(ens1^ ens2)      
         
            

collection(ens1={"red", "vert", "bleu", "jaune"},ens2={"red","green"})

####collction
print(50*"=")

def dif(ense1: set ,ense2:set):
         
        print(ense1 - ense2)      
         
            

dif(ense1={"red", "vert", "bleu", "jaune"},ense2={"red","green"})

print(50*"à")

def founMagazin(Magasin:set):
 for nom_magasin, ensemble_couleurs in Magasin.items():
        print("Couleurs disponibles pour le magasin", nom_magasin, ":")
        afficherCouleurs(ensemble_couleurs)
        dispo(ensemble_couleurs,"vert") 
        print("les couleurs disponibles dans les deux magasin")
       
        collection(magasin1,magasin2)
        ajouter(magasin1,"pink")
       # afficherCouleurs(ensemble_couleurs)
        print()
       
 print("les couleurs disponibles dans le magasin 1 mais pas dans le magasin 2")
 dif(magasin1,magasin2)              
       
magasin1 = {"rouge", "vert", "bleu", "jaune"}
magasin2 = {"rouge", "noir"}

Magasin = {"Magasin 1": magasin1, "Magasin 2": magasin2}

      
founMagazin(Magasin)








