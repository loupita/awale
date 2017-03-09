# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 11:51:35 2017

@author: Maurelle Gohep
"""
from IA import IA
from Joueur import Joueur
from Plateau import Plateau


class Jeu(object):
    
    
    """
    Classe décrivant les éléments necessaire pour que le jeu puisse se réaliser. 
    """
    
    def __init__(self,joueur1,joueur2, contreIa=False,niveauIa=7):
        
        """
        creation de deux joueurs et d'un plateau de jeu
        """
        self.tour=0
        self.joueur2=Joueur(joueur2,1)
        if contreIa:
            self.joueur1=IA(joueur1,0,niveauIa)
     
        
        else:
            self.joueur1=Joueur(joueur1,0)
        self.plateau=Plateau()
        
        
        
    def clone(self):
    
        clo=Jeu(self.joueur1.clone(),self.joueur2.clone())
        clo.tour=self.tour
        clo.plateau=Plateau(self.plateau)
        return clo
     
    def notation(self,j):
        
        if j==0:
            rep = self.joueur1.nombreCapture-self.joueur2.nombreCapture
           
        else:
            rep = self.joueur2.nombreCapture-self.joueur1.nombreCapture
     
        return  self.plateau.notation(j)+rep*20
    
    def jouerAuto(self):
        j=self.tour%2
        if j==0:
            if self.joueur1.isIA:
                self.joueur1.play(self)
            else:
                rep = input("Jouer entre 0 et 6 ")
                self.jouer(int(rep))
        else:
            if self.joueur2.isIA:
                self.joueur2.play(self)
            else:
                rep = input("Jouer entre 0 et 6 ")
                self.jouer(int(rep)+6)
        
    def jouer(self,i):
        
        """
        cette méthode permet de vérifier si le tour est possible ou pas
        car on est obligé de nourir l'adversaire quand toute ces cases sont vides, au 
        contraire on joue de façon qui nous sera favorable 
        
        j joueur
        i est la case où le jouer commence le jeu et i allant de (0,5)
        nou_i designe la case de l'adversaire, la case où les graines doivent être distribuées 
        """
        j=(self.tour)%2
        if j==0:
            joueur=self.joueur1
            
            nou_i=i
            j2=1
            if self.plateau.cases[nou_i].graines==0:
                print("ce coup n'est pas valide" + str(nou_i) +" "+str(self.tour) +" "+str(j))
               
                return 0
            if self.plateau.verifie(j2)==False:
            
                if i+self.plateau.cases[i].graines>5:
                    #print("le tour est valide")
              
                    self.plateau.jouer(nou_i,joueur)
                    self.tour=self.tour+1
                    #self.plateau.printC()
#                     print(self.tour)
               
                else:
                    print("ce coup n'est pas valide faite jouer l'adversaire")
                    
                  
                  
            else:
                
                
                
                nou_i=i
                self.plateau.jouer(nou_i,joueur)
                self.tour=self.tour+1
                #self.plateau.printC()
            

        else:
            
            joueur=self.joueur2
           
            j2=0
            nou_i=i
            if self.plateau.cases[nou_i].graines==0:
                print("ce coup n'est pas valide 2")
                return 0
            if self.plateau.verifie(j2)==False:
                
                if i+self.plateau.cases[nou_i].graines>5:
                    #print("le tour est valide")
                 
                    self.plateau.jouer(nou_i,joueur)
                    self.tour=self.tour+1
                    #self.plateau.printC()
#                     print(self.tour)
                else:
                    print("ce coup n'est pas valide fait jouer l'adversaire")
  
                    #self.plateau.printC()
#                     print(self.tour)
            else:
                
                self.plateau.jouer(nou_i,joueur)
                self.tour=self.tour+1
                #self.plateau.printC()
                #print(self.tour)
            
                
        self.verify()         
    def printC(self):
        print(self.tour)       
        print(self.joueur1.nom +" : " + str(self.joueur1.nombreCapture) + " | " +self.joueur2.nom +" : " + str(self.joueur2.nombreCapture))
        self.plateau.printC()
        
        
        
        
    def verifiewin(self,j):
        
        
        """
        cette méthode affiche le nom du joueur qui a gagné en donnant la 
        totalité de ces points.
        """

        if j==0:
      
            j2=1
            if  self.joueur1.nombreCapture >=25:
                print("le joueur" + joueur1.nom + "a gagne la partie avec" + self.joueur1.nombreCapture + "points")
                return True
            
            if self.plateau.verifie(j2)==False:
                
                for i in range(0,6):
                    nbAux = self.plateau.cases[i].graines
                    k = i + 1
                    
                    while nbAux > 0:
                        if self.plateau.cases[k].graines != 12:
                            nbAux = nbAux - 1
                      
                        k = k + 1 
                        if k >= 12:
                            k = 0
                    
                    if k == 0:
                        arrive = 11
                    else:
                        arrive = k - 1
                    if arrive >5:
            
                        print("le joueur" + joueur1.nom + "a gagne")
                        return False
                
                return self.joueur1.nombreCapture>=self.joueur2.nombreCapture
            else:
        
                #print("continuer la partie")
                return False
            
        if j==1:
          
            j2=0
            if  self.joueur2.nombreCapture >25:
                print("le joueur" + joueur2.nom + "a gagne la partie avec" + self.joueur2.nombreCapture + "points")
                return True
            
            if self.plateau.verifie(j2)==False:
                
                for i in range(6,12):
                    nbAux = self.plateau.cases[i].graines
                    k = i + 1
                    
                    while nbAux > 0:
                        if self.plateau.cases[k].graines != 12:
                            nbAux = nbAux - 1
                      
                        k = k + 1 
                        if k >= 12:
                            k = 0
                    
                    if k == 0:
                        arrive = 11
                    else:
                        arrive = k - 1
                    if arrive>=0:
            
                        print("le joueur" + joueur2.nom + "a gagne")
                        return False
                return self.joueur2.nombreCapture>=self.joueur1.nombreCapture
            else:
        
                #print("continuer la partie")
                return False
            
        return False           
    def verify(self):
        
        """
        cette méthode permet de vérifier si le jeu est toujours possible
        
        """
        if self.verifiewin(0):
            return True
       
            
        if self.verifiewin(1):
            return True
        
        return False
    def printG(self,myfont,screen): 
        
          
        self.plateau.printCases(myfont, screen)
        
        label = myfont.render(str(self.joueur1.nom)+ " a "+ str(self.joueur1.nombreCapture) + " points", 6, (255,255,255))
        screen.blit(label, ((177, 64)))
        
        label = myfont.render( str(self.joueur2.nom)+ " a "+ str(self.joueur2.nombreCapture) + " points", 6, (255,255,255))
        screen.blit(label, ((177, 630)))
        
    
    def mouseChech(self,i,j):
        print(str(i) + " " +str(j))
        if self.tour%2==0:
            for k in range(6):
                
           
                if self.isInCarre(i,j,110+150+130*k,87+150):
                    self.jouer(k)
        else:           
            for k in range(6):
                
                if self.isInCarre(i,j,110+150+130*k,87+150+170):
                    self.jouer(11-k)
            
            
              
    def isInCarre(self,i,j,x,y):
        h=93
        l=93
        return i>=x and j>=y and i<=x+l and j<=h+y
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#        if  self.plateau.cases[nou_i].graines==0:
#            
#            self.tour=self.tour
#            self.plateau.jouer(nou_i,joueur)
#            print(self.tour)
#            print("vous n'avez plus de graines dans cette cas")
#        else:
#            self.plateau.jouer(nou_i,joueur)
#            self.tour=self.tour+1
#            self.plateau.printC()
#            print(self.tour)
#            
            

        
        
        
        
        
        
        
        
        
        