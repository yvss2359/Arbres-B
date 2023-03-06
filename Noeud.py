"""
A class that creates a node ( a branch of the tree)
authors : Ilyas RACHEDI & Nadine SAADI
"""

class Noeud:
    def __init__(self):
        """
        the constructor of a node
        """
        self.leaf = True
        self.values = list()
        self.parent=None
        self.kids = list()
        self.size = 0


    def add(self,cle):
        """
        add a values to the values of the node
        :param cle: (int) the value to add
        :return: None
        """
        self.values.append(cle)
        self.values.sort()
        self.size += 1

    def delete(self,cle):
        """
        delete a value from the values of the node
        :param cle: (int) the value to delete
        :return: None
        """
        self.values.remove(cle)
        self.size -=1

    def get_size(self):
        """
        get the size of the node
        :return: (int) the size of the node
        """
        return self.size
    
    


