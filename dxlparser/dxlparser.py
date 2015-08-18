import pyparsing as p

# from .atoms.literal import dxlliteral

def d(x): 
    print ("OH NO: ", x)
    return x


class DXLParser: 
    def parseStatement(self, toks ):
        print ("Parsing Statement:", (toks))

    def statement_terminator(self): 
        # statements may be terminated by ";" by the end of the line or by the end of the data 
        return p.lineEnd | p.Literal(";") or p.StringEnd()
    
    def unknown_statement(self):
        return p.SkipTo(self.statement_terminator())
        
    def statement (self): 
        statements = [
            self.unknown_statement(),
        ];
        
        statement = p.Group( p.Or(statements) )
        statement.setWhitespaceChars(" \t")
        
        return statement

    
    def __init__(self):        
        self.grammar = p.ZeroOrMore( self.statement() ); 
        
    
    def parse(self, data):
        result = self.grammar.parseString(data)
        return result


if __name__ == "__main__":
    pass