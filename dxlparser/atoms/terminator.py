# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 09:50:06 2015

@author: uidv7683
"""
import pyparsing as p 

def statement_terminator(): 
    # statements may be terminated by ";" by the end of the line or by the end of the data 
    return p.lineEnd | p.Literal(";") or p.StringEnd()