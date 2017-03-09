# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 11:45:44 2017

@author: Maurelle Gohep
"""

class Joueur(object):
    
    """
    Classe decrivant les caractéristiques du joueur, donnant son nom et 
    son camp.
    nombreCapture nous donne le nombre de points du joueur c'est à dire le
        nombre de graine qu'il a gagné.
    """
    
    def __init__(self,nom,camp):
        self.nom=nom
        self.camp=camp
        self.nombreCapture=0
        self.isIA=False
    
    def clone(self):
        clo=Joueur(self.nom,self.camp)
        clo.nombreCapture=self.nombreCapture
        
        return clo
