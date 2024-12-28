import ply.yacc as yacc
# from lexer import tokens  # Assuming tokens are defined in the lexer

# Grammar Rules
def p_program(p):
    '''program : function_list'''
    p[0] = ('program', p[1])

def p_function_list(p):
    '''function_list : function function_list
                      | function'''
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    else:
        p[0] = [p[1]]

def p_function(p):
    '''function : KEYWORD_MAIN LPAREN RPAREN block
                 | IDENTIFIER LPAREN param_list RPAREN block'''
    if p[1] == 'main':
        p[0] = ('main_function', p[4])
    else:
        p[0] = ('function', p[1], p[3], p[5])

def p_param_list(p):
    '''param_list : IDENTIFIER COMMA param_list
                   | IDENTIFIER
                   | empty'''
    if len(p) == 4:
        p[0] = [p[1]] + p[3]
    elif len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = []

def p_block(p):
    '''block : LBRACE statement_list RBRACE'''
    p[0] = p[2]

def p_statement_list(p):
    '''statement_list : statement statement_list
                       | statement'''
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    else:
        p[0] = [p[1]]

def p_statement(p):
    '''statement : assignment SEMICOLON
                 | if_statement
                 | while_statement
                 | return_statement SEMICOLON'''
    p[0] = p[1]

def p_assignment(p):
    '''assignment : IDENTIFIER ASSIGN expression'''
    p[0] = ('assign', p[1], p[3])

def p_if_statement(p):
    '''if_statement : KEYWORD_IF LPAREN expression RPAREN block'''
    p[0] = ('if', p[3], p[5])

def p_while_statement(p):
    '''while_statement : KEYWORD_WHILE LPAREN expression RPAREN block'''
    p[0] = ('while', p[3], p[5])

def p_return_statement(p):
    '''return_statement : KEYWORD_RETURN expression'''
    p[0] = ('return', p[2])

def p_expression(p):
    '''expression : expression PLUS term
                  | expression MINUS term
                  | term'''
    if len(p) == 4:
        p[0] = ('binary_op', p[2], p[1], p[3])
    else:
        p[0] = p[1]

def p_term(p):
    '''term : term TIMES factor
            | term DIVIDE factor
            | factor'''
    if len(p) == 4:
        p[0] = ('binary_op', p[2], p[1], p[3])
    else:
        p[0] = p[1]

def p_factor(p):
    '''factor : NUMBER
              | IDENTIFIER
              | LPAREN expression RPAREN'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

def p_empty(p):
    'empty :'
    p[0] = None

def p_error(p):
    print(f"Syntax error at '{p.value}'")

# Build the parser
parser = yacc.yacc()

# Example usage
if __name__ == "__main__":
    code = """
    main() {
        x = 10;
        if (x > 0) {
            x = x - 1;
        }
        return x;
    }
    """
    result = parser.parse(code)
    print(result)
