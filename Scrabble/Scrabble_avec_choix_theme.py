import random
print("Bienvenue dans le jeu du mini Scrabble !") 
Liste_Manga = ["naruto", "bleach","blackjack", "golgo","berserk","ippo","dreamland","foodwars","hellsing"]
Liste_SuperHero = ["superman", "batman", "spiderman", "thor", "blackpanther", "catwoman","flash","deadpool","hulk"]
Liste_Pays = ["france", "russie", "belgique", "espagne", "inde", "espagne", "croatie", "canada", "portugal"]
Liste_theme = ["manga", "superhero", "pays"]
Score = 0
Liste_de_trois = []
liste_test = []
print("Les thèmes sont  : Manga , Heros , Pays")
choice = input("Choisissez votre thème : ")
choice = choice.lower()
        
        
def Tirage(Liste_Manga,Liste_SuperHero,Liste_Pays,Liste_de_trois,choice):                                            #  Création d'une fonction Tirage qui va tirée 3 mots au hasard dans la liste de départ.                                                          #  Les 3 mots se trouvent dans la liste "Liste_de_trois"
    if choice == "manga":
        i = 0
        while i < 3:
            Un_mot_au_hasard = Liste_Manga[random.randint(0, len(Liste_Manga)) - 1]
            Liste_de_trois.append(Un_mot_au_hasard)
            Liste_Manga.remove(Un_mot_au_hasard)
            i = i + 1
        return Liste_de_trois
    elif choice == "superhero":
        i = 0
        while i < 3:
            Un_mot_au_hasard = Liste_SuperHero[random.randint(0, len(Liste_SuperHero)) - 1]
            Liste_de_trois.append(Un_mot_au_hasard)
            Liste_SuperHero.remove(Un_mot_au_hasard)
            i = i + 1
        return Liste_de_trois
    elif choice == "pays":
        i = 0
        while i < 3:
            Un_mot_au_hasard = Liste_Pays[random.randint(0, len(Liste_Pays)) - 1]
            Liste_de_trois.append(Un_mot_au_hasard)
            Liste_Pays.remove(Un_mot_au_hasard)
            i = i + 1
        return Liste_de_trois
   

def liste_temoin(Liste_de_trois):
    Liste_melange = Liste_de_trois[0]+Liste_de_trois[1]+Liste_de_trois[2]
    Liste_melange = list(set(Liste_melange))
    random.shuffle(Liste_melange)
    return Liste_melange

# La fonction melange ne sert à rien, du coup je l'ai mis en commentaire. Ri
#def melange(Liste_de_trois):
#    Liste_melange = Liste_de_trois[0]+Liste_de_trois[1]+Liste_de_trois[2]
#    Liste_melange = list(set(Liste_melange))
#    random.shuffle(Liste_melange)
#    print("-".join(Liste_melange))



def chaine_liste(maChaine):                                      #Cette fonction sert à séparer les caractères d'un mot entrée par l'utilisateur.
    maListe = []
    for i in maChaine:
        maListe.append(i)
    return maListe

def test_lettre(mot_liste, list_test):
    longueur_mot = 0 
    while longueur_mot < len(mot_liste):
        for i in range(0, len(mot_liste)):
            if mot_liste[i] in list_test :
                longueur_mot = longueur_mot + 1 
            else:
                return 1
        return 0
    
def Scrabble(Liste_de_trois, Score, a):
    while a < 4:
        Tirage(Liste_Manga,Liste_SuperHero,Liste_Pays,Liste_de_trois,choice)
        liste_test = liste_temoin(Liste_de_trois)
        essai = 3
        print("Votre liste de lettre est :", "-".join(liste_test))
        print("Vous êtes à la manche : ",a, ".", "Vous avez 3 tentatives au total")   
        for i in range(3):
            proposition = input("Rentrer une proposition d'un mot / Quit : ")
            proposition = proposition.lower()
            mot_liste = chaine_liste(proposition) 
            mot = True
            test_mot = test_lettre(mot_liste, liste_test)
            if proposition == "quit":
                break
            if test_mot == 1:
                essai = essai - 1 
                print("Erreur, votre proposition contient une lettre qui n'est pas dans la liste !", "Il vous reste", essai, "tentative(s)", "Merci de ressaisir une proposition")
            else:
                for i in range(3):
                    if proposition == Liste_de_trois[i]:
                        Liste_de_trois[i] = ""
                        print("Bravo tu as trouvé un mot.")
                        Score = Score + 1
                        mot = False
                        print("Ton score est de", Score, "points !")
                        essai = essai - 1
                        print("Vous avez gagné ce tour !", "Il vous reste", essai, "tentative(s)")
                if mot == True:
                    print("Mauvais mot ou vous avez deja rentré ce mot")
                    essai = essai - 1
                    print("Vous avez perdu ce tour !", "Il vous reste", essai, "tentative(s)")
        a = a + 1
        Liste_de_trois = []
        return Scrabble(Liste_de_trois, Score, a)
    if a == 4:
        print("Vous avez finis le jeu du mini Scrabble avec", Score, "points !")

# Ceci permet de redemander un thème si le thème entrée par l'utilisateur n'est pas un thème disponible.

while choice not in Liste_theme :
    print("Erreur ! Le thème selectionné n'est pas disponible.")
    print("Les thèmes sont  : Manga , SuperHero , Pays")
    choice = input("Choisissez votre thème : ")
    choice = choice.lower() 
else : 
    Scrabble(Liste_de_trois, Score, 1)