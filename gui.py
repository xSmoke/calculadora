# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

def soma(a,b=None): 
      
     if b == None: 
         b = a 
      
     if is_number(a) and is_number(b): 
         return float(a) + float(b) 
     else: 
        return None 
  
 
def is_number(s): 
      try: 
          float(s) 
          return True 
      except ValueError: 
          return False 
