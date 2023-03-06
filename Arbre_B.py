from Noeud import *
from dicho import *


"""
A class that creates a B-Tree
authors : Nadine SAADI & Ilyas RACHEDI  
"""
class Arbre_B:

    def __init__(self, l, u):
        """
            the constructor of the class Arbre
        """
        self.L = l
        self.U = u
        self.racine = Noeud()


    def recherche(self,node, n):
        """
        search a value n in the node
        param node : (Noeud) the node
        param n : (int) the value to search
        return : (bool,node) (true,Node) if the value found in Node, (false,Node) if the value isn't found and the search stopped in Node

        """
        noeud = node
        res = (False,noeud)
        if dicho(n,node.values):
            res = (True,noeud)
        elif (node.leaf):
            res =  (dicho(n,node.values),noeud)
        else:
            i = 0
            indice=-1
            while(i<node.size and indice==-1):
                if n < node.values[i]:
                    indice=i
                i+=1
           
            if(node.kids[indice] !=None):
               res = self.recherche(node.kids[indice],n)
        return res
    
    
    def noeudRecherche(self,node,n):
        
        return self.recherche(node,n)[1]
    
    def complet(self,node):
        
        if node.size==self.U:
            return True
        else:
            return False
        
        
    def scinder(self,node):
        
        m = (node.size-1)//2

        if node.leaf:
            node.parent.add(node.values[m])
            node.delete(node.values[m])
            nouveauFils=Noeud()
            nouveauFils.parent=node.parent
            node.parent.kids.insert(node.parent.kids.index(node)+1,nouveauFils)

            for i in range(m,node.size):
                nouveauFils.add(node.values[i])
                node.delete(node.values[i])
        
        else:

            nouveauFils=Noeud()
            
            for j in range(m+1,node.size+1):
                nouveauFils.kids.append(node.kids[j])                      

            for j in range(m+1,node.size):
                nouveauFils.add(node.values[j])
                node.delete(node.values[j])
                
            nouveauFils.leaf=False
            node.parent.kids.insert(node.parent.kids.index(node)+1,nouveauFils)
            nouveauFils.parent=node.parent
            node.parent.add(node.values[m])
            node.delete(node.values[m])
            
            while len(node.kids) > node.size+1:
                node.kids.pop()
                                        
            for j in range(nouveauFils.size+1):
                nouveauFils.kids[j].parent=nouveauFils
                
   
   
   
    def insertion(self,node,n):
        """
        insert a value n in the node
        param node:(Noeud) the node
        param n: (int) the value to insert
        return:None
        
        """
        
        debut=self.noeudRecherche(node,n)
        
        if not self.complet(debut):
            debut.add(n)
            
        
        elif self.complet(debut) and debut.parent==None:
       
            m = (debut.size-1)//2
            fg=Noeud()
            fd=Noeud()
            fg.parent=debut
            fd.parent=debut
            debut.leaf=False
            
            debut.kids.append(fg)
            debut.kids.append(fd)
            
            for i in range(0,m):
                fg.add(debut.values[i])
                debut.delete(debut.values[i])
            for j in range(m,debut.size):
                fd.add(debut.values[j])
                debut.delete(debut.values[j])
            
            self.insertion(self.noeudRecherche(node,n),n)
            
        elif self.complet(debut) and debut.parent!=None and not self.complet(debut.parent):
            self.scinder(debut)
            self.insertion(self.noeudRecherche(node,n),n)
            
            
            
        elif self.complet(debut) and debut.parent!=None and self.complet(debut.parent) and debut.parent.parent!=None:
            self.scinder(debut.parent)
            self.insertion(self.noeudRecherche(node,n),n)


            
        elif self.complet(debut) and debut.parent!=None and self.complet(debut.parent):
            
            
            m = (debut.parent.size-1)//2
            
            fg=Noeud()
            fd=Noeud()
            
            for i in range(m):
                fg.kids.append(debut.parent.kids[i])
                fg.kids.append(debut.parent.kids[i+1])
                fg.add(debut.parent.values[i])
                debut.parent.kids[i].parent=fg

            for j in range(m+1,debut.parent.size+1):
                fd.kids.append(debut.parent.kids[j])
                      

            for j in range(m+1,debut.parent.size):
                fd.add(debut.parent.values[j])
                debut.parent.delete(debut.parent.values[j])
                 
            fd.leaf=False
            fg.leaf=False
            
            debut.parent.kids.insert(0,fg)
            debut.parent.kids.insert(1,fd)
            fg.parent=debut.parent
            fd.parent=debut.parent
            
            for i in range(m):
                debut.parent.delete(debut.parent.values[i])
                
            while len(debut.parent.kids) > 2:
                debut.parent.kids.pop()
                                        
            for j in range(fd.size+1):
                fd.kids[j].parent=fd
            
            for i in range(fg.size+1):
                fg.kids[i].parent=fg
                
            self.insertion(self.noeudRecherche(node,n).parent,n)
            
            
    def suppression(self,node,s):
        
        noeud=self.noeudRecherche(node,s)
        
  
        if not noeud.leaf and noeud.kids[0].size>self.L:
            
            noeud.add(noeud.parent.values[0])
            noeud.parent.delete(noeud.parent.values[0])
            noeud.parent.add(noeud.parent.kids[noeud.parent.kids.index(noeud)+1].values[0])
            noeud.parent.kids[noeud.parent.kids.index(noeud)+1].delete(noeud.parent.kids[noeud.parent.kids.index(noeud)+1].values[0])
            noeud.kids.append(noeud.parent.kids[noeud.parent.kids.index(noeud)+1].kids[0])
            noeud.parent.kids[noeud.parent.kids.index(noeud)+1].kids.remove(noeud.parent.kids[noeud.parent.kids.index(noeud)+1].kids[0])
            noeud.parent.kids[noeud.parent.kids.index(noeud)+1].kids[0].parent=noeud
            noeud.delete(s)
            noeud.add(noeud.kids[0].values[noeud.size])
            noeud.kids[0].delete(noeud.kids[0].values[noeud.size-1])
                
                
        elif not noeud.leaf and noeud.kids[0].size==self.L:
            
            noeud.kids[0].add(s)
            noeud.kids[0].add(noeud.kids[1].values[0])
            noeud.delete(s)
            noeud.kids.remove(noeud.kids[1])
            if len(noeud.parent.kids[noeud.parent.kids.index(noeud)+1].values)==0:
                noeud.parent.kids.remove(noeud.parent.kids[noeud.parent.kids.index(noeud)+1])
            noeud.kids[0].delete(s)
            
                    
