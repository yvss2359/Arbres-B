import unittest
from Arbre_B import *
"""
A class that tests the methode "recherche" of the class Arbre_b
authors : Ilyas RACHEDI & Nadine SAADI
"""
class Test_Arbre_Recherche(unittest.TestCase):

    def setUp(self):
        self.tree = Arbre_B(2,4)
        self.tree.racine.add(16)
        self.tree.racine.add(21)


        self.tree.racine.kids.append(Noeud())
        self.tree.racine.kids.append(Noeud())
        self.tree.racine.kids.append(Noeud())

        self.tree.racine.leaf = False
        self.tree.racine.kids[0].values.append(1)
        self.tree.racine.kids[0].values.append(2)
        self.tree.racine.kids[1].values.append(17)
        self.tree.racine.kids[1].values.append(19)
        self.tree.racine.kids[2].values.append(22)
        self.tree.racine.kids[2].values.append(30)
        self.tree.racine.kids[2].leaf = False
        self.tree.racine.kids[2].kids.append(Noeud())
        self.tree.racine.kids[2].kids[0].values.append(50)

    def test_recherche_valeur_existante(self):

        self.assertEqual(self.tree.recherche(self.tree.racine, 16),(True,self.tree.racine))
        self.assertEqual(self.tree.recherche(self.tree.racine, 21),(True,self.tree.racine))
        self.assertEqual(self.tree.recherche(self.tree.racine, 22),(True,self.tree.racine.kids[2]))
        self.assertEqual(self.tree.recherche(self.tree.racine, 19),(True,self.tree.racine.kids[1]))
        self.assertEqual(self.tree.recherche(self.tree.racine, 1),(True,self.tree.racine.kids[0]))
        self.assertEqual(self.tree.recherche(self.tree.racine, 30),(True,self.tree.racine.kids[2]))
        self.assertEqual(self.tree.recherche(self.tree.racine, 50),(True,self.tree.racine.kids[2].kids[0]))

    def test_recherche_valeur_inexistante(self):
        res =  self.tree.recherche(self.tree.racine, 5)
        self.assertEqual( self.tree.recherche(self.tree.racine, 5),(False,res[1]))



if __name__ == "__main__":
    test = Test_Arbre_Recherche()
    test.setUp()
    test.test_recherche_valeur_existante()
    test.test_recherche_valeur_inexistante()
