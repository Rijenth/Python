# Liste type d'un monstre :
# monstre = ["nom du monstre", lvl, HP, ATK, DEF, EXP, VIT]
from random import randint
from time import sleep
from Player import *
from item import *
from Potion_soin import *

# Liste des monstres disponibles
monstre_liste = ["Python", "JavaScript", "HTML/CSS"]

# Permet de changer la couleur de certains textes et enlève les guillements dans les arguments.
def print_fond_noir(*args):
    return '\x1b[6;37;40m ' + "".join(str(a) for a in args) + '\x1b[0m'
def print_green_word(*args):
    return '\x1b[0;32;40m' + "".join(str(a) for a in args) + '\x1b[0m'
def print_red_word(*args):
    return '\x1b[0;33;40m' + "".join(str(a) for a in args) + '\x1b[0m'
def print_purple_word(*args):
    return '\x1b[0;35;40m' + "".join(str(a) for a in args) + '\x1b[0m'

# Cette fonction choisit un monstre parmi python, javascript et html/css
def monstre_choix(monstre_liste):
    random = randint(0, 2)
    monstre_final = monstre_liste[random]
    return monstre_final

# Permet de définir les stats d'un monstre en fonction de son niveau
def stats_mob(name, level):
    HP = level*randint(8, 14)
    ATK = level*(randint(3, 4))
    DEF = level*(randint(3, 5))
    EXP = level*(randint(6, 18))
    VIT = level*(randint(3, 5))
    return [name, level, HP, ATK, DEF, EXP, VIT]

# Cette fonction choisit un monstre dans la liste de monstre.
def monstre(monstre_liste, Player): 
    name = monstre_choix(monstre_liste)
    level = Player.lvl
    monstre = stats_mob(name, level)
    return monstre
    
# Cette fonction définit les dégats d'une attaque d'un monstre sur le joueur
def monstre_attaque(entite_attaque, Player):
    fluctuation_degat = randint(8, 12)
    damage = (entite_attaque[3]*fluctuation_degat)/10
    final_damage = defense(damage, defense_en_fonction_armure(Player))
    final_damage = round(final_damage)
    return final_damage

# Cette fonction définit les dégats d'une attaque du joueur sur un monstre
def joueur_attaque(Player, entite_defense):
    fluctuation_degat = randint(8, 12)
    damage = (damage_en_fonction_arme(Player)*fluctuation_degat)/10
    final_damage = defense(damage, entite_defense[4])
    final_damage = round(final_damage)
    return final_damage

# Remplacer Player.ATK par Player.INT
def mage(Player, entite_defense):
    damage = Player.ATK 
    final_damage = defense(damage, entite_defense[4])
    return final_damage

def mage_feu(Player, entite_defense):
    damage = degat_en_fonction_int(Player)
    final_damage = defense(damage, entite_defense[4])
    return final_damage
# attaque_bonus = randint(0,1)
           
def mage_eau(Player, entite_defense):
    damage = degat_en_fonction_int(Player)
    final_damage = defense(damage, entite_defense[4])
    return final_damage
# Heal de 25% des dégâts infligés

def mage_terre(Player):
    damage = degat_en_fonction_int(Player)
    final_damage = defense(damage, 0)
    return final_damage
# Ignore la defense de l'adversaire


# Cette fonction permet d'augmenter les dégâts en fonction du taux critique du player.
def coup_critique(Player):
    chance_de_crit = randint(0, 100)
    if chance_de_crit <= Player.CRIT:
        return "oui"
    return "non"
    

# Permet de réduire les dégats subis en fonction de ta defense. 
def defense(damage, maDEF):
    final_damage = damage - ((damage*maDEF)/100)
    return final_damage

# Verifie si quelqu'un est mort. Renvoie un "true" ou un "false"
# Pour voir si joueur est mort
def check_defeat(Player):
    etat = False
    if Player.HP <= 0 :
        etat = True
    return etat
# Pour voir si monstre est mort
def check_defeat_monster(monster):
    etat = False
    if monster[2] <= 0 :
        etat = True
    return etat


    
# Cette fonctionne ajoute un peu de hasard lors des combat.
# Le monstre réduit les dégats reçu par 2 lorsque cette effet s'active.
def monster_ia():
    choice = randint(0, 5) # 1 chance sur 6 
    if choice == 0 :
        return "defendre"
    return 

# Demande à l'utilisateur l'action qu'il souhaite effectuer.
def ask_user_action_combat(Player):
    print("Choisissez votre action :")
    if Player.classe not in ["Mage de feu", "Mage d'eau", "Mage de terre", "mage"]:
        print("[A] : Attaquer","[P] : Potion", "[F] : Fuir")
    else:
        print("[M] : Magie ","[P] : Potion", "[F] : Fuir")
    print("")
    print("#######################################################################################")
    action = input()
    action = action.lower()
    if Player.classe not in ["Mage de feu", "Mage d'eau", "Mage de terre", "mage"]:
        while action != "a" and action != "f" and action != "p":
            print("Action incorrect !")
            print("[A] : Attaquer","[P] : Potion", "[F] : Fuir")
            action = input()
            action = action.lower()
        if action == "p":
            soin(Player)
            return "soin"
        if action == "a":
            return "attaque"
        # La liste des objets est défini dans l'inventaire
        if action == "f":
            return "fuite"
    else:
        while action != "m" and action != "f" and action != "p":
            print("Action incorrect !")
            print("[M] : Magie","[P] : Potion", "[F] : Fuir")
            action = input()
            action = action.lower()
        if action == "p":
            soin(Player)
            return "soin"
        if action == "m":
            return "magie"
        # La liste des objets est défini dans l'inventaire
        if action == "f":
            return "fuite"
        

    
# Cette fonction permet de determiner l'initiative entre deux personnages lors d'un combat.
# Elle retourne "monster" si c'est le monstre qui a l'initiative. Sinon, elle renvoie "player", et c'est le joueur qui joue.
def initiative(Player, monster):
    if monster[6] > Player.VIT:
        return "monster"
    return "player"

# Cette fonction affiche les HP des entités, elle les ramène à "0" si au cours du combats les HP sont inférieur à 0
def fight_hp(Player, monster):
    if monster[2] <= 0:
        monster[2] = 0
        print("")
        print("     ###### Points de vie de l'adversaire:", monster[2], "######")
        print("     ###### Vos points de vie :", Player.HP, "######")
        print("")
        return
    if Player.HP <= 0:
        Player.HP = 0
        print("")
        print("     ###### Points de vie de l'adversaire:", monster[2], "######")
        print("     ###### Vos points de vie :", Player.HP, "######")
        print("")
        return
    print("")
    print("     ###### Points de vie de l'adversaire:", monster[2], "######")
    print("     ###### Vos points de vie :", Player.HP, "######")
    print("")

def fuite(Player, monster, who_play_first):
    if who_play_first == "monster":
        print("")
        print("Vous tentez de fuir...")
        sleep(1)
        echec_fuite = randint(0, 2)
        if echec_fuite <= 1 :
            print("Vous n'avez pas reussi à fuir !")
            sleep(1)
            return "echec"
        print("Vous avez reussi à fuir !")
        sleep(1)
        return "reussite"
    if monster[6] == Player.VIT:
        print("")
        print("Vous tentez de fuir...")
        sleep(1)
        echec_fuite = randint(0, 2)
        if echec_fuite <= 1:
            print("Vous avez reussi à fuir !")
            sleep(1)
            return "reussite"
        print("Vous n'avez pas reussi à fuir !")
        sleep(1)
        return "echec"
    # Les classes très rapide ne peuvent pas échouer la fuite.
    print("Vous tentez de fuir...")
    sleep(1)
    print("... Et vous réussissez sans problème !")
    return "reussite"
    
    
    
# Voici la fonction finale de combat
def combat(Player, monster):
    player_defeated = False
    print("Vous affrontez", '\x1b[0;33;40m', monster[0],'\x1b[0m',"de niveau", monster[1])
    fight_hp(Player, monster)
    # Initialisation de la variable esquive du monstre
    monster_cancel_damage = False
    # Ici j'intègre le système d'initiative.
    who_play_first = initiative(Player, monster)
    # Tant que les HP des deux combattants sont supérieur à 0.
    while monster[2] > 0 and Player.HP > 0:
        action = ask_user_action_combat(Player)
        print("")
        print("#######################################################################################")
        result = ""
        # La fonction monster_ia() determine si le monstre prévoit de parade la prochaine attaque.
        monster_choice = monster_ia()
        # Le joueur commence son tour.
        if action == "fuite":
            result = fuite(Player, monster, who_play_first)
            if result == "reussite":
                return
        if who_play_first == "player":
            
            # Les attaques du mage selon sa spécialisation.
            if action == "magie":
                
                if Player.classe == "Mage de feu":
                    final_damage = mage_feu(Player, monster)
                    final_damage = round(final_damage)
                    monster[2] = monster[2] - final_damage
                    print("Vous lancez une boule de feu !")
                    print(monster[0], print_green_word("subit : " , final_damage, " points de dégâts !"))
                    bonus_attaque = randint(0, 1)
                    if bonus_attaque == 1:
                        sleep(2)
                        print("Vous attaquez une seconde fois ! ")
                        final_damage = mage_feu(Player, monster)
                        final_damage = round(final_damage)
                        monster[2] = monster[2] - final_damage
                        print(monster[0], print_green_word("subit : " , final_damage, " points de dégâts !"))
                    if check_defeat_monster(monster) == True:
                        fight_hp(Player, monster)
                        print("Vous avez vaincu ",monster[0], print_fond_noir("Vous gagnez : ", monster[5], " EXP"))
                        Player.EXP = Player.EXP + monster[5]
                        return player_defeated
                if Player.classe == "Mage d'eau":
                    final_damage = mage_eau(Player, monster)
                    final_damage = round(final_damage)
                    monster[2] = monster[2] - final_damage
                    print("Vous lancez une vague sur l'ennemi !")
                    print(monster[0], print_green_word("subit : " , final_damage, " points de dégâts !"))
                    heal = (final_damage/4)
                    heal = round(heal)
                    print(print_green_word("Vous récupérez ", heal, " points de vie."))
                    Player.HP = Player.HP + heal
                    if Player.HP > Player.MAXHP:
                        Player.HP = Player.MAXHP
                    if check_defeat_monster(monster) == True:
                        fight_hp(Player, monster)
                        print("Vous avez vaincu ",monster[0], print_fond_noir("Vous gagnez : ", monster[5], " EXP"))
                        Player.EXP = Player.EXP + monster[5]
                        return player_defeated
                if Player.classe == "Mage de terre":
                    final_damage = mage_terre(Player)
                    final_damage = round(final_damage)
                    monster[2] = monster[2] - final_damage
                    print("Vous lancez un rocher sur l'ennemi ! La défense de l'ennemi est ignoré.")
                    print(monster[0], print_green_word("subit : " , final_damage, " points de dégâts !"))
                    if check_defeat_monster(monster) == True:
                        fight_hp(Player, monster)
                        print("Vous avez vaincu ",monster[0], print_fond_noir("Vous gagnez : ", monster[5], " EXP"))
                        Player.EXP = Player.EXP + monster[5]
                        return player_defeated
                if Player.classe == "mage":
                    final_damage = mage(Player, monster)
                    final_damage = round(final_damage)
                    monster[2] = monster[2] - final_damage
                    print("Vous lancez un sort sur votre ennemi !")
                    print(monster[0], print_green_word("subit : " , final_damage, " points de dégâts !"))
                    if check_defeat_monster(monster) == True:
                        fight_hp(Player, monster)
                        print("Vous avez vaincu ",monster[0], print_fond_noir("Vous gagnez : ", monster[5], " EXP"))
                        Player.EXP = Player.EXP + monster[5]
                        return player_defeated
                
            if action == "attaque":
                if monster_cancel_damage == True:
                    # Le monstre se défend et ne subis que la moitié des dégâts et bloque les coups critiques.
                    final_damage = joueur_attaque(Player, monster)/2
                    final_damage = round(final_damage)
                    monster[2] = monster[2] - final_damage
                    print(monster[0] , " se protège et subit moins de dégâts ! " , print_purple_word(" Il subit : ", final_damage, " de dégâts au lieu de ", final_damage*2, " dégâts."))
                    sleep(1)
                    monster_cancel_damage = False
                    if check_defeat_monster(monster) == True:
                        fight_hp(Player, monster)
                        print("Vous avez vaincu ",monster[0], print_fond_noir("Vous gagnez : ", monster[5], " EXP"))
                        Player.EXP = Player.EXP + monster[5]
                        return player_defeated
                else: 
                    final_damage = joueur_attaque(Player, monster)
                    crit_check = coup_critique(Player)
                    if crit_check == "oui":
                        final_damage = final_damage*2
                        monster[2] = monster[2] - final_damage
                        print("Vous infligez un coup critique !", "Le", monster[0], print_red_word("subit : " , final_damage, " points de dégâts !"))
                        sleep(1)
                        if check_defeat_monster(monster) == True:
                            fight_hp(Player, monster)
                            print("Vous avez vaincu ",monster[0], print_fond_noir("Vous gagnez : " , monster[5], " EXP"))
                            Player.EXP = Player.EXP + monster[5]
                            return player_defeated
                    else:
                        monster[2] = monster[2] - final_damage
                        print(monster[0], print_green_word("subit : " , final_damage, " points de dégâts !"))
                        sleep(1)
                        if check_defeat_monster(monster) == True:
                            fight_hp(Player, monster)
                            print("Vous avez vaincu ",monster[0], print_fond_noir("Vous gagnez : " , monster[5], " EXP"))
                            Player.EXP = Player.EXP + monster[5]
                            return player_defeated
        # L'ennemi commence son tour
        final_damage = monstre_attaque(monster, Player)
        Player.HP = Player.HP - final_damage
        print(monster[0], "vous attaque et", print_red_word("vous inflige : ", final_damage, " points de dégâts !" ))
        sleep(1)
        if check_defeat(Player) == True:
            fight_hp(Player, monster)
            print("Vous avez été vaincu !")
            player_defeated = True
            return player_defeated
        if monster_choice == "defendre":
            monster_cancel_damage = True
        if who_play_first == "monster" and result != "echec" and action != "soin":
            # Si le monstre a l'initiative, le joueur attaque après le monstre.
            if action == "magie":
                if Player.classe == "mage":
                    final_damage = mage(Player, monster)
                    final_damage = round(final_damage)
                    monster[2] = monster[2] - final_damage
                    print("Vous lancez un sort sur votre ennemi !")
                    print(monster[0], print_green_word("subit : " , final_damage, " points de dégâts !"))
                    if check_defeat_monster(monster) == True:
                        fight_hp(Player, monster)
                        print("Vous avez vaincu ",monster[0], print_fond_noir("Vous gagnez : ", monster[5], " EXP"))
                        Player.EXP = Player.EXP + monster[5]
                        return player_defeated
                if Player.classe == "Mage de feu":
                    final_damage = mage_feu(Player, monster)
                    final_damage = round(final_damage)
                    monster[2] = monster[2] - final_damage
                    print("Vous lancez une boule de feu !")
                    print(monster[0], print_green_word("subit : " , final_damage, " points de dégâts !"))
                    bonus_attaque = randint(0, 1)
                    if bonus_attaque == 1:
                        sleep(2)
                        print("Vous attaquez une seconde fois ! ")
                        final_damage = mage_feu(Player, monster)
                        final_damage = round(final_damage)
                        monster[2] = monster[2] - final_damage
                        print(monster[0], print_green_word("subit : " , final_damage, " points de dégâts !"))
                    if check_defeat_monster(monster) == True:
                        fight_hp(Player, monster)
                        print("Vous avez vaincu ",monster[0], print_fond_noir("Vous gagnez : ", monster[5], " EXP"))
                        Player.EXP = Player.EXP + monster[5]
                        return player_defeated
                if Player.classe == "Mage d'eau":
                    final_damage = mage_eau(Player, monster)
                    final_damage = round(final_damage)
                    monster[2] = monster[2] - final_damage
                    print("Vous lancez une vague sur l'ennemi !")
                    print(monster[0], print_green_word("subit : " , final_damage, " points de dégâts !"))
                    heal = (final_damage/4)
                    heal = round(heal)
                    print(print_green_word("Vous récupérez ", heal , " points de vie."))
                    Player.HP = Player.HP + heal
                    if Player.HP > Player.MAXHP:
                        Player.HP = Player.MAXHP
                    if check_defeat_monster(monster) == True:
                        fight_hp(Player, monster)
                        print("Vous avez vaincu ",monster[0], print_fond_noir("Vous gagnez : ", monster[5], " EXP"))
                        Player.EXP = Player.EXP + monster[5]
                        return player_defeated
                if Player.classe == "Mage de terre":
                    final_damage = mage_terre(Player)
                    final_damage = round(final_damage)
                    monster[2] = monster[2] - final_damage
                    print("Vous lancez un rocher sur l'ennemi ! La défense de l'ennemi est ignoré.")
                    print(monster[0], print_green_word("subit : " , final_damage, " points de dégâts !"))
                    if check_defeat_monster(monster) == True:
                        fight_hp(Player, monster)
                        print("Vous avez vaincu ",monster[0], print_fond_noir("Vous gagnez : ", monster[5], " EXP"))
                        Player.EXP = Player.EXP + monster[5]
                        return player_defeated
            
            else: 
                final_damage = joueur_attaque(Player, monster)
                crit_check = coup_critique(Player)
                if crit_check == "oui":
                    final_damage = final_damage*2
                    monster[2] = monster[2] - final_damage
                    print("Vous infligez un coup critique !", "Le", monster[0], print_red_word("subit : " , final_damage, " points de dégâts !"))
                    sleep(1)
                    if check_defeat_monster(monster) == True:
                        fight_hp(Player, monster)
                        print("Vous avez vaincu ",monster[0], print_fond_noir("Vous gagnez : " , monster[5], " EXP"))
                        Player.EXP = Player.EXP + monster[5]
                        Player.level(Player)
                        return player_defeated
                else:
                    monster[2] = monster[2] - final_damage
                    print("Le", monster[0], print_green_word("subit : " , final_damage, " points de dégâts !"))
                    sleep(1)
                    if check_defeat_monster(monster) == True:
                        fight_hp(Player, monster)
                        print("Vous avez vaincu ",monster[0], print_fond_noir("Vous gagnez : " , monster[5], " EXP"))
                        Player.EXP = Player.EXP + monster[5]
                        Player.level(Player)
                        return player_defeated
        fight_hp(Player, monster)
        # Ici on affiche les HP des deux entités afin d'avoir un suivi du combat.
        
# Les compétences du boss secret Valentin
#valentin = ["Valentin, Le ninja ctrlc_ctrlv", Player.lvl, 1800, Player.ATK, Player.DEF, 1, 40]
#2/ Sort d'eau : Degats + soin (25% de chance)
#3/ Sort de feu : Degats + attaque bonus (50%) (25% de chance)
#4/ Sort de terre : Attaque qui ignore def (25% de chance)

def tricherie(Player):
    print('\x1b[0;33;40m',"Valentin, Le ninja ctrlc_ctrlv",'\x1b[0m', "utilise un pouvoir secret et réduit vos HP à 1 !")
    Player.HP = 1
    return Player.HP

def competence_valentin(Player, valentin):
    random = randint(0,2)
    if random == 0: #Sort d'eau
        print('\x1b[0;33;40m',"Valentin, Le ninja ctrlc_ctrlv",'\x1b[0m', "utilise le pouvoir de l'eau et vous envoie une vague !")
        damage = valentin[3]
        final_damage = defense(damage, Player.DEF)
        return final_damage, "sort d'eau"
    if random == 1: #Sort de feu
        print('\x1b[0;33;40m',"Valentin, Le ninja ctrlc_ctrlv",'\x1b[0m', "utilise le pouvoir du feu et vous envoie une boule de feu !")
        damage = valentin[3]
        final_damage = defense(damage, Player.DEF)
        return final_damage, "sort de feu"
    if random == 2: #Sort de terre
        print('\x1b[0;33;40m',"Valentin, Le ninja ctrlc_ctrlv",'\x1b[0m', "utilise le pouvoir de la terre et vous envoie un rocher. Votre défense est ignorée !")
        damage = valentin[3]
        final_damage = defense(damage, 0)
        return final_damage, ""
        

    
# Le combat contre le boss Valentin étant particulier, le code de combat a dû être reconsiderer en conséquence.
def combat_valentin(Player, Valentin):
    player_defeated = False
    print('\x1b[0;33;40m',"Valentin, Le ninja ctrlc_ctrlv",'\x1b[0m', "vous défie !")
    fight_hp(Player, Valentin)
    while Valentin[2] > 0 and Player.HP > 0:
        action = ask_user_action_combat(Player)
        print("")
        print("#######################################################################################")
        if action == "fuite":
            print('\x1b[0;33;40m',"[Valentin, Le ninja ctrlc_ctrlv]:",'\x1b[0m',"Le pouvoir du copier-coller à eu raison de toi.")
            sleep(2)
            return
        if action == "magie":
            
            if Player.classe == "Mage de feu":
                final_damage = mage_feu(Player, Valentin)
                final_damage = round(final_damage)
                Valentin[2] = Valentin[2] - final_damage
                print("Vous lancez une boule de feu !")
                print('\x1b[0;33;40m',"Valentin, Le ninja ctrlc_ctrlv",'\x1b[0m', print_green_word("subit : " , final_damage, " points de dégâts !"))
                bonus_attaque = randint(0, 1)
                if bonus_attaque == 1:
                    sleep(2)
                    print("Vous attaquez une seconde fois ! ")
                    final_damage = mage_feu(Player, Valentin)
                    final_damage = round(final_damage)
                    Valentin[2] = Valentin[2] - final_damage
                    print('\x1b[0;33;40m',"Valentin, Le ninja ctrlc_ctrlv",'\x1b[0m', print_green_word("subit : " , final_damage, " points de dégâts !"))
                if check_defeat_monster(Valentin) == True:
                    fight_hp(Player, Valentin)
                    print('\x1b[0;33;40m',"Valentin, Le ninja ctrlc_ctrlv",'\x1b[0m', print_fond_noir("Vous gagnez : ", Valentin[5], " EXP"))
                    Player.EXP = Player.EXP + Valentin[5]
                    return player_defeated
            if Player.classe == "Mage d'eau":
                final_damage = mage_eau(Player, Valentin)
                final_damage = round(final_damage)
                Valentin[2] = Valentin[2] - final_damage
                print("Vous lancez une vague sur l'ennemi !")
                print('\x1b[0;33;40m',"Valentin, Le ninja ctrlc_ctrlv",'\x1b[0m', print_green_word("subit : " , final_damage, " points de dégâts !"))
                heal = (final_damage/4)
                heal = round(heal)
                print(print_green_word("Vous récupérez ", heal, " points de vie."))
                Player.HP = Player.HP + heal
                if Player.HP > Player.MAXHP:
                    Player.HP = Player.MAXHP
                if check_defeat_monster(Valentin) == True:
                    fight_hp(Player, Valentin)
                    print('\x1b[0;33;40m',"Valentin, Le ninja ctrlc_ctrlv",'\x1b[0m', print_fond_noir("Vous gagnez : ", Valentin[5], " EXP"))
                    Player.EXP = Player.EXP + Valentin[5]
                    return player_defeated
            if Player.classe == "Mage de terre":
                final_damage = mage_terre(Player)
                final_damage = round(final_damage)
                Valentin[2] = Valentin[2] - final_damage
                print("Vous lancez un rocher sur l'ennemi ! La défense de l'ennemi est ignoré.")
                print('\x1b[0;33;40m',"Valentin, Le ninja ctrlc_ctrlv",'\x1b[0m', print_green_word("subit : " , final_damage, " points de dégâts !"))
                if check_defeat_monster(Valentin) == True:
                    fight_hp(Player, Valentin)
                    print('\x1b[0;33;40m',"Valentin, Le ninja ctrlc_ctrlv",'\x1b[0m', print_fond_noir("Vous gagnez : ", Valentin[5], " EXP"))
                    Player.EXP = Player.EXP + Valentin[5]
                    return player_defeated
            if Player.classe == "mage":
                final_damage = mage(Player, Valentin)
                final_damage = round(final_damage)
                Valentin[2] = Valentin[2] - final_damage
                print("Vous lancez un sort sur votre ennemi !")
                print('\x1b[0;33;40m',"Valentin, Le ninja ctrlc_ctrlv",'\x1b[0m', print_green_word("subit : " , final_damage, " points de dégâts !"))
                if check_defeat_monster(Valentin) == True:
                    fight_hp(Player, Valentin)
                    print('\x1b[0;33;40m',"Valentin, Le ninja ctrlc_ctrlv",'\x1b[0m', print_fond_noir("Vous gagnez : ", Valentin[5], " EXP"))
                    Player.EXP = Player.EXP + Valentin[5]
                    return player_defeated
            
        if action == "attaque":
            
            final_damage = joueur_attaque(Player, Valentin)
            crit_check = coup_critique(Player)
            if crit_check == "oui":
                final_damage = final_damage*2
                Valentin[2] = Valentin[2] - final_damage
                print("Vous infligez un coup critique !",'\x1b[0;33;40m',"Valentin, Le ninja ctrlc_ctrlv",'\x1b[0m', print_red_word("subit : " , final_damage, " points de dégâts !"))
                sleep(1)
                if check_defeat_monster(Valentin) == True:
                    fight_hp(Player, Valentin)
                    print("Vous avez vaincu ", '\x1b[0;33;40m',"Valentin, Le ninja ctrlc_ctrlv",'\x1b[0m', print_fond_noir("Vous gagnez : " , Valentin[5], " EXP"))
                    Player.EXP = Player.EXP + Valentin[5]
                    return player_defeated
            else:
                Valentin[2] = Valentin[2] - final_damage
                print('\x1b[0;33;40m',"Valentin, Le ninja ctrlc_ctrlv",'\x1b[0m', print_green_word("subit : " , final_damage, " points de dégâts !"))
                sleep(1)
                if check_defeat_monster(Valentin) == True:
                    fight_hp(Player, Valentin)
                    print("Vous avez vaincu", '\x1b[0;33;40m',"Valentin, Le ninja ctrlc_ctrlv",'\x1b[0m', print_fond_noir("Vous gagnez : " , Valentin[5], " EXP"))
                    Player.EXP = Player.EXP + Valentin[5]
                    return player_defeated
        # Valentin commence son tour
        type_sort = "" # On reset le sort que Valentin avait choisi.
        choix_attaque_valentin = randint(0,5)
        if choix_attaque_valentin == 0:
            Player.HP = tricherie(Player)
        else:
            final_damage, type_sort = competence_valentin(Player, Valentin) # "type_sort" est le type de sort que Valentin a utilisé dans la fonction competence_valentin()
            final_damage = round(final_damage)
            print('\x1b[0;33;40m',"Valentin, Le ninja ctrlc_ctrlv",'\x1b[0m', "vous attaque et", print_red_word("vous inflige : ", final_damage, " points de dégâts !" ))
            Player.HP = Player.HP - final_damage
            if type_sort == "sort de feu":
                choix_attaque_valentin = randint(0, 1)
                if choix_attaque_valentin == 0:
                    print('\x1b[0;33;40m',"Valentin, Le ninja ctrlc_ctrlv",'\x1b[0m', "vous attaque une seconde fois avec une boule de feu et",print_red_word("vous inflige : ", final_damage, " points de dégâts supplémentaire !" ))
                    Player.HP = Player.HP - final_damage
            if type_sort == "sort d'eau":
                heal = final_damage/2
                heal = round(heal)
                print('\x1b[0;33;40m',"Valentin, Le ninja ctrlc_ctrlv",'\x1b[0m', "récupère",heal,"points de vie !")
                Valentin[2] = Valentin[2] + heal
        sleep(1)
        if check_defeat(Player) == True:
            fight_hp(Player, Valentin)
            print("Vous avez été vaincu !")
            player_defeated = True
            return player_defeated
        print("")
        fight_hp(Player, Valentin)
        
    


        