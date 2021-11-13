import ply.lex as lex

#LP asignado : PHP

reserved = {
    'if': 'IF',
    'break' : 'BREAK',
    'final': 'FINAL',
    'print': 'PRINT',
    'return': 'RETURN',
    'for': 'FOR'
}

# List of token names.   This is always required
tokens = (
             'NUMBER',
             'MAS',
             'MINUS',
             'TIMES',
             'DIVIDE',
             'LPAREN',
             'RPAREN',
             'FLOTANTE',
             'VARIABLE',
             'STRING',
             'EQUALS',
             'SAME',
             'MENORQUE',
             'MAYORQUE',
             'DOUBLE'
         ) + tuple(reserved.values())

# Regular expression rules for simple tokens
t_MAS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NUMBER = r'\d+'
t_FLOTANTE = r'\d+\.\d+'
t_EQUALS = r'==' #son iguales
t_SAME = '===' #son iguales y del mismo tipo (el mismo objeto)
t_MAYORQUE = r'>'
t_MENORQUE = r'<'

# t_VARIABLE = r'[a-z]+'

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_VARIABLE(t):
    r'[a-zA-Z]+'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

def t_STRING(t):
  r'\'.+\''
  t.type = reserved.get(t.value, 'STRING')
  return t

def t_DOUBLE(t):
  r'(\d+,\d+)+'
  t.type = reserved.get(t.value, 'DOUBLE')
  return t

# Error handling rule
def t_error(t):
    print("Componente léxico no reconocido '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''for i\n a \n 4<5\n 6>8 'esto es un string'
1,2222
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)