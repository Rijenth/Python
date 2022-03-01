import copy
from time import sleep
from ecran_aventure import*

def print_map(m, currentIndex):
    # permet de generer une nouvelle carte pour modifier les actions du joueur
    for i, row in enumerate(m):

        row_copy = copy.deepcopy(row)

        if i != currentIndex[0]:
            # suppression des "" et des crochets dans la nouvelle carte qu'on a généré en axe X
            print(" ".join(str(r) for r in row_copy))
        else:
            row_copy[currentIndex[1]] = "◊"
# suppression des "" et des crochets dans la nouvelle carte qu'on a généré en axe Y

            print(" ".join(str(r) for r in row_copy))


# Renvoie currentIndex dans tout les cas de figure
def carte(m, currentIndex, action):
 

# UsedObstacle : ╔ ║ ═ ╚ ╣ ╠ ╝ ╗
    
    if action == "z" or action =="q" or action == "s" or action == "d":
        while True:
            if action == 'z':
                # permet au joueur de ne pas depasser les limites de la carte
                if 0 <= currentIndex[0] - 1 < len(m[0]):
                    # mis a jour de la position du joueur
                    newIndex = [currentIndex[0] - 1, currentIndex[1]]
                    # X devient un obstacle pour le joueur et il ne peut y acceder
                    if m[newIndex[0]][newIndex[1]] != '╠' and m[newIndex[0]][newIndex[1]] != '╣' and m[newIndex[0]][newIndex[1]] != '╔' and m[newIndex[0]][newIndex[1]] != '═' and m[newIndex[0]][newIndex[1]] != "║" and m[newIndex[0]][newIndex[1]] != "╝" and m[newIndex[0]][newIndex[1]] != "╚" and m[newIndex[0]][newIndex[1]] != '╗':

                        currentIndex = newIndex

            elif action == 's':

                if 0 <= currentIndex[0] + 1 < len(m[0]):

                    newIndex = [currentIndex[0] + 1, currentIndex[1]]

                    if m[newIndex[0]][newIndex[1]] != '╠' and m[newIndex[0]][newIndex[1]] != '╣' and m[newIndex[0]][newIndex[1]] != '╔' and m[newIndex[0]][newIndex[1]] != '═' and m[newIndex[0]][newIndex[1]] != "║" and m[newIndex[0]][newIndex[1]] != "╝" and m[newIndex[0]][newIndex[1]] != "╚" and m[newIndex[0]][newIndex[1]] != '╗':

                        currentIndex = newIndex
                        
            elif action == 'q':

                if 0 <= currentIndex[1] - 1 < len(m[0]):

                    newIndex = [currentIndex[0], currentIndex[1] - 1]

                    if m[newIndex[0]][newIndex[1]] != '╠' and m[newIndex[0]][newIndex[1]] != '╣' and m[newIndex[0]][newIndex[1]] != '╔' and m[newIndex[0]][newIndex[1]] != '═' and m[newIndex[0]][newIndex[1]] != "║" and m[newIndex[0]][newIndex[1]] != "╝" and m[newIndex[0]][newIndex[1]] != "╚" and m[newIndex[0]][newIndex[1]] != '╗':

                        currentIndex = newIndex

            elif action == 'd':

                if 0 <= currentIndex[1] + 1 < len(m[0]):

                    newIndex = [currentIndex[0], currentIndex[1] + 1]

                    if m[newIndex[0]][newIndex[1]] != '╠' and m[newIndex[0]][newIndex[1]] != '╣' and m[newIndex[0]][newIndex[1]] != '╔' and m[newIndex[0]][newIndex[1]] != '═' and m[newIndex[0]][newIndex[1]] != "║" and m[newIndex[0]][newIndex[1]] != "╝" and m[newIndex[0]][newIndex[1]] != "╚" and m[newIndex[0]][newIndex[1]] != '╗':

                        currentIndex = newIndex
            return currentIndex
        
    else:
        print_map(m, currentIndex) 
        return currentIndex

# Cette fonction nous permet d'empecher le lancement d'event si la case 
# de destination du joueur est un obstacle. Paramètre : position actuel, 
# la carte et le choix déplacement du joueur.
def attention_obstacle(m, currentIndex, action):
    carte_test = m

    if action == "z":
        if 0 <= currentIndex[0] - 1 < len(carte_test[0]):
            test_obstacle = [currentIndex[0] - 1, currentIndex[1]]
            if carte_test[test_obstacle[0]][test_obstacle[1]] == '╠' or carte_test[test_obstacle[0]][test_obstacle[1]] == '╣' or carte_test[test_obstacle[0]][test_obstacle[1]] == '╔' or carte_test[test_obstacle[0]][test_obstacle[1]] == '═' or carte_test[test_obstacle[0]][test_obstacle[1]] == "║" or carte_test[test_obstacle[0]][test_obstacle[1]] == "╝" or carte_test[test_obstacle[0]][test_obstacle[1]] == "╚" or carte_test[test_obstacle[0]][test_obstacle[1]] == '╗':
                print("")
                print('\x1b[0;33;40m',"Vous ne pouvez pas aller par là !",'\x1b[0m')
                sleep(1)
                return "oui"
            return "non"
    elif action == "s":
        if 0 <= currentIndex[0] + 1 < len(carte_test[0]):    
            test_obstacle = [currentIndex[0] + 1, currentIndex[1]]
            if carte_test[test_obstacle[0]][test_obstacle[1]] == '╠' or carte_test[test_obstacle[0]][test_obstacle[1]] == '╣' or carte_test[test_obstacle[0]][test_obstacle[1]] == '╔' or carte_test[test_obstacle[0]][test_obstacle[1]] == '═' or carte_test[test_obstacle[0]][test_obstacle[1]] == "║" or carte_test[test_obstacle[0]][test_obstacle[1]] == "╝" or carte_test[test_obstacle[0]][test_obstacle[1]] == "╚" or carte_test[test_obstacle[0]][test_obstacle[1]] == '╗':
                print("")
                print('\x1b[0;33;40m',"Vous ne pouvez pas aller par là !",'\x1b[0m')
                sleep(1)
                return "oui"
            return "non"
    elif action == "q":
        if 0 <= currentIndex[0] - 1 < len(carte_test[0]):
            test_obstacle = [currentIndex[0], currentIndex[1] - 1]
            if carte_test[test_obstacle[0]][test_obstacle[1]] == '╠' or carte_test[test_obstacle[0]][test_obstacle[1]] == '╣' or carte_test[test_obstacle[0]][test_obstacle[1]] == '╔' or carte_test[test_obstacle[0]][test_obstacle[1]] == '═' or carte_test[test_obstacle[0]][test_obstacle[1]] == "║" or carte_test[test_obstacle[0]][test_obstacle[1]] == "╝" or carte_test[test_obstacle[0]][test_obstacle[1]] == "╚" or carte_test[test_obstacle[0]][test_obstacle[1]] == '╗':
                print("")
                print('\x1b[0;33;40m',"Vous ne pouvez pas aller par là !",'\x1b[0m')
                sleep(1)
                return "oui"
            return "non"
    elif action == "d":
        if 0 <= currentIndex[0] + 1 < len(carte_test[0]):
            test_obstacle = [currentIndex[0], currentIndex[1] + 1]
            if carte_test[test_obstacle[0]][test_obstacle[1]] == '╠' or carte_test[test_obstacle[0]][test_obstacle[1]] == '╣' or carte_test[test_obstacle[0]][test_obstacle[1]] == '╔' or carte_test[test_obstacle[0]][test_obstacle[1]] == '═' or carte_test[test_obstacle[0]][test_obstacle[1]] == "║" or carte_test[test_obstacle[0]][test_obstacle[1]] == "╝" or carte_test[test_obstacle[0]][test_obstacle[1]] == "╚" or carte_test[test_obstacle[0]][test_obstacle[1]] == '╗':
                print("")
                print('\x1b[0;33;40m',"Vous ne pouvez pas aller par là !",'\x1b[0m')
                sleep(1)
                return "oui"
            return "non"
    
    
        
    