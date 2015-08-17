# -*- coding: utf-8 -*-

from dxlparser import DXLPreprocessor

def preprocess(data, expected):
    result = DXLPreprocessor().preprocess(data)
    if not result == expected: 
        print ("Expected: |" + expected + "|\nObserved: |" + result + "|\n")
        
    assert result == expected


testdata = [
    ("", ""), # empty string
    ("Hallo \n", "Hallo \n"), # simple statement 
    ("Hallo // single line Comment\nSecond Line", "Hallo \nSecond Line"), # normal single line comment 
    ("Hallo // single line Comment-\nSecond Line", "Hallo Second Line"),  # single line comment ending with - lf
    ("Hallo // single line Comment-\r\nSecond Line", "Hallo Second Line"), # single line comment ending with - cr lf
    ("Hallo // single line Comment- \r\nSecond Line", "Hallo \nSecond Line"), # single line comment with minus in middle
    ("Multi/*Line*/Comment", "MultiComment"), # multi line comment 1
    ("Multi/*Li/*\nne*/Comment", "MultiComment"), # multi line comment 2
    ("Multi\n/*\nne*/\r\nComment", "Multi\n\r\nComment"), # multi line comment 2

# real code test
("""
int c = 4 /* important */
string s = "some text" //-
"more text"
int d = 5;""", 

"""
int c = 4 
string s = "some text" "more text"
int d = 5;"""
),
    ]


def test_preprocessor(): 
    for data, expected in testdata: 
        yield preprocess, data, expected
    