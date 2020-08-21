

# This file was *autogenerated* from the file gif_maker.sage
from sage.all_cmdline import *   # import sage library

_sage_const_16 = Integer(16); _sage_const_1 = Integer(1); _sage_const_30 = Integer(30); _sage_const_7 = Integer(7)
import os                                                                          
from sage.plot.colors import rainbow                                               
from functions import graphField, plotGraph, rightEdges, dynamics, makeimages, p   
K = GF(_sage_const_16 ,'a', names=('a',)); (a,) = K._first_ngens(1)
f = p([_sage_const_1 ,_sage_const_1 ,_sage_const_1 ])          
elements = [x for x in K]                            
vs = graphField(K).vertices()                        
newelements = []                                     
for i in range(len(elements)):                       
   if str(elements[i]) != vs[i]:                     
       for b in elements:                            
           if str(b) == vs[i]:                       
               newelements.append(b)                 
   else:                                             
       newelements.append(elements[i])               
qs = []                                              
for c in newelements:                                
   qs += _sage_const_30 *[makeimages(K,f,c,figuresize=(_sage_const_7 ,_sage_const_7 ))[-_sage_const_1 ]]  
anim = animate(qs)                                   
anim.ffmpeg(savefile="gifs/[1,1,1]_16.gif")            

