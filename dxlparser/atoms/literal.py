# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 18:23:55 2015

@author: admin
"""

import pyparsing as p
import re
    
class Unescape:
    @staticmethod 
    def parse_dxl_string(s, loc, toks):
        # strip the quotes
        unquoted = toks[0][1:-1]

        return Unescape.unescape(unquoted) # escaped_string    
    
    pattern = re.compile(r"\\([0-7]{1,3})|\\(.)|[^\\]+")
    
    escapechars = { 'n': "\n", 
                    't': "\t",                    
                    'b': "\b",                    
                    'r': "\r",
                    'f': "\f",
    }

    @staticmethod 
    def replace(match):
        if match.group(2) is not None:
            return Unescape.escapechars.get(match.group(2), match.group(2))
        elif match.group(1) is not None:
            return chr(int(match.group(1), 8))
        else:
            return match.group(0)


    @staticmethod
    def unescape(data):
        print (Unescape.pattern)
        result = Unescape.pattern.sub(Unescape.replace, data)
        return result
        



def dxlliteral():
    # string literal 
    lit_str = p.Regex(r'"(?:\\"|[^"])+"')
    lit_str.setParseAction(Unescape.parse_dxl_string)
    
    # dezimal literal         
    lit_int_dez = p.Regex("[1-9]+[0-9]*")
    lit_int_dez.setParseAction(lambda s,p,t: int(t[0]))

    # octal literal         
    lit_int_oct = p.Regex("0[0-9]*")
    lit_int_oct.setParseAction(lambda s,p,t: int(t[0],8))
    
    # hexadezimal literal 
    lit_int_hex = p.Regex("0x[0-9a-fA-F]+")
    lit_int_hex.setParseAction(lambda s,p,t: int(t[0],16))
    
    # floating point literal 
    lit_float   = p.Regex("[1-9][0-9]*\\.[0-9]*(?:E[-+]?[1-9][0-9]*)?")  
    lit_float.setParseAction(lambda s,p,t: float(t[0]))
    
    # make sure hex is matched before octal! 
    return lit_str | lit_float | lit_int_hex | lit_int_oct | lit_int_dez 