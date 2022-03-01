from random import randint
from item import *
from time import sleep

fourchette = Arme(0, 1, "fourchette")

dague = Arme(200, 1.1, "dague")

epee_courte = Arme(300, 1.2, "epee_courte")

hache = Arme(600, 1.5, "hache")

epee_legendaire = Arme(7500, 50, "epee_legendaire")

katana = Arme(3000, 1.9, "katana")

les_bas_fonds_de_python = Arme(1,1,"LBFDP")

ballon_de_basket = Arme(1, 1, "ballon_de_basket")

calecon_troue = Armure(0, 1,"calecon_troue")

armure_en_cuir = Armure(200, 1.1, "armure_en_cuir")

armure_acier = Armure(600, 1.3, "armure_acier")

armure_legendaire = Armure(7500, 50, "armure_legendaire")

potion_de_vie = Potion(100, 80, "potion_de_vie")

potion_int_de_vie = Potion(150, 150, "potion_int_de_vie")

potion_leg_de_vie = Potion(300, 220, "potion_leg_de_vie")

livre_de_mage_int = Arme(550, 1.2, "livre_de_mage_int")

livre_de_mage_leg = Arme(1000, 1.5, "livre_de_mage_leg")


def classe_mage(Player):
    list_classe_sup = ["[1] - Mage de feu. Vous avez 50% de chance d'attaquer une nouvelle fois après votre attaque initial.", "[2] - Mage d'eau. Vous récupérez 25% des dégâts infligés en HP.","[3] - Mage de terre. Votre attaque ignore la défense de l'adversaire."]
    print(list_classe_sup[0])
    print(list_classe_sup[1])
    print(list_classe_sup[2])
    choice = int(input("Quel spécialisation choisissez vous ?:"))
    while choice != 1 and choice != 2 and choice != 3:
        print("Option de menu invalide.")
        choice = int(input("Entrer votre choix: "))
    if choice == 1:
        Player.classe = "Mage de feu"
    if choice == 2:
        Player.classe = "Mage d'eau"
    if choice == 3:
        Player.classe = "Mage de terre"
    return


# Ces trois fonctions augmentent l'attaque / defense du joueur en fonction de ce qu'il possède dans son inventaire.
def damage_en_fonction_arme(Player):
    Player.ATK = Player.baseATK
    if "fourchette" in Player.arme :
        fourchette.GetDegat(Player)
    if "dague" in Player.arme :
        dague.GetDegat(Player)
    if "epee_courte" in Player.arme :
        epee_courte.GetDegat(Player) 
    if "hache" in Player.arme:
        hache.GetDegat(Player)
    if "katana" in Player.arme:
        katana.GetDegat(Player)
    if "epee_legendaire" in Player.arme:
        epee_legendaire.GetDegat(Player)
    return Player.ATK

def defense_en_fonction_armure(Player):
    Player.DEF = Player.baseDEF
    if "calecon_troué" in Player.armure :
        calecon_troue.GetProtection(Player)
    if "armure_en_cuir" in Player.armure :
        armure_en_cuir.GetProtection(Player)
    if "armure_acier" in Player.armure :
        armure_acier.GetProtection(Player) 
    if "armure_legendaire" in Player.armure:
        armure_legendaire.GetProtection(Player)
    return Player.DEF

def degat_en_fonction_int(Player):
    Player.INT = Player.baseINT
    if "livre_de_mage_int" in Player.arme:
        livre_de_mage_int.GetDegat(Player)
    if "livre_de_mage_leg" in Player.arme:
        livre_de_mage_leg.GetDegat(Player)
    return Player.INT
    

class Player:

    def __init__(self):
        self.nom = "_"
        self.gold = 10
        self.arme = ["fourchette"]  
        self.armure = ["calecon_troue"]  
        self.potion = ["potion_de_vie"]  
        self.classe = "_"
        self.INT = 0
        self.VIT = 0
        self.baseVIT = 0
        self.baseATK = 0
        self.ATK = 0
        self.DEF = 0
        self.baseDEF = 0
        self.HP = 0
        self.MAXHP = 0
        self.CRIT = 0
        self.EXP = 0
        self.lmtEXP = 10
        self.lvl = 1
        self.item = 0
        

    def level(self):
        if self.EXP >= self.lmtEXP :
            self.lvl = self.lvl + 1
            if self.classe == "chevalier":
                self.MAXHP = self.lvl * 20
                self.VIT = self.lvl * 4
                self.baseATK =  self.lvl * 5
                self.ATK = self.lvl * 5
                self.baseINT = self.lvl * 6
                self.INT = self.lvl * 6
                self.baseDEF =  self.lvl * 6
                self.DEF = self.lvl * 6
                self.HP = self.lvl * 20
                self.CRIT = self.lvl * 5
                self.EXP = 0
            elif self.classe == "assassin":
                self.MAXHP = self.lvl * 12
                self.VIT = self.lvl * 6
                self.baseINT = self.lvl * 6
                self.INT = self.lvl * 6
                self.baseATK =  self.lvl * 7
                self.ATK = self.lvl * 7
                self.baseDEF = self.lvl * 4
                self.DEF = self.lvl * 4
                self.HP = self.lvl * 12
                self.CRIT = self.lvl * 10
                self.EXP = 0
            elif self.classe == "mage" or self.classe == "Mage de feu" or self.classe == "Mage d'eau" or self.classe == "Mage de terre" :
                self.MAXHP = self.lvl * 15
                self.VIT = self.lvl * 4
                self.baseINT = self.lvl * 6
                self.INT = self.lvl * 6
                self.baseATK = self.lvl * 6
                self.ATK = self.lvl * 6
                self.baseDEF = self.lvl * 5
                self.DEF = self.lvl * 5
                self.HP = self.lvl * 15
                self.CRIT = self.lvl * 0
                self.EXP = 0
            self.lmtEXP = self.lmtEXP * 2
            print('\x1b[0;33;40m', "Bravo tu est passé niveau ", self.lvl, "!", '\x1b[0m')
            sleep(2)

    # il faut maintenant choisir votre classe ce qui changera le gameplay.

    def classes(self):

        i = False
        while i == False:
            print("########################################")
            print("")
            print("Même dans un rêve, vous devez choisir un rôle...")
            print("[","Chevalier","]","[","Assassin","]","[","Mage","]")
            print("")
            print("[","Chevalier","]",":","Si vous voulez une classe pas marrante, mais solide comme un mur.")
            print("[","Assassin","]",":", "Frappe très fort, joue souvent en premier mais aussi fragile qu'une balle de ping pong.")
            print("[","Mage","]",":", "Polyvalent, trois spécialisation après le niveau 5, Fabrice approuve.")
            print("")
            print("########################################")
            classe = input("Quel classe choisissez vous:")
            classe = classe.lower()
            self.classe = classe
            if self.classe  == "chevalier":
                print("Vous avez choisi l'art des chevaliers")
                self.gold = 10
                self.arme = ["fourchette"] 
                self.armure = ["calecon_troue"]  
                self.potion = ["potion_de_vie"]  
                self.lmtEXP = 10
                self.MAXHP = 20
                self.lvl = 1
                self.VIT = 4
                self.baseVIT = 4
                self.baseINT = 5
                self.INT = 1
                self.ATK = 5
                self.baseATK = 5
                self.DEF = 6
                self.baseDEF = 6
                self.HP = 20
                self.CRIT = 5
                self.EXP = 0
                i = True
            elif self.classe  == "assassin":
                print("Vous avez choisi l'art des assassins")
                self.gold = 10
                self.arme = ["fourchette"]  
                self.armure = ["calecon_troue"]  
                self.potion = ["potion_de_vie"]  
                self.lmtEXP = 10
                self.MAXHP = 12
                self.lvl = 1
                self.VIT = 6
                self.baseVIT = 6
                self.baseINT = 5
                self.INT = 5
                self.ATK = 7
                self.baseATK = 7
                self.DEF = 4
                self.baseDEF = 4
                self.HP = 12
                self.CRIT = 10
                self.EXP = 0
                i = True
            elif self.classe == "mage" or self.classe == "Mage de feu" or self.classe == "Mage d'eau" or self.classe == "Mage de terre" :
                print("Vous avez choisi l'art des mages")
                self.gold = 10
                self.arme = ["fourchette"]  
                self.armure = ["calecon_troue"] 
                self.potion = ["potion_de_vie"] 
                self.lmtEXP = 10
                self.MAXHP = 15
                self.lvl = 1
                self.VIT = 4
                self.baseVIT = 4
                self.baseINT = 6
                self.INT = 6
                self.ATK = 6
                self.baseATK = 6
                self.DEF = 5
                self.baseDEF = 5
                self.HP = 15
                self.CRIT = 0
                self.EXP = 0
                i = True
            else:
                print("Vous avez le choix parmis les classes mage , assassin et chevalier")
                i = False

    

    def stats(self):
        print("Vous avez choisi la classe", self.classe,".")
        print("Vos statistiques sont :","[", damage_en_fonction_arme(self) ,"ATK","]","[", degat_en_fonction_int(Player), "INT","]", "[", defense_en_fonction_armure(self), "DEF" ,"]", "[", self.MAXHP, "HP","]", "[", self.VIT, "VIT", "]","[", self.CRIT,"%", "Chance de CRIT", "]")
        print("")
        print('\x1b[0;30;47m'+'Appuyez sur [A] pour continuer'+'\x1b[0m')
        choice = input()
        choice = choice.lower()
        while choice != "a":
            choice = input()
        return

    # le joueur doit pouvoir voir ce qu'il possède


    def inventaire(self):
        print("Vous avez :")
        print("")
        print("Gold :", "[",self.gold,"]")
        print("Arme(s) :", "[",self.arme,"]")
        print("Armure(s) :", "[", self.armure,"]")
        print("Potion(s) :", "[", self.potion,"]")
        print("")
        print('\x1b[0;30;47m'+'Appuyez sur [A] pour continuer'+'\x1b[0m')
        choice = input()
        choice = choice.lower()
        while choice != "a":
            choice = input()
# Une liste random de phrases pour le marchand.
def random_phrase_marchand(Player):
    text = randint(0, 4)
    print('\x1b[0;33;40m',"[Un marchand sympa]:",'\x1b[0m')
    if text == 0:
        print("Bonjour", Player.nom,"!","Je vois que tu aimes faire appel à des connaisseurs.")
        sleep(2)
        print("J'ai tout ce qui te faut pour continuer l'aventure dans de bonnes conditions :)")
        return
    if text == 1:
        print("Salut",Player.nom,"!! Même dans un rêve, les pauvres marchands comme moi se contente d'attendre")
        sleep(2)
        print("l'arrivée d'un bel aventurier pleins de sous... de courage, oui... pardon.")
        return
    if text == 2:
        print("qjlkfqn, qklzdql...")
        sleep(2)
        print("...")
        sleep(2)
        print("???")
        sleep(1)
        print("Oups pardon... Mais ou sont donc mes manières ?!", "Vous savez, on finis par perdre")
        sleep(1)
        print("la raison quand on est enfermé, seul, dans un inventaire...")
        return
    if text == 3:
        print("*Chuchotte*", "Oh noon, pas lui...")
        sleep(3)
        print("Bonjour", Player.nom,"!", "Je suis heureux de vous voir !")
        sleep(2)
        print("Votre présence réchauffe le coeur de l'humble marchand que je suis.")
        return
    if text == 4:
        print("Vous tombez à pic ! J'avais justement besoin d'un peu d'argent")
        sleep(2)
        print("Oui, bon, je suis un marchand. Je m'intéresse plus à votre argent qu'à votre personne.")
        sleep(1)
        print("Est-ce que celà vous surprends réellement ?")


def check_marchand(Player):
    lArmes = ["dague", "epee_courte", "hache", "katana","livre_de_mage_int","epee_legendaire"]
    lArmures = ["armure_en_cuir", "armure_acier", "armure_legendaire"]
    lPotion = ["potion_int_de_vie","potion_leg_de_vie"]
    print("")
    print("#######################################################################################")
    print("")
    sleep(1)
    random_phrase_marchand(Player)
    sleep(2)
    print("Comment puis-je vous aider,", Player.nom, "?")
    sleep(2)
    print("")
    print("#################################")
    print("")
    print("[1]: Acheter")
    print("[2]: Vendre")
    print("[3]: Quitter")
    print("")
    print("#################################")
    print("Votre argent:",'\x1b[1;33;40m',Player.gold,'\x1b[0m')
    print("Votre choix:")
    choice = input()
    while choice not in ["1","2","3"]:
        print("Erreur !")
        print("#################################")
        print("Votre argent:",'\x1b[0;44;40m',Player.gold,'\x1b[0m')
        print("Votre choix:")
        choice = input()
    if choice == "3":
        print("À bientôt", Player.nom, "!")
        sleep(2)
        return
    # La partie ACHAT
    if choice == "1":
        print("#################################")
        print("")
        print("Que souhaitez-vous acheter ?")
        print("")
        sleep(1)
        choix_achat = choix_marchand(Player)
        if choix_achat == "arme":
            item = achat_X_marchand(Player, lArmes)
            while item == "erreur":
                item = achat_X_marchand(Player, lArmes)
            if item == "au revoir":
                return
            
            Player.arme.append(item.nom)
            print("Votre argent:", '\x1b[1;33;40m', Player.gold,'\x1b[0m')
            print("#################################")
            print("")
            print(" Etes vous sur que se sera tout ?[oui]/[non]")
            print("")
            sleep(1)
            choix = input()
            while choix not in ["oui", "non"]:
                print("Erreur!")
                print("Voulez-vous me vendre autre chose ?[oui]/[non]")
                choix = input()
            if choix == "oui":
                print("Merci de votre visite et à bientôt !")
                sleep(1)
                return
            if choix == "non":
                print("#################################")
                print("")
                print("Que souhaitez-vous acheter ?")
                print("")
                sleep(1)
                choix_achat = choix_marchand(Player)
                if choix_achat == "arme":
                    item = achat_X_marchand(Player, lArmes)
                    while item == "erreur":
                        item = achat_X_marchand(Player, lArmes)
                    if item == "au revoir":
                        return

                    Player.arme.append(item.nom)
                    print("Votre argent:", '\x1b[1;33;40m', Player.gold, '\x1b[0m')
                    print("Merci de votre achat !")
                    print("À bientôt !")
                    sleep(2)
                    return
        if choix_achat == "armure":
            item = achat_X_marchand(Player, lArmures)
            while item == "erreur":
                item = achat_X_marchand(Player, lArmures)
            if item == "au revoir":
                return
            Player.armure.append(item.nom)
            print("Votre argent:", '\x1b[1;33;40m', Player.gold,'\x1b[0m')
            print("#################################")
            print("")
            print(" Etes vous sur que se sera tout ?[oui]/[non]")
            print("")
            sleep(1)
            choix = input()
            while choix not in ["oui", "non"]:
                print("Erreur!")
                print("Voulez-vous me achetez autre chose ?[oui]/[non]")
                choix = input()
            if choix == "oui":
                print("Merci de votre visite et à bientôt !")
                sleep(1)
                return
            if choix == "non":
                print("#################################")
                print("")
                print("Que souhaitez-vous acheter ?")
                print("")
                sleep(1)
                choix_achat = choix_marchand(Player)
                if choix_achat == "arme":
                    item = achat_X_marchand(Player, lArmures)
                    while item == "erreur":
                        item = achat_X_marchand(Player, lArmures)
                    if item == "au revoir":
                        return

                    Player.armure.append(item.nom)
                    print("Votre argent:", '\x1b[1;33;40m', Player.gold, '\x1b[0m')
                    print("Merci de votre achat !")
                    print("À bientôt !")
                    sleep(2)
                    return
        if choix_achat == "potion":
            item = achat_X_marchand(Player, lPotion)
            if item == "au revoir":
                return 
            while item == "erreur":
                item = achat_X_marchand(Player, lArmures)
            Player.potion.append(item.nom)
            print("Votre argent:", '\x1b[1;33;40m', Player.gold,'\x1b[0m')
            print("#################################")
            print("")
            print(" Etes vous sur que se sera tout ?[oui]/[non]")
            print("")
            sleep(1)
            choix = input()
            while choix not in ["oui", "non"]:
                print("Erreur!")
                print("Voulez-vous me achetez autre chose ?[oui]/[non]")
                choix = input()
            if choix == "oui":
                print("Merci de votre visite et à bientôt !")
                sleep(1)
                return
            if choix == "non":
                print("#################################")
                print("")
                print("Que souhaitez-vous acheter ?")
                print("")
                sleep(1)
                choix_achat = choix_marchand(Player)
                if choix_achat == "arme":
                    item = achat_X_marchand(Player, lPotion)
                    while item == "erreur":
                        item = achat_X_marchand(Player, lPotion)
                    if item == "au revoir":
                        return

                    Player.potion.append(item.nom)
                    print("Votre argent:", '\x1b[1;33;40m', Player.gold, '\x1b[0m')
                    print("Merci de votre achat !")
                    print("À bientôt !")
                    sleep(2)
                    return
    # La partie VENTE
    if choice == "2":
        vendre = True
        while vendre == True:
            item = vendre_X_marchand(Player)
            if item == "oui":
                print("Votre argent:", '\x1b[1;33;40m', Player.gold,'\x1b[0m')
                print("#################################")
                print("")
                print(" Etes vous sur que se sera tout ?[oui]/[non]")
                print("")
                sleep(1)
                choix = input()
                while choix not in ["oui", "non"]:
                    print("Erreur!")
                    print("Voulez-vous me vendre autre chose ?[oui]/[non]")
                    choix = input()
                if choix == "oui":
                    print("Merci de votre visite et à bientôt !")
                    sleep(1)
                    return
                if choix == "non":
                    item = vendre_X_marchand(Player)
                    while item == "erreur":
                        item = vendre_X_marchand(Player)
                    if item == "au revoir":
                        return



            if item == "non":
                print("Voulez-vous me vendre autre chose ?[oui]/[non]")
                choix = input()
                while choix not in ["oui", "non"]:
                    print("Erreur!")
                    print("Voulez-vous me vendre autre chose ?[oui]/[non]")
                    choix = input()
                if choix == "non":
                    print("Merci de votre visite et à bientôt !")
                    sleep(1)
                    vendre = False
        return
    
def choix_marchand(Player):
    print("#################################") 
    print("")
    print("[1]: Une arme")
    print("[2]: Une armure")
    print("[3]: Une potion") 
    print("")
    print("#################################") 
    print("Votre argent:",'\x1b[1;33;40m',Player.gold,'\x1b[0m')
    print("Votre choix:")      
    choice = input()
    while choice not in ["1","2","3"]:
        print("Erreur!")
        choice = input()
    if choice == "1":
        return "arme"
    if choice == "2":
        return "armure"
    if choice == "3":
        return "potion"
    
def achat_X_marchand(Player, X): 
    lArmes = ["dague", "epee_courte", "hache", "katana","livre_de_mage_int","epee_legendaire"]
    lArmures = ["armure_en_cuir", "armure_acier", "armure_legendaire"]
    lPotion = ["potion_int_de_vie","potion_leg_de_vie"]
    print("Liste d'objet à vendre':", X)
    print("Faites votre choix !")
    print("")
    print("#################################") 
    print("Votre argent:",'\x1b[1;33;40m',Player.gold,'\x1b[0m')
    print("Votre choix: ([x] : Quitter)")
    choice = str(input())
    while choice not in X and choice != "x":
        print("Ce choix n'est pas disponible...")
        print("Votre choix:")
        choice = str(input())
    if choice == "x":
        print("Très bien dans ce cas... À bientôt !")
        return "au revoir"
    item = eval(choice)
    if choice in Player.arme or choice in Player.armure :
        print("Vous avez déjà cet objet ! Je ne peux pas vous en donner un deuxième...")
        sleep(2)
        return "erreur"
    print("#################################") 
    print("")
    print(item, "coûte",'\x1b[1;33;40m',item.prix,'\x1b[0m',"gold")
    print("")
    print("#################################") 
    print("Votre argent:",'\x1b[1;33;40m',Player.gold,'\x1b[0m')
    print("Votre choix:")   
    if Player.gold >= item.prix:
        print("Voulez-vous l'acheter ? [oui]/[non]")
        choix = input()
        while choix not in ["oui", "non"]:
            print("Erreur!")
            print("#################################") 
            print("")
            print(item, "coûte",'\x1b[1;33;40m',item.prix,'\x1b[0m',"gold")
            print("")
            print("#################################")
            print("Votre argent:", '\x1b[1;33;40m', Player.gold,'\x1b[0m')
            print("Voulez-vous l'acheter ? [oui]/[non]")
            choix = input()
        if choix == "oui":
            Player.gold = Player.gold - item.prix
            return item
        if choix == "non":
            print("Très bien... Voulez-vous autre chose ? [oui]/[non]")
            choix = input()
            while choix not in ["oui", "non"]:
                print("Erreur!")
                print("...Voulez-vous autre chose ? [oui]/[non]")
                choix = input()
            if choix == "non":
                print("Merci de votre visite et à bientôt !")
                return "au revoir"
            if choix == "oui":
                print("Quel catégorie d'objets voulez-vous voir ?")
                print("#################################") 
                print("")
                print("[1]: Une arme")
                print("[2]: Une armure")
                print("[3]: Une potion") 
                print("")
                print("#################################") 
                print("Votre argent:",'\x1b[1;33;40m',Player.gold,'\x1b[0m')
                print("Votre choix:") 
                choice = input()
                while choice not in ["1","2","3"]:
                    print("Erreur!")
                    choix = input()
                if choice == "1":
                    return achat_X_marchand(Player, lArmes)
                if choice == "2":
                    return achat_X_marchand(Player, lArmures)
                if choice == "3":
                    return achat_X_marchand(Player, lPotion)
                
    else: 
        print("Désolé, vous n'avez pas assez d'argent pour cet objet...")
        return achat_X_marchand(Player, X)

def vendre_X_marchand(Player):
    print("Très bien, quel est la catégorie de l'objet que vous voulez me vendre ?")
    choice_type = choix_marchand(Player)
    if choice_type == "arme":            
        print("#################################") 
        print("")
        print("Votre inventaire d'armes': ")
        print(Player.arme)
        print("")
        print("#################################") 
        if Player.arme == []:
            print("Vous n'avez rien à me vendre...")
            sleep(1)
            return "non"
        print("Quel objet voulez-vous me vendre ?")
        choice_item = input()
        while choice_item not in Player.arme:
            print("Vous n'avez pas cette objet...")
            print("#################################") 
            print("")
            print("Votre inventaire d'armes': ")
            print(Player.arme)
            print("")
            print("#################################")
            print("Quel objet voulez-vous me vendre ?")
            choice_item = input()
        item = eval(choice_item)
        print("Je vous achète", item, "pour",'\x1b[1;33;40m',item.prix,'\x1b[0m',"gold", "ça vous convient ?")
        print("Votre choix: [oui]/[non]")
        choice = input()
        while choice not in ["oui","non"]:
            print("Je vous achète", item, "pour",'\x1b[1;33;40m',item.prix,'\x1b[0m',"gold", "ça vous convient ?")
            print("Votre choix: [oui]/[non]")
            choice = input()
        if choice == "non":
            print("D'accord ! Pas de soucis...")
            sleep(2)
            return "non"
        if choice == "oui":
            print("Parfait ! À moooii")
            Player.gold = Player.gold + item.prix
            Player.arme.remove(item.nom)
            sleep(2)
            return "oui"
    if choice_type == "armure":
        print("#################################") 
        print("")
        print("Votre inventaire d'armure': ")
        print(Player.armure)
        print("")
        print("#################################") 
        if Player.armure == []:
            print("Vous n'avez rien à me vendre...")
            sleep(1)
            return "non"
        print("Quel objet voulez-vous me vendre ?")
        choice_item = input()
        while choice_item not in Player.armure:
            print("Vous n'avez pas cette objet...")
            print("#################################") 
            print("")
            print("Votre inventaire d'armure': ")
            print(Player.armure)
            print("")
            print("#################################")
            print("Quel objet voulez-vous me vendre ?")
            choice_item = input()
        item = eval(choice_item)
        print("Je vous achète", item, "pour",'\x1b[1;33;40m',item.prix,'\x1b[0m',"gold", "ça vous convient ?")
        print("Votre choix: [oui]/[non]")
        choice = input()
        while choice not in ["oui","non"]:
            print("Je vous achète", item, "pour",'\x1b[1;33;40m',item.prix,'\x1b[0m',"gold", "ça vous convient ?")
            print("Votre choix: [oui]/[non]")
            choice = input()
        if choice == "non":
            print("D'accord ! Pas de soucis...")
            sleep(2)
            return "non"
        if choice == "oui":
            print("Parfait ! À moooii")
            Player.gold = Player.gold + item.prix
            Player.armure.remove(item.nom)
            sleep(2)
            return "oui"
    if choice_type == "potion":
        print("#################################") 
        print("")
        print("Votre inventaire de potion: ")
        print(Player.potion)
        print("")
        print("#################################") 
        if Player.potion == []:
            print("Vous n'avez rien à me vendre...")
            sleep(1)
            return "non"
        print("Quel objet voulez-vous me vendre ?")
        choice_item = input()
        while choice_item not in Player.potion:
            print("Vous n'avez pas cette objet...")
            print("#################################") 
            print("")
            print("Votre inventaire de potion: ")
            print(Player.potion)
            print("")
            print("#################################")
            print("Quel objet voulez-vous me vendre ?")
            choice_item = input()
        item = eval(choice_item)
        print("Je vous achète", item, "pour",'\x1b[1;33;40m',item.prix,'\x1b[0m',"gold", "ça vous convient ?")
        print("Votre choix: [oui]/[non]")
        choice = input()
        while choice not in ["oui","non"]:
            print("Je vous achète", item, "pour",'\x1b[1;33;40m',item.prix,'\x1b[0m',"gold", "ça vous convient ?")
            print("Votre choix: [oui]/[non]")
            choice = input()
        if choice == "non":
            print("D'accord ! Pas de soucis...")
            sleep(2)
            return "non"
        if choice == "oui":
            print("Parfait ! À moooii")
            Player.gold = Player.gold + item.prix
            Player.potion.remove(item.nom)
            sleep(2)
            return "oui"
