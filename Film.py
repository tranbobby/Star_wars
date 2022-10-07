import collections
from pyclbr import Function


class Film:
    """
    Class Film avec les attributs titre, année, épisode, cout, recette
    """

    def __init__(self, titre, annee, episode, cout, recette, collection_acteur, collection_personnage):
        self.setTitre(titre)
        self.setAnnee(annee)
        self.setEpisode(episode)
        self.setCout(cout)
        self.setRecette(recette)
        self.setCollectionActeur(collection_acteur)
        self.setCollectionPersonnage(collection_personnage)

    def __str__(self):
        # return self.titre, str(self.annee), str(self.episode), str(self.cout), str(self.recette)
        return "Titre : "+str(self.getTitre()) + ", Année : " + str(self.getAnnee()) + ", Episode : " + str(self.getEpisode()) + ", Coût : " + str(self.getCout()) + ", Recette : " + str(self.getRecette()) + "\n Collection d'acteurs : \n" + str(self.getCollectionActeurStr()) + "\n Collection de Personnages : \n" + str(self.getCollectionPersonnageStr())

    # setter

    def setTitre(self, titre):
        self.titre = titre

    def setAnnee(self, annee):
        self.annee = annee

    def setEpisode(self, episode):
        self.episode = episode

    def setCout(self, cout):
        self.cout = cout

    def setRecette(self, recette):
        self.recette = recette

    def setCollectionActeur(self, collection_acteur):
        self.collection_acteur = collection_acteur

    def setCollectionPersonnage(self, collection_personnage):
        self.collection_personnage = collection_personnage

    # getter

    def getTitre(self):
        return self.titre

    def getAnnee(self):
        return self.annee

    def getEpisode(self):
        return self.episode

    def getCout(self):
        return self.cout

    def getRecette(self):
        return self.recette

    def getCollectionActeur(self):
        return self.collection_acteur

    def getCollectionPersonnage(self):
        return self.collection_personnage

    # Function

    def getCollectionActeurStr(self):
        stri = ""
        act = 1
        for i in self.getCollectionActeur():
            stri += "acteur "+str(act)+" " + \
                self.getCollectionActeur()[i].__str__()
            act += 1
        return stri

    def getCollectionPersonnageStr(self):
        stri = ""
        perso = 1
        for i in self.getCollectionPersonnage():
            stri += "personnage "+str(perso)+" " + \
                self.getCollectionPersonnage()[i].__str__()
            perso += 1
        return stri

    # Exercice 11

    def nbActeurs(self):
        return len(self.getCollectionActeur())

    def nbPersonnages(self):
        return len(self.getCollectionPersonnage())

    def calculBénéfice(self):
        if (self.getCout() >= self.getRecette()):
            return (False, self.getRecette()-self.getCout())
        else:
            return (False, self.getRecette()-self.getCout())

    def isBefore(self, annee):
        return self.getAnnee() < annee

    def triActeur(self):
        dic = {}
        dic_trie = {}
        for i in self.getCollectionActeur():
            dic[self.getCollectionActeur()[i].getNom()
                ] = self.getCollectionActeur()[i]

        j = 0
        print(dic["José"], "babas")
        for i in sorted(dic.keys()):
            dic_trie[j] = dic[i]
            j += 1
        return dic_trie
