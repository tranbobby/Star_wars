from xmlrpc.client import boolean
from Personnage import Personnage


class Mechan(Personnage):

    def __init__(self, nom, prenom, cote_obscur: boolean):
        Personnage.__init__(self, nom, prenom)
        self.setCote_obscur(cote_obscur)

    def __str__(self):
        return super(Mechan, self).__str__() + ", cote_obscur : " + str(self.getCote_obscur())
    # setter

    def setCote_obscur(self, cote_obscur):
        self.cote_obscur = cote_obscur

    # getter
    def getCote_obscur(self):
        return self.cote_obscur
