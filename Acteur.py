class Acteur:
    """
    Class acteur avec les attributs nom et prénom
    """

    def __init__(self, nom, prenom, tuple_personnages):
        self.setNom(nom)
        self.setPrenom(prenom)
        self.setTuple_personnages(tuple_personnages)

    def __str__(self):
        return "Nom : " + str(self.getNom()) + ", Prénom : " + str(self.getPrenom()) + "\nRôles : \n" + str(self.getTupleStr())

    # setter

    def setNom(self, nom):
        self.nom = nom

    def setTuple_personnages(self, tuple_personnages):
        self.tuple_personnages = tuple_personnages

    def setPrenom(self, prenom):
        self.prenom = prenom

    # getter
    def getNom(self):
        return self.nom

    def getPrenom(self):
        return self.prenom

    def getTuple_personnages(self):
        return self.tuple_personnages

    # function

    def getTupleStr(self):
        tab = list(self.getTuple_personnages())
        stri = ""
        i = 0
        while i < len(tab):
            stri += "Role " + str(i+1) + " : " + tab[i].__str__()+"\n"
            i += 1
        return stri

# Exercice 9
    def nbPersonnages(self):
        return len(list(self.getTuple_personnages()))
