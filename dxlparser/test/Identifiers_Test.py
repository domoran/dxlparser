# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 21:27:10 2015

@author: admin
"""

from dxlparser.atoms.identifiers import Identifier, DXLIdentifier

from nose.tools import raises
import pyparsing as p 

def retFalse(symbol): 
    return False
    
def retTrue(symbol): 
    return True

@raises( p.ParseException )
def test_valid_identifier_BadSymbol(): 
    I = Identifier("b+", retFalse)
    I.parseString("bbb")
    
@raises( p.ParseException )
def test_invalid_identifier_BadSymbol(): 
    I = Identifier("b+", retFalse)
    I.parseString("a")

def test_valid_identifier_GoodSymbol(): 
    I = Identifier("b+", retTrue)
    I.parseString("bbb")    
   
@raises( p.ParseException )
def test_invalid_identifier_GoodSymbol(): 
    I = Identifier("b+", retTrue)
    I.parseString("a")    

symbols = ['::hallo','a', '0', '__main', '__main__', 'testing123', "::a's"]

badsymbols = ['0', 'abc', 'nosuchSymbol']

I = DXLIdentifier(symbols.__contains__)

def process(symbol):
    I.parseString(symbol)
    assert True

def test_goodSymbols():
    for s in symbols:
        yield process, s

@raises( p.ParseException )   
def test_badSymbols():
    for s in badsymbols:
        yield process, s


if __name__ == "__main__":
    import nose 
    nose.run()
    