from Arbre_B import *
"""
The Main of the methodes insertion the class Arbre-B
"""

if __name__ == "__main__":
    a = Arbre_B(1, 3)
    n = Noeud()

    a.racine = n

    a.insertion(a.racine, 10)
    a.insertion(a.racine, 8)
    a.insertion(a.racine, 15)
    a.insertion(a.racine, 5)
    a.insertion(a.racine, 9)
    a.insertion(a.racine, 7)
    a.insertion(a.racine, 17)
    a.insertion(a.racine, 16)
    a.insertion(a.racine, 13)
    a.insertion(a.racine, 11)
    a.insertion(a.racine, 12)
    a.insertion(a.racine, 7.5)
    a.insertion(a.racine, 9.5)
    a.insertion(a.racine, 9.2)
    a.insertion(a.racine, 7.3)
    a.insertion(a.racine, 7.4)
    a.insertion(a.racine, 5.1)
    a.insertion(a.racine, 5.2)
    a.insertion(a.racine, 9.6)
    a.insertion(a.racine, 9.8)
    a.insertion(a.racine, 8.5)
    a.insertion(a.racine, 8.7)
    a.insertion(a.racine, 14)
    a.insertion(a.racine, 18)
    a.insertion(a.racine, 19)
    a.insertion(a.racine, 15.5)
    a.insertion(a.racine, 12.5)
    a.insertion(a.racine, 20)
    a.insertion(a.racine, 21)





    print("La racine")
    print(n.values)

    print("\n")
    print("les efants du noeud 1 et ses sous enfants ")
    print(n.kids[0].values)
    print(n.kids[0].kids[0].values)
    print(n.kids[0].kids[1].values)
    print(n.kids[0].kids[2].values)
    print(n.kids[0].kids[3].values)

    print("\n")
    print("les efants du noeud 2 et ses sous enfants ")
    print(n.kids[1].values)
    print(n.kids[1].kids[0].values)
    print(n.kids[1].kids[1].values)













