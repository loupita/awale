from Case import Case
""" 
"""

class Plateau(object):
    
    """
    Classe décrivant le plateau de jeu.  
    """
    
    def __init__(self,autreP=None):
        
        
        
        """
        Créaction des douzes cases du plateau de jeu contenant initialement 4 graines .
        ces cases vont de 0 à 11.
        autreP represente le clônage d'un autre plateau
        """
        if autreP==None:
            
            
            self.cases = []
            for i in range(0, 12):
                c = Case(4)
                self.cases.append(c)
                
                
                
        else:
            self.cases = []
            for c in autreP.cases:
                c2=c.clone()
                self.cases.append(c2)
            
   
        
            
    def printC(self):
        
        """"
        Affiche le nombre de graines restant dans chacune des cases des deux joeurs, de (0 à 6) désignent
        les cases du premier joueur et de (6 à 11) désignent les cases du second joueur.
        self.cases[i].graines designe le nombre de graine restant dans la case i.    
        """
        print()
        strf = ""
        for i in range(0, 6):
            strf = strf + " - " + str(self.cases[5-i].graines)
        print(strf + " - ")  
        strf = ""
        for i in range(0, 6):
            strf = strf + " - " + str(self.cases[i+6].graines)
        print(strf + " - ")
        print()
        
    def jouer(self, i, joueur):
        
        """
        méthode décrivant les cases dans lesquels les graines prisent
        dans une case quelconque doivent être distribuées et on gagne 
        lorsque les graines sont égales à deux ou trois.
        
        
        Paramètre
        ---------------
        i designe le numero de la case que le joueur choisi de prendre 
        les graines.
        joueur designe le nom du joueur.
        j designe les cases où les graines prisent dans la case i doivent
        être distrubuer.
        """
        
        nombreGraine = self.cases[i].graines
        j = i + 1
        if j > 11:
            j = 0
        while nombreGraine > 0:
            if j > 11:
                if self.cases[j - 12].graines < 12:
                    
                    self.cases[j - 12].graines = self.cases[j - 12].graines + 1
                    nombreGraine = nombreGraine - 1
            else:
                if self.cases[j].graines < 12:
                    self.cases[j].graines = self.cases[j].graines + 1
                    nombreGraine = nombreGraine - 1
            
            if nombreGraine == 0:
                continuer = True
                while continuer:
                    
                    if self.cases[j].graines == 2 or self.cases[j].graines == 3:
                        if (joueur.camp == 0 and j > 5) or (joueur.camp == 1 and j <= 5):
                            joueur.nombreCapture = joueur.nombreCapture + self.cases[j].graines
                            self.cases[j].graines = 0
                        else:
                            continuer = False
                    else:
                        continuer = False
                    
                    j = j - 1
                    
                    if j < 0:
                        j = 11
                
            j = j + 1
            if j > 11:
                j = 0
        
        self.cases[i].graines = 0 


          
    def verifie(self,j):
        
        
        """
        cette méthode permet de verifie si un joueur peut jouer ou pas.
        car on vérifie si au moins des cases des joueurs est vide ou pas.
        j désigne le joueur, s'il est égal à 0 c'est le premier joueur au cas 
        contraire c'est le deuxième.
        """
        
#   
    
        if j==0:
           
            reponse=False
            for i in range(0,6):
                if self.cases[i].graines!=0:
                    reponse=True
                
            return reponse        
        else:
           
            reponse=False
            for i in range(6,12):
                if self.cases[i].graines!=0:
                    reponse=True
            return reponse      
                
                
    def notation(self,j):
        
        """"
         
        cette méthode favorise le coup possible, on verifie si en jouant(le joueur 1) tel ou tel coup
        le resultat lui sera favorable et non à l'adversaire et vis versa, ceci se faisant  en calculant
        le nombre de points que ce coup engendrera.
       
        
        si j=0 c'est le joueur 1
        si J=1 c'est le joueur 2
        """

        

        malus=0
        bonus=0

        for i in range(12):
            
            if self.cases[i].graines==2 or self.cases[i].graines==1:
            
                if (j==0 and i in range(6,12)) or (j==1 and i in range(0,6)):
                
                    bonus=bonus+self.cases[i].graines
                else:
                    malus=malus-self.cases[i].graines


        return malus+bonus    
            
    def mouseChech(self,i,j):
        print(i,j)
            
    def printCases(self,myfont,screen):
        
       
     
        for i in range(6):
          
            label = myfont.render(str(self.cases[i].graines), 6, (255,255,255))
            screen.blit(label, (133+150+130*i, 101+150))
            
        for i in range(6):
            
          
            label = myfont.render(str(self.cases[11-i].graines), 6, (255,255,255))
            screen.blit(label, (133+150+130*i, 270.50+150))
                
            
            
            
            
            
        
           
                
                



























