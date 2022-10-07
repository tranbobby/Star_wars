import Acteur
import Film
import Gentil
import Mechan
import Personnage

# Exercice 5


def parcours_collection(collection):
    for i in collections:
        print(collections[i])


# Exercice 2
film1 = Film.Film("Un nouvel espoir", 1977, 4, 180000, 250000, {}, {})
film2 = Film.Film("L'Empire contre-attaque", 1980, 5, 2900000, 3500000, {}, {})
film3 = Film.Film(str(input("Entrez le nom du film : ")), int(input("entrez la date : ")), int(input(
    "entrez le numero d'épisode : ")), int(input("entrez la cout de l'épisode : ")), int(input("entrez la recette de l'épisode : ")), {}, {})
print(film3)

# film3 = Film.Film("12", 12, 12, 12, 12, {}, {})
film4 = Film.Film("La Menace fantôme", 1999, 1, 2900000, 3500000, {}, {})

# Exercice 3
luc = Personnage.Personnage("Luc", "Skywalker")
print(luc)

# Exercice 4
collections = {"premier": film4, "deuxième": film2, "troisième": film3}

# Exercice 6
parcours_collection(collections)

# Exercice 8

anakin = Personnage.Personnage("Anakin ", "Skywalker")

mommy = Acteur.Acteur("José", "Morigno", (luc, anakin))
morgana = Acteur.Acteur("Tran", "Bobby", (luc, anakin))
leona = Acteur.Acteur("Coulandro", "Léonie", (luc, anakin))
print(mommy)
print(mommy.nbPersonnages())

# Exercice 9 (voir classe Acteur)

# Exercice 10

film1.setCollectionActeur(collections)
print(film1)

# Exercice 11

print(film1.nbActeurs())
print(film1.nbPersonnages())
print(film1.calculBénéfice())
print(film1.isBefore(1900))

# Exercice 12
collection_acteur = {"1": mommy, "2": morgana, "3": leona}
film1.setCollectionActeur(collection_acteur)
print("\n test sans rien:", film1.triActeur())
print("\n test :", film1.triActeur()[0])


# Exercice 13
# [annee]=obj film
def makeBackUp(dico_film):
    for i in dico_film:
        print(str(dico_film[i].getAnnee())+" - " +
              str(dico_film[i].getTitre())+" - "+str(dico_film[i].calculBénéfice()[1]))


dico_film = {film1.getAnnee(): film1, film2.getAnnee(): film2,
             film3.getAnnee(): film3}
makeBackUp(dico_film)
