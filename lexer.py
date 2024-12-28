import ply.lex as lex

# List of token names.   This is always required
tokens = (
   'MAIN',
   'USE',
   'IF',
   'WHILE',
   'ELSE',
   'RETURN',
   'INT',
   'BOOL',
   'TRUE',
   'FALSE',
   'IDENTIFIER',
   'INTEGER',
   'EQUALITY',
   'INEQUALITY',
   'LT',
   'LE',
   'GT',
   'GE',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'MOD',
   'AND',
   'OR',
   'NOT',
   'LPAREN',
   'RPAREN',
   'COLON',
   'LBRACE',
   'RBRACE',
   'COMMA',
   'SEMICOLON',
   'ASSIGN',
   'LSQUARE',
   'RSQUARE',
   'COMMENT_SINGLE',
   'COMMENT_MULTI',
)

# Regular expression rules for simple tokens
t_MAIN        = r'main'
t_USE         = r'use'
t_IF          = r'if'
t_WHILE       = r'while'
t_ELSE        = r'else'
t_RETURN      = r'return'
t_INT         = r'int'
t_BOOL        = r'bool'
t_TRUE        = r'true'
t_FALSE       = r'false'
t_EQUALITY    = r'=='
t_INEQUALITY  = r'!='
t_LT          = r'<'
t_LE          = r'<='
t_GT          = r'>'
t_GE          = r'>='
t_PLUS        = r'\+'
t_MINUS       = r'-'
t_TIMES       = r'\*'
t_DIVIDE      = r'/'
t_MOD         = r'%'
t_AND         = r'&'
t_OR          = r'\|'
t_NOT         = r'!'
t_LPAREN      = r'\('
t_RPAREN      = r'\)'
t_COLON       = r':'
t_LBRACE      = r'{'
t_RBRACE      = r'}'
t_COMMA       = r','
t_SEMICOLON   = r';'
t_ASSIGN      = r'='
t_LSQUARE     = r'\['
t_RSQUARE     = r'\]'

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Rule for identifiers
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

# Rule for integers
def t_INTEGER(t):
    r'(-)?[0-9]+'
    return t

# Rule for single-line comments
def t_COMMENT_SINGLE(t):
    r'//.*'
    pass 

# Rule for multi-line comments
def t_COMMENT_MULTI(t):
    r'%%%([^%]|\n|%[^%]|%%[^%])*"%%%'
    pass

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
main() {
  int x = 10;
  if (x > 5) {
    print("x is greater than 5");
  }
}
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)