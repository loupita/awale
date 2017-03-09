# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 20:54:58 2017

@author: Maurelle Gohep
"""
from os.path import sys


class Noeud():
    
    def __init__(self, chiffre,meilleurCoup,valeurMoyenne,valeurExteme):
        
        """
        elle retourne le chiffre qu'ily'a dans chaque noeud
        """
        
        self.chiffre = chiffre
        self.meilleurCoup=meilleurCoup
        self.valeurMoyenne=valeurMoyenne
        self.valeurExteme=valeurExteme
        
        
        
class Arbre():
    
    """"
    creation d'un arbre qui va schématiser l'ensemble des coups possibles
    creation d'un arbre qui donne tout les cas posssibles
    
    
    """
    def __init__(self, noeud=None, fils=None, jeu=None, nb=None, j=None, test=None,useAB=True):
        
        
        """
        noeud represente les noeuds de l'arbre
        fils represente tout les autres arbres 
        le premier principale est le noeud represente le noeud qui donne à la position actuelle
        """
        self.test=test
        self.nbNoeud = 0
        self.noeud = noeud
        self.fils = fils
        if jeu != None:
            if test!=None:
            
                arb = self.generer(jeu, nb, j, True,None,0,nb,useAB=useAB)
            else:
                arb = self.generer(jeu, nb, j, True,None,useAB=useAB)
            self.noeud = arb.noeud
            self.fils = arb.fils
            self.nbNoeud=arb.nbNoeud
            
            
    def printA(self):    
        listte=[]
        self.printArbre(0, listte)
        for l in listte:
            print(l)            
        
    def printArbre(self,h,liste):  
        if len(liste)<=h:
            liste.append("")
  
        liste[h]=liste[h]+ " # " + str(self.noeud.chiffre) + " " + str(self.noeud.meilleurCoup)+ " " + str(self.noeud.valeurMoyenne)
        for l in self.fils:
            l.printArbre(h+1,liste)

            
            
            
    def generer(self, jeu, nb, j, moidejouer,alphaBeta, test=None, h=None,useAB=True):
        
        """"
        l désigne la liste des fils
        nb nonbre de coup possible
        j designe le joueur
        moidejouer désigne celui qui commence le jeu
        
        
        
        """
       
        if jeu.verifiewin(j):
            
            a= Arbre(noeud=Noeud(10000000,0,0,0), fils=[])
            a.nbNoeud=1
            return a
            
        if j==0:
            j1=1
        else:
            j1=0
        
        if jeu.verifiewin(j1):
            a= Arbre(noeud=Noeud(-10000000,0,0,0), fils=[])
            a.nbNoeud=1
            return a

        
        if nb == 0:
            
            if test!=None:
     
                n = Noeud(self.test[test],0,0,0)
              
                a = Arbre(noeud=n, fils=[])
                a.nbNoeud=1
            else:
                n = Noeud(jeu.notation(j),0,0,0)
                  
                a = Arbre(noeud=n, fils=[])
                a.nbNoeud=1
            return a
        else:
            if test==None:
                if (j == 0 and moidejouer) or (j==1 and not moidejouer):
                    
                    rangee = range(0,6)
                else:
                    rangee = range(6, 12)
            else:
                rangee = range(0,3)
            l = []
            maxx = -1000000000
            minn = 1000000000
            meilleurCoupMin=[]
            meilleurCoupMax=[]
            valeurMoyenne=0
            nbNoeud=0
      
            for i in rangee:
                
                if jeu.plateau.cases[i].graines > 0:
                    
                    if (j == 0 and moidejouer) or (j==1 and not moidejouer):
                        j1 = 1
                        
                    else:
                        j1 = 0
                    
                    passer = False
                    j2 = jeu.clone()
                   
                  
                    if j2.jouer(i)==0:
                        j2.plateau.printC()
                       
                        sys.exit(-1)
                    if test!=None and not j2.plateau.verifie(j1):
                        nbAux = j2.plateau.cases[i].graines
                        
                        if nbAux<6:
                            k = i + 1
                            
                            while nbAux > 0:
                                if j2.plateau.cases[k].graines != 12:
                                    nbAux = nbAux - 1
                              
                                k = k + 1 
                                if k >= 12:
                                    k = 0
                            
                            if k == 0:
                                arrive = 11
                            else:
                                arrive = k - 1
                                
                            if (j1 == 1 and arrive <6) or (j1 == 0 and arrive >= 6):
                                passer = True
                               
                            
                   
                    if not passer:
                      
                        
                        
                        if moidejouer:
                            newalphaBeta=maxx
                        else:
                            newalphaBeta=minn
                        
                        if test!=None:
                           
                              
                               
                            a = self.generer(jeu, nb - 1, j, not moidejouer,newalphaBeta, i+3*(h-nb)*test,h,useAB=useAB)
                        else:
                            
                            a = self.generer(j2, nb - 1, j, not moidejouer,newalphaBeta,useAB=useAB)
                        nbNoeud=nbNoeud+a.nbNoeud
                        val = a.noeud.chiffre
                               
                        
                        valeurMoyenne=valeurMoyenne+val
                    
                        
                        if val > maxx:
                            maxx = val
                            meilleurCoupMax= [[i,a.noeud.valeurMoyenne,a.noeud.valeurExteme]]
                        elif  val == maxx:
                            meilleurCoupMax.append([i,a.noeud.valeurMoyenne,a.noeud.valeurExteme])
                        if val < minn:
                            minn = val
                            meilleurCoupMin=[[i,a.noeud.valeurMoyenne,a.noeud.valeurExteme]]
                        elif  val == minn:
                            meilleurCoupMin.append([i,a.noeud.valeurMoyenne,a.noeud.valeurExteme])
                        
                        l.append(a)
                      
                        if useAB:
                            if alphaBeta!=None:
                                if moidejouer:
                                     
                                    if val>alphaBeta:
                                       
                                   
                                        break
                                else:
                                    if val<alphaBeta:
                                     
                                        break  
                                    
            if len(l)==0:
                jeu.plateau.printC()
                print(j)          
                sys.exit(-1)
                
                
                
                
                a= Arbre(noeud=Noeud(10000000,0,0,0), fils=[])

                return a
        
                    
            valeurMoyenne=valeurMoyenne/len(l)
            
            mmax=0
            bestMoy=-100000000
            mmin=0
            wostMoy=1000000000
            for jaux in meilleurCoupMax:
                moy=jaux[1]
                if moy>bestMoy:
                    bestMoy=moy
                    mmax=jaux[0]
                    
            for jaux in meilleurCoupMin:
                moy=jaux[1]
                
                if moy<wostMoy:
                    wostMoy=moy
                    mmin=jaux[0]
                 

                      
            if moidejouer:

                a = Arbre(noeud=Noeud(maxx,mmax,valeurMoyenne,minn), fils=l)
               
            else:
                a = Arbre(noeud=Noeud(minn,mmin,valeurMoyenne,maxx), fils=l)
          
            a.nbNoeud=nbNoeud
            return a
    
        
