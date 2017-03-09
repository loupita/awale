# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 12:17:58 2017

@author: Maurelle Gohep
"""



class Case(object):
    
    """
    
    
    """
    def __init__(self,graines):
        self.graines=graines
        
        
    def clone(self):
        
        """
        cette methode retourne le nombre de graine de chaque case
        """
        c=Case(self.graines)
        
        return c
        
        
        
       
        