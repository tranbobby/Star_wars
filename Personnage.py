class Personnage:
    """
    Class Personnage avec les attributs nom et prénom
    """

    def __init__(self, nom, prenom):
        self.setNom(nom)
        self.setPrenom(prenom)

    def __str__(self):
        return "Nom : " + str(self.getNom()) + ", Prénom : " + str(self.getPrenom())
    # setter

    def setNom(self, nom):
        self.nom = nom

    def setPrenom(self, prenom):
        self.prenom = prenom

    # getter
    def getNom(self):
        return self.nom

    def getPrenom(self):
        return self.prenom
