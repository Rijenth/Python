


class Arme:
    def __init__(self, prix, degats, nom):
        self.prix = prix
        self.degats = degats
        self.nom = nom
    def __str__(self):
        return self.nom

    def GetDegat(self,Player):
        if Player.classe == "Mage" or Player.classe == "chevalier" or Player.classe == "assassin":
            Player.ATK = Player.ATK * self.degats
        if Player.classe == "Mage de feu" or Player.classe == "Mage d'eau" or Player.classe == "Mage de terre":
            Player.INT = Player.INT * self.degats


class Armure:

    def __init__(self, prix, protection,nom):
        self.prix = prix
        self.protection = protection
        self.nom = nom
    def __str__(self):
        return self.nom
    def GetProtection(self,Player):
        Player.DEF = Player.DEF * self.protection

class Potion:

    def __init__(self, prix, soin, nom):

        self.prix = prix
        self.soin = soin
        self.nom = nom
    def __str__(self):
        return self.nom
    def GetSoin(self,Player):
        Player.HP = Player.HP + self.soin
        if Player.HP > Player.MAXHP:
            Player.HP = Player.MAXHP
            

            
