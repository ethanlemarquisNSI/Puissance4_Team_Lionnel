def Affiche_grille(grille):
    """ fonction permettant d'afficher la grille où la partie de Puissance 4 se déroulera
    """
    for suite in grille:
        for caractere in suite:
            if caractere == 1:
                print("X ", end = " ")
            elif caractere == 2:
                print("O ", end = " ")
            else:
                print(". ", end = " ")
        print()
