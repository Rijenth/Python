from Player import*
from item import*
from time import sleep
from random import randint

# Cette fonction permet au joueur de se soigner avec ces potions.
def soin(Player):
    if Player.HP == Player.MAXHP:
        print("Votre santé est déjà au maximum !")
        sleep(1)
        return
    print("")
    print("Potion : ", Player.potion)
    potion_disponible = []
    A = ""
    B = ""
    C = ""
    if "potion_de_vie" in Player.potion :
        A = "[1]:Potion de vie (+80 PV)"
        potion_disponible.append("1")
    if "potion_int_de_vie" in Player.potion :
        B = "[2]:Potion intermédaire de vie (+150 PV)"
        potion_disponible.append("2")
    if "potion_leg_de_vie" in Player.potion:
        C = "[3]:Potion légendaire de vie (+220 PV)"
        potion_disponible.append("3")
    if A == "" and B == "" and C == "":
        print("Vous n'avez plus de potion...")
        sleep(1)
        return
    print("")
    print('\x1b[0;30;47m', "Quel potion voulez-vous utiliser :", '\x1b[0m')
    print("")
    print(A)
    print(B)
    print(C)
    print('\x1b[0;30;47m', "Votre choix:",'\x1b[0m')
    choice = input()    
    while choice not in potion_disponible:
        print("Erreur!")
        sleep(1)
        print("")
        print('\x1b[0;30;47m', "Quel potion voulez-vous utiliser :", '\x1b[0m')
        print("")
        print(A)
        print(B)
        print(C)
        print('\x1b[0;30;47m', "Votre choix:",'\x1b[0m')
        choice = input()
    if choice == "1":
        Potion.GetSoin(potion_de_vie, Player)
        Player.potion.remove(potion_de_vie.nom)
        print('\x1b[0;32;40m', "Vous utilisez une potion de vie et vous récupérez 80 PV",'\x1b[0m')
        sleep(1)
        return
    if choice == "2":
        Potion.GetSoin(potion_int_de_vie, Player)
        Player.potion.remove(potion_int_de_vie.nom)
        print('\x1b[0;32;40m',"Vous utilisez une potion intermédiaire de vie et vous récupérez 150 PV",'\x1b[0m')
        sleep(1)
        return
    if choice == "3":
        Potion.GetSoin(potion_leg_de_vie, Player)
        Player.potion.remove(potion_leg_de_vie.nom)
        print('\x1b[0;32;40m',"Vous utilisez une potion légendaire de vie et vous récupérez 220 PV",'\x1b[0m')
        sleep(1)
        return
    
def chest(Player):
    chance = randint(0,100)
    if chance < 95:
        print("########################################")
        print("########################################")
        print("")
        print('\x1b[0;35;40m' +'Vous avez trouvé un coffre !:' + '\x1b[0m')
        print("")
        print("########################################")
        print("########################################")
        print("")
        print("Le coffre contient :")
        chance = randint(0, 15)
        if chance <= 14:
            chance = randint(0, 1)
            if chance == 0 :
                print("- potion_de_vie")
                print("")
                print("########################################")
                print("########################################")
                Player.potion.append(potion_de_vie.nom)
                print('\x1b[0;30;47m'+'Appuyez sur [A] pour continuer'+'\x1b[0m')
                choice = input()
                choice = choice.lower()
                while choice != "a":
                    choice = input()
            if chance == 1:
                argent = randint(100, 150)
                print("- ", argent, "gold")
                print("")
                print("########################################")
                print("########################################")
                Player.gold = Player.gold + argent
                print('\x1b[0;30;47m'+'Appuyez sur [A] pour continuer'+'\x1b[0m')
                choice = input()
                choice = choice.lower()
                while choice != "a":
                    choice = input()
        if chance == 15 and Player.classe in ["mage", "Mage de feu", "Mage d'eau", "Mage de terre"]:
            if "livre_de_mage_leg" not in Player.arme:
                print("- Livre de magie légendaire !")
                print("Cette ouvrage augmente grandement vos pouvoirs de mage.")
                Player.arme.append(livre_de_mage_leg.nom)
                print("")
                print("########################################")
                print("########################################")
                print('\x1b[0;30;47m'+'Appuyez sur [A] pour continuer'+'\x1b[0m')
                choice = input()
                choice = choice.lower()
                while choice != "a":
                    choice = input()
            else:
                    print("- Potion int de vie")
                    print("")
                    print("########################################")
                    print("########################################")
                    Player.potion.append(potion_int_de_vie.nom)
                    print('\x1b[0;30;47m'+'Appuyez sur [A] pour continuer'+'\x1b[0m')
                    choice = input()
                    choice = choice.lower()
                    while choice != "a":
                        choice = input()
        else:
            if chance == 15:
                print("- Potion int de vie")
                print("")
                print("########################################")
                print("########################################")
                Player.potion.append(potion_int_de_vie.nom)
                print('\x1b[0;30;47m'+'Appuyez sur [A] pour continuer'+'\x1b[0m')
                choice = input()
                choice = choice.lower()
                while choice != "a":
                    choice = input()
        return
    
    if chance >= 95:
        print("########################################")
        print("########################################")
        print("")
        print('\x1b[0;33;40m' +'Félicitation! Vous avez trouvé un coffre critique !:' + '\x1b[0m')
        print("")
        print("########################################")
        print("########################################")
        sleep(2)
        print("")
        print("Le coffre contient :")
        sleep(2)
        chance = randint(0, 50)
        if chance < 49:
            argent = randint(300, 400)
            print("- ", argent, "gold")
            print("- Potion légendaire de vie")
            print("")
            print("########################################")
            print("########################################")
            Player.potion.append(potion_leg_de_vie.nom)
            Player.gold = Player.gold + argent
            print('\x1b[0;30;47m'+'Appuyez sur [A] pour continuer'+'\x1b[0m')
            choice = input()
            choice = choice.lower()
            while choice != "a":
                choice = input()
        if chance == 49:
            print("- Epée légendaire !")
            Player.arme.append(epee_legendaire.nom)
            sleep(2)
            print("Le jeu devient soudainement beaucoup plus facile...")
            print("")
            print("########################################")
            print("########################################")
            print('\x1b[0;30;47m'+'Appuyez sur [A] pour continuer'+'\x1b[0m')
            choice = input()
            choice = choice.lower()
            while choice != "a":
                choice = input()
        if chance == 50:
            print("- Armure légendaire !")
            Player.armure.append(armure_legendaire.nom)
            sleep(2)
            print("Le jeu devient soudainement beaucoup plus facile...")
            print("")
            print("########################################")
            print("########################################")
            print('\x1b[0;30;47m'+'Appuyez sur [A] pour continuer'+'\x1b[0m')
            choice = input()
            choice = choice.lower()
            while choice != "a":
                choice = input()
        return