# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 09:53:08 2015

@author: uidv7683
"""

import pyparsing as p 


class StatementParser: 
    def __init__ (self): 
        self.statements = []
    
    def addStatement (self, statement):
        statement.setWhitespaceChars(" \t")
        self.statements.append(statement)
        
    def getParser(self): 
        return p.ZeroOrMore( p.Group( p.Or(self.statements) ) )
