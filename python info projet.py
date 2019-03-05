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
