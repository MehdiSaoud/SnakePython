from upemtk import *
from time import sleep
from random import randint


# dimensions du jeu
taille_case = 15
largeur_plateau = 45  # en nombre de cases
hauteur_plateau = 30  # en nombre de cases


def case_vers_pixel(case):
    """
	Fonction recevant les coordonnÃ©es d'une case du plateau sous la 
	forme d'un couple d'entiers (ligne, colonne) et renvoyant les 
	coordonnÃ©es du pixel se trouvant au centre de cette case. Ce calcul 
	prend en compte la taille de chaque case, donnÃ©e par la variable 
	globale taille_case.
    """
    i, j = case
    return (i + .5) * taille_case, (j + .5) * taille_case


def affiche_pommes(pomme):
    x, y = case_vers_pixel(pomme) 

    cercle(x, y, taille_case/2,
           couleur='darkred', remplissage='red')
    rectangle(x-2, y-taille_case*.4, x+2, y-taille_case*.7,
              couleur='darkgreen', remplissage='darkgreen')
              
def deplace_pommes(lst, pomme):
    x = randint(0,44)
    y = randint(0,29)
    z = randint(1,50)
    if lst[0] == pomme :
        pomme = (x, y)
        return pomme
    else :
        return pomme
        
def touche_serpent(lst) :
    i = 1
    while i < len(lst) :
        if lst[0] == lst[i] :
            i = 'perdu'
            return i
        i += 1


def affiche_serpent(lst):
    i = 0
    while i < len(lst) :
        x, y = case_vers_pixel(lst[i])  
        
        cercle(x, y, taille_case/2 + 1,
           couleur='darkgreen', remplissage='green')
        i += 1
        
def affiche_serpent2(lst):
    i = 0
    while i < len(lst) :
        x, y = case_vers_pixel(lst[i])  
        
        cercle(x, y, taille_case/2 + 1,
           couleur='yellow', remplissage='blue')
        i += 1
        
def affiche_serpent3(lst):
    i = 0
    while i < len(lst) :
        x, y = case_vers_pixel(lst[i])  
        
        cercle(x, y, taille_case/2 + 1,
           couleur='red', remplissage='yellow')
        i += 1
        
def grandir_serpent(pomme,lst) :
    if lst[0] == pomme :
        lst.append(lst[0])
        return lst
    else :
        return lst
    
           

           
def change_direction(direction, touche):
    if touche == 'Up':
        return (0, -1)
    elif touche == 'Down':
        return (0, 1)
    elif touche == 'Left':
        return (-1, 0)
    elif touche == 'Right':
        return (1, 0)
    else:
        # pas de changement !
        return direction
        
        
def deplace_serpent(direction, lst) :
    i = len(lst)-1
    if lst[0][0] > 44 or lst[0][0] < 0 or lst[0][1] < 0 or lst[0][1] > 29 :
        return x
    elif direction == (0,-1) :
        if len(lst) > 1 :
            while i > 0 :
                lst[i] = lst[i-1]
                i -= 1
        lst[0] = (lst[0][0] , lst[0][1]-1)
        return lst
    elif direction == (0,1) :
        if len(lst) > 1 :
            while i > 0 :
                lst[i] = lst[i-1]
                i -= 1
        lst[0] = (lst[0][0], lst[0][1]+1)
        return lst
    elif direction == (1,0) :
        if len(lst) > 1 :
            while i > 0 :
                lst[i] = lst[i-1]
                i -= 1
        lst[0] = (lst[0][0]+1, lst[0][1])
        return lst
    elif direction == (-1,0) :
        if len(lst) > 1 :
            while i > 0 :
                lst[i] = lst[i-1]
                i -= 1
        lst[0] = (lst[0][0]-1,lst[0][1])
        return lst
    else :
        return lst
        
def affichage_fenetre0(cpt, largeur_plateau, hauteur_plateau) :
    texte(largeur_plateau//2, hauteur_plateau//2, "                Croquez le fruit défendu" ,couleur='black', ancrage='nw', police='Helvetica', taille=25, tag='')
    
def affichage_fenetre(cpt, largeur_plateau, hauteur_plateau) :
    texte(largeur_plateau//2, hauteur_plateau//2, "Level 1\nScore : "+str(cpt) ,couleur='darkgreen', ancrage='nw', police='Helvetica', taille=15, tag='')
    
def affichage_fenetre2(cpt, largeur_plateau, hauteur_plateau) :
    texte(largeur_plateau//2, hauteur_plateau//2, "Level 2\nScore : "+str(cpt) ,couleur='blue', ancrage='nw', police='Helvetica', taille=15, tag='')
    
def affichage_fenetre3(cpt, largeur_plateau, hauteur_plateau) :
    texte(largeur_plateau//2, hauteur_plateau//2, "Level 3\nScore : "+str(cpt) ,couleur='orange', ancrage='nw', police='Helvetica', taille=15, tag='')


# programme principal
if __name__ == "__main__":

    # initialisation du jeu
    x = 1
    cpt = 0
    cpt2 = 0
    lst = [(22, 13)]
    pomme = (9,13)
    framerate = 12   # taux de rafraÃ®chissement du jeu en images/s
    direction = (0, 0)  # direction initiale du serpent
    cree_fenetre(taille_case * largeur_plateau,
                 taille_case * hauteur_plateau)


    # boucle principale
    while True:
        # affichage des objets
        efface_tout()
        affichage_fenetre0(cpt, largeur_plateau, hauteur_plateau)
        affiche_pommes(pomme)
        affiche_serpent(lst)
        mise_a_jour()

        # gestion des Ã©vÃ©nements'
        ev = donne_evenement()
        ty = type_evenement(ev)
        if ty == 'Quitte':
            break
        elif ty == 'Touche':
            affichage_fenetre0 = affichage_fenetre
            direction = change_direction(direction, touche(ev))
        lst = deplace_serpent(direction, lst)
        if lst == x :
            break
        touche_serpent(lst)
        if touche_serpent(lst) == 'perdu' :
            break
        lst = grandir_serpent(pomme,lst)
        if lst[0] == pomme :
            cpt += 1
            cpt2 += 1
            if cpt2 == 10 :
                framerate += 2
                cpt2 = 0
        if cpt >= 25 :
            affiche_serpent = affiche_serpent2
            affichage_fenetre0 = affichage_fenetre2
        if cpt >= 50 :
            affiche_serpent = affiche_serpent3
            affichage_fenetre0 = affichage_fenetre3
        pomme = deplace_pommes(lst, pomme)
            
        
#Il y a 3 niveau dans le jeu : Le serpent est Vert pour le niveau 1, Bleu pour le niveau 2, et Rouge pour le niveau 3.
#Le jeu s'accèlere toute les 10 pommes mangé

            

        # attente avant rafraÃ®chissement
        sleep(1/framerate)
        
    efface_tout()
    texte(largeur_plateau//2, hauteur_plateau//2, "Perdu ! Nombre de pommes mangées : "+str(cpt) ,couleur='black', ancrage='nw', police='Helvetica', taille=25, tag='')

    # fermeture et sortie
    ferme_fenetre()