# Fichier de sauvegarde
from Player import *

# sauvegarde = 
#["nom_du_joueur", classe_du_joueur, map_actuel_du_joueur, Position_du_joueur, hp_joueur, level_du_joueur, gold, arme, armure, potion, experience]

def sauvegarde(nom, classe, m, currentIndex, HP, lvl, gold, arme, armure, potion, EXP):
    sauvegarde = []
    sauvegarde.append(nom)
    sauvegarde.append(classe)
    sauvegarde.append(m)
    sauvegarde.append(currentIndex)
    sauvegarde.append(HP)
    sauvegarde.append(lvl)
    sauvegarde.append(gold)
    sauvegarde.append(arme)
    sauvegarde.append(armure)
    sauvegarde.append(potion)
    sauvegarde.append(EXP)
    return sauvegarde

