# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 13:09:52 2015

@author: uidv7683
"""

import re

"""
    The DXLPreprocessor will currently remove comments from the code and take care
    of the special DXL case of single line comments ending on a '-' which will also include
    the line break in the single line comment. 
""" 
class DXLPreprocessor: 
    def __init__(self): 
        #            string literal    | (multi line comment  | single line comment)
        pattern = r"(\"(?:\\\"|[^\"])*\")|(/\*.*?\*/)|(//[^\r\n]*\r?\n)"
        self.regex = re.compile(pattern, re.MULTILINE | re.DOTALL)

    def replace(self, match):
        # if the 2nd group (capturing comments) is not None,
        # it means we have captured a non-quoted (real) comment string.
        multi_line  = match.group(2)
        single_line = match.group(3)

        if multi_line is not None:
            return ""
        elif single_line is not None:
            if single_line.strip("\r\n")[-1] == '-' or single_line == "": 
                return "" # we eat the newline
            else:
                return "\n" # we keep the newline
        else: 
            # quoted string literal 
            return match.group(1) # captured quoted-string
                
    
    def preprocess (self, data):
        return self.regex.sub(self.replace, data)

