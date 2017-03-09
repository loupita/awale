# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 20:50:07 2017

@author: Maurelle Gohep
"""

from Joueur import Joueur
from Noeud import Arbre


class IA(Joueur):
    
    def __init__(self,nom,camp, niveau):
        super(IA,self).__init__(nom,camp)
        self.niveau=niveau
        self.isIA=True
    
    
    def play(self,jeu):
        a=Arbre(jeu=jeu,nb=self.niveau,j=self.camp)
        
        meilleurC=a.noeud.meilleurCoup
        print(str(a.nbNoeud) + " feuills on été calculés. L'Ia a noté la grille à "+ str(a.noeud.chiffre))
        
        jeu.jouer(meilleurC)
        
        