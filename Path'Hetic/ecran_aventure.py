from deplacement_test import*
from time import sleep
from random import randint
from combat import *
from Player import *
from item import *
from boss_file import *
from sys import exit
from sauvegarde import *



def description_depart():
    print(("#######################################################################################"))
    print("")
    print('\x1b[0;30;47m'+'DESCRIPTION:'+'\x1b[0m')
    print("Brouillard, visibilité faible, des craquements sous vos semelles à chacun de vos pas... ")
    print("Vous arrivez dans ce qui semble être l'enceinte d'une institution plutôt lugubre.")
    sleep(3)
    print("Vous entendez des hurlements qui vous pétrifie... ")
    print("...")
    sleep(3)
    print("Vous avez l'étrange sentiment que quelqu'un vous attend...")
    print("")
    print(("#######################################################################################"))
    print('\x1b[0;30;47m'+'Appuyez sur [A] pour mettre fin à la discussion.'+'\x1b[0m')
    choice = input()
    choice = choice.lower()
    while choice != "a":
        choice = input()
    return


# Créer une fonction qui prend la valeur menu
def menu(save, m, currentIndex, Player):
    # Titre du jeu avec affichage
    print("####################################################################")
    # Le code "'\x1b[0;30;47m'+'Pathetic'+'\x1b[0m'" permet d'afficher le texte cible sur un fond blanc.
    print("###########################", '\x1b[0;30;47m' + "Path'Hetic" + '\x1b[0m', "###############################")
    print("####################################################################")
    print("##########  [1] Nouvelle partie")  # le choix du jeux
    print("##########  [2] Reprendre")  # le choix
    print("##########  [3] Info/Credit")  # le choix
    print("##########  [4] Quitter")  # le choix
    print("####################################################################")
    print("Choisissez ce que vous voulez faire :")
    choice = input()
    while choice not in ["1", "2", "3", "4"]:
        print("Erreur, ce choix ne figure pas dans la liste.")
        print("Choisissez ce que vous voulez faire :")
        choice = input()
    if choice == "1":
        save = []
        currentIndex = [1, 7]
        print("Entrez votre nom :")
        name = str(input())
        Player.nom = name
        print("Votre nom est:", Player.nom)
        sleep(1)
        Player.classes(Player)
        sleep(1)
        action = "rien"
        description_depart()
        interface_user(save, m , Player, currentIndex, action)
        return menu(save, m, currentIndex, Player)
    if choice == "2":
        if save != []:
            print('\x1b[0;32;40m',"Chargement de votre partie...",'\x1b[0m')
            Player.nom = save[0]
            Player.classe = save[1]
            m = save[2]
            currentIndex = save[3]
            Player.HP = save[4]
            Player.lvl = save[5]
            Player.gold = save[6]
            Player.arme = save[7]
            Player.armure = save[8]
            Player.potion = save[9]
            Player.EXP = save[10]
            action = "rien"
            sleep(2)
            interface_user(save,m,Player, currentIndex, action)
        else:
            print('\x1b[0;32;40m',"Aucune donnée disponible...",'\x1b[0m')
            sleep(2)
            return menu(save, m, currentIndex, Player)
    if choice == "3":
        info_credit(save, m, currentIndex)
    if choice == "4":
        print("Fin du jeu")
        exit()

def info_credit(save, m, currentIndex):
    print("####################################################################")
    print("###########################", '\x1b[0;30;47m' + 'HISTOIRE' + '\x1b[0m', "###############################")
    print("####################################################################")
    print("")
    print("Vous êtes un développeur accompli, fraichement diplomé et")
    print("intégré au monde du travail.", "Vous vous rememorez votre parcours en ")
    print("1ère année à Hetic.", "Un parcours qui, pour une raison inconnue, vous ")
    print("a profondemment marqué.", "Vous allez devoir revivre l'enfer de votre ")
    print("1ère année, affronter vos vieux démons et", "en finir avec votre passé.")
    print("")
    print("####################################################################")
    print("###########################", '\x1b[0;30;47m' + 'CREDITS' + '\x1b[0m', "###############################")
    print("####################################################################")
    print("")
    print("ARUMAINATHAN Rijenth : [Système combat][Design monstre/boss][Interface utilisateur][Gestion des évènements]")
    print("")
    print("BAKAYOKO Kader : [Joueur][Système de commerce][Système d'équipement][Système d'expérience][Système de clase]")
    print("")
    print("PIVERT Fabrice : [Conception de la map][Système de déplacement][Optimisation des déplacements][Design des quêtes]")
    print("")
    print("LESOING Valentin : [Narration][Système combat][Aspect graphique][Sauvegarde]")
    print("")
    print("LOPES Hugo : [Architecture du menu]")
    print("")
    print("####################################################################")
    print("####################################################################")
    print("####################################################################")
    print("Appuyez sur [A] pour retourner au menu")
    choice = input()
    choice = choice.lower()
    while choice != "a":
        choice = input()
        choice = choice.lower()
    return menu(save, m, currentIndex, Player)



# Ce programme affiche une interface qui sert de lien entre l'utilisateur
# et l'univers du jeu.

def interface_user(save,m,Player, currentIndex, action):
    # Retourne au menu principal si le joueur décide de quitter le jeu
    if action == "menu":
        print('\x1b[0;30;47m'+'Vous retournez au menu principal'+'\x1b[0m')
        print("")
        sleep(2)
        return menu(save, m, currentIndex, Player)
    else:
        affichage_interface(m,Player, currentIndex, action) #Regroupe toutes les fonctions d'interface, pour plus de lisibilité.
        choice = choix_joueur()
        while choice not in ["z", "q", "s", "d", "a", "e", "f", "x","w"]:
            print("Erreur, votre choix n'est pas disponible")
            choice = choix_joueur()
        action = decision(choice)
        game(save, m,currentIndex, action, Player) 

# Cette fonction permet de définir une action en fonction de ce que le joueur choisit de faire.
def game(save, m, currentIndex, action, Player):
    if action == "w":
        nom = Player.nom
        classe = Player.classe
        actual_map = m
        HP = Player.HP
        lvl = Player.lvl
        gold = Player.gold
        arme = Player.arme
        armure = Player.armure
        potion = Player.potion
        EXP = Player.EXP
        save = sauvegarde(nom, classe, actual_map, currentIndex, HP, lvl, gold, arme, armure, potion, EXP)
        print('\x1b[0;32;40m',"Votre partie a été sauvegardée ! Vous pouvez maintenant quitter le jeu l'esprit tranquille.",'\x1b[0m')
        print("")
        print('\x1b[0;30;47m'+'Appuyez sur [A] pour continuer'+'\x1b[0m')
        choice = input()
        choice = choice.lower()
        while choice != "a":
            choice = input()
        action = "void"
        return interface_user(save,m,Player, currentIndex, action)
    if action == "a":
        check_stats(Player)
        action = "void"
        interface_user(save,m,Player, currentIndex, action)
    if action == "e":
        check_inventaire(Player)
        action = "void"
        interface_user(save,m,Player, currentIndex, action)
    if action == "q":
        test_obstacle = attention_obstacle(m,currentIndex, action)
        currentIndex = carte(m,currentIndex, action)
        if test_obstacle == "oui":
            action = "void"
            return interface_user(save,m,Player, currentIndex, action)
        event = evenement(save, m,currentIndex, Player, monstre,action)
        action = "void"
        if event == "death":
            action = "menu"
            return interface_user(save,m,Player, currentIndex, action)
        return interface_user(save,m,Player, currentIndex, action)
    if action == "z":
        test_obstacle = attention_obstacle(m,currentIndex, action)
        currentIndex = carte(m,currentIndex, action)
        if test_obstacle == "oui":
            action = "void"
            return interface_user(save,m,Player, currentIndex, action)
        event = evenement(save, m,currentIndex, Player, monstre,action)
        action = "void"
        if event == "death":
            action = "menu"
            return interface_user(save,m,Player, currentIndex, action)
        return interface_user(save,m,Player, currentIndex, action)
    if action == "s":
        test_obstacle = attention_obstacle(m,currentIndex, action)
        currentIndex = carte(m,currentIndex, action)
        if test_obstacle == "oui":
            action = "void"
            return interface_user(save,m,Player, currentIndex, action)
        event = evenement(save, m,currentIndex, Player, monstre, action)
        action = "void"
        if event == "death":
            action = "menu"
            return interface_user(save,m,Player, currentIndex, action)
        return interface_user(save,m,Player, currentIndex, action)
    if action == "d":
        test_obstacle = attention_obstacle(m,currentIndex, action)
        currentIndex = carte(m,currentIndex, action)
        if test_obstacle == "oui":
            action = "void"
            return interface_user(save,m,Player, currentIndex, action)
        event = evenement(save, m,currentIndex, Player, monstre,action)
        action = "void"
        if event == "death":
            action = "menu"
            return interface_user(save,m,Player, currentIndex, action)
        return interface_user(save,m,Player, currentIndex, action)
    if action == "x":
        action = "menu"
        interface_user(save,m,Player, currentIndex, action)
    if action == "f":
        check_marchand(Player)
        action = "void"
        interface_user(save,m,Player, currentIndex, action)
        

###############################
######### EVENEMENT ###########
###############################   



def evenement(save, m,currentIndex, Player, monstre,action):
    if currentIndex == [2, 43]:
        if m[2][43] == "V":
            boss_valentin(Player)
            titre = "** BOSS SECRET **"
            print ('\x1b[0;33;40m',"*" * len(titre),'\x1b[0m')
            print ('\x1b[0;33;40m', titre,'\x1b[0m')
            print ('\x1b[0;33;40m',"*" * len(titre),'\x1b[0m')
            print("")
            sleep(3)
            Valentin = ["Valentin, Le ninja ctrlc_ctrlv", Player.lvl, 750, Player.ATK, (Player.DEF*0.85), 1, 40]
            result = combat_valentin(Player, Valentin)
            sleep(2)
            if result == True:
                print("########################################")
                print("########################################")
                print("")
                print('\x1b[0;30;47m'+'Vous perdez conscience...'+'\x1b[0m')
                print("")
                print("########################################")
                print("########################################")
                sleep(1)
                return "death"
            Player.level(Player)
            print('\x1b[0;33;40m',"Vous avez fini le jeu et vaincu le boss secret !",'\x1b[0m')
            sleep(3)
            return "death"
    if currentIndex == [5, 43]:
        if m[5][43] == "B":
            debut_quiz(Player)
            score = entree_utilisateur(Player)
            print("")
            print("Ton score est de:", score)
            sleep(2)
            if score <= 6 :
                print("Et bien..., je suis déçu, vous auriez pû faire un sans faute.") 
                sleep(2)
                print("Je ne pensais pas devoir en arriver là mais...")
                sleep(2)
                print("Comme tout bon boss final de rpg, je me dois de vous mettre des batons dans les roues.")
                sleep(2)
                print("En garde !")
                sleep(2)
                titre = "** BOSS FINAL **"
                print ('\x1b[0;33;40m',"*" * len(titre),'\x1b[0m')
                print ('\x1b[0;33;40m', titre,'\x1b[0m')
                print ('\x1b[0;33;40m',"*" * len(titre),'\x1b[0m')
                loic = ["Loïc, le professeur", 20, 1000, (Player.ATK), 30, 1500, 200]
                print("")
                sleep(2)
                result = combat(Player, loic)
                sleep(1)
                if result == True:
                    print("########################################")
                    print("########################################")
                    print("")
                    print('\x1b[0;30;47m'+'Vous perdez conscience...'+'\x1b[0m')
                    print("")
                    print("########################################")
                    print("########################################")
                    sleep(1)
                    return "death"
                Player.level(Player)
                if Player.classe == "mage":
                    if Player.lvl == 5:
                        print("")
                        print("Vous êtes niveaux 5 !")
                        print("Attention ! À partir de maintenant, seul les livres de magie augmentent vos dégâts.")
                        sleep(2)
                        print("Vous pouvez choisir votre spécialisation parmi :")
                        classe_mage(Player)
                        return
            
            print("Parfait, vous avez fini le jeu !")
            sleep(2)
            print("Maintenant, je vais me plonger dans votre code pour voir si vous avez bien travailler.")
            sleep(2)
            print("Et surtout, bien vérifier qu'il n'y ait aucun",'\x1b[0;33;40m',"copier-coller"'\x1b[0m',"sinon 0.")
            sleep(2)
            print("Alors, avez-vous une dernière chose à me dire ?[oui][non]")
            choice = input()
            choice = choice.lower()
            while choice not in ["oui","non"]:
                print("Votre choix est incorrect !")
                print('\x1b[0;30;47m',"(Lui dire que vous avez retrouvé le ballon de Kader)[oui][non]",'\x1b[0m')
                choice = input()
            if choice == "non":
                print('\x1b[0;33;40m',"[Loïc, le professeur]:",'\x1b[0m')
                print("Salut !")
                sleep(2)
                action = "menu"
                return interface_user(save, m, Player, currentIndex, action)
            if choice == "oui":
                print('\x1b[0;33;40m',"[Loïc, le professeur]:",'\x1b[0m')
                print("Je vous écoute.")
                reponse = str(input())
                if reponse == "ctrlc_ctrlv":
                    print("...Et bien je pense que quelqu'un vous attends, plus haut.")
                    sleep(3)
                    m[5][43] = "⥣"
                    m[4][43] = "-"
                    m[2][43] = "V"
                    action = "void"
                    return interface_user(save, m, Player, currentIndex, action)
                else:
                    print("D'accord...")
                    sleep(1)
                    print("Il semblerait que vous n'ayez pas fait attention au dialogue",'\x1b[0;33;40m',"d'un des personnages du jeu.",'\x1b[0m')
                    sleep(3)
                    print("Quel dommage !")
                    sleep(2)
                    return menu(save, m, currentIndex, Player)
        else:
            return
            
    if currentIndex == [4 , 21]:
        if ballon_de_basket.nom not in Player.arme:
            print("Bravo ! Vous avez retrouvé le",'\x1b[0;33;40m',"ballon de basket",'\x1b[0m',"de Kader !")
            sleep(2)
            print("Mais quel idiot a pu faire tomber le ballon ici...")
            print('\x1b[0;30;47m'+'Appuyez sur [A] pour continuer'+'\x1b[0m')
            choice = input()
            choice = choice.lower()
            while choice != "a":
                choice = input()
            Player.arme.append( ballon_de_basket.nom)
            action = "void"
            return interface_user(save,m,Player, currentIndex, action) # "p" est la nouvelle carte mise à jour
        else:
            return
    if currentIndex == [5, 34]:
        if m[5][34] == "R":
            currentIndex = [5, 33]
            p = quest_rijenth(m, Player)
            action = "void"
            return interface_user(save,m,Player, currentIndex, action) # "p" est la nouvelle carte mise à jour
        else:
            return
    if currentIndex == [1 , 19]:
        if m[1][19] == "?":
           if action == "d":
                currentIndex = [1,18]
           elif action == "z":
                currentIndex = [2,19]
           elif action == "q":
                currentIndex = [1,20]
           print("Vous avez trouvé un",'\x1b[0;33;40m',"levier",'\x1b[0m',"!")
           choice = input("Voulez-vous l'actionner ?[oui][non]")
           if choice == "oui":
               print("Le",'\x1b[0;33;40m',"levier",'\x1b[0m',"a été actionné ! Vous entendez une porte s'ouvrir à votre gauche...")
               sleep(3)
               m[4][15] = "⥣"
               m[1][19] = "*"
               action = "void"
               return interface_user(save,m,Player, currentIndex, action)  # "p" est la nouvelle carte mise à jour
           else:
               action = "void"
               return interface_user(save,m,Player, currentIndex, action)
        else:
            return
    if currentIndex == [7, 12]:
        if m[7][12] == "?":
           currentIndex = [8, 12]
           print("Vous avez trouvé un",'\x1b[0;33;40m',"levier",'\x1b[0m',"!")
           choice = input("Voulez-vous l'actionner ?[oui][non]")
           if choice == "oui":
               print("Le",'\x1b[0;33;40m',"levier",'\x1b[0m',"a été actionné ! Vous entendez une porte s'ouvrir à votre droite...")
               sleep(3)
               m[8][22] = "⥣"
               m[7][12] = "*"
               action = "void"
               return interface_user(save,m,Player, currentIndex, action)  # "p" est la nouvelle carte mise à jour
           else:
               action = "void"
               return interface_user(save,m,Player, currentIndex, action)
        else:
            return
    if currentIndex == [2, 3]:
        if m[2][3] == "F":
            currentIndex = [1,3] # Pour pas que joueur se superpose avec le png
            p = quest_fabrice(m, Player)
            action = "void"
            return interface_user(save,m,Player, currentIndex, action) # "p" est la nouvelle carte mise à jour
        else:
            return
    if currentIndex == [1, 26]:
        if m[1][26] == "K":
            currentIndex = [1,25] 
            p = quest_kader(m, Player)
            action = "void"
            return interface_user(save,m,Player, currentIndex, action) # "p" est la nouvelle carte mise à jour
        else:
            return
    if currentIndex == [9,5]:
        if m[9][5] == "-" and m[9][5] != "Ø":
            Hugo_A()
            Hugo = ["Hugo boss", 5, 300, 9, 10, 100, 55]
            result = combat(Player,Hugo)
            if result == True:
                print("########################################")
                print("########################################")
                print("")
                print('\x1b[0;30;47m'+'Vous perdez conscience...'+'\x1b[0m')
                print("")
                print("########################################")
                print("########################################")
                sleep(1)
                return "death"
            sleep(2)
            print('\x1b[0;33;40m',"[Hugo]:",'\x1b[0m')
            print("Arghhhh...")
            sleep(2)
            print("Comment puis-je perdre dans un jeu que j'ai moi même programmé !!")
            print("...")
            sleep(3)
            print("Maintenant tu dois fouiller la",'\x1b[0;33;40m' "Bibliotheque",'\x1b[0m' "pour trouver le livre tant recherché par Fabrice")
            sleep(2)
            print('\x1b[0;30;47m'+'Appuyez sur [A] pour mettre fin à la discussion.'+'\x1b[0m')
            choice = input()
            choice = choice.lower()
            while choice != "a":
                choice = input()
            m[9][5] = "Ø"
            Player.level(Player)
            if Player.classe == "mage":
                if Player.lvl == 5:
                    print("")
                    print("Vous êtes niveaux 5 !")
                    print("Attention ! À partir de maintenant, seul les livres de magie augmentent vos dégâts.")
                    sleep(2)
                    print("Vous pouvez choisir votre spécialisation parmi :")
                    classe_mage(Player)
            return 
        else:
            return
    if currentIndex == [6,9]:
        if les_bas_fonds_de_python.nom not in Player.arme:
            print("Felicitation ! Vous avez trouvé le",'\x1b[0;33;40m',"Très precieux livre",'\x1b[0m',"de Fabrice !")
            sleep(2)
            print("Maintenant retounez voir Fabrice afin de continuer votre aventure")
            sleep(2)
            print('\x1b[0;30;47m'+'Appuyez sur [A] pour continuer'+'\x1b[0m')
            m[5][7] = "⥣"
            m[1][4] = "⥢"
            choice = input()
            choice = choice.lower()
            while choice != "a":
                choice = input()
            Player.arme.append(les_bas_fonds_de_python.nom)
            action = "void"
            return interface_user(save,m,Player, currentIndex, action)  # "p" est la nouvelle carte mise à jour
        else:
            return
    else: 
        # Soit on trouve un coffre, soit on lance un combat, soit rien ne se passe.
        chance = randint(0,5)
        
        if chance <= 3:
            return
        if chance == 4:
            chest(Player)
            return
        
        if chance == 5:
            monstre = monstre(monstre_liste, Player)
            print("########################################")
            print("########################################")
            print("")
            print('\x1b[0;35;40m' +"Un monstre vous attaque !" + '\x1b[0m')
            print("")
            print("########################################")
            print("########################################")
            result = combat(Player, monstre)
            sleep(2)
            if result == True:
                print("########################################")
                print("########################################")
                print("")
                print('\x1b[0;30;47m'+'Vous perdez conscience...'+'\x1b[0m')
                print("")
                print("########################################")
                print("########################################")
                sleep(1)
                return "death"
            Player.level(Player)
            if Player.classe == "mage":
                if Player.lvl == 5:
                    print("")
                    print("Vous êtes niveaux 5 !")
                    print("Attention ! À partir de maintenant, seul les livres de magie augmentent vos dégâts.")
                    sleep(2)
                    print("Vous pouvez choisir votre spécialisation parmi :")
                    classe_mage(Player)
                    
            return 
        
        
 
###############################
######## FIN EVENEMENT ########
###############################


# Cette fonction vas décrire la zone ou se trouve le joueur. La description s'affiche dans la partie haute
# de l'interface utilisateur.
def zone_description(currentIndex): 
    # Décrire le coeur du batiment.
    if currentIndex == [5, 12]:
        print(("#######################################################################################"))
        print("")
        print('\x1b[0;30;47m'+'DESCRIPTION:'+'\x1b[0m')
        print("Vous arrivez au coeur de l'institution.")
        sleep(2)
        print("Vous apercevez un squelette au sol, la bouche ouvert avec une fourchette plantée dans l'orteil gauche.")
        sleep(3)
        print("Devant vous, un long couloir mal éclairé.")
        print("")
        print(("#######################################################################################"))
        print('\x1b[0;30;47m'+'Appuyez sur [A] pour mettre fin à la discussion.'+'\x1b[0m')
        choice = input()
        choice = choice.lower()
        while choice != "a":
            choice = input()
        return
    # Decrire l'amphithéatre
    if currentIndex == [9, 28]:
        print(("#######################################################################################"))
        print("")
        print('\x1b[0;30;47m'+'DESCRIPTION:'+'\x1b[0m')
        print("")
        print("Vous apercevez un panneau 'BIENVENUE dans le manoir Path'Hetic'.")
        print("...")
        sleep(3)
        print("Le manoir est entouré de brouillard et une odeur putride plombe l'atmosphère.")
        sleep(2)
        print(("#######################################################################################"))
        print('\x1b[0;30;47m'+'Appuyez sur [A] pour mettre fin à la discussion.'+'\x1b[0m')
        choice = input()
        choice = choice.lower()
        while choice != "a":
            choice = input()
        return
    if currentIndex == [1, 28]:
        print(("#######################################################################################"))
        print("")
        print('\x1b[0;30;47m'+'DESCRIPTION:'+'\x1b[0m')
        print("")
        print("Vous voici dans l'amphithéâtre.")
        print("Un endroit d'habitude plein de vie.")
        sleep(3)
        print("L'ambiance est lourde et pesante, mais le lieu vous rappelle de bons souvenirs...")
        print("...")
        sleep(3)
        print(("#######################################################################################"))
        print('\x1b[0;30;47m'+'Appuyez sur [A] pour mettre fin à la discussion.'+'\x1b[0m')
        choice = input()
        choice = choice.lower()
        while choice != "a":
            choice = input()
        return
    if currentIndex == [9, 38]:
        print(("#######################################################################################"))
        print("")
        print('\x1b[0;30;47m'+'DESCRIPTION:'+'\x1b[0m')
        print("")
        print("Vous arrivez dans un long couloir plutôt étroit.")
        sleep(3)
        print("Les portes en mauvaise état ne vous rassure pas vis à vis de la suite...")
        print("...")
        sleep(3)
        print(("#######################################################################################"))
        print('\x1b[0;30;47m'+'Appuyez sur [A] pour mettre fin à la discussion.'+'\x1b[0m')
        choice = input()
        choice = choice.lower()
        while choice != "a":
            choice = input()
        return
    if currentIndex == [5, 39]:
        print(("#######################################################################################"))
        print("")
        print('\x1b[0;30;47m'+'DESCRIPTION:'+'\x1b[0m')
        print("")
        print("Une nuée d'insectes volants surgissent de nulle part !")
        sleep(2)
        print("...")
        sleep(3)
        print("Elles obscurcissent votre vision l'espace d'un instant... Vous apercevez des tables et des chaises rongées de part et d'autre.")
        print("")
        print(("#######################################################################################"))
        print('\x1b[0;30;47m'+'Appuyez sur [A] pour mettre fin à la discussion.'+'\x1b[0m')
        choice = input()
        choice = choice.lower()
        while choice != "a":
            choice = input()
        return
    
    
    
def description_player(Player, currentIndex): # currentIndex => position actuelle du joueur
    zone_description(currentIndex)
    print("#######################################################################################")
    print("")
    print("[Nom] -", Player.nom)
    print("[Classe] -", Player.classe)
    print("[EXP] -", "Vous avez :", Player.EXP, "d'expérience")
    print("[LVL] -", "Vous êtes niveau(x):", Player.lvl)
    print("[HP] -", "Vous avez :", Player.HP, "PV")
    print("")
    print('\x1b[0;30;47m'+'MAP:'+'\x1b[0m')
    print("")
    return



# Cette fonction décrit au joueur la zone (Nord, Ouest, Sud, Est) de la case ou il se trouve.
def choix_direction(): 
    print("")
    print('\x1b[0;30;47m'+'DEPLACEMENT:'+'\x1b[0m')
    print("")
    print("[z] -", "▲ Aller au nord ")
    print("[s] -", "▼ Aller au sud ")
    print("[q] -", "◄ Aller à l'ouest ")
    print("[d] -", "► Aller à l'est ")
    print("")
    print("#######################################################################################")

# Cette fonction permet au joueur d'agir sur la carte ou il se trouve.
# Choix d'une action : (Explorer, Inventaire, Stats, Marchand)

def choix_action():
    print("")
    print('\x1b[0;30;47m'+'ACTION:'+'\x1b[0m')
    print("")
    print("[a] -", "Afficher les statistiques de votre personnage")
    print("[e] -", "Afficher l'inventaire")
    print("[f] -", "Consulter le marchand") # Cette evenement est conditionnel
    print("[w] -", "Sauvegarder votre progression")
    print("[x] -", "Quitter le jeu")
    return

# Ici le joueur choisit sont action en entrant la lettre correspondant à l'action.
def choix_joueur():
    print("")
    print(("#######################################################################################"))
    print('\x1b[0;30;47m'+'Veuillez entrer votre choix :'+'\x1b[0m')
    choice = input()
    choice = choice.lower()
    return choice

# Retourne la decision du joueur. La decision du joueur définit la valeur de la variable "action".
def decision(choice):
    # Rajouter un check d'erreur pour ne pas que le jeu s'arrête sur un missclick /!\
    if choice == "x":
        action = "x"
        return action
    if choice == "f":
        action = "f"
        return action
    if choice == "z":
        action = "z"
        return action
    if choice == "q":
        action = "q"
        return action
    if choice == "s":
        action = "s"
        return action
    if choice == "d":
        action = "d"
        return action
    if choice == "a":
        action = "a"
        return action
    if choice == "e":
        action = "e"
        return action
    if choice == "w":
        action = "w"
        return action
    

def affichage_interface(m, Player, currentIndex, action):
    description_player(Player, currentIndex)
    carte(m, currentIndex, action)
    choix_direction()
    choix_action()
    return 
    
    
"""
Cette partie regroupe les fonctions gérant trois options. (Inventaire, Stats, Marchand) 
"""

def check_inventaire(Player):
    Player.inventaire(Player)
    if Player.HP < Player.MAXHP:
        print("")
        print("Voulez-vous utilisez une potion ? ", "[oui]/[non]")
        choice = input()
        choice = choice.lower()
        while choice != "oui" and choice != "non":
            print("")
            print("Erreur ! ")
            print("Voulez-vous utilisez une potion ? ", "[oui]/[non]")
            choice = input()
            choice = choice.lower()
        if choice == "oui":
            soin(Player)
        return
    return

def check_stats(Player):
    Player.stats(Player)
    return

