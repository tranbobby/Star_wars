from xmlrpc.client import boolean
from Personnage import Personnage


class Gentil(Personnage):

    def __init__(self, nom, prenom, force: boolean):
        Personnage.__init__(self, nom, prenom)
        self.setForce(force)

    def __str__(self):
        return super(Gentil, self).__str__() + ", Force : " + str(self.getForce())
    # setter

    def setForce(self, force):
        self.force = force

    # getter
    def getForce(self):
        return self.force
