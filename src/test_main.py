import main as M 

def test_somme():
    """
    Fonction de test pour le main.py
    ================================

    Ce script va vérifier que la fonction "somme" de deux nombres (a = 1 ; b = 2) retourne effectivement leur somme (3 dans ce test)

    C'est un exemple pour illustrer cette fonctionalité dans le cadre du Workshop Git
    """
    assert M.somme(1, 2) == 3

test_somme()

