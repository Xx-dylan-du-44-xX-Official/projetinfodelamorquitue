from math import *
from random import randint, random

##
'''
joueur 1 achète petites cases
joueur 2 achete grosses cases
joueur 3 aléatoire
joueur 4 achete rien
J1 = 0
J2 = 0
Cases(J1) = [[],[]]
Cases[J1]
'''
##
L = [2,-1,-2,0,-3,-4]
position_j1 = position_j2 = 0
argent_j1 = argent_j2 = 5
Cases_j1 = [2,1,0,0,3,0]
Cases_j2 = [2,0,-2,0,0,4]
Cases_j3 = [0 for k in range(len(L))]
Cases_j3[0] = 2
for k in range(1,len(L)):
    if random()<1/2:
        Cases_j3[k] = -L[k]
joueurs = [[argent_j1,argent_j2],[Cases_j1, Cases_j2],[position_j1,position_j2]]
nb_joueurs = len(joueurs[0])

def lancerdede():
    '''Stimule un lancer de dé'''
    return randint(1,6)
'''
def compteur(argent,nb_lancer):
    p = position
    while nb_lancer != 0 :
        p += lancerdede()
        nb_lancer -= 1
        if p > len(L) :
            p -= len(L)
            argent += 2
        print(argent,p)
        #if input("acheter la case"+ L[p-1] + "?") == "oui":
        argent += L[p-1]
    return (argent, p)
'''
def acheter(position, numero_joueur):
    '''
    entrée : position du joueur, numero du joueur
    sortie : informations des joueurs si le joueur avec lequel on travaille achète une propriété 
    '''
    if position != 0 and joueurs[1][numero_joueur][position] > 0 and joueurs[0][numero_joueur] > joueurs[1][numero_joueur][position]:    
        joueurs[0][numero_joueur] -= joueurs[1][numero_joueur][position]
        for i in range(nb_joueur):
            if i != numero_joueur:
                joueurs[1][i][position] = -joueurs[1][numero_joueur][position]
            joueurs[1][numero_joueur][position] = 0
    return joueurs

def payer(position, numero_joueur):
    '''
    entrée : position du joueur, numero du joueur
    sortie : informations des joueurs si le joueur avec lequel on travaille tombe sur une case achetée par un autre joueur
    '''
    argent_perdu = joueurs[1][numero_joueur][position]
    if argent_perdu < 0:
        joueurs[0][numero_joueur] += argent_perdu
    for i in range(nb_joueur):
        if i != numero_joueur:
            if joueurs[1][i][position] == 0:
                joueurs[0][i] -= argent_perdu
    return joueurs

def jeu(joueurs):
    '''
    entrée : informations sur les joueurs avant de commencer la partie
    Sortie : joueur gagnant, et informations sur les joueurs
    Comment ? Un joueur lance un dé, achète la propriété ou non, c'est au joueur suivant qui lance un dé, paye ou achète, etc
    '''
    position = 0
    numero_joueur = randint(0,nb_joueurs)
    for i in range(nb_joueurs):
        while joueurs[0][i] > 0 :
            r = lancerdede()
            joueurs[2][numero_joueur] += r
            if joueurs[2][numero_joueur] > len(L) : 
                joueurs[2][numero_joueur] -= len(L)
                joueurs[0][numero_joueur] += 2
            for k in range(nb_joueurs):
                joueurs = acheter(joueurs[2][numero_joueur], numero_joueur)
                joueurs = payer(joueurs[2][numero_joueur], numero_joueur)
    return joueurs
