from time import sleep # Cette fonction permet de mettre en pause le code.
from random import randint
# Nous allons préparer les boss et les combats ainsi que les quêtes liés au boss.
# Cette page contient aussi les dialogues des PNJs.

def quest_fabrice(m, Player):
    if "LBFDP" not in Player.arme:
        print('\x1b[0;33;40m', "[Fabrice]:", '\x1b[0m')
        print("Salut.. ")
        sleep(1)
        print("..euuhh")
        sleep(2)
        print(Player.nom)
        sleep(2)
        print("Je suis dans une situation compliquée, dans 2 jours j'ai un examen ultra complexe à Path'Hétic..'")
        sleep(2.5)
        print("..j'ai besoin d'un livre très rare afin de reussir mon examen..")
        sleep(2.5)
        print('\x1b[0;33;40m', "...Les bas fonds de Python...", '\x1b[0m')
        sleep(2.5)
        print("Il n'existe que quatres exemplaire dans le monde dont l'un se trouve dans une mysterieuse bibliothèque au sud de la carte.. ")
        sleep(2.5)
        print("..la legende raconte que personne n'a reussi jusqu'à ce jour à accéder à l'interieur de ce lieu")
        sleep(2)
        print(
            "Souhaites-tu m'aider à m'armer de savoir au péril de ta vie? [oui/non]")
        reponse = input()
        while reponse not in ["oui", "non"]:
            print("Plus sérieusement !")
            reponse = input()
        if reponse == "oui":
            print("Parfait, je savais que je pouvais compter sur toi mon pote!")
            sleep(2)
            print(
                "Maintenant rend toi à la", '\x1b[0;33;40m', "BIBLI", '\x1b[0m', "au sud-est de ta carte et tente de récupérer le précieux livre")

            m[11][9] = "B"
            m[11][10] = "I"
            m[11][11] = "B"
            m[11][12] = "L"
            m[11][13] = "I"

            sleep(2)
            print("Cependant....")
            sleep(3)
            print(
                "FAIT ATTENTION... il y a un terrible", '\x1b[0;33;40m', "gardien", '\x1b[0m', "qui veille sur ces lieux..")
            sleep(4)
            m[9][4] = "-"
            return m
        if reponse == "non":
            print("Tant pis alors, je vais rater mon exam à cause de toi :(")
            sleep(2)
            return m
    if "LBFDP" in Player.arme:
        print('\x1b[0;33;40m', "[Fabrice]:", '\x1b[0m')
        print("Waouw tu as reussi l'imposssible")
        sleep(2)
        print("Je ne sais pas si tu te rends compte mais personne n'avait reussi à accéder à la",
              '\x1b[0;33;40m', "bibliothèque secrète", '\x1b[0m', "auparavant.")
        sleep(2)
        print("Je vais maintenant te débloquer l'accès à la suite de la carte")
        sleep(2)
        print("...")
        sleep(2)
        print("Voilà ! Dirige toi vers l'est afin de continuer ton aventure.")
        sleep(2)
        print("D'ailleurs... vu que tu m'as l'air sympathique...")
        sleep(3)
        print("Je vais te réveler un petit",
              '\x1b[0;33;40m', "secret.", '\x1b[0m')
        sleep(4)
        print("Si jamais le", '\x1b[0;33;40m', "BOSS FINAL.",
              '\x1b[0m', "te demande si tu as quelque chose à lui dire.")
        sleep(4)
        print("Répond lui", '\x1b[0;33;40m', "ctrlc_ctrlv", '\x1b[0m')
        sleep(4)
        m[2][9] = "-"
        print("Salut, et bonne continuation mon pote !")
        m[2][3] = "-"
        Player.arme.remove("LBFDP")
        m[5][7] = "═"
        m[1][4] = "⥤"
        m[3][9] = "⥣"
        return m


def Hugo_A():
    print('\x1b[0;33;40m', "[Hugo]:", '\x1b[0m')
    print("Halte là !")
    sleep(2)
    print("Que fais-tu sur mon territoire ?")
    sleep(2)
    print("Je suis le maitre des lieux !!")
    sleep(2)
    print("je suis certain que c'est,"'\x1b[0;33;40m', "Fabrice",
          '\x1b[0m', " qui t'envoie car il a peur de m'affronter..")
    sleep(2)
    print("HA HA HA HA HA")
    sleep(2)
    print("TU CROYAIS POUVOIR PASSER SANS PROBLEME ?")
    sleep(2)
    print("Si tu me bats, tu auras accès à la",
          '\x1b[0;33;40m', "MATRICE DU SAVOIR", '\x1b[0m')
    sleep(2)
    print("")
    print("")
    return


def quest_rijenth(m, Player):
    print('\x1b[0;33;40m', "[Rijenth]:", '\x1b[0m')
    print("... !!")
    sleep(2)
    print("Oui ? Enfaite, j'aimerais beaucoup discuter avec toi mais... je suis actuellement en difficulté...")
    sleep(3)
    print('\x1b[0;30;47m', "(Lui demander pourquoi ?)[oui][non]", '\x1b[0m')
    choice = input()
    choice = choice.lower()
    while choice not in ["oui", "non"]:
        print("Votre choix est incorrect !")
        print('\x1b[0;30;47m',
              "(Lui demander ce qui lui arrive ?)[oui][non]", '\x1b[0m')
        choice = input()
    if choice == "non":
        print('\x1b[0;33;40m', "[Rijenth]:", '\x1b[0m')
        print("...")
        sleep(2)
        return m
    if choice == "oui":
        print('\x1b[0;33;40m', "[Rijenth]:", '\x1b[0m')
        print("Enfaite... Je jouais avec le",
              '\x1b[0;33;40m', "ballon de basket", '\x1b[0m', "d'un ami...")
        sleep(2)
        print("Et j'ai perdu son ballon !")
        print(
            '\x1b[0;30;47m', "(Lui dire que vous avez retrouvé le ballon de Kader)[oui][non]", '\x1b[0m')
        choice = input()
        choice = choice.lower()
        while choice not in ["oui", "non"]:
            print("Votre choix est incorrect !")
            print(
                '\x1b[0;30;47m', "(Lui dire que vous avez retrouvé le ballon de Kader)[oui][non]", '\x1b[0m')
            choice = input()
        if choice == "oui":
            print('\x1b[0;33;40m', "[Rijenth]:", '\x1b[0m')
            print("Super ! Un problème de moins... Maintenant, le second problème.")
            sleep(3)
            print(
                "J'ai en face de moi une personne, qui semble vouloir passer à la suite du jeu.")
            sleep(3)
            print("Et moi, je ne suis qu'un pauvre PNJ, auquel mon créateur n'a pas jugé utile de lui confier une quête amusante.")
            sleep(3)
            print("De peur de rendre le jeu trop long sûrement.")
            sleep(3)
            print("Du coup, on vas jouer à un",
                  '\x1b[0;33;40m', "jeu tout bête.", '\x1b[0m')
            print('\x1b[0;30;47m'+'Appuyez sur [A] pour continuer'+'\x1b[0m')
            choice = input()
            choice = choice.lower()
            while choice != "a":
                choice = input()
            result = jeu_tout_bête()
            if result == "reussite":
                m[5][34] = "-"
                m[6][41] = "╔"
                m[6][42] = "═"
                m[4][41] = "╚"
                m[4][42] = "╝"
                m[5][41] = "⥤"
                m[5][42] = "-"
                return m
            else:
                return m
        if choice == "non":
            print('\x1b[0;33;40m', "[Rijenth]:", '\x1b[0m')
            print("... Il faut que je le retrouve... Sinon il ne voudra plus signer pour moi au prochain cours de monsieur Loic...")
            sleep(3)
            print("Si seulement une", '\x1b[0;33;40m', "âme charitable",
                  '\x1b[0m', "pouvait s'en occuper à ma place...")
            print(
                '\x1b[0;30;47m'+'Appuyez sur [A] pour mettre fin à la discussion.'+'\x1b[0m')
            choice = input()
            choice = choice.lower()
            while choice != "a":
                choice = input()
            return m


def jeu_tout_bête():
    print('\x1b[0;33;40m', "[Rijenth]:", '\x1b[0m')
    print("Très bien cher ami, commençons !")
    sleep(2)
    list_chiffre = [99999, 9999, 999, 99, 1]
    i = 0
    result = ""
    while i < 5:
        liste_chiffre_jeu = list_chiffre[i]
        ri_choice = randint(0, liste_chiffre_jeu)
        if i >= 1 and i <= 4:
            print("Bon, je vois que c'est pas facile... Je vais faire plus simple")
            print("")
            sleep(2)
            print("J'ai choisi un nombre compris entre", '\x1b[0;32;40m', "0", '\x1b[0m',
                  "et", '\x1b[0;32;40m', liste_chiffre_jeu, '\x1b[0m', "à toi de le deviner.")
            print("")
        else:
            print("J'ai choisi un nombre compris entre", '\x1b[0;32;40m', "0", '\x1b[0m',
                  "et", '\x1b[0;32;40m', liste_chiffre_jeu, '\x1b[0m', "à toi de le deviner.")
            print("")
        result = joueur_reponse(ri_choice)
        if result == "reussite":
            return "reussite"
        if result == "echec":
            i = i + 1
    print("")
    print('\x1b[0;33;40m', "[Rijenth]:", '\x1b[0m')
    print("Tu as perdu... Reviens me voir quand tu seras un peu plus sûr de tes choix.")
    print("")
    sleep(3)
    return "echec"


def random_phrase_ri():
    random = randint(0, 3)
    print("")
    print('\x1b[0;33;40m', "[Rijenth]:", '\x1b[0m')
    if random == 1:
        print("Les chiens aboient, la caravane passe...")
        print("")
        sleep(2)
        return
    if random == 2:
        print("Je suis un PNJ dans un rpg fait par des développeurs débutant... Pas un commissariat !")
        print("")
        sleep(2)
        return
    if random == 3:
        print("C'est bien beau de se plaindre, mais en attendant il n'y a que 15 min de présentation...")
        print("")
        sleep(2)
        return
    if random == 0:
        print("Oui, cette option est réellement fonctionnel. Et oui, j'ai passé de très bonne vacance /s")
        print("")
        sleep(2)
        return


# Cette fonction permet de récuperer le choix du PNJ en fonction de ce que le joueur a choisi de faire. (reussite, echec, plainte)
def joueur_reponse(ri_choice):
    print('\x1b[0;30;47m'+'Choisissez votre option:'+'\x1b[0m')
    print("[1]: Proposer une réponse")
    print("[2]: Se plaindre")
    choice = input()
    while choice not in ["1", "2"]:
        print('\x1b[0;30;47m'+'Choisissez votre option:'+'\x1b[0m')
        print("[1]: Proposer une réponse")
        print("[2]: Se plaindre")
        choice = input()
    if choice == "1":
        print('\x1b[0;30;47m'+'Entrez votre réponse:'+'\x1b[0m')
        choice = int(input())
        if choice == ri_choice:
            print('\x1b[0;33;40m', "[Rijenth]:", '\x1b[0m')
            print("Bravo ! Je pensais bien à", ri_choice)
            sleep(2)
            print("Je t'ai ouvert la voie, bonne chance pour la suite !")
            print("")
            sleep(3)
            return "reussite"
        else:
            print('\x1b[0;33;40m', "[Rijenth]:", '\x1b[0m')
            print("Et non !", "je pensais au nombre", ri_choice, "!")
            sleep(2)
            return "echec"
    if choice == "2":
        random_phrase_ri()
        return joueur_reponse(ri_choice)


def quest_kader(m, Player):
    print('\x1b[0;33;40m', "[Kader]:", '\x1b[0m')
    if "ballon_de_basket" in Player.arme:
        print("Super !! Tu as retrouvé mon",
              '\x1b[0;33;40m', "ballon de basket", '\x1b[0m', "!")
        sleep(2)
        m[9][23] = "⥤ "
        m[5][18] = "⥥"
        m[9][24] = "-"
        m[8][23] = "═"
        m[8][24] = "═"
        m[10][23] = "═"
        m[10][24] = "═"
        m[1][26] = "-"
        m[4][15] = "═"
        m[8][22] = "═"
        m[4][15] = "-"
        m[8][22] = "-"
        m[9][5] = "-"
        print("Tu peux maintenant continuer ton chemin, je t'ai ouvert un passage en bas de la carte.")
        print('\x1b[0;30;47m'+'Appuyez sur [A] pour continuer'+'\x1b[0m')
        choice = input()
        choice = choice.lower()
        while choice != "a":
            choice = input()
        print("Salut !")
        Player.arme.remove("ballon_de_basket")
        return m
    if "ballon_de_basket" not in Player.arme:
        print("Salut !", Player.nom)
        sleep(2)
        print("J'imagine que tu veux de l'aide pour passer à droite de la carte ?")
        sleep(2)
        print("Je voudrais bien t'aider mais j'ai perdu mon",
              '\x1b[0;33;40m', "ballon de basket", '\x1b[0m', "!!")
        sleep(2)
        print("Oui... il y a des urgences plus importantes que d'autres...")
        sleep(3)
        print("Si tu le retrouves, alors je t'ouvrirai la voie.")
        sleep(3)
        print("Celon", '\x1b[0;33;40m', "l'un de mes collègues", '\x1b[0m',
              "le ballon est dans l'un des deux terrains de basket. (Les zones remplies de 'x')")
        sleep(3)
        print("Mais comme tu peux le voir, ces zones sont actuellement inaccessibles.")
        sleep(4)
        print("Deux", '\x1b[0;33;40m', "leviers",
              '\x1b[0m', "sont cachés sur cette carte.")
        sleep(3)
        print("Cherche et active les deux",
              '\x1b[0;33;40m', "leviers", '\x1b[0m', "pour accéder aux deux terrains.")
        m[1][19] = "?"
        m[7][12] = "?"
        m[1][4] = "-"
        m[3][9] = "-"
        print('\x1b[0;30;47m'+'Appuyez sur [A] pour continuer'+'\x1b[0m')
        choice = input()
        choice = choice.lower()
        while choice != "a":
            choice = input()
        return m


def debut_quiz(Player):
    titre = "** BOSS FINAL **"
    print('\x1b[0;33;40m', "*" * len(titre), '\x1b[0m')
    print('\x1b[0;33;40m', titre, '\x1b[0m')
    print('\x1b[0;33;40m', "*" * len(titre), '\x1b[0m')
    sleep(2)
    print("")
    print('\x1b[0;33;40m', "[Loïc, le professeur]:", '\x1b[0m')
    print("...")
    sleep(1)
    print("Vous voilà enfin j'ai failli m'impatienter...")
    sleep(2)
    print("Vous vous demandez sûrement ce que je fais ici.")
    sleep(1)
    print("...")
    sleep(2)
    print("Et bien moi aussi !")
    sleep(1)
    print("Mais bon, passons. J'espère que les vacances ont été bonnes.")
    sleep(3)
    print("Pour conclure ce 'jeu' je vais vérifier que vous avez bien retenu mes leçons.")
    sleep(2)
    print("J'espère que vous êtes prêt...")
    print('\x1b[0;30;47m'+'Appuyez sur [A] pour continuer'+'\x1b[0m')
    choice = input()
    choice = choice.lower()
    while choice != "a":
        choice = input()
    return

# Quiz + Ligne de dialogue du boss Loic.
def entree_utilisateur(Player):
    # Quiz lié au boss Loic on trouvera des question sur le Python
    # si vous pas plus de 4 bonne reponse vous affrontez Loic.
    score = 0
    # Question 1
    print('\x1b[0;33;40m', "[Loïc, le professeur]:", '\x1b[0m')
    print("")
    print("Q1 - Quelle est la syntaxe correcte pour afficher 'Hello World' dans une console Python ?")
    sleep(2)
    print("")
    liste_q0 = ["1 - echo 'Hello World'",
                "2 - print('Hello World')  ", "3 - p('Hello World')", "4 - echo('Hello World');"]
    print(liste_q0[0])
    print(liste_q0[1])
    print(liste_q0[2])
    print(liste_q0[3])
    entree_utilisateur = int(input("Entrer votre choix: "))
    while entree_utilisateur != 1 and entree_utilisateur != 2 and entree_utilisateur != 3 and entree_utilisateur != 4:
        print("Option de menu invalide.")
        entree_utilisateur = int(input("Entrer votre choix: "))
    if entree_utilisateur == 2:
        print('\x1b[0;33;40m', "[Loïc, le professeur]:", '\x1b[0m')
        print("Très bien", Player.nom, "je vois que tu te souviens de la base.")
        sleep(1)
        score += 1
    else:
        print('\x1b[0;33;40m', "[Loïc, le professeur]:", '\x1b[0m')
        print("Je ne suis pas confiant pour la suite...")
        sleep(2)
    # Question 2
    print("")
    print("Q2 - Comment insérer des commentaires dans un code Python ?")
    print("")
    liste_q1 = ["1 - /*This is a comment*/ ",
                "2 - //This is a comment ", "3 - #This is a comment", ]
    print(liste_q1[0])
    print(liste_q1[1])
    print(liste_q1[2])
    entree_utilisateur = int(input("Entrer votre choix: "))
    while entree_utilisateur != 1 and entree_utilisateur != 2 and entree_utilisateur != 3:
        print("Option de menu invalide.")
        entree_utilisateur = int(input("Entrer votre choix: "))
    if entree_utilisateur == 3:
        print('\x1b[0;33;40m', "[Loïc, le professeur]:", '\x1b[0m')
        print("Pas mal", Player.nom,
              "je vois que je n'ai pas parler à l'oreille d'un sourd.")
        sleep(1)
        score += 1
    else:
        print('\x1b[0;33;40m', "[Loïc, le professeur]:", '\x1b[0m')
        print("... c'était simple pourtant...")
        sleep(2)
    # Question 3
    print("Q3 - Laquelle de ces propositions n’est pas une variable valable ?")
    liste_q2 = ["1 - my-var  ", "2 - my_var ", "3 - Myvar", "4 - _myvar"]
    print(liste_q2[0])
    print(liste_q2[1])
    print(liste_q2[2])
    print(liste_q2[3])
    entree_utilisateur = int(input("Entrer votre choix: "))
    while entree_utilisateur != 1 and entree_utilisateur != 2 and entree_utilisateur != 3 and entree_utilisateur != 4:
        print("Option de menu invalide.")
        entree_utilisateur = int(input("Entrer votre choix: "))
    if entree_utilisateur == 1:
        print('\x1b[0;33;40m', "[Loïc, le professeur]:", '\x1b[0m')
        print("Oui, tout à fait", Player.nom, ".")
        sleep(1)
        score += 1
    else:
        print('\x1b[0;33;40m', "[Loïc, le professeur]:", '\x1b[0m')
        print("Mais comment avez-vous pu faire tout un RPG sans savoir celà...")
        sleep(2)
    # Question 4
    print("Q4 - Quel opérateur peut être utilisé pour comparer deux valeurs ?")
    liste_q3 = ["1 - =  ", "2 - >< ", "3 - <>", "4 - ==  "]
    print(liste_q3[0])
    print(liste_q3[1])
    print(liste_q3[2])
    print(liste_q3[3])
    entree_utilisateur = int(input("Entrer votre choix: "))
    while entree_utilisateur != 1 and entree_utilisateur != 2 and entree_utilisateur != 3 and entree_utilisateur != 4:
        print("Option de menu invalide.")
        entree_utilisateur = int(input("Entrer votre choix: "))
    if entree_utilisateur == 4:
        print('\x1b[0;33;40m', "[Loïc, le professeur]:", '\x1b[0m')
        print("Oui c'est bien ça", Player.nom, "!")
        sleep(1)
        score += 1
    else:
        print('\x1b[0;33;40m', "[Loïc, le professeur]:", '\x1b[0m')
        print("Non...")
        sleep(2)
    # Question 5
    print("Q5 -Comment commencer à écrire une boucle en Python ?")
    liste_q4 = ["1 - while (x > y) ", "2 - while x > y:   ",
                "3 - x > y while {", "4 - while x > y { "]
    print(liste_q4[0])
    print(liste_q4[1])
    print(liste_q4[2])
    print(liste_q4[3])
    entree_utilisateur = int(input("Entrer votre choix: "))
    while entree_utilisateur != 1 and entree_utilisateur != 2 and entree_utilisateur != 3 and entree_utilisateur != 4:
        print("Option de menu invalide.")
        entree_utilisateur = int(input("Entrer votre choix: "))
    if entree_utilisateur == 2:
        print('\x1b[0;33;40m', "[Loïc, le professeur]:", '\x1b[0m')
        print("Parfait", Player.nom,
              "Mais j'espère que vous n'êtes pas aller chercher la réponse sur internet !")
        sleep(1)
        score += 1
    else:
        print('\x1b[0;33;40m', "[Loïc, le professeur]:", '\x1b[0m')
        print("Eeeeh...")
        sleep(1)
        print("Non.")
        sleep(2)
    # Question 6
    print("Q6 -Comment commencer à écrire une boucle 'for' en Python ?")
    liste_q5 = ["1 - for x > y: ",
                "2 - for each x in y:   ", "3 - for x in y:  ", ]
    print(liste_q5[0])
    print(liste_q5[1])
    print(liste_q5[2])
    entree_utilisateur = int(input("Entrer votre choix: "))
    while entree_utilisateur != 1 and entree_utilisateur != 2 and entree_utilisateur != 3:
        print("Option de menu invalide.")
        entree_utilisateur = int(input("Entrer votre choix: "))
    if entree_utilisateur == 3:
        print('\x1b[0;33;40m', "[Loïc, le professeur]:", '\x1b[0m')
        print("Bravo", Player.nom, "Celle çi était plus subtile.")
        sleep(1)
        score += 1
    else:
        print('\x1b[0;33;40m', "[Loïc, le professeur]:", '\x1b[0m')
        print("... non, il faut revoir ces notions au plus vite !")
        sleep(2)
    # Question 7
    print("Q7 -Quelle commande est utilisée pour arrêter une boucle ?")
    liste_q6 = ["1 - return  ", "2 - stop   ", "3 - exit  ", "4 - break "]
    print(liste_q6[0])
    print(liste_q6[1])
    print(liste_q6[2])
    print(liste_q6[3])
    entree_utilisateur = int(input("Entrer votre choix: "))
    while entree_utilisateur != 1 and entree_utilisateur != 2 and entree_utilisateur != 3 and entree_utilisateur != 4:
        print("Option de menu invalide.")
        entree_utilisateur = int(input("Entrer votre choix: "))
    if entree_utilisateur == 4:
        print('\x1b[0;33;40m', "[Loïc, le professeur]:", '\x1b[0m')
        print("Super,", Player.nom, "!")
        sleep(1)
        score += 1
    else:
        print('\x1b[0;33;40m', "[Loïc, le professeur]:", '\x1b[0m')
        print("Pas vraiment... la réponse était 'break'", Player.nom)
    return score


# Ligne de dialogue du PNJ Valentin
def random_phrase_valentin():
    random = randint(0, 3)
    if random == 0:
        print('\x1b[0;33;40m', "[Valentin, Le ninja ctrlc_ctrlv]:", '\x1b[0m')
        print("Le combat avait déjà commencer ?",
              "Je ne l’avais même pas remarquer...")
        sleep(2)
        return
    if random == 1:
        print('\x1b[0;33;40m', "[Valentin, Le ninja ctrlc_ctrlv]:", '\x1b[0m')
        print("Oops, je ne pensais pas que ça irai si vite...")
        sleep(2)
        return
    if random == 2:
        print('\x1b[0;33;40m', "[Valentin, Le ninja ctrlc_ctrlv]:", '\x1b[0m')
        print("Hors de ma vue ...")
        sleep(2)
        return
    if random == 3:
        print('\x1b[0;33;40m', "[Valentin, Le ninja ctrlc_ctrlv]:", '\x1b[0m')
        print("Je me suis donc tromper sur ton compte...")
        sleep(2)
        return

# Ligne de dialogue du BOSS Valentin
def boss_valentin(Player):
    print("*Bruit de chaine...*")
    print("...")
    sleep(2)
    print("")
    print('\x1b[0;33;40m', "[Valentin, Le ninja ctrlc_ctrlv]:", '\x1b[0m')
    print("AH AH AH AH AH, je t’attendais, élu.")
    print("")
    sleep(2)
    print("Je vois que tu as bien retenu le code secret que j’ai laissé à",
          '\x1b[0;33;40m', "Fabrice.", '\x1b[0m')
    sleep(2)
    print("Durant des années, on m’a enfermé ici, sous la menace de",
          '\x1b[0;33;40m', "l'EPEE LEGENDAIRE.", '\x1b[0m')
    sleep(2)
    print("")
    print("Je me suis beaucoup ennuyer durant ce séjour... Mais ta présence ici me fait plaisir.")
    sleep(2)
    print("J'ai volé des lignes de code de personnages aussi puissant que toi.")
    sleep(2)
    print("")
    print("Ils font désormais partie de moi ! Je suis le personnage le plus puissant de ce jeu.")
    sleep(2)
    print("Tu sais donc ce qu'il te reste à faire ?")
    sleep(2)
    print("")
    print("En garde", Player.nom, "!")
    print("")
    sleep(3)
    return



