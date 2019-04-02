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

############################## xd
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

Cases_j1 = [2,1,2,0,3,0]
Cases_j2 = [2,0,0,0,0,4]
Cases_j3 = [2]
for k in range(1,len(L)-1):
    if random() <= 1/2 :
        Cases_j3.append(L[k])
    else : Cases_j3.append(0)

joueurs = [[argent_j1,argent_j2],[Cases_j1, Cases_j2],[position_j1,position_j2]]
nb_joueurs = len(joueurs[0])

def lancerdede():
    return randint(1,6)

def acheter(position, numero_joueur):
    '''
    entrée : position du joueur, numero du joueur
    sortie : informations des joueurs si le joueur avec lequel on travaille achète une propriété 
    '''
    if joueurs[0][numero_joueur] > joueurs[1][numero_joueur][position] and position != 0 and joueurs[1][numero_joueur][position] != 0:
        joueurs[0][numero_joueur] -= joueurs[1][numero_joueur][position]
        for i in range(nb_joueurs) :
            if i != numero_joueur :
                joueurs[1][i][position] -= joueurs[1][numero_joueur][position]
        joueurs[1][numero_joueur][position] = 0
    return joueurs

def payer(position, numero_joueur):
    '''
    entrée : position du joueur, numero du joueur
    sortie : informations des joueurs si le joueur avec lequel on travaille tombe sur une case achetée par un autre joueur
    '''
    if joueurs[1][numero_joueur][position] < 0:
        joueurs[0][numero_joueur] += joueurs[1][numero_joueur][position]
    for k in range(nb_joueurs):
        if k != numero_joueur:
            if joueurs[1][k][position] == 0 :
                joueurs[0][k] -= joueurs[1][numero_joueur][position]
    return joueurs

def jeu(joueurs):
    position = 0
    numero_joueur = 0
    #numero_joueur = randint(0,nb_joueurs)
    for k in range(nb_joueurs):
        while joueurs[0][k] > 0:
            r = lancerdede()
            joueurs[2][numero_joueur] += r
            if joueurs[2][numero_joueur] > len(L) : 
                joueurs[2][numero_joueur] -= len(L)
                joueurs[0][numero_joueur] += 2
            joueurs = acheter(joueurs[2][numero_joueur], numero_joueur)
            joueurs = payer(joueurs[2][numero_joueur], numero_joueur)
            numero_joueur += 1
            if numero_joueur >= nb_joueurs : 
                numero_joueur -= nb_joueurs
    return joueurs

##
L = [2,-1,-2,0,-3,-4]
position_j1 = position_j2 = 0
argent_j1 = argent_j2 = 5
Cases_j1 = [2,1,2,0,3,0]
Cases_j2 = [2,0,0,0,0,4]
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
    if joueurs[0][numero_joueur] > abs(joueurs[1][numero_joueur][position-1]) and position != 0 and joueurs[1][numero_joueur][position-1] != 0:
        joueurs[0][numero_joueur] -= joueurs[1][numero_joueur][position-1]
        for i in range(nb_joueurs) :
            if i != numero_joueur :
                joueurs[1][i][position-1] = -joueurs[1][numero_joueur][position-1]
        joueurs[1][numero_joueur][position-1] = 0
    return joueurs

def payer(position, numero_joueur):
    '''
    entrée : position du joueur, numero du joueur
    sortie : informations des joueurs si le joueur avec lequel on travaille tombe sur une case achetée par un autre joueur
    '''
    if joueurs[1][numero_joueur][position-1] < 0:
        joueurs[0][numero_joueur] += joueurs[1][numero_joueur][position-1]
    for k in range(nb_joueurs):
        if k != numero_joueur:
            if joueurs[1][k][position-1] == 0 :
                joueurs[0][k] -= joueurs[1][numero_joueur][position-1]
    return joueurs

def elimination():
    k <= 0
    return k in joueurs[0] 

def jeu(joueurs):
    '''
    entrée : informations sur les joueurs avant de commencer la partie
    Sortie : joueur gagnant, et informations sur les joueurs
    Comment ? Un joueur lance un dé, achète la propriété ou non, c'est au joueur suivant qui lance un dé, paye ou achète, etc
    '''
    position = 0
    numero_joueur = randint(0,nb_joueurs)
    #for i in range(nb_joueurs): #pour chaque joueur
    while not elimination() : #tant qu'aucun joueur n'est éliminé
        r = lancerdede() #on lance le dé
        joueurs[2][numero_joueur] += r #le joueur se trouve sur la nouvelle case
        if joueurs[2][numero_joueur] > len(L) : #si il est au bout
            joueurs[2][numero_joueur] -= len(L) #il recommence un tour
        joueurs = acheter(joueurs[2][numero_joueur], numero_joueur) #soit il achete 
        joueurs = payer(joueurs[2][numero_joueur], numero_joueur) #soit il paye
        numero_joueur += 1 #on passe au joueur suivant
        if numero_joueur >= nb_joueurs: #si on est au dernier joueur,
            numero_joueur -= nb_joueurs #on retourne au premier joueur
    return joueurs













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
from random import random, randint
import matplotlib.pyplot as plt
import numpy as np

Liste = [2,-1,-2,0,-3,-4]
argent_j1 = argent_j2 = argent_j3 = 5
Cases_j1 = [2,1,2,0,3,0]
Cases_j2 = [2,0,0,0,0,4]
Cases_j3 = [0 for k in range(len(Liste))]
Cases_j3[0] = 2
for k in range(1,len(Liste)):
    if random()<1/2:
        Cases_j3[k] = -Liste[k]
argent = [argent_j1, argent_j2, argent_j3]
case = [Cases_j1, Cases_j2, Cases_j3]

nb_joueurs = 3

def lancerdede():
    '''Stimule un lancer de dé'''
    return randint(1,6)
    
def acheter(place, numero_joueur):
    """ entrée : case où se trouve le joueur
                 le joueur qui joue
        sortie : la liste joueurs modifiée avec les nouvelles valeurs d'argent et des cases
        fonction permettant au joueur de pouvoir acheter une case 
    """
    print("numero_joueur", numero_joueur)
    print("place",place)
    # position[numero_joueur] = place
    if place != 0 and argent[numero_joueur] > case[numero_joueur][place] > 0:
        argent[numero_joueur] -= case[numero_joueur][place]
        case[numero_joueur][place] = 0
        for i in range(3):
            if i != numero_joueur:
                case[i][place] = Liste[place]
    print("case",case)
    print("argent", argent)
    print(" ")
    return argent,case 
    
def payer (place, numero_joueur):
    """ entrée : case où se trouve le joueur
                 le joueur qui joue
        sortie : la liste joueurs modifiée avec les nouvelles valeurs d'argent et des cases
        fonction permettant au joueur de payer au joueur possédant la case où il se trouve
    """ 
    # position[numero_joueur] = place
    argent_perdu = case[numero_joueur][place]
    if argent_perdu < 0:
        argent[numero_joueur] += argent_perdu
    for i in range(3):
        if i != numero_joueur:
            if case[i][place] == 0:
                argent[i] -= argent_perdu
    return argent,case
        
    
        
# ----------------------------------------------------------PROGRAMME----------------------------------------------------------------------
  
# Case = np.array([[2,-1,-2,0,-3,-4],[-1,1,1,1,1,-1],[-2,1,1,1,1,-2],[0,1,1,1,1,0],[-3,1,1,1,1,-3],[-4,-1,-2,0,-3,-4]])
# Plateau = plt.matshow(Case)
# plt.colorbar(Plateau)
# plt.show()

def elimination(L):
    c = 0
    for i in range(len(L)):
        if L[i] <= 0:
            c += 1
    return c!=0
            
def tour(numero_joueur, argent, case, position):
    r = lancerdede()
    print("lancerdede", r)
    position[numero_joueur] += r #le joueur avance
    if position[numero_joueur] > len(Liste)-1 : #si il est au bout
        position[numero_joueur] -= len(Liste) #il recommence un tour
        argent[numero_joueur] += 2
    print("position_numero_joueur",position[numero_joueur])
    argent,case = acheter(position[numero_joueur], numero_joueur) #soit il achete
    argent,case = payer(position[numero_joueur], numero_joueur) #soit il paye
    return argent,case,position

def jeu(argent,case,position_j1,position_j2, position_j3):
    '''
    entrée : informations sur les joueurs avant de commencer la partie
    Sortie : joueur gagnant, et informations sur les joueurs
    Comment ? Un joueur lance un dé, achète la propriété ou non, c'est au joueur suivant qui lance un dé, paye ou achète, etc
    '''
    position = [position_j1,position_j2, position_j3]
    while not elimination(argent): #tant qu'aucun joueur n'est éliminé
        for i in range(nb_joueurs):
            argent,case,position = tour(i,argent,case,position)
    return argent,case,position

print(jeu(argent,case,0,0,0))























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
from random import random, randint
import matplotlib.pyplot as plt
import numpy as np

Liste = [2,-1,-2,0,-3,-4]
argent_j1 = argent_j2 = argent_j3 = 5
Cases_j1 = [2,1,2,0,3,0]
Cases_j2 = [2,0,0,0,0,4]
Cases_j3 = [0 for k in range(len(Liste))]
Cases_j3[0] = 2
for k in range(1,len(Liste)):
    if random()<1/2:
        Cases_j3[k] = -Liste[k]
argent = [argent_j1, argent_j2, argent_j3]
case = [Cases_j1, Cases_j2, Cases_j3]

nb_joueurs = 3

def lancerdede():
    '''Stimule un lancer de dé'''
    return randint(1,6)
    
def acheter(place, numero_joueur):
    """ entrée : case où se trouve le joueur
                 le joueur qui joue
        sortie : la liste joueurs modifiée avec les nouvelles valeurs d'argent et des cases
        fonction permettant au joueur de pouvoir acheter une case 
    """
    print("numero_joueur", numero_joueur)
    print("place",place)
    # position[numero_joueur] = place
    if place != 0 and argent[numero_joueur] > case[numero_joueur][place] > 0:
        argent[numero_joueur] -= case[numero_joueur][place]
        case[numero_joueur][place] = 0
        for i in range(3):
            if i != numero_joueur:
                case[i][place] = Liste[place]
    print("case",case)
    print("argent", argent)
    print(" ")
    return argent,case 
    
def payer (place, numero_joueur):
    """ entrée : case où se trouve le joueur
                 le joueur qui joue
        sortie : la liste joueurs modifiée avec les nouvelles valeurs d'argent et des cases
        fonction permettant au joueur de payer au joueur possédant la case où il se trouve
    """ 
    # position[numero_joueur] = place
    argent_perdu = case[numero_joueur][place]
    if argent_perdu < 0:
        argent[numero_joueur] += argent_perdu
    for i in range(3):
        if i != numero_joueur:
            if case[i][place] == 0:
                argent[i] -= argent_perdu
    return argent,case
        
    
        
# ----------------------------------------------------------PROGRAMME----------------------------------------------------------------------
  
# Case = np.array([[2,-1,-2,0,-3,-4],[-1,1,1,1,1,-1],[-2,1,1,1,1,-2],[0,1,1,1,1,0],[-3,1,1,1,1,-3],[-4,-1,-2,0,-3,-4]])
# Plateau = plt.matshow(Case)
# plt.colorbar(Plateau)
# plt.show()

def elimination(L):
    c = 0
    for i in range(len(L)):
        if L[i] <= 0:
            c += 1
    return c!=0
            
def tour(numero_joueur, argent, case, position):
    r = lancerdede()
    print("lancerdede", r)
    position[numero_joueur] += r #le joueur avance
    if position[numero_joueur] > len(Liste)-1 : #si il est au bout
        position[numero_joueur] -= len(Liste) #il recommence un tour
        argent[numero_joueur] += 2
    print("position_numero_joueur",position[numero_joueur])
    argent,case = acheter(position[numero_joueur], numero_joueur) #soit il achete
    argent,case = payer(position[numero_joueur], numero_joueur) #soit il paye
    return argent,case,position

def jeu(argent,case,position_j1,position_j2, position_j3):
    '''
    entrée : informations sur les joueurs avant de commencer la partie
    Sortie : joueur gagnant, et informations sur les joueurs
    Comment ? Un joueur lance un dé, achète la propriété ou non, c'est au joueur suivant qui lance un dé, paye ou achète, etc
    '''
    position = [position_j1,position_j2, position_j3]
    k=0
    while not elimination(argent) and k < 100 : #tant qu'aucun joueur n'est éliminé
        for i in range(nb_joueurs):
            argent,case,position = tour(i,argent,case,position)
            k+=1
    return argent,case,position

print(jeu(argent,case,0,0,0))











YOUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU

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
#coallition 

##
from random import random, randint
import matplotlib.pyplot as plt
import numpy as np

Liste = [200,-60,-60,0,-100,-100,-120,0,-140,-140,-160,0,-180,-180,-200,0,-220,-220,-240,0,-260,-260,-280,0,-300,-300,-320,0,-350,-400]
argent_j1 = argent_j2 = argent_j3 = argent_j4 = 1500

# Cases joueur 1
Cases_j1 = []
for k in Liste:
    if k >= -280 and k != 200 :
        Cases_j1.append(abs(k))
    elif k == 200:
        Cases_j1.append(k)
    else :
        Cases_j1.append(0)

# Cases joueur 2
Cases_j2 = []
for k in Liste :
    if k < -280:
        Cases_j2.append(abs(k))
    elif k == 200 :
        Cases_j2.append(k)
    else :
        Cases_j2.append(0)

# Cases joueur 3
Cases_j3 = [0 for k in range(len(Liste))]
Cases_j3[0] = 200
for k in range(1,len(Liste)):
    if random()<1/2:
        Cases_j3[k] = -Liste[k]
        
# Cases joueur 4
Cases_j4 = []
for k in Liste:
    Cases_j4.append(abs(k))

argent = [argent_j1, argent_j2, argent_j3, argent_j4]
case = [Cases_j1, Cases_j2, Cases_j3, Cases_j4]
# position = [position_j1, position_j2]

nb_joueurs = 4

def lancerdede():
    '''Stimule un lancer de dé'''
    return randint(1,6)
    
def acheter(place, numero_joueur):
    """ entrée : case où se trouve le joueur
                 le joueur qui joue
        sortie : la liste joueurs modifiée avec les nouvelles valeurs d'argent et des cases
        fonction permettant au joueur de pouvoir acheter une case 
    """
    print("numero_joueur", numero_joueur)
    print("place",place)
    # position[numero_joueur] = place
    if place != 0 and argent[numero_joueur] > case[numero_joueur][place] > 0:
        argent[numero_joueur] -= case[numero_joueur][place]
        case[numero_joueur][place] = 0
        for i in range(4):
            if i != numero_joueur:
                case[i][place] = Liste[place]/2
    print("case",case)
    print("argent", argent)
    print(" ")
    return argent,case 
    
def payer (place, numero_joueur):
    """ entrée : case où se trouve le joueur
                 le joueur qui joue
        sortie : la liste joueurs modifiée avec les nouvelles valeurs d'argent et des cases
        fonction permettant au joueur de payer au joueur possédant la case où il se trouve
    """ 
    # position[numero_joueur] = place
    argent_perdu = case[numero_joueur][place]
    if argent_perdu < 0:
        argent[numero_joueur] += argent_perdu
    for i in range(4):
        if i != numero_joueur:
            if case[i][place] == 0:
                argent[i] -= argent_perdu
    return argent,case
        
    
        
# --------------------------------------------------PROGRAMME----------------------------------------------------------------------
  
# Case = np.array([[200,-60,-60,0,-100,-100,-120,0],[0,1,1,1,1,1,1,-140],[-320,1,1,1,1,1,1,-140],[-300,1,1,1,1,1,1,-160],[-300,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,-180],[-280,1,1,1,1,1,1,-180],[-260,-260,0,-240,-240,-220,-220,-200]])
# Plateau = plt.matshow(Case)
# plt.colorbar(Plateau)
# plt.show()

def elimination(L):
    c = 0
    for i in range(len(L)):
        if L[i] <= 0:
            c += 1
    return c!=0
            
def tour(numero_joueur, argent, case, position):
    r = lancerdede()
    position[numero_joueur] += r #le joueur avance
    if position[numero_joueur] > len(Liste)-1 : #si il est au bout
        position[numero_joueur] -= len(Liste) #il recommence un tour
        argent[numero_joueur] += 200
    argent,case = acheter(position[numero_joueur], numero_joueur) #soit il achete
    argent,case = payer(position[numero_joueur], numero_joueur) #soit il paye
    return argent,case,position

def jeu(argent,case,position_j1,position_j2, position_j3, position_j4):
    '''
    entrée : informations sur les joueurs avant de commencer la partie
    Sortie : joueur gagnant, et informations sur les joueurs
    Comment ? Un joueur lance un dé, achète la propriété ou non, c'est au joueur suivant qui lance un dé, paye ou achète, etc
    '''
    position = [position_j1,position_j2, position_j3, position_j4]
    k = 0
    while not elimination(argent) and k != 100: #tant qu'aucun joueur n'est éliminé et que l'on ne fait pas un match nul
        for i in range(nb_joueurs):
            argent,case,position = tour(i,argent,case,position)
        k += 1
        print("tour", k)
    return argent,case,position

print(jeu(argent,case,0,0,0,0))






























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
#coallition 

##
from random import random, randint
import matplotlib.pyplot as plt
import numpy as np
from copy import deepcopy

Liste = [200,-60,-60,0,-100,-100,-120,0,-140,-140,-160,0,-180,-180,-200,0,-220,-220,-240,0,-260,-260,-280,0,-300,-300,-320,0,-350,-400]
argent_j1 = argent_j2 = argent_j3 = argent_j4 = 1500

# Cases joueur 1
Cases_j1 = []
for k in Liste:
    if k >= -280 and k != 200 :
        Cases_j1.append(abs(k))
    elif k == 200:
        Cases_j1.append(k)
    else :
        Cases_j1.append(0)

# Cases joueur 2
Cases_j2 = []
for k in Liste :
    if k < -280:
        Cases_j2.append(abs(k))
    elif k == 200 :
        Cases_j2.append(k)
    else :
        Cases_j2.append(0)

# Cases joueur 3
Cases_j3 = [0 for k in range(len(Liste))]
Cases_j3[0] = 200
for k in range(1,len(Liste)):
    if random()<1/2:
        Cases_j3[k] = -Liste[k]
        
# Cases joueur 4
Cases_j4 = []
for k in Liste:
    Cases_j4.append(abs(k))

argent = [argent_j1, argent_j2, argent_j3, argent_j4]
case = [Cases_j1, Cases_j2, Cases_j3, Cases_j4]
# position = [position_j1, position_j2]

nb_joueurs = 4

def lancerdede():
    '''Stimule un lancer de dé'''
    return randint(1,6)
    
def acheter(place, numero_joueur):
    """ entrée : case où se trouve le joueur
                 le joueur qui joue
        sortie : la liste joueurs modifiée avec les nouvelles valeurs d'argent et des cases
        fonction permettant au joueur de pouvoir acheter une case 
    """
    print("numero_joueur", numero_joueur)
    print("place",place)
    # position[numero_joueur] = place
    if place != 0 and argent[numero_joueur] > case[numero_joueur][place] > 0:
        argent[numero_joueur] -= case[numero_joueur][place]
        case[numero_joueur][place] = 0
        for i in range(4):
            if i != numero_joueur:
                case[i][place] = Liste[place]/2
    print("case",case)
    print("argent", argent)
    print(" ")
    return argent,case 
    
def payer (place, numero_joueur):
    """ entrée : case où se trouve le joueur
                 le joueur qui joue
        sortie : la liste joueurs modifiée avec les nouvelles valeurs d'argent et des cases
        fonction permettant au joueur de payer au joueur possédant la case où il se trouve
    """ 
    # position[numero_joueur] = place
    argent_perdu = case[numero_joueur][place]
    if argent_perdu < 0:
        argent[numero_joueur] += argent_perdu
    for i in range(4):
        if i != numero_joueur:
            if case[i][place] == 0:
                argent[i] -= argent_perdu
    return argent,case
        
    
        
# --------------------------------------------------PROGRAMME----------------------------------------------------------------------
  
# Case = np.array([[200,-60,-60,0,-100,-100,-120,0],[0,1,1,1,1,1,1,-140],[-320,1,1,1,1,1,1,-140],[-300,1,1,1,1,1,1,-160],[-300,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,-180],[-280,1,1,1,1,1,1,-180],[-260,-260,0,-240,-240,-220,-220,-200]])
# Plateau = plt.matshow(Case)
# plt.colorbar(Plateau)
# plt.show()

def elimination(L):
    c = 0
    for i in range(len(L)):
        if L[i] <= 0:
            c += 1
    return c!=0
            
def tour(numero_joueur, argent, case, position):
    argent0 = argent.copy()
    case0 = deepcopy(case)
    r = lancerdede()
    position[numero_joueur] += r #le joueur avance
    if position[numero_joueur] > len(Liste)-1 : #si il est au bout
        position[numero_joueur] -= len(Liste) #il recommence un tour
        argent0[numero_joueur] += 200
    argent0,case0 = acheter(position[numero_joueur], numero_joueur) #soit il achete
    argent0,case0 = payer(position[numero_joueur], numero_joueur) #soit il paye
    return argent0,case0,position

def jeu(argent,case,position_j1,position_j2, position_j3, position_j4):
    '''
    entrée : informations sur les joueurs avant de commencer la partie
    Sortie : joueur gagnant, et informations sur les joueurs
    Comment ? Un joueur lance un dé, achète la propriété ou non, c'est au joueur suivant qui lance un dé, paye ou achète, etc
    '''
    argent1 = argent.copy()
    case1 = deepcopy(case)
    position = [position_j1,position_j2, position_j3, position_j4]
    k = 0
    while not elimination(argent1) and k != 100: #tant qu'aucun joueur n'est éliminé et que l'on ne fait pas un match nul
        for i in range(nb_joueurs):
            argent1,case1,position = tour(i,argent1,case1,position)
        k += 1
        print("tour", k)
    return argent1,case1,position

print(jeu(argent,case,0,0,0,0))

def nouveau_jeu():
    argent2 = [1500, 1500, 1500, 1500]
    case2 = [Cases_j1, Cases_j2, Cases_j3, Cases_j4]
    return argent2, case2

def perdant(L):
    x = min(L)
    return L.index(x)
    
def moyenne(argent, case):
    argent2 = argent.copy()
    case2 = deepcopy(case)
    Perdants = []
    for i in range(100):
        Argent = jeu(argent1,case1,0,0,0,0)[0]
        Perdants.append(perdant(Argent))
        print("Argent", Argent)
    return Perdants
        
print(moyenne(argent, case))


















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
#coallition 

##
from random import random, randint
import matplotlib.pyplot as plt
import numpy as np
from copy import deepcopy

Liste = [200,-60,-60,0,-100,-100,-120,0,-140,-140,-160,0,-180,-180,-200,0,-220,
-220,-240,0,-260,-260,-280,0,-300,-300,-320,0,-350,-400]
argent_j1 = argent_j2 = argent_j3 = argent_j4 = 1500

# Cases joueur 1
Cases_j1 = []
for k in Liste:
    if k >= -280 and k != 200 :
        Cases_j1.append(abs(k))
    elif k == 200:
        Cases_j1.append(k)
    else :
        Cases_j1.append(0)
        
        
        
def initS1():
    
    #mettre les stratégies sous forme de fonctions pour en faire des constantes
    
    return L        
   
   
   
        
        
Cases_j1bis = Cases_j1.copy()

# Cases joueur 2
Cases_j2 = []
for k in Liste :
    if k < -280:
        Cases_j2.append(abs(k))
    elif k == 200 :
        Cases_j2.append(k)
    else :
        Cases_j2.append(0)
Cases_j2bis = Cases_j2.copy()

# Cases joueur 3
Cases_j3 = [0 for k in range(len(Liste))]
Cases_j3[0] = 200
for k in range(1,len(Liste)):
    if random()<1/2:
        Cases_j3[k] = -Liste[k]
Cases_j3bis = Cases_j3.copy()
        
# Cases joueur 4
Cases_j4 = []
for k in Liste:
    Cases_j4.append(abs(k))
Cases_j4bis = Cases_j4.copy()

argent = [argent_j1, argent_j2, argent_j3, argent_j4]
case = [Cases_j1, Cases_j2, Cases_j3, Cases_j4]
# position = [position_j1, position_j2]

nb_joueurs = 4

def lancerdede():
    '''Stimule un lancer de dé'''
    return randint(1,6)
    
def acheter(place, numero_joueur):
    """ entrée : case où se trouve le joueur
                 le joueur qui joue
        sortie : la liste joueurs modifiée avec les nouvelles valeurs d'argent et des cases
        fonction permettant au joueur de pouvoir acheter une case 
    """
    # print("numero_joueur", numero_joueur)
    # print("place",place)
    # position[numero_joueur] = place
    if place != 0 and argent[numero_joueur] > case[numero_joueur][place] > 0:
        argent[numero_joueur] -= case[numero_joueur][place]
        case[numero_joueur][place] = 0
        for i in range(4):
            if i != numero_joueur:
                case[i][place] = Liste[place]/2
    # print("case",case)
    # print("argent", argent)
    # print(" ")
    return argent,case 
    
def payer (place, numero_joueur):
    """ entrée : case où se trouve le joueur
                 le joueur qui joue
        sortie : la liste joueurs modifiée avec les nouvelles valeurs d'argent et des cases
        fonction permettant au joueur de payer au joueur possédant la case où il se trouve
    """ 
    # position[numero_joueur] = place
    argent_perdu = case[numero_joueur][place]
    if argent_perdu < 0:
        argent[numero_joueur] += argent_perdu
    for i in range(4):
        if i != numero_joueur:
            if case[i][place] == 0:
                argent[i] -= argent_perdu
    return argent,case
        
    
        
# --------------------------------------------------PROGRAMME----------------------------------------------------------------------
  
# Case = np.array([[200,-60,-60,0,-100,-100,-120,0],[0,1,1,1,1,1,1,-140],[-320,1,1,1,1,1,1,-140],[-300,1,1,1,1,1,1,-160],[-300,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,-180],[-280,1,1,1,1,1,1,-180],[-260,-260,0,-240,-240,-220,-220,-200]])
# Plateau = plt.matshow(Case)
# plt.colorbar(Plateau)
# plt.show()

def elimination(L):
    c = 0
    for i in range(len(L)):
        if L[i] <= 0:
            c += 1
    return c!=0
            
def tour(numero_joueur, argent, case, position):
    argent0 = argent.copy()
    case0 = deepcopy(case)
    r = lancerdede()
    position[numero_joueur] += r #le joueur avance
    if position[numero_joueur] > len(Liste)-1 : #si il est au bout
        position[numero_joueur] -= len(Liste) #il recommence un tour
        argent0[numero_joueur] += 200
    argent0,case0 = acheter(position[numero_joueur], numero_joueur) #soit il achete
    argent0,case0 = payer(position[numero_joueur], numero_joueur) #soit il paye
    return argent0,case0,position

def jeu2(Liste):
    '''
    entrée : informations sur les joueurs avant de commencer la partie
    Sortie : joueur gagnant, et informations sur les joueurs
    Comment ? Un joueur lance un dé, achète la propriété ou non, c'est au joueur suivant qui lance un dé, paye ou achète, etc
    '''
    argent = [1500,1500,1500,1500]
    argent1 = argent.copy()
    case = [Cases_j1bis,Cases_j2bis,Cases_j3bis,Cases_j4bis]
    case1 = deepcopy(case)
    position = [0,0,0,0]
    k = 0
    while not elimination(argent1) and k != 100: #tant qu'aucun joueur n'est éliminé et que l'on ne fait pas un match nul
        for i in range(nb_joueurs):
            argent1,case1,position = tour(i,argent1,case1,position)
        k += 1
        # print("tour", k)
    return argent1,case1,position

print(jeu2())

def perdant(L):
    x = min(L)
    return L.index(x)

def moyenne2():
    # argent2 = argent.copy()
    # case2 = deepcopy(case)
    # argentA, caseC = nouveau_jeu() 
    P = []
    k = 0
    while k<100:
        jeux = jeu2()
        Argent = jeux[0]
        P.append(perdant(Argent))
        print("Argent", Argent)
        k += 1
    return P
        
print(moyenne2())





'''
joueur 1 achète petites cases
joueur 2 achete grosses cases
joueur 3 aléatoire
joueur 4 achete tout
J1 = 0
J2 = 0
Cases(J1) = [[],[]]
Cases[J1]
'''
#coallition 

##
from random import random, randint
import matplotlib.pyplot as plt
import numpy as np
from copy import deepcopy

Liste = [200,-60,-60,0,-100,-100,-120,0,-140,-140,-160,0,-180,-180,-200,0,-220,
-220,-240,0,-260,-260,-280,0,-300,-300,-320,0,-350,-400]
argent_j1 = argent_j2 = argent_j3 = argent_j4 = 1500
        
def initS1(Li):
    L = []
    for k in Li:
        if k >= -280 and k != 200 :
            L.append(abs(k))
        elif k == 200:
            L.append(k)
        else :
            L.append(0)
    return L        

def initS2(Li):
    L = []
    for k in Li :
        if k < -280:
            L.append(abs(k))
        elif k == 200 :
            L.append(k)
        else :
            L.append(0)
    return L

def initS3(Li):
    L = [0 for k in range(len(Li))]
    L[0] = 200
    for k in range(1,len(Li)):
        if random()<1/2:
            L[k] = -Li[k]
    return L

def initS4(Li):
    L = []
    for k in Li:
        L.append(abs(k))
    return L
    
Cases_j1 = initS1(Liste)
Cases_j2 = initS2(Liste)
Cases_j3 = initS3(Liste)
Cases_j4 = initS4(Liste)

argent = [argent_j1, argent_j2, argent_j3, argent_j4]
case = [Cases_j1, Cases_j2, Cases_j3, Cases_j4]
position = [0,0,0,0]

nb_joueurs = 4

def lancerdede():
    '''Stimule un lancer de dé'''
    return randint(1,6)
    
def acheter(place, numero_joueur, A, C):
    """ entrée : case où se trouve le joueur qui joue
        sortie : la liste joueurs modifiée avec les nouvelles valeurs 
        d'argent et des cases
        fonction permettant au joueur de pouvoir acheter une case 
    """
    # print("numero_joueur", numero_joueur)
    # print("place",place)
    # position[numero_joueur] = place
    if place != 0 and A[numero_joueur] > C[numero_joueur][place] > 0:
        A[numero_joueur] -= C[numero_joueur][place]
        C[numero_joueur][place] = 0
        for i in range(4):
            if i != numero_joueur:
                C[i][place] = Liste[place]/2
    # print("case",case)
    # print("argent", argent)
    # print(" ")
    return A,C 
    
def payer (place, numero_joueur, A, C):
    """ entrée : case où se trouve le joueur qui joue
        sortie : la liste joueurs modifiée avec les nouvelles valeurs 
        d'argent et des cases
        fonction permettant au joueur de payer au joueur possédant la case 
    """ 
    # position[numero_joueur] = place
    argent_perdu = C[numero_joueur][place]
    if argent_perdu < 0:
        A[numero_joueur] += argent_perdu
    for i in range(4):
        if i != numero_joueur:
            if C[i][place] == 0:
                A[i] -= argent_perdu
    return A,C
        
    
        
# --------------------------------------------------PROGRAMME----------------------------------------------------------------------
  
# Case = np.array([[200,-60,-60,0,-100,-100,-120,0],[0,1,1,1,1,1,1,-140],[-320,1,1,1,1,1,1,-140],[-300,1,1,1,1,1,1,-160],[-300,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,-180],[-280,1,1,1,1,1,1,-180],[-260,-260,0,-240,-240,-220,-220,-200]])
# Plateau = plt.matshow(Case)
# plt.colorbar(Plateau)
# plt.show()

def elimination(L):
    c = 0
    for i in range(len(L)):
        if L[i] <= 0:
            c += 1
    return c!=0
            
def tour(numero_joueur, A, C, P):
    argent0 = A.copy()
    case0 = deepcopy(C)
    r = lancerdede()
    P[numero_joueur] += r #le joueur avance
    if P[numero_joueur] > len(Liste)-1 : #si il est au bout
        P[numero_joueur] -= len(Liste) #il recommence un tour
        argent0[numero_joueur] += 200
    argent0,case0 = acheter(P[numero_joueur], numero_joueur, A, C) #soit il achete
    argent0,case0 = payer(P[numero_joueur], numero_joueur, A, C) #soit il paye
    return argent0,case0,P

def jeu(A, C, P):
    '''
    entrée : informations sur les joueurs avant de commencer la partie
    Sortie : joueur gagnant, et informations sur les joueurs
    Comment ? Un joueur lance un dé, achète la propriété ou non, c'est au joueur suivant qui lance un dé, paye ou achète, etc
    '''
    argent1 = A.copy()
    case1 = deepcopy(C)
    k = 0
    while not elimination(argent1) and k != 100: #tant qu'aucun joueur n'est éliminé et que l'on ne fait pas un match nul
        for i in range(nb_joueurs):
            argent1,case1,P = tour(i,argent1,case1,P)
        k += 1
        # print("tour", k)
    return argent1,case1,P

print(jeu2(argent, case, position))

def perdant(L):
    x = min(L)
    return L.index(x)

def moyenne(Li):
    Perdant = []
    for i in range(100):
        argent = [1500,1500,1500,1500]
        Cases_j1 = initS1(Li)
        Cases_j2 = initS2(Li)
        Cases_j3 = initS3(Li)
        Cases_j4 = initS4(Li)
        case = [Cases_j1, Cases_j2, Cases_j3, Cases_j4]
        position = [0,0,0,0]
        # print("argent joueur", argent)
        # print("case joueur", case)
        # print("position", position)
        jeux = jeu(argent, case, position)
        # print("jeux", jeux)
        Argent = jeux[0]
        Perdant.append(perdant(Argent))
        print("Argent", Argent)
        Argent = []
    return Perdant
        
print(moyenne(Liste))

def jeufinal(argent,case,position_j1,position_j2, position_j3, position_j4):
    joueurs_en_jeu = [1,2,3,4]
    argent1 = argent.copy()
    case1 = deepcopy(case)
    position = [position_j1,position_j2, position_j3, position_j4]
    while len(argent1) != 1 :
        jeu1 = jeu(argent1,case1,position_j1,position_j2, position_j3, position_j4)
        perd = perdant(jeu1[0])
        print(perd)
        joueurs_en_jeu.pop(perd)
        for i in range(len(case1[perd])) :
            if case1[perd][i] == 0 and i != 0 :
                for k in joueurs_en_jeu:
                    case1[k-1][i] = Case_init[k-1][i]
        argent1.pop(perd)
        case1.pop(perd)
    return joueurs_en_jeu
















'''
joueur 1 achète petites cases
joueur 2 achete grosses cases
joueur 3 aléatoire
joueur 4 achete tout
J1 = 0
J2 = 0
Cases(J1) = [[],[]]
Cases[J1]
'''
#coallition 

##
from random import random, randint
import matplotlib.pyplot as plt
import numpy as np
from copy import deepcopy

Liste = [200,-60,-60,0,-100,-100,-120,0,-140,-140,-160,0,-180,-180,-200,0,-220,
-220,-240,0,-260,-260,-280,0,-300,-300,-320,0,-350,-400]
argent_j1 = argent_j2 = argent_j3 = argent_j4 = 1500
        
def initS1(Li):
    L = []
    for k in Li:
        if k >= -280 and k != 200 :
            L.append(abs(k))
        elif k == 200:
            L.append(k)
        else :
            L.append(0)
    return L        

def initS2(Li):
    L = []
    for k in Li :
        if k < -280:
            L.append(abs(k))
        elif k == 200 :
            L.append(k)
        else :
            L.append(0)
    return L

def initS3(Li):
    L = [0 for k in range(len(Li))]
    L[0] = 200
    for k in range(1,len(Li)):
        if random()<1/2:
            L[k] = -Li[k]
    return L

def initS4(Li):
    L = []
    for k in Li:
        L.append(abs(k))
    return L
    
Cases_j1 = initS1(Liste)
Cases_j2 = initS2(Liste)
Cases_j3 = initS3(Liste)
Cases_j4 = initS4(Liste)

argent = [argent_j1, argent_j2, argent_j3, argent_j4]
case = [Cases_j1, Cases_j2, Cases_j3, Cases_j4]
position = [0,0,0,0]

nb_joueurs = 4

def lancerdede():
    '''Stimule un lancer de dé'''
    return randint(1,6)
    
def acheter(place, numero_joueur, A, C):
    """ entrée : case où se trouve le joueur qui joue
        sortie : la liste joueurs modifiée avec les nouvelles valeurs 
        d'argent et des cases
        fonction permettant au joueur de pouvoir acheter une case 
    """
    # print("numero_joueur", numero_joueur)
    # print("place",place)
    # position[numero_joueur] = place
    if place != 0 and A[numero_joueur] > C[numero_joueur][place] > 0:
        A[numero_joueur] -= C[numero_joueur][place]
        C[numero_joueur][place] = 0
        for i in range(nb_joueurs):
            if i != numero_joueur:
                C[i][place] = Liste[place]/2
    # print("case",case)
    # print("argent", argent)
    # print(" ")
    return A,C 
    
def payer (place, numero_joueur, A, C):
    """ entrée : case où se trouve le joueur qui joue
        sortie : la liste joueurs modifiée avec les nouvelles valeurs 
        d'argent et des cases
        fonction permettant au joueur de payer au joueur possédant la case 
    """ 
    # position[numero_joueur] = place
    argent_perdu = C[numero_joueur][place]
    if argent_perdu < 0:
        A[numero_joueur] += argent_perdu
    for i in range(nb_joueurs):
        if i != numero_joueur:
            if C[i][place] == 0:
                A[i] -= argent_perdu
    return A,C
        
    
        
# --------------------------------------------------PROGRAMME----------------------------------------------------------------------
  
# Case = np.array([[200,-60,-60,0,-100,-100,-120,0],[0,1,1,1,1,1,1,-140],[-320,1,1,1,1,1,1,-140],[-300,1,1,1,1,1,1,-160],[-300,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,-180],[-280,1,1,1,1,1,1,-180],[-260,-260,0,-240,-240,-220,-220,-200]])
# Plateau = plt.matshow(Case)
# plt.colorbar(Plateau)
# plt.show()

def elimination(L):
    c = 0
    for i in range(len(L)):
        if L[i] <= 0:
            c += 1
    return c!=0
            
def tour(numero_joueur, A, C, P):
    argent0 = A.copy()
    case0 = deepcopy(C)
    r = lancerdede()
    P[numero_joueur] += r #le joueur avance
    if P[numero_joueur] > len(Liste)-1 : #si il est au bout
        P[numero_joueur] -= len(Liste) #il recommence un tour
        argent0[numero_joueur] += 200
    argent0,case0 = acheter(P[numero_joueur], numero_joueur, A, C) #soit il achete
    argent0,case0 = payer(P[numero_joueur], numero_joueur, A, C) #soit il paye
    return argent0,case0,P

def jeu(A, C, P):
    '''
    entrée : informations sur les joueurs avant de commencer la partie
    Sortie : joueur gagnant, et informations sur les joueurs
    Comment ? Un joueur lance un dé, achète la propriété ou non, c'est au joueur suivant qui lance un dé, paye ou achète, etc
    '''
    argent1 = A.copy()
    case1 = deepcopy(C)
    k = 0
    while not elimination(argent1) and k != 100: #tant qu'aucun joueur n'est éliminé et que l'on ne fait pas un match nul
        for i in range(nb_joueurs):
            argent1,case1,P = tour(i,argent1,case1,P)
        k += 1
        # print("tour", k)
    return argent1,case1,P

# print(jeu(argent, case, position))

def perdant(L):
    x = min(L)
    return L.index(x)

def moyenne(Li):
    Perdant = []
    for i in range(100):
        argent = [1500,1500,1500,1500]
        Cases_j1 = initS1(Li)
        Cases_j2 = initS2(Li)
        Cases_j3 = initS3(Li)
        Cases_j4 = initS4(Li)
        case = [Cases_j1, Cases_j2, Cases_j3, Cases_j4]
        position = [0,0,0,0]
        # print("argent joueur", argent)
        # print("case joueur", case)
        # print("position", position)
        jeux = jeu(argent, case, position)
        # print("jeux", jeux)
        Argent = jeux[0]
        Perdant.append(perdant(Argent))
        print("Argent", Argent)
        Argent = []
    return Perdant
        
# print(moyenne(Liste))


def jeufinal(A, C, P):
    nb_joueurs = 4
    joueurs_en_jeu = [1,2,3,4]
    argent1 = A.copy()
    case1 = deepcopy(C)
    while len(argent1) != 1 :
        jeu1 = jeu(argent1,case1,P)
        perd = perdant(jeu1[0])
        joueurs_en_jeu.pop(perd)
        for i in range(len(case1[perd])) :
            if case1[perd][i] == 0:
                for k in joueurs_en_jeu:
                    case1[k-1][i] = C[k-1][i]
        argent1.pop(perd)
        case1.pop(perd)
        nb_joueurs -= 1
    return joueurs_en_jeu

print(jeufinal(argent, case, position))
















'''
joueur 1 achète petites cases
joueur 2 achete grosses cases
joueur 3 aléatoire
joueur 4 achete tout

variance du nombre de parties gagnées
identifier inversion de tendance en modifiant un paramètre du jeu
regarder argent qui reste au gagnant à la fin
faire représetation graphique 
voir quand le joueur achete les cases en premier
'''
#coallition 

##
from random import random, randint
from copy import deepcopy
Liste = [200,-60,0,-60,0,0,-100,0,-100,-120,0,-140,0,-140,-160,0,-180,0,-180,-200,0,-220,
0,-220,-240,0,-260,-260,0,-280,0,-300,-300,0,-320,0,0,-350,0,-400]
argent_j1 = argent_j2 = argent_j3 = argent_j4 = 1500
        
def initS1(Li):
    L = []
    for k in Li:
        if k >= -280 and k != 200 :
            L.append(abs(k))
        elif k == 200:
            L.append(k)
        else :
            L.append(0)
    return L        

def initS2(Li):
    L = []
    for k in Li :
        if k < -280:
            L.append(abs(k))
        elif k == 200 :
            L.append(k)
        else :
            L.append(0)
    return L

def initS3(Li):
    L = [0 for k in range(len(Li))]
    L[0] = 200
    for k in range(1,len(Li)):
        if random()<1/2:
            L[k] = -Li[k]
    return L

def initS4(Li):
    L = []
    for k in Li:
        L.append(abs(k))
    return L
    
Cases_j1 = initS1(Liste)
Cases_j2 = initS2(Liste)
Cases_j3 = initS3(Liste)
Cases_j4 = initS4(Liste)

argent = [argent_j1, argent_j2, argent_j3, argent_j4]
case = [Cases_j1, Cases_j2, Cases_j3, Cases_j4]
position = [0,0,0,0]

nb_joueurs = 4

def lancerdede():
    '''Stimule un lancer de dé'''
    return randint(1,6)
    
def acheter(place, numero_joueur, A, C):
    """ entrée : case où se trouve le joueur qui joue
        sortie : la liste joueurs modifiée avec les nouvelles valeurs 
        d'argent et des cases
        fonction permettant au joueur de pouvoir acheter une case si il le peut
    """
    # print("numero_joueur", numero_joueur)
    # print("place",place)
    # position[numero_joueur] = place
    argent1 = A.copy()
    case1 = C.copy()
    n = numero_joueur
    if place != 0 and argent1[n] > case1[n][place] > 0:
        argent1[n] -= case1[n][place]
        case1[n][place] = 0
        for i in range(nb_joueurs):
            if i != n:
                print(case1[i][place])
                case1[i][place] = Liste[place]/2
    # print("case",case)
    # print("argent", argent)
    # print(" ")
    return argent1, case1
    
def payer (place, numero_joueur, A, C):
    """ entrée : case où se trouve le joueur qui joue
        sortie : la liste joueurs modifiée avec les nouvelles valeurs
        d'argent et des cases
        fonction permettant au joueur de payer au joueur possédant la case
    """ 
    # position[numero_joueur] = place
    n = numero_joueur
    argent1 = A.copy()
    case1 = C.copy()
    argent_perdu = case1[n][place]
    if argent_perdu < 0:
        argent1[n] += argent_perdu
    for i in range(nb_joueurs):
        if i != numero_joueur:
            if case1[i][place] == 0:
                argent1[i] -= argent_perdu
    return argent1,case1
        
    
        
# --------------------------------------------------PROGRAMME----------------------------------------------------------------------
  
Case = np.array([[200,-60,0,-60,0,0,-100,0,-100,-120,0],
[-400,50,50,50,50,50,50,50,50,50,-140], 
[0,50,50,50,50,50,50,50,50,50,0], 
[-350,50,50,50,50,50,50,50,50,50,-140], 
[0,50,50,50,50,50,50,50,50,50,-160], 
[0,50,50,50,50,50,50,50,50,50,0], 
[-320,50,50,50,50,50,50,50,50,50,-180], 
[0,50,50,50,50,50,50,50,50,50,0], 
[-300,50,50,50,50,50,50,50,50,50,-180], 
[-300,50,50,50,50,50,50,50,50,50,-200], 
[0,-280,1,-260,-260,1,-240,-220,1,-220,0]])

Plateau = plt.matshow(Case)
plt.colorbar(Plateau)
plt.show()

def elimination(L):
    '''
    entrée : liste L de l'argent des joueurs
    sortie : indice du joueur perdant
    '''
    c = 0
    for i in range(len(L)):
        if L[i] <= 0:
            c += 1
    return c!=0
            
def tour(numero_joueur, A, C, P):
    '''
    entrée : numero du joueur qui joue, argent des joueurs, cases des joueurs, positions des joueurs
    sortie : valeurs de l'aregnt des joueurs, cases, position à la fin du tour du joueur
    '''
    n = numero_joueur
    position0 = P.copy()
    argent0 = A.copy()
    case0 = deepcopy(C)
    r = lancerdede()
    position0[n] += r #le joueur avance
    if position0[n] > len(Liste)-1 : #si il est au bout
        position0[n] -= len(Liste) #il recommence un tour
        argent0[n] += 200
    argent0,case0 = acheter(position0[n], n, argent0, case0) #soit il achete
    argent0,case0 = payer(position0[n], n, argent0, case0) #soit il paye
    return argent0,case0,position0

def jeu(A, C, P):
    '''
    entrée : informations sur les joueurs avant de commencer la partie
    Sortie : informations sur les joueurs une fois qu'un des joueurs est éliminé
    Comment ? Un joueur lance un dé, achète la propriété ou non, c'est au joueur suivant qui lance un dé, paye ou achète, etc
    '''
    argent1 = A.copy()
    case1 = deepcopy(C)
    position1 = P.copy()
    k = 0
    while not elimination(argent1) and k != 100: #tant qu'aucun joueur n'est éliminé et que l'on ne fait pas un match nul
        for i in range(nb_joueurs):
            argent1,case1,position1 = tour(i,argent1,case1,position1)
        k += 1
        # print("tour", k)
    return argent1,case1,P

# print(jeu(argent, case, position))

def perdant(L):
    '''
    entrée : liste d'argent des joueurs 
    sortie : indice dans cette liste du joueur perdant 
    '''
    x = min(L)
    return L.index(x)

def moyenne(Li):
    '''
    entrée : liste du jeu de base
    sortie : liste des perdants pour un grand nombre de session de jeu (jusqu'à ce qu'un joueur perde)
    '''
    Perdant = []
    for i in range(100):
        argent = [1500,1500,1500,1500]
        Cases_j1 = initS1(Li)
        Cases_j2 = initS2(Li)
        Cases_j3 = initS3(Li)
        Cases_j4 = initS4(Li)
        case = [Cases_j1, Cases_j2, Cases_j3, Cases_j4]
        position = [0,0,0,0]
        # print("argent joueur", argent)
        # print("case joueur", case)
        # print("position", position)
        jeux = jeu(argent, case, position)
        # print("jeux", jeux)
        Argent = jeux[0]
        Perdant.append(perdant(Argent))
        print("Argent", Argent)
        Argent = []
    return Perdant
        
# print(moyenne(Liste))

def nb_defaites(L):
    Defaites = [0,0,0,0]
    for j in range(len(Defaites)):
        for k in range(len(L)):
            if L[k] == j:
                Defaites[j] += 1
    return Defaites
    
print(nb_defaites(moyenne(Liste)))

def jeufinal(A, C, P):
    '''
    entrée : informations sur les joueurs
    sortie : joueur gagnant à la fin d'une partie, après3 sessions de jeu
    '''
    position1 = P.copy()
    nb_joueurs = 4
    joueurs_en_jeu = [0,1,2,3]
    argent1 = A.copy()
    case1 = deepcopy(C)
    while len(argent1) != 1 :
        jeu1 = jeu(argent1,case1,position1)
        perd = perdant(jeu1[0])
        joueurs_en_jeu.pop(perd)
        for i in range(len(case1[perd])) :
            if case1[perd][i] == 0:
                for k in joueurs_en_jeu:
                    case1[k][i] = C[k][i]
        argent1.pop(perd)
        case1.pop(perd)
        position1.pop(perd)
        nb_joueurs -= 1
    return joueurs_en_jeu

print(jeufinal(argent, case, position))















'''
joueur 1 achète petites cases
joueur 2 achete grosses cases
joueur 3 aléatoire
joueur 4 achete tout
variance du nombre de parties gagnées
identifier inversion de tendance en modifiant un paramètre du jeu
regarder argent qui reste au gagnant à la fin
faire représetation graphique 
voir quand le joueur achete les cases en premier
'''
#coallition 

##
from random import random, randint
from copy import deepcopy
import numpy as np
import matplotlib.pyplot as plt
Liste = [200,-60,0,-60,0,0,-100,0,-100,-120,0,-140,0,-140,-160,0,-180,0,-180,-200,0,-220,
0,-220,-240,0,-260,-260,0,-280,0,-300,-300,0,-320,0,0,-350,0,-400]
argent_j1 = argent_j2 = argent_j3 = argent_j4 = 1500
        
def initS1(Li):
    L = []
    for k in Li:
        if k >= -280 and k != 200 :
            L.append(abs(k))
        elif k == 200:
            L.append(k)
        else :
            L.append(0)
    return L        

def initS2(Li):
    L = []
    for k in Li :
        if k < -280:
            L.append(abs(k))
        elif k == 200 :
            L.append(k)
        else :
            L.append(0)
    return L

def initS3(Li):
    L = [0 for k in range(len(Li))]
    L[0] = 200
    for k in range(1,len(Li)):
        if random()<1/2:
            L[k] = -Li[k]
    return L

def initS4(Li):
    L = []
    for k in Li:
        L.append(abs(k))
    return L
    
Cases_j1 = initS1(Liste)
Cases_j2 = initS2(Liste)
Cases_j3 = initS3(Liste)
Cases_j4 = initS4(Liste)

argent = [argent_j1, argent_j2, argent_j3, argent_j4]
case = [Cases_j1, Cases_j2, Cases_j3, Cases_j4]
position = [0,0,0,0]

nb_joueurs = 4

def lancerdede():
    '''Stimule un lancer de dé'''
    return randint(1,6)
    
def acheter(place, numero_joueur, A, C):
    """ entrée : case où se trouve le joueur qui joue
        sortie : la liste joueurs modifiée avec les nouvelles valeurs 
        d'argent et des cases
        fonction permettant au joueur de pouvoir acheter une case si il le peut
    """
    # print("numero_joueur", numero_joueur)
    # print("place",place)
    # position[numero_joueur] = place
    argent1 = A.copy()
    case1 = C.copy()
    n = numero_joueur
    if place != 0 and argent1[n] > case1[n][place] > 0:
        argent1[n] -= case1[n][place]
        case1[n][place] = 0
        for i in range(nb_joueurs):
            if i != n:
                # print(case1[i][place])
                case1[i][place] = Liste[place]/2
    # print("case",case)
    # print("argent", argent)
    # print(" ")
    return argent1, case1
    
def payer (place, numero_joueur, A, C):
    """ entrée : case où se trouve le joueur qui joue
        sortie : la liste joueurs modifiée avec les nouvelles valeurs
        d'argent et des cases
        fonction permettant au joueur de payer au joueur possédant la case
    """ 
    # position[numero_joueur] = place
    n = numero_joueur
    argent1 = A.copy()
    case1 = C.copy()
    argent_perdu = case1[n][place]
    if argent_perdu < 0:
        argent1[n] += argent_perdu
    for i in range(nb_joueurs):
        if i != numero_joueur:
            if case1[i][place] == 0:
                argent1[i] -= argent_perdu
    return argent1,case1
    
def joue_toujours (L):
    L1 = []
    for i in range (4):
        if i in L:
            L1.append(1)
        else:
            L1.append(0)
    return L1
    
        
    
        
# --------------------------------------------------PROGRAMME----------------------------------------------------------------------
  
# Case = np.array([[200,-60,0,-60,0,0,-100,0,-100,-120,0],
# [-400,50,50,50,50,50,50,50,50,50,-140], 
# [0,50,50,50,50,50,50,50,50,50,0], 
# [-350,50,50,50,50,50,50,50,50,50,-140], 
# [0,50,50,50,50,50,50,50,50,50,-160], 
# [0,50,50,50,50,50,50,50,50,50,0], 
# [-320,50,50,50,50,50,50,50,50,50,-180], 
# [0,50,50,50,50,50,50,50,50,50,0], 
# [-300,50,50,50,50,50,50,50,50,50,-180], 
# [-300,50,50,50,50,50,50,50,50,50,-200], 
# [0,-280,1,-260,-260,1,-240,-220,1,-220,0]])
# 
# Plateau = plt.matshow(Case)
# plt.colorbar(Plateau)
# plt.show()

def elimination(L):
    '''
    entrée : liste L de l'argent des joueurs
    sortie : indice du joueur perdant
    '''
    c = 0
    for i in range(len(L)):
        if L[i] <= 0:
            c += 1
    return c!=0
            
def tour(numero_joueur, A, C, P, LJ):
    '''
    entrée : numero du joueur qui joue, argent des joueurs, cases des joueurs, positions des joueurs
    sortie : valeurs de l'aregnt des joueurs, cases, position à la fin du tour du joueur
    '''
    n = numero_joueur
    position0 = P.copy()
    argent0 = A.copy()
    case0 = deepcopy(C)
    if joue_toujours(LJ)[n] == 1:
        r = lancerdede()
        position0[n] += r #le joueur avance
        if position0[n] > len(Liste)-1 : #si il est au bout
            position0[n] -= len(Liste) #il recommence un tour
            argent0[n] += 200
        argent0,case0 = acheter(position0[n], n, argent0, case0) #soit il achete
        argent0,case0 = payer(position0[n], n, argent0, case0) #soit il paye
    return argent0,case0,position0

def jeu(A, C, P, LJ):
    '''
    entrée : informations sur les joueurs avant de commencer la partie
    Sortie : informations sur les joueurs une fois qu'un des joueurs est éliminé
    Comment ? Un joueur lance un dé, achète la propriété ou non, c'est au joueur suivant qui lance un dé, paye ou achète, etc
    '''
    argent1 = A.copy()
    case1 = deepcopy(C)
    position1 = P.copy()
    k = 0
    while not elimination(argent1) and k != 100: #tant qu'aucun joueur n'est éliminé et que l'on ne fait pas un match nul
        for i in range(nb_joueurs):
            argent1,case1,position1 = tour(i,argent1,case1,position1, LJ)
        k += 1
        # print("tour", k)
    return argent1,case1,P

# print(jeu(argent, case, position))

def perdant(L, LJ):
    '''
    entrée : liste d'argent des joueurs 
    sortie : indice dans cette liste du joueur perdant 
    '''
    LJ1 = joue_toujours(LJ)
    for i in range(len(LJ1)):
        if LJ1[i] == 0:
            L.pop(LJ1[i])
    x = min(L)
    return L.index(x)

# def moyenne(Li):
#     '''
#     entrée : liste du jeu de base
#     sortie : liste des perdants pour un grand nombre de session de jeu (jusqu'à ce qu'un joueur perde)
#     '''
#     Perdant = []
#     for i in range(100):
#         argent = [1500,1500,1500,1500]
#         Cases_j1 = initS1(Li)
#         Cases_j2 = initS2(Li)
#         Cases_j3 = initS3(Li)
#         Cases_j4 = initS4(Li)
#         case = [Cases_j1, Cases_j2, Cases_j3, Cases_j4]
#         position = [0,0,0,0]
#         # print("argent joueur", argent)
#         # print("case joueur", case)
#         # print("position", position)
#         jeux = jeu(argent, case, position)
#         # print("jeux", jeux)
#         Argent = jeux[0]
#         Perdant.append(perdant(Argent))
#         print("Argent", Argent)
#         Argent = []
#     return Perdant
        
# print(moyenne(Liste))

# def nb_defaites(L):
#     Defaites = [0,0,0,0]
#     for j in range(len(Defaites)):
#         for k in range(len(L)):
#             if L[k] == j:
#                 Defaites[j] += 1
#     return Defaites
#     
# print(nb_defaites(moyenne(Liste)))

def jeufinal(A, C, P):
    '''
    entrée : informations sur les joueurs
    sortie : joueur gagnant à la fin d'une partie, après3 sessions de jeu
    '''
    position1 = P.copy()
    nb_joueurs = 4
    joueurs_en_jeu = [0,1,2,3]
    argent1 = A.copy()
    case1 = deepcopy(C)
    while len(joueurs_en_jeu) != 1 :
        jeu1 = jeu(argent1,case1,position1, joueurs_en_jeu)
        perd = perdant(jeu1[0], joueurs_en_jeu)
        joueurs_en_jeu.pop(perd)
        for i in range(len(case1[perd])) :
            if case1[perd][i] == 0:
                for k in joueurs_en_jeu:
                    case1[k][i] = C[k][i]
                    case1[perd][i] = C[perd][i]
        argent1[perd] = 1    
    return joueurs_en_jeu

print(jeufinal(argent, case, position))

## graphique représentant le nombre de victoires par joueur en fonction du nombre de parties jouées
Lx = [i for i in range(100)]
y = [[jeufinal(argent, case, position)[0] for k in range(i)] for i in Lx]
print(y)
L1 = [y[i].count(0) for i in Lx]
L2 = [y[i].count(1) for i in Lx]
L3 = [y[i].count(2) for i in Lx]
L4 = [y[i].count(3) for i in Lx]
plt.plot(Lx,L1)
plt.plot(Lx,L2)
plt.plot(Lx,L3)
plt.plot(Lx,L4)
plt.show()

## graphique représentant le nombre de défaites par joueur en fonction du nombre de parties jouées
Lx = [i for i in range(100)]
y = [[perdant(jeu(argent,case,position)[0]) for k in range(i)] for i in Lx]
print(y)
L1 = [y[i].count(0) for i in Lx]
L2 = [y[i].count(1) for i in Lx]
L3 = [y[i].count(2) for i in Lx]
L4 = [y[i].count(3) for i in Lx]
plt.plot(Lx,L1)
plt.plot(Lx,L2)
plt.plot(Lx,L3)
plt.plot(Lx,L4)
plt.show()

## graphique représentant le nombre de victoire par joueur en fonction de l'argent de départ
argentnew = [i for i in range(1000, 11000, 1000)]
print(argentnew)
Lx = argentnew
y = [[perdant(jeu([argentnew[i] for k in range(4)],case,position)[0]) for i in range(len(argentnew))]]
print(y)
L1 = [y[i].count(0) for i in Lx]
L2 = [y[i].count(1) for i in Lx]
L3 = [y[i].count(2) for i in Lx]
L4 = [y[i].count(3) for i in Lx]
plt.plot(Lx,L1)
plt.plot(Lx,L2)
plt.plot(Lx,L3)
plt.plot(Lx,L4)
plt.show()









'''
joueur 1 achète petites cases
joueur 2 achete grosses cases
joueur 3 aléatoire
joueur 4 achete tout
variance du nombre de parties gagnées
identifier inversion de tendance en modifiant un paramètre du jeu
regarder argent qui reste au gagnant à la fin
faire représetation graphique 
voir quand le joueur achete les cases en premier
'''
#coallition 

##
from random import random, randint
from copy import deepcopy
import numpy as np
import matplotlib.pyplot as plt
Liste = [200,-60,0,-60,0,0,-100,0,-100,-120,0,-140,0,-140,-160,0,-180,0,-180,-200,0,-220,
0,-220,-240,0,-260,-260,0,-280,0,-300,-300,0,-320,0,0,-350,0,-400]
argent_j1 = argent_j2 = argent_j3 = argent_j4 = 1500
        
def initS1(Li):
    L = []
    for k in Li:
        if k >= -280 and k != 200 :
            L.append(abs(k))
        elif k == 200:
            L.append(k)
        else :
            L.append(0)
    return L        

def initS2(Li):
    L = []
    for k in Li :
        if k < -280:
            L.append(abs(k))
        elif k == 200 :
            L.append(k)
        else :
            L.append(0)
    return L

def initS3(Li):
    L = [0 for k in range(len(Li))]
    L[0] = 200
    for k in range(1,len(Li)):
        if random()<1/2:
            L[k] = -Li[k]
    return L

def initS4(Li):
    L = []
    for k in Li:
        L.append(abs(k))
    return L
    
Cases_j1 = initS1(Liste)
Cases_j2 = initS2(Liste)
Cases_j3 = initS3(Liste)
Cases_j4 = initS4(Liste)

argent = [argent_j1, argent_j2, argent_j3, argent_j4]
case = [Cases_j1, Cases_j2, Cases_j3, Cases_j4]
position = [0,0,0,0]

nb_joueurs = 4

def lancerdede():
    '''Stimule un lancer de dé'''
    return randint(1,6)
    
def acheter(place, numero_joueur, A, C):
    """ entrée : case où se trouve le joueur qui joue
        sortie : la liste joueurs modifiée avec les nouvelles valeurs 
        d'argent et des cases
        fonction permettant au joueur de pouvoir acheter une case si il le peut
    """
    # print("numero_joueur", numero_joueur)
    # print("place",place)
    # position[numero_joueur] = place
    argent1 = A.copy()
    case1 = C.copy()
    n = numero_joueur
    if place != 0 and argent1[n] > case1[n][place] > 0:
        argent1[n] -= case1[n][place]
        case1[n][place] = 0
        for i in range(nb_joueurs):
            if i != n:
                # print(case1[i][place])
                case1[i][place] = Liste[place]/2
    # print("case",case)
    # print("argent", argent)
    # print(" ")
    return argent1, case1
    
def payer (place, numero_joueur, A, C):
    """ entrée : case où se trouve le joueur qui joue
        sortie : la liste joueurs modifiée avec les nouvelles valeurs
        d'argent et des cases
        fonction permettant au joueur de payer au joueur possédant la case
    """ 
    # position[numero_joueur] = place
    n = numero_joueur
    argent1 = A.copy()
    case1 = C.copy()
    argent_perdu = case1[n][place]
    if argent_perdu < 0:
        argent1[n] += argent_perdu
    for i in range(nb_joueurs):
        if i != numero_joueur:
            if case1[i][place] == 0:
                argent1[i] -= argent_perdu
    return argent1,case1
    
def joue_toujours (L):
    L1 = []
    for i in range (4):
        if i in L:
            L1.append(1)
        else:
            L1.append(0)
    return L1
    
        
    
        
# --------------------------------------------------PROGRAMME----------------------------------------------------------------------
  
Case = np.array([[200,-60,0,-60,0,0,-100,0,-100,-120,0],
[-400,50,50,50,50,50,50,50,50,50,-140], 
[0,50,50,50,50,50,50,50,50,50,0], 
[-350,50,50,50,50,50,50,50,50,50,-140], 
[0,50,50,50,50,50,50,50,50,50,-160], 
[0,50,50,50,50,50,50,50,50,50,0], 
[-320,50,50,50,50,50,50,50,50,50,-180], 
[0,50,50,50,50,50,50,50,50,50,0], 
[-300,50,50,50,50,50,50,50,50,50,-180], 
[-300,50,50,50,50,50,50,50,50,50,-200], 
[0,-280,1,-260,-260,1,-240,-220,1,-220,0]])

Plateau = plt.matshow(Case)
plt.colorbar(Plateau)
plt.show()

def elimination(L):
    '''
    entrée : liste L de l'argent des joueurs
    sortie : indice du joueur perdant
    '''
    c = 0
    for i in range(len(L)):
        if L[i] <= 0:
            c += 1
    return c!=0
            
def tour(numero_joueur, A, C, P, LJ):
    '''
    entrée : numero du joueur qui joue, argent des joueurs, cases des joueurs, positions des joueurs
    sortie : valeurs de l'aregnt des joueurs, cases, position à la fin du tour du joueur
    '''
    n = numero_joueur
    position0 = P.copy()
    argent0 = A.copy()
    case0 = deepcopy(C)
    if joue_toujours(LJ)[n] == 1:
        r = lancerdede()
        position0[n] += r #le joueur avance
        if position0[n] > len(Liste)-1 : #si il est au bout
            position0[n] -= len(Liste) #il recommence un tour
            argent0[n] += 200
        argent0,case0 = acheter(position0[n], n, argent0, case0) #soit il achete
        argent0,case0 = payer(position0[n], n, argent0, case0) #soit il paye
    return argent0,case0,position0

def jeu(A, C, P, LJ):
    '''
    entrée : informations sur les joueurs avant de commencer la partie
    Sortie : informations sur les joueurs une fois qu'un des joueurs est éliminé
    Comment ? Un joueur lance un dé, achète la propriété ou non, c'est au joueur suivant qui lance un dé, paye ou achète, etc
    '''
    argent1 = A.copy()
    case1 = deepcopy(C)
    position1 = P.copy()
    k = 0
    while not elimination(argent1) and k != 100: #tant qu'aucun joueur n'est éliminé et que l'on ne fait pas un match nul
        for i in range(nb_joueurs):
            argent1,case1,position1 = tour(i,argent1,case1,position1, LJ)
        k += 1
        # print("tour", k)
    return argent1,case1,P

# print(jeu(argent, case, position))

def jeufinal(A, C, P):
    '''
    entrée : informations sur les joueurs
    sortie : joueur gagnant à la fin d'une partie, après3 sessions de jeu
    '''
    position1 = P.copy()
    nb_joueurs = 4
    joueurs_en_jeu = [0,1,2,3]
    argent1 = A.copy()
    case1 = deepcopy(C)
    while len(joueurs_en_jeu) != 1 :
        jeu1 = jeu(argent1,case1,position1, joueurs_en_jeu)
        perd = perdant(jeu1[0], joueurs_en_jeu)
        joueurs_en_jeu.pop(perd)
        for i in range(len(case1[perd])) :
            if case1[perd][i] == 0:
                for k in joueurs_en_jeu:
                    case1[k][i] = C[k][i]
                    case1[perd][i] = C[perd][i]
        argent1[perd] = 1    
    return joueurs_en_jeu[0]

# print(jeufinal(argent, case, position))

def perdant(L, LJ):
    '''
    entrée : liste d'argent des joueurs 
    sortie : indice dans cette liste du joueur perdant 
    '''
    LJ1 = joue_toujours(LJ)
    for i in range(len(LJ1)):
        if LJ1[i] == 0:
            L.pop(LJ1[i])
    x = min(L)
    return L.index(x)

def moyenne(Li):
    '''
    entrée : liste du jeu de base
    sortie : liste des perdants pour un grand nombre de session de jeu (jusqu'à ce qu'un joueur perde)
    '''
    Perdant = []
    Gagnant = []
    Defaites = [0,0,0,0]
    Victoires = [0,0,0,0]
    for i in range(100):
        argent = [1500,1500,1500,1500]
        Cases_j1 = initS1(Li)
        Cases_j2 = initS2(Li)
        Cases_j3 = initS3(Li)
        Cases_j4 = initS4(Li)
        case = [Cases_j1, Cases_j2, Cases_j3, Cases_j4]
        position = [0,0,0,0]
        # print("argent joueur", argent)
        # print("case joueur", case)
        # print("position", position)
        jeux = jeu(argent, case, position, [0,1,2,3])
        jeuxf = jeufinal(argent, case, position)
        # print("jeux", jeux)
        Argent = jeux[0]
        Perdant.append(perdant(Argent, [0,1,2,3]))
        Gagnant.append(jeuxf)
        # print("Argent", Argent)
        Argent = []
    for j in range(len(Defaites)):
        for k in range(len(Perdant)):
            if Perdant[k] == j:
                Defaites[j] += 1
            if Gagnant[k] == j:
                Victoires[j] += 1
    return Defaites, Victoires
        

    
    
    
    
    
    
    
    
    
    
    
    '''
joueur 1 achète petites cases
joueur 2 achete grosses cases
joueur 3 aléatoire
joueur 4 achete tout
variance du nombre de parties gagnées
identifier inversion de tendance en modifiant un paramètre du jeu
regarder argent qui reste au gagnant à la fin
faire représetation graphique 
voir quand le joueur achete les cases en premier
'''
#coallition 

##

# Bibliothèque

from random import random, randint
from copy import deepcopy
import numpy as np
import matplotlib.pyplot as plt

# Constantes

Liste = [200,-60,0,-60,0,0,-100,0,-100,-120,0,-140,0,-140,-160,0,-180,0,-180,
-200,0,-220,0,-220,-240,0,-260,-260,0,-280,0,-300,-300,0,-320,0,0,-350,0,-400]
argent_j1 = argent_j2 = argent_j3 = argent_j4 = 1500

# Fonctions de base

""" 
La liste des cases d'un joueur représente les cases achetables ou non :
    - elles sont positives si elles sont achetables
    - elles sont nulles si elles sont achetées ou non achetables
    - elles sont négatives si un joueur possède déjà cette case dans ce cas il 
    devra payer à ce joueur
"""
        
def strat_J1(Li):
    """
    entrée : liste Li des cases et leurs valeurs de départ
    sortie : liste L des cases du joueur 1
    Le joueur 1 ne va acheter que les cases les moins chères, elles sont 
    nombreuses
    Fonction créant la liste des cases achetables par le joueur 1
    """
    L = []
    for k in Li:
        if k >= -280 and k != 200 : 
        # ne prend que les cases coutant au plus 280, case départ exclue
            L.append(abs(k))
        elif k == 200:
            L.append(k)
        else :
            L.append(0)  
    return L        

def strat_J2(Li):
    """
    entrée : liste Li des cases et leurs valeurs de départ
    sortie : liste L des cases du joueur 2
    Le joueur 2 ne va acheter que les cases les plus chères, elles sont peu 
    nombreuses
    Fonction créant la liste des cases achetables par le joueur 2
    """
    L = []
    for k in Li :
        if k < -280:    
        # ne prend que les cases coutant plus de 280, case départ exclue
            L.append(abs(k))
        elif k == 200 :
            L.append(k)
        else :
            L.append(0)
    return L

def strat_J3(Li):
    """ 
    entrée : liste Li des cases et leurs valeurs de départ
    sortie : liste L des cases du joueur 3
    Le joueur 3 va acheter les cases de façon aléatoire
    Fonction créant la liste des cases achetables par le joueur 3
    """
    L = [200]   # on initialise avec la case départ
    for k in range(1,len(Li)):
        if random()<1/2:    
        # le joueur a une chance sur deux de choisir d'acheter la case
            L.append(-Li[k])
        else :
            L.append(0)
    return L

def strat_J4(Li):
    """ 
    entrée : liste Li des cases et leurs valeurs de départ
    sortie : liste L des cases du joueur 4
    Le joueur 4 peut acheter toutes les cases
    Fonction créant la liste des cases achetables par le joueur 4
    """
    L = []
    for k in Li:
        L.append(abs(k))
    return L
    
Cases_j1 = strat_J1(Liste)
Cases_j2 = strat_J2(Liste)
Cases_j3 = strat_J3(Liste)
Cases_j4 = strat_J4(Liste)

argent = [argent_j1, argent_j2, argent_j3, argent_j4]
case = [Cases_j1, Cases_j2, Cases_j3, Cases_j4]
position = [0,0,0,0]    
# on initialise les positions des joueurs sur la case départ

nb_joueurs = 4

def lancer_de_de():
    """ Simule un lancer de dé 
    """
    return randint(1,6)
    
def acheter(place, numero_joueur, A, C):
    """
    entrée : case où se trouve le joueur qui joue et les listes A et C 
    respectivement argent et case des joueurs
    sortie : listes argent et case modifiées avec les nouvelles valeurs 
    Fonction permettant au joueur de pouvoir acheter une case s'il a assez 
    d'argent
    """
    argent1 = A.copy()
    case1 = C.copy()
    n = numero_joueur
    if place != 0 and argent1[n] > case1[n][place] > 0:
        # conditions d'achat de la case
        argent1[n] -= case1[n][place]
        case1[n][place] = 0    # la case est achetée
        for i in range(nb_joueurs):
            if i != n:
                case1[i][place] = Liste[place]/2
                # les autres joueurs paieront la moitié du prix initial au 
                # joueur possédant la case
    return argent1, case1
    
def payer (place, numero_joueur, A, C):
    """
    entrée : case (place) où se trouve le joueur qui joue, numéro du joueur qui 
    joue, listes A et C respectivement argent et case des joueurs
    sortie : listes argent et case modifiées avec les nouvelles valeurs
    Fonction permettant au joueur de payer au joueur possédant la case
    """ 
    n = numero_joueur
    argent1 = A.copy()
    case1 = C.copy()
    somme_a_payer = case1[n][place]
    if somme_a_payer < 0:
        argent1[n] += argent_perdu
    for i in range(nb_joueurs):
        if i != n:
            if case1[i][place] == 0:
                argent1[i] -= somme_a_payer
    return argent1,case1
    
def joue_toujours (L):
    """
    entrée : liste L des joueurs encore en jeu
    sortie : liste L1 de tous les joueurs en différenciant ceux qui jouent et 
    ceux qui ne jouent plus
    Fonction différenciant les perdants des joueurs encore en jeu
    """
    L1 = []
    for i in range (4):
        if i in L:
            L1.append(1)    # le joueur i joue toujours
        else:
            L1.append(0)
    return L1
    
def elimination(L):
    """ 
    entrée : liste L de l'argent des joueurs
    sortie : booléen indiquant qu'un des joueurs a perdu
    Fonction donnant la condition d'arrêt du jeu 
    """
    c = 0
    for i in range(len(L)):
        if L[i] <= 0:
            c += 1
    return c!=0
            
def tour(numero_joueur, A, C, P, LJ):
    """
    entrée : numero du joueur qui joue, listes A, C, P respectivement argent,  
    case, position des joueurs, liste LJ des joueurs encore en jeu
    sortie : valeurs de l'argent des joueurs, cases, position à la fin du tour 
    du joueur
    Fonction simulant un tour d'un joueur
    """
    n = numero_joueur
    position0 = P.copy()
    argent0 = A.copy()
    case0 = deepcopy(C)
    if joue_toujours(LJ)[n] == 1:   # si le joueur est encore en jeu
        r = lancer_de_de()
        position0[n] += r      # le joueur avance
        if position0[n] > len(Liste)-1 : # si il est au bout du circuit
            position0[n] -= len(Liste) # il recommence un tour
            argent0[n] += 200
        argent0,case0 = acheter(position0[n], n, argent0, case0) 
        argent0,case0 = payer(position0[n], n, argent0, case0) 
    return argent0,case0,position0

def jeu(A, C, P, LJ):
    """
    entrée : listes A, C, P respectivement argent, case, position des joueurs, 
    liste LJ des joueurs encore en jeu
    sortie : valeurs de l'argent des joueurs, cases, position à la fin du tour 
    du joueur
    Fonction simulant un jeu jusqu'à ce qu'un joueur perde
    """
    argent1 = A.copy()
    case1 = deepcopy(C)
    position1 = P.copy()
    nb_tours = 0
    while not elimination(argent1) and nb_tours != 100: 
    # tant qu'aucun joueur n'est éliminé 
        for i in range(nb_joueurs):
            argent1,case1,position1 = tour(i,argent1,case1,position1, LJ)
        nb_tours += 1
    return argent1,case1,P
    
def perdant(L, LJ):
    """
    entrée : liste L d'argent des joueurs, liste LJ des joueurs en jeu
    sortie : indice du joueur perdant 
    Fonction donnant l'indice du joueur perdant
    """
    joueurs_en_jeu = joue_toujours(LJ)
    for i in range(len(joueurs_en_jeu)):
        if joueurs_en_jeu[i] == 0:
            L.pop(joueurs_en_jeu[i])
    x = min(L)
    return L.index(x)

def jeu_complet(A, C, P):
    """
    entrée : listes A, C, P respectivement argent, case, position des joueurs
    sortie : joueur gagnant à la fin d'une partie, après3 sessions de jeu
    Fonction simulant un jeu complet 
    """
    position1 = P.copy()
    nb_joueurs = 4
    joueurs_en_jeu = [0,1,2,3]
    argent1 = A.copy()
    case1 = deepcopy(C)
    while len(joueurs_en_jeu) != 1 :
        jeu1 = jeu(argent1,case1,position1, joueurs_en_jeu)
        perd = perdant(jeu1[0], joueurs_en_jeu)
        joueurs_en_jeu.pop(perd)
        for i in range(len(case1[perd])) :
            if case1[perd][i] == 0:
                for k in joueurs_en_jeu:
                    case1[k][i] = C[k][i]
                    case1[perd][i] = C[perd][i]
        argent1[perd] = 1    
    return joueurs_en_jeu[0]

def moyenne(Li):
    '''
    entrée : liste du jeu de base
    sortie : liste des perdants pour un grand nombre de session de jeu (jusqu'à ce qu'un joueur perde)
    '''
    Perdant = []
    Gagnant = []
    Defaites = [0,0,0,0]
    Victoires = [0,0,0,0]
    for i in range(100):
        argent = [1500,1500,1500,1500]
        Cases_j1 = initS1(Li)
        Cases_j2 = initS2(Li)
        Cases_j3 = initS3(Li)
        Cases_j4 = initS4(Li)
        case = [Cases_j1, Cases_j2, Cases_j3, Cases_j4]
        position = [0,0,0,0]
        # print("argent joueur", argent)
        # print("case joueur", case)
        # print("position", position)
        jeux = jeu(argent, case, position, [0,1,2,3])
        jeuxf = jeu_complet(argent, case, position)
        # print("jeux", jeux)
        Argent = jeux[0]
        Perdant.append(perdant(Argent, [0,1,2,3]))
        Gagnant.append(jeuxf)
        # print("Argent", Argent)
        Argent = []
    for j in range(len(Defaites)):
        for k in range(len(Perdant)):
            if Perdant[k] == j:
                Defaites[j] += 1
            if Gagnant[k] == j:
                Victoires[j] += 1
    return Defaites, Victoires
        
print(moyenne(Liste))

Case = np.array([[200,-60,0,-60,0,0,-100,0,-100,-120,0],
[-400,50,50,50,50,50,50,50,50,50,-140], 
[0,50,50,50,50,50,50,50,50,50,0], 
[-350,50,50,50,50,50,50,50,50,50,-140], 
[0,50,50,50,50,50,50,50,50,50,-160], 
[0,50,50,50,50,50,50,50,50,50,0], 
[-320,50,50,50,50,50,50,50,50,50,-180], 
[0,50,50,50,50,50,50,50,50,50,0], 
[-300,50,50,50,50,50,50,50,50,50,-180], 
[-300,50,50,50,50,50,50,50,50,50,-200], 
[0,-280,1,-260,-260,1,-240,-220,1,-220,0]])

Plateau = plt.matshow(Case)
plt.colorbar(Plateau)
plt.show()

## graphique représentant le taux de victoires par joueur en fonction du nombre de parties jouées
Lx = [i for i in range(0, 61, 10)]
y = [[jeufinal(argent, case, position) for k in range(i)] for i in range(len(Lx))]
print(y)
L1 = [y[i].count(0)/(i+1) for i in range(len(Lx))]
L2 = [y[i].count(1)/(i+1) for i in range(len(Lx))]
L3 = [y[i].count(2)/(i+1) for i in range(len(Lx))]
L4 = [y[i].count(3)/(i+1) for i in range(len(Lx))]
plt.plot(Lx,L1)
plt.plot(Lx,L2)
plt.plot(Lx,L3)
plt.plot(Lx,L4)
plt.show()

## graphique représentant le nombre de victoire par joueur en fonction de l'argent de départ
largbarre = 0.2

argentnew = [i for i in [150, 1500, 15000]]
y = [[jeufinal([argentnew[i] for k in range(4)],case,position) for k in range(100) ] for i in range(len(argentnew))]
LX = [i for i in range(len(argentnew))]

L1 = [y[i].count(0) for i in LX]
L2 = [y[i].count(1) for i in LX]
L3 = [y[i].count(2) for i in LX]
L4 = [y[i].count(3) for i in LX]
plt.bar([LX[i] - 2*largbarre for i in range(len(LX))], L1, width = largbarre, color = 'pink')
plt.bar([LX[i] - largbarre for i in range(len(LX))], L2, width = largbarre, color = 'blue')
plt.bar(LX, L3, width = largbarre, color = 'green')
plt.bar([LX[i] + largbarre for i in range(len(LX))], L4, width = largbarre, color = 'red')

plt.show()





"""
joueur 1 achète petites cases
joueur 2 achete grosses cases
joueur 3 aléatoire
joueur 4 achete tout
variance du nombre de parties gagnées
identifier inversion de tendance en modifiant un paramètre du jeu
regarder argent qui reste au gagnant à la fin
faire représetation graphique 
voir quand le joueur achete les cases en premier
"""
##

# Bibliothèque

from random import random, randint
from copy import deepcopy
import numpy as np
import matplotlib.pyplot as plt

# Constantes

Liste = [200,-60,0,-60,0,0,-100,0,-100,-120,0,-140,0,-140,-160,0,-180,0,-180,
-200,0,-220,0,-220,-240,0,-260,-260,0,-280,0,-300,-300,0,-320,0,0,-350,0,-400]
argent_j1 = argent_j2 = argent_j3 = argent_j4 = 1500

# Fonctions de base

""" 
La liste des cases d'un joueur représente les cases achetables ou non :
    - elles sont positives si elles sont achetables
    - elles sont nulles si elles sont achetées ou non achetables
    - elles sont négatives si un joueur possède déjà cette case dans ce cas il 
    devra payer à ce joueur
"""
        
def strat_J1(Li):
    """
    entrée : liste Li des cases et leurs valeurs de départ
    sortie : liste L des cases du joueur 1
    Le joueur 1 ne va acheter que les cases les moins chères, elles sont 
    nombreuses
    Fonction créant la liste des cases achetables par le joueur 1
    """
    L = []
    for k in Li:
        if k >= -280 and k != 200 : 
        # ne prend que les cases coutant au plus 280, case départ exclue
            L.append(abs(k))
        elif k == 200:
            L.append(k)
        else :
            L.append(0)  
    return L        

def strat_J2(Li):
    """
    entrée : liste Li des cases et leurs valeurs de départ
    sortie : liste L des cases du joueur 2
    Le joueur 2 ne va acheter que les cases les plus chères, elles sont peu 
    nombreuses
    Fonction créant la liste des cases achetables par le joueur 2
    """
    L = []
    for k in Li :
        if k < -280:    
        # ne prend que les cases coutant plus de 280, case départ exclue
            L.append(abs(k))
        elif k == 200 :
            L.append(k)
        else :
            L.append(0)
    return L

def strat_J3(Li):
    """ 
    entrée : liste Li des cases et leurs valeurs de départ
    sortie : liste L des cases du joueur 3
    Le joueur 3 va acheter les cases de façon aléatoire
    Fonction créant la liste des cases achetables par le joueur 3
    """
    L = [200]   # on initialise avec la case départ
    for k in range(1,len(Li)):
        if random()<1/2:    
        # le joueur a une chance sur deux de choisir d'acheter la case
            L.append(-Li[k])
        else :
            L.append(0)
    return L

def strat_J4(Li):
    """ 
    entrée : liste Li des cases et leurs valeurs de départ
    sortie : liste L des cases du joueur 4
    Le joueur 4 peut acheter toutes les cases
    Fonction créant la liste des cases achetables par le joueur 4
    """
    L = []
    for k in Li:
        L.append(abs(k))
    return L
    
Cases_j1 = strat_J1(Liste)
Cases_j2 = strat_J2(Liste)
Cases_j3 = strat_J3(Liste)
Cases_j4 = strat_J4(Liste)

argent = [argent_j1, argent_j2, argent_j3, argent_j4]
case = [Cases_j1, Cases_j2, Cases_j3, Cases_j4]
position = [0,0,0,0]    
# on initialise les positions des joueurs sur la case départ

nb_joueurs = 4

def lancer_de_de():
    """ Simule un lancer de dé 
    """
    return randint(1,6)
    
def acheter(place, numero_joueur, A, C):
    """
    entrée : case où se trouve le joueur qui joue et les listes A et C 
    respectivement argent et case des joueurs
    sortie : listes argent et case modifiées avec les nouvelles valeurs 
    Fonction permettant au joueur de pouvoir acheter une case s'il a assez 
    d'argent
    """
    argent1 = A.copy()
    case1 = C.copy()
    n = numero_joueur
    if place != 0 and argent1[n] > case1[n][place] > 0:
        # conditions d'achat de la case
        argent1[n] -= case1[n][place]
        case1[n][place] = 0    # la case est achetée
        for i in range(nb_joueurs):
            if i != n:
                case1[i][place] = Liste[place]/2
                # les autres joueurs paieront la moitié du prix initial au 
                # joueur possédant la case
    return argent1, case1
    
def payer (place, numero_joueur, A, C):
    """
    entrée : case (place) où se trouve le joueur qui joue, numéro du joueur qui 
    joue, listes A et C respectivement argent et case des joueurs
    sortie : listes argent et case modifiées avec les nouvelles valeurs
    Fonction permettant au joueur de payer au joueur possédant la case
    """ 
    n = numero_joueur
    argent1 = A.copy()
    case1 = C.copy()
    somme_a_payer = case1[n][place]
    if somme_a_payer < 0:
        argent1[n] += somme_a_payer
    for i in range(nb_joueurs):
        if i != n:
            if case1[i][place] == 0:
                argent1[i] -= somme_a_payer
    return argent1,case1
    
def joue_toujours (L):
    """
    entrée : liste L des joueurs encore en jeu
    sortie : liste L1 de tous les joueurs en différenciant ceux qui jouent et 
    ceux qui ne jouent plus
    Fonction différenciant les perdants des joueurs encore en jeu
    """
    L1 = []
    for i in range (4):
        if i in L:
            L1.append(1)    # le joueur i joue toujours
        else:
            L1.append(0)
    return L1
    
def elimination(L):
    """ 
    entrée : liste L de l'argent des joueurs
    sortie : booléen indiquant qu'un des joueurs a perdu
    Fonction donnant la condition d'arrêt du jeu 
    """
    c = 0
    for i in range(len(L)):
        if L[i] <= 0:
            c += 1
    return c!=0
            
def tour(numero_joueur, A, C, P, LJ):
    """
    entrée : numero du joueur qui joue, listes A, C, P respectivement argent,  
    case, position des joueurs, liste LJ des joueurs encore en jeu
    sortie : valeurs de l'argent des joueurs, cases, position à la fin du tour 
    du joueur
    Fonction simulant un tour d'un joueur
    """
    n = numero_joueur
    position0 = P.copy()
    argent0 = A.copy()
    case0 = deepcopy(C)
    if joue_toujours(LJ)[n] == 1:   # si le joueur est encore en jeu
        r = lancer_de_de()
        position0[n] += r      # le joueur avance
        if position0[n] > len(Liste)-1 : # si il est au bout du circuit
            position0[n] -= len(Liste) # il recommence un tour
            argent0[n] += 200
        argent0,case0 = acheter(position0[n], n, argent0, case0) 
        argent0,case0 = payer(position0[n], n, argent0, case0) 
    return argent0,case0,position0

def jeu(A, C, P, LJ):
    """
    entrée : listes A, C, P respectivement argent, case, position des joueurs, 
    liste LJ des joueurs encore en jeu
    sortie : valeurs de l'argent des joueurs, cases, position à la fin du tour 
    du joueur
    Fonction simulant un jeu jusqu'à ce qu'un joueur perde
    """
    argent1 = A.copy()
    case1 = deepcopy(C)
    position1 = P.copy()
    nb_tours = 0
    while not elimination(argent1) and nb_tours != 100: 
    # tant qu'aucun joueur n'est éliminé 
        for i in range(nb_joueurs):
            argent1,case1,position1 = tour(i,argent1,case1,position1, LJ)
        nb_tours += 1
    return argent1,case1,P
    
def perdant(L, LJ):
    """
    entrée : liste L d'argent des joueurs, liste LJ des joueurs en jeu
    sortie : indice du joueur perdant 
    Fonction donnant l'indice du joueur perdant
    """
    joueurs_en_jeu = joue_toujours(LJ)
    for i in range(len(joueurs_en_jeu)):
        if joueurs_en_jeu[i] == 0:  # le joueur i ne joue plus
            L.pop(joueurs_en_jeu[i])
    x = min(L)
    return L.index(x)

def jeu_complet(A, C, P):
    """
    entrée : listes A, C, P respectivement argent, case, position des joueurs
    sortie : joueur gagnant à la fin d'une partie, après 3 sessions de jeu
    Fonction simulant un jeu complet jusqu'à l'obtention d'un gagnant
    """
    position1 = P.copy()
    nb_joueurs = 4
    joueurs_en_jeu = [0,1,2,3]
    argent1 = A.copy()
    case1 = deepcopy(C)
    while len(joueurs_en_jeu) != 1 :
        jeu1 = jeu(argent1,case1,position1, joueurs_en_jeu)
        perd = perdant(jeu1[0], joueurs_en_jeu)
        joueurs_en_jeu.pop(perd)
        for i in range(len(case1[perd])) :
            if case1[perd][i] == 0:
                for k in joueurs_en_jeu:
                    # on remet les cases en vente comme initialement 
                    case1[k][i] = C[k][i]
                    case1[perd][i] = C[perd][i]
        argent1[perd] = 1    
        # on met l'argent à 1 arbitrairement pour qu'il ne puisse plus acheter 
        # ou payer sans être éliminé
    return joueurs_en_jeu[0]

def moyenne(Li, n, A):
    """
    entrée : liste Li du prix des cases du plateau de base, nombre de parties n 
             pour avoir une moyenne empirique
    sortie : listes Défaites et Victoires respectivement du nombre de défaites 
             et de victoires par joueur 
    Fonction qui permet de constater l'efficacité des différentes stratégies
    """
    Perdant = []
    Gagnant = []
    Defaites = [0,0,0,0]
    Victoires = [0,0,0,0]
    for i in range(n):
        argent = A
        Cases_j1 = strat_J1(Li)
        Cases_j2 = strat_J2(Li)
        Cases_j3 = strat_J3(Li)
        Cases_j4 = strat_J4(Li)
        case = [Cases_j1, Cases_j2, Cases_j3, Cases_j4]
        position = [0,0,0,0]
        jeux = jeu(argent, case, position, [0,1,2,3])
        jeuxf = jeu_complet(argent, case, position)
        Argent = jeux[0]
        Perdant.append(perdant(Argent, [0,1,2,3]))
        Gagnant.append(jeuxf)
        Argent = []     # on réinitialise la liste Argent
    for j in range(len(Defaites)):
        for k in range(len(Perdant)):
            if Perdant[k] == j:
                Defaites[j] += 1
            if Gagnant[k] == j:
                Victoires[j] += 1
    return Defaites, Victoires
        
print(moyenne(Liste, 100, [1500, 1500, 1500, 1500]))

## Représentation du plateau de jeu

Case = np.array([[200,-60,0,-60,0,0,-100,0,-100,-120,0],
[-400,50,50,50,50,50,50,50,50,50,-140], 
[0,50,50,50,50,50,50,50,50,50,0], 
[-350,50,50,50,50,50,50,50,50,50,-140], 
[0,50,50,50,50,50,50,50,50,50,-160], 
[0,50,50,50,50,50,50,50,50,50,0], 
[-320,50,50,50,50,50,50,50,50,50,-180], 
[0,50,50,50,50,50,50,50,50,50,0], 
[-300,50,50,50,50,50,50,50,50,50,-180], 
[-300,50,50,50,50,50,50,50,50,50,-200], 
[0,-280,1,-260,-260,1,-240,-220,1,-220,0]])

Plateau = plt.matshow(Case)
plt.colorbar(Plateau)
plt.show()


## graphique représentant le taux de victoires par joueur en fonction du nombre de parties jouées

Lx = [i for i in range(0, 61, 10)]
y = [[jeu_complet(argent, case, position) for k in range(i)] for i in range(len(Lx))]
print(y)
L1 = [y[i].count(0)/(i+1) for i in range(len(Lx))]
L2 = [y[i].count(1)/(i+1) for i in range(len(Lx))]
L3 = [y[i].count(2)/(i+1) for i in range(len(Lx))]
L4 = [y[i].count(3)/(i+1) for i in range(len(Lx))]
plt.plot(Lx,L1)
plt.plot(Lx,L2)
plt.plot(Lx,L3)
plt.plot(Lx,L4)
plt.show()

## graphique représentant le nombre de victoires par joueur en fonction de l'argent de départ

largbarre = 0.2

var_argent = [150, 1500, 15000]
y = [[jeu_complet([var_argent[i] for j in range(4)],case,position) for k in range(100) ] for i in range(len(var_argent))]
LX = [i for i in range(len(var_argent))]
Argents = ['150', '1500', '15000']
Joueurs = ['joueur 1', 'joueur 2', 'joueur 3', 'joueur 4']

L0 = [y[i].count(0) for i in LX]
L1 = [y[i].count(1) for i in LX] 
L2 = [y[i].count(2) for i in LX]
L3 = [y[i].count(3) for i in LX]
plt.bar([LX[i] - 1.5*largbarre for i in range(len(LX))], L0, width = largbarre, color = 'pink')
plt.bar([LX[i] - 0.5*largbarre for i in range(len(LX))], L1, width = largbarre, color = 'blue')
plt.bar([LX[i] + 0.5*largbarre for i in range(len(LX))], L2, width = largbarre, color = 'green')
plt.bar([LX[i] + 1.5*largbarre for i in range(len(LX))], L3, width = largbarre, color = 'red')

plt.xticks(np.arange(len(Argents)), Argents)
plt.legend(Joueurs, loc=0)
plt.title('Graphique représentant le nombre de victoires en fonction de l'+"'"+'argent de départ')
plt.show()


## graphique représentant le nombre de défaites par joueur en fonction de l'argent de départ

largbarre = 0.2

joueurs_en_jeu = [0,1,2,3]
var_argent = [150, 1500, 15000]
y = [[jeu([var_argent[i] for j in range(4)],case,position, joueurs_en_jeu) for k 
in range(100) ] for i in range(len(var_argent))]
LX = [i for i in range(len(var_argent))]
Argents = ['150', '1500', '15000']
Joueurs = ['joueur 1', 'joueur 2', 'joueur 3', 'joueur 4']

L0 = [y[i].count(0) for i in LX]
L1 = [y[i].count(1) for i in LX] 
L2 = [y[i].count(2) for i in LX]
L3 = [y[i].count(3) for i in LX]
plt.bar([LX[i] - 1.5*largbarre for i in range(len(LX))], L0, width = largbarre, color = 'pink')
plt.bar([LX[i] - 0.5*largbarre for i in range(len(LX))], L1, width = largbarre, color = 'blue')
plt.bar([LX[i] + 0.5*largbarre for i in range(len(LX))], L2, width = largbarre, color = 'green')
plt.bar([LX[i] + 1.5*largbarre for i in range(len(LX))], L3, width = largbarre, color = 'red')

plt.xticks(np.arange(len(Argents)), Argents)
plt.legend(Joueurs, loc=0)
plt.title('Graphique représentant le nombre de défaites en fonction de l'+"'"+'argent de départ')
plt.show()
