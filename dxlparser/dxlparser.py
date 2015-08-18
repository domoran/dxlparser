import pyparsing as p

# from .atoms.literal import dxlliteral

def d(x): 
    print ("OH NO: ", x)
    return x


class DXLParser: 
    def parseStatement(self, toks ):
        print ("Parsing Statement:", (toks))


    
    def unknown_statement(self):
        return p.SkipTo(self.statement_terminator())
        
    def statement (self): 
        statements = [
            self.unknown_statement(),
        ];
        
        statement = p.Group( p.Or(statements) )
        
        
        return statement

    
    def __init__(self):        
        self.grammar = 
        
    
    def parse(self, data):
        result = self.grammar.parseString(data)
        return result


if __name__ == "__main__":
    pass