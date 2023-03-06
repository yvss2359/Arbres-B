import unittest
from Arbre_B import *
"""
A class that tests the methode insertion of the class Arbre_b
authors : Ilyas RACHEDI & Nadine SAADI
"""
class Test_Arbre_Insertion(unittest.TestCase):

    def setUp(self):
        self.tree = Arbre_B(1,3)
        self.n = Noeud()
        self.tree.racine = self.n


    def test_insertion(self):
        self.tree.insertion(self.tree.racine, 10)
        self.assertEqual(self.tree.recherche(self.tree.racine,10), (True,self.tree.noeudRecherche(self.tree.racine,10)))
        self.tree.insertion(self.tree.racine,8)
        self.assertEqual(self.tree.recherche(self.tree.racine,8), (True,self.tree.noeudRecherche(self.tree.racine,8)))
        self.tree.insertion(self.tree.racine,15)
        self.assertEqual(self.tree.recherche(self.tree.racine,15) , (True,self.tree.noeudRecherche(self.tree.racine,15)))
        self.tree.insertion(self.tree.racine, 5)
        self.assertEqual(self.tree.recherche(self.tree.racine, 5),(True, self.tree.noeudRecherche(self.tree.racine, 5)))
        self.tree.insertion(self.tree.racine, 9)
        self.assertEqual(self.tree.recherche(self.tree.racine, 9),(True, self.tree.noeudRecherche(self.tree.racine, 9)))
        self.tree.insertion(self.tree.racine, 7)
        self.assertEqual(self.tree.recherche(self.tree.racine, 7),(True, self.tree.noeudRecherche(self.tree.racine, 7)))
        self.tree.insertion(self.tree.racine, 17)
        self.assertEqual(self.tree.recherche(self.tree.racine, 17),(True, self.tree.noeudRecherche(self.tree.racine, 17)))
        self.tree.insertion(self.tree.racine, 16)
        self.assertEqual(self.tree.recherche(self.tree.racine, 16),(True, self.tree.noeudRecherche(self.tree.racine, 16)))
        self.tree.insertion(self.tree.racine, 13)
        self.assertEqual(self.tree.recherche(self.tree.racine, 13),(True, self.tree.noeudRecherche(self.tree.racine, 13)))
        self.tree.insertion(self.tree.racine, 11)
        self.assertEqual(self.tree.recherche(self.tree.racine, 11),(True, self.tree.noeudRecherche(self.tree.racine, 11)))
        self.tree.insertion(self.tree.racine, 12)
        self.assertEqual(self.tree.recherche(self.tree.racine, 12),(True, self.tree.noeudRecherche(self.tree.racine, 12)))
        self.tree.insertion(self.tree.racine, 14)
        self.assertEqual(self.tree.recherche(self.tree.racine, 14),(True, self.tree.noeudRecherche(self.tree.racine, 14)))
        self.tree.insertion(self.tree.racine, 18)
        self.assertEqual(self.tree.recherche(self.tree.racine, 18),(True, self.tree.noeudRecherche(self.tree.racine, 18)))
        self.tree.insertion(self.tree.racine, 19)
        self.assertEqual(self.tree.recherche(self.tree.racine, 19),(True, self.tree.noeudRecherche(self.tree.racine, 19)))
        self.tree.insertion(self.tree.racine, 15.5)
        self.assertEqual(self.tree.recherche(self.tree.racine, 15.5),(True, self.tree.noeudRecherche(self.tree.racine, 15.5)))
        self.tree.insertion(self.tree.racine, 12.5)
        self.assertEqual(self.tree.recherche(self.tree.racine, 12.5),(True, self.tree.noeudRecherche(self.tree.racine, 12.5)))
        self.tree.insertion(self.tree.racine, 20)
        self.assertEqual(self.tree.recherche(self.tree.racine, 20),(True, self.tree.noeudRecherche(self.tree.racine, 20)))
        self.tree.insertion(self.tree.racine, 21)
        self.assertEqual(self.tree.recherche(self.tree.racine, 21),(True, self.tree.noeudRecherche(self.tree.racine, 21)))



if __name__ == "__main__":
    test = Test_Arbre_Insertion()
    test.setUp()
    test_insertion()
