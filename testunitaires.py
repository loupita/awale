'''
Created on 7 mars 2017

@author: Utilisateur
'''
import unittest

from Case import Case
from IA import IA
from Jeu import Jeu
from Joueur import Joueur
from Noeud import Arbre
from Plateau import Plateau


def fonction_a_tester(param1, param2):
    return param1 + param2

class Test(unittest.TestCase):


    def testCase(self,c=None,c2=None):
        if c==None:
            c=Case(4)
        if c2==None:
             
            c2=c.clone()
        assert c.graines == c2.graines 
        
        c.graines=5
        assert c.graines != c2.graines 
        
        
        
    def testJoueur(self, clo=None, clo1=None):
        if clo==None:
            clo=Joueur(" Hollande",0)
        if clo1==None:
            clo1=clo.clone()
             
       
        assert clo1.nombreCapture==clo.nombreCapture
        clo1.nombreCapture=2
        assert clo1.nombreCapture!=clo.nombreCapture
            
    def testJeu(self):
        self.testJeuclone(True)
        self.testJeuclone(False)
        
    def testPlateau(self,p=None,clo1=None): 
        if p==None :
            p=Plateau()
            
        if clo1==None :
 
            clo1=Plateau(p)
        
        
        for i in range(12):
            self.testCase(c=p.cases[i], c2=clo1.cases[i])
    
        
    def testjouerPlateau(self):
        
        
        j=Joueur("Hollande",0)
        for i in range(12):
            p=Plateau()
            p.jouer(i,j)
                
            assert p.cases[i].graines==0
        
        p=Plateau()
        
        p.cases[5].graines=2
         
        p.jouer(2,j) 
        print(p.cases[5].graines) 
        assert p.cases[5].graines==3 
        p=Plateau()
        p.cases[7].graines=2
         
        p.jouer(3,j) 
       
        print(p.cases[7].graines) 
        assert p.cases[7].graines==0
        assert j.nombreCapture==3
        
            
    def testverifiePlateau(self):
        
        p=Plateau()
        
        assert p.verifie(0)
        assert p.verifie(1)
        for i in range(6,12):
            p.cases[i].graines=0
            
        assert not p.verifie(1)
        assert p.verifie(0)
        
    def testnotationPlateau(self):
        p=Plateau()
        
        assert p.notation(0)==0
        assert p.notation(1)==0
        p=Plateau()
        p.cases[2].graines=2
        assert p.notation(1)==2
        assert p.notation(0)==-2
        
  
    def testJeuclone(self,contreIa=False):
    
       
        init=Jeu(" Hollande"," Obama",contreIa)
        
        clo=init.clone()
        
        assert clo.tour == init.tour
     
        self.testJoueur(clo=clo.joueur1, clo1=init.joueur1)
        self.testPlateau(p=clo.plateau,clo1=init.plateau)
        
        
    def testnotationJeu(self):
       
    
       
        init=Jeu("Hollande"," Obama",contreIa=False)
        
        assert init.notation(0)==0
        assert init.notation(1)==0
        init.joueur2.nombreCapture=5
        init.joueur1.nombreCapture=2
        assert init.notation(0)==-60
        assert init.notation(1)==60
      
        init.plateau.cases[2].graines=2
        assert init.notation(0)==-62
        
    def testjouerJeu(self):
        

       
        init=Jeu("Hollande"," Obama",contreIa=False)
        tour=init.tour
        assert init.jouer(3)==None 
        """ il y'a pas d'erreur par consequent on retourne tout simplement None"""
        assert init.tour==tour+1
        assert   init.plateau.cases[3].graines==0
        assert init.jouer(3)==0
        """ on verifie que lorsqu'on joue dans la 3eme case, il y'a plus de plus de graines dans cette dernière """
        
    def testverifiewinJeu(self):
    
        init=Jeu("Hollande","Obama",contreIa=True)
        
        assert  not init.verifiewin(1)
        assert  not init.verifiewin(0)
        assert not  init.verify()
        init.joueur1.nombreCapture=30
        
        assert  init.verifiewin(0)
        assert  not init.verifiewin(1)
        assert init.verify()
     
        
        
        init.joueur1.nombreCapture=3
        init.joueur2.nombreCapture=0
        for i in range(6,12):
        
            init.plateau.cases[i].graines=0
        for i in range(4):   
            init.plateau.cases[i].graines=2
        for i in range(4,6):    
            init.plateau.cases[i].graines=0
        
        assert not init.verifiewin(1)
        assert  init.verifiewin(0)
        assert init.verify()
       
    def testgenererNoued(self) :   
 
        init=Jeu("Hollande","Obama",contreIa=False)
        
        """ soit cet arbre,   
        
        
                                        # 5 #
        
                # 3 #                    # 5 #                     # 1 #
                   
                   
        # 12 #  # 10 #  # 3 #     # 5 #  # 8 #  # 10 #     # 1 #  # 11 #  # 12 #      
        
    
        """    
        """ lorsqu'on utilise l'AlphaBeta"""    
        
        l=[12,10,3,5,8,10,1,11,12]        
        a=Arbre(jeu=init,nb=2,j=0,test=l)
        assert a.noeud.meilleurCoup==1
        assert a.noeud.chiffre==5
        assert a.noeud.valeurMoyenne==3
        assert a.noeud.valeurExteme==1
        
        """ lorsqu'on utilise pas l'AlphaBeta"""
        a2=Arbre(jeu=init,nb=2,j=0,test=l,useAB=False)
        assert a2.noeud.meilleurCoup==1
        assert a2.noeud.chiffre==5
      
        assert a.nbNoeud < a2.nbNoeud
        

        
        jeu=Jeu("Hollande"," Obama",contreIa=False)
        
        a=Arbre(jeu=jeu,nb=4,j=0)
        a.printA()
        
        a1=Arbre(jeu=jeu,nb=4,j=0,useAB=False)
        a1.printA()
        assert a1.noeud.meilleurCoup==a.noeud.meilleurCoup
        assert a1.noeud.chiffre==a.noeud.chiffre
    
      
        assert a.nbNoeud < a1.nbNoeud
        
    def testplayIA(self):
        
        
        
        jeu=Jeu("Hollande"," Obama",contreIa=True)
        tour=jeu.tour
        jeu.joueur1.play(jeu)
        
        assert jeu.tour==tour+1
     
        
  
        
        
        
        
        
        
      
        
        
        
        
        
           
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()