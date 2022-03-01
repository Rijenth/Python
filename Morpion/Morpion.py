# Créer un programme permettant de jouer au morpion. Le principe du jeu est simple. C’est un jeu au tour par tour, 
# Où le but est d’aligner un trio de cercles ou de croix en diagonale, horizontalement ou verticalement sur une grille 
# de 3×3 carrés pour obtenir la victoire.
from time import sleep

morpion = [["_", "_", "_"],
           ["_", "_", "_"],
           ["_", "_", "_"]]
#Préparation de variable
signe_joueur_1 = ""
signe_joueur_2 = ""
A = ""
B = ""

# Nombre de tour de jeu et check de victoire
etat = False 
tour_j1 = 0
tour_j2 = 0 
somme_tour = 0

#Pour choisir le signe du joueur 1 et joueur 2
def choix_signe(signe_joueur_1): #Cette fonction permet de choisir de jouer soit le "X", soit le "O"
    print("Bienvenue dans le morpion !")
    print("Choisissez votre signe :", "(O) ou (X)")
    choice = input()
    choice.lower()
    while choice != "x" and choice != "o":
        print("Erreur, veuillez entrez un signe correct")
        choice = input()
    if choice == "x":
        print("Vous avez choisi : X")
        signe_joueur_1 = "X"
        return signe_joueur_1
    if choice == "o":
        print("Vous avez choisi : O")
        signe_joueur_1 = "O"
        return signe_joueur_1
    

def choix_signe_j2(signe_joueur_1):
    if signe_joueur_1 == "O":
        signe_joueur_2 = "X"
        return signe_joueur_2 
    if signe_joueur_1 == "X":
        signe_joueur_2 = "O"
        return signe_joueur_2
 
# Pour montrer la carte du morpion
def show_map(): # Affiche la map du morpion
    i = 0
    while i < len(morpion):
        print(morpion[i])
        i += 1
#Pour placer une lettre dans une des cases de la liste morpion
def placement (morpion, signe_joueur): #joueur est égale à "X" ou "O", j'utilise cette fonction pour placer un mot
    print("Entrez les coordonnées de la case :")
    print("X = ", "Y =")
    X = int(input())
    Y = int(input())
    while morpion[X-1][Y-1] != "_":
        print("Erreur ! La case est deja prise.")
        print("Entre les coordonnées de la case :")
        print("X = Ligne ", "Y = Case")
        X = int(input())
        Y = int(input())
    if morpion[X-1][Y-1] == "_":
        morpion[X-1][Y-1] = signe_joueur
    return show_map()

#Pour vérifier la victoire ou non des joueurs dans le morpion
def check_victory(morpion, A, etat):#A est le signe "O" ou "X"
    if morpion[0][0] == A and morpion [0][1] == A and morpion [0][2] == A:
        etat = True
        return etat
    if morpion[1][0] == A and morpion [1][1] == A and morpion [1][2] == A:
        etat = True
        return etat
    if morpion[2][0] == A and morpion [2][1] == A and morpion [2][2] == A:
        etat = True
        return etat
    if morpion[0][0] == A and morpion [1][0] == A and morpion [2][0] == A:
        etat = True
        return etat
    if morpion[0][1] == A and morpion [1][1] == A and morpion [2][1] == A:
        etat = True
        return etat
    if morpion[0][2] == A and morpion [1][2] == A and morpion [2][2] == A:
        etat = True
        return etat
    if morpion[0][0] == A and morpion [1][1] == A and morpion [2][2] == A:
        etat = True
        return etat
    if morpion[0][2] == A and morpion [1][1] == A and morpion [2][0] == A:
        etat = True
        return etat
    return etat
    
                
# Le script final du jeu
def jeu(tour_j1, tour_j2, A, B, etat, somme_tour):# A et B sont les joueurs "O" et "X"
    A = choix_signe(signe_joueur_1) # Joueur 1, signe
    B = choix_signe_j2(A) # Joueur 2, signe
    print(A, B)
    print("Joueur1 =", A, "Joueur2 =", B)
    show_map()
    while etat == False:
        if tour_j1 == tour_j2 :
            print("Tour du joueur 1")
            placement(morpion, A)
            tour_j1 += 1
            somme_tour = somme_tour + 1
            check_victory(morpion, A, etat)
            if check_victory(morpion, A, etat) == True and tour_j1 > tour_j2:
                print("Joueur 1 a gagné !")
                print("Fin du jeu !")
                return
            if somme_tour == 9:
                print("Fin de partie ! Match nul")
                return
        if tour_j1 > tour_j2:
            print("Tour du joueur 2")
            placement(morpion, B)
            tour_j2 += 1
            somme_tour = somme_tour + 1 
            check_victory(morpion, B, etat)
            if check_victory(morpion, B, etat) == True and tour_j2 > tour_j1:
                print("Joueur 2 a gagné !")
                print("Fin du jeu !")
                sleep(10)
                return
            if somme_tour == 9:
                print("Fin de partie ! Match nul")
                sleep(10)
                return
                
# Lancement du jeu, avec toutes les variables nécessaire
jeu(tour_j1, tour_j2, A, B, etat, somme_tour)





