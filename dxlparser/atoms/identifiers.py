# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 18:35:02 2015

@author: admin
"""

import pyparsing as p


class Identifier(p.Regex):
    def __init__(self, pattern, checkFunc, fl = 0):
        p.Regex.__init__(self, pattern, flags=fl)
        self.checkFunction = checkFunc
        
    def parseImpl( self, instring, loc, doActions=True ):
        loc,ret = super().parseImpl(instring, loc, doActions)
        
        if ret and len(ret) > 0:
            symb = ret[0]
            if not self.checkFunction(symb):
                raise p.ParseException("Invalid Symbol: " + symb)            
                
        return loc, ret
    
    
        
def DXLIdentifier(checkFunction):
    return Identifier ("(?:::)?[a-zA-Z_][a-zA-Z0-9_']*", checkFunction)
        
        
    
        
    