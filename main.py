# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 11:37:38 2017

@author: Maurelle Gohep
"""
from Jeu import Jeu
from Noeud import Arbre, Noeud
from Plateau import Plateau


if __name__ == "__main__":
    
   
    jeu=Jeu("jeanClaude"," obama",True)
    jeu.printC()
    i=0
    while i==0:
        jeu.jouerAuto()
        jeu.printC()
        
        if jeu.verifiewin(0):
            print(jeu.joueur1.nom +" à gagné")
            i=1
        elif jeu.verifiewin(1):
            print(jeu.joueur2.nom +" à gagné")
            i=1
        print("////////////////////////")
     
#     eurC=a.noeud.meilleurCoup
#     print(str(a.nbNoeud) + " feuills on été calculés. L'Ia a noté la grille à "+ str(a.noeud.chiffre))
#     print(jeu.printC())
#      
#     a.printA()