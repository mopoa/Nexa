import ply.lex as lex
import ply.yacc as yacc

# Lexer
# List of token names
tokens = (
    'NUMBER',
    'IDENTIFIER',
    'LBRACE', 'RBRACE',
    'LPAREN', 'RPAREN',
    'SEMICOLON',
    'ASSIGN',
    'COMMA',
    'FUNCTION', 'RETURN',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'COMMENT',
)

# Token regex definitions
t_ignore = ' \t'  # Ignore spaces and tabs
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_ASSIGN = r'='
t_COMMA = r','
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

# Keywords
def t_FUNCTION(t):
    r'function'
    return t

def t_RETURN(t):
    r'return'
    return t

# Comments
def t_COMMENT(t):
    r'//.*'
    pass  # Ignore comments

# Identifiers and numbers
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Newlines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Parser
# Grammar rules

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
    '''function : FUNCTION IDENTIFIER LPAREN param_list RPAREN LBRACE statement_list RBRACE'''
    p[0] = ('function', p[2], p[4], p[7])

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

def p_statement_list(p):
    '''statement_list : statement statement_list
                       | statement'''
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    else:
        p[0] = [p[1]]

def p_statement(p):
    '''statement : RETURN expression SEMICOLON
                 | IDENTIFIER ASSIGN expression SEMICOLON'''
    if len(p) == 4:
        p[0] = ('return', p[2])
    else:
        p[0] = ('assign', p[1], p[3])

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

# Error rule for syntax errors
def p_error(p):
    print(f"Syntax error at '{p.value}'")

# Build the parser
parser = yacc.yacc()

# Example usage
if __name__ == "__main__":
    code = """
    function main() {
        x = 42;
        return x;
    }
    """
    result = parser.parse(code)
    print(result)
