# dxlparser

This might become a complete parser for the Doors Extension Language (DXL) for IBM(R) Rational(R) DOORS(R).

DXL is a C-like domain specific language, that allows Users of IBM(R) Rational(R) DOORS(R) users to customize the product. Unfortunately in difference to C it supports some syntax changes (like functions of one parameter to be callable without parameters, that makes DXL incompatible with common code analysis tools. 

In this project I try to create a complete DOORS DXL Parser using python. The first approach will be to create a parser from scratch using the awesome pyparsing library. If that does not work out, I will probably resort to extracting the original DXL grammar from the DOORS client and reimplement it using the ply (python lex/yacc) library. 
