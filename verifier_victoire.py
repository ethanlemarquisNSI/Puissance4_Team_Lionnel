def verifier_victoire_verticale(grille, numero_joueur, index_ligne, index_colonne):
    a = 0
    b = False
    for i in range(len(grille[index_colonne])):
        if grille[index_colonne][i] == numero_joueur:
            a +=1
            if a == 4:
                b = True
        else:
            a = 0
    return b

def verifier_victoire_horizontale(grille, numero_joueur, index_ligne, index_colonne):
    a = 0
    b = False
    for i in range(len(grille[index_ligne])):
        if grille[index_ligne][i] == numero_joueur:
            a += 1
            if a == 4:
                b = True
        else:
            a = 0
    return b


def verifier_victoire_diagonale(grille, numero_joueur, index_ligne, index_colonne):
    a = 0
    b = False
    i = index_colonne
    j = index_ligne
    while (i <= len(grille[index_colonne]) and j <= len(grille[index_ligne])):
        if grille[j][i] == numero_joueur:
            a += 1
            if a == 4:
                b = True
        else:
            a = 0
        i = i + 1
        j = j + 1
    return b
