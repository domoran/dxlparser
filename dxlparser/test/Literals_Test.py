# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 11:32:55 2015

@author: uidv7683
"""

from dxlparser import DXLParser


data = [ i for i in 
r"""
123
0
0x1F
0111
"Hallo"
1.
1.1
1.1E1
"123"
"\"Hall\"o"
"Hallo\r\nDu"
"Hallo\30Du"
"Hallo\030Du"
"\n\t\b\r\f\\\'\"\M"
""".split("\n") if i.strip()]

expected = [
123,
0,
31,
73,
"Hallo",
1.0,
1.1,
11.0, 
"123",
"\"Hall\"o",
"Hallo\r\nDu",
"Hallo" + chr(24) + "Du",
"Hallo" + chr(24) + "Du",
"\n\t\b\r\f\\\'\"M"
]


def process(data, expected):
    print ("Parsing:|"+  data + "|")
    result_array = DXLParser().literal().parseString(data)
    
    assert result_array and len(result_array) == 1
    
    result = result_array[0]
    
    if type(result) != type(expected) or result != expected : 
        print ("Result:", result, type(result), "Expected:", expected, type(expected))
        
    assert  result == expected and  type(result) == type(expected)


def test_literals():
    #for i in print zip(data, expected)    
    #assert False
    for d, e in zip(data, expected):
        yield process, d, e
