from Arbre_B import *
"""
The Main of the methodes recherche the class Arbre-B
"""

if __name__ == "__main__":

    a = Arbre_B(2,7)
    n = Noeud()
    n2 = Noeud()
    n3 = Noeud()

    n.add(5)
    n.add(6)
    n.add(7)
    n.add(8)
    # n.values=[5,6,7,8]

    n2.add(3)
    n2.add(4)
    n2.add(5)
    # n2.values=[2,3,4]
    n.kids=[n2]
    n.leaf=False

    a.racine = n

    print("la valeur 5  est dans l'arbre? : " + str(a.recherche(a.racine,5)))

    n.add(9)
    print("la valeur 9  est dans l'arbre? : " + str(a.recherche(a.racine, 9)))
    n.delete(9)
    print("la valeur 9  est dans l'arbre apres la suppresion ? : " + str(a.recherche(a.racine, 9)))

    print("la valeur 3  est dans l'arbre? : " + str(a.recherche(a.racine, 3)))
    print("la valeur 4  est dans l'arbre? : " + str(a.recherche(a.racine, 4)))

    n3.add(1)
    n3.add(2)
    n2.kids=[n3]
    n2.leaf=False
    print("la valeur 1  est dans l'arbre? : " + str(a.recherche(a.racine, 1)))
