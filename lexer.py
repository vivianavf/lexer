import ply.lex as lex

#LP asignado : PHP

#palabras reservadas

reserved = {
    'abstract': 'ABSTRACT',
    'and': 'AND',
    'as': 'AS',
    'array': 'ARRAY',
    'break': 'BREAK',
    'case': 'CASE',
    'catch': 'CATCH',
    'class': 'CLASS',
    'clone': 'CLONE',
    'callable': 'CALLABLE',
    'const': 'CONST',
    'continue': 'CONTINUE',
    'declare': 'DECLARE',
    'default': 'DEFAULT',
    'die': 'DIE',
    'do': 'DO',
    'echo': 'ECHO',
    'else': 'ELSE',
    'elseif': 'ELSEIF',
    'empty': 'EMPTY',
    'endswitch': 'ENDSWITCH',
    'endif': 'ENDIF',
    'endforeach': 'ENDFOREACH',
    'endfor': 'ENDFOR',
    'enddeclare': 'ENDDECLARE',
    'eval': 'EVAL',
    'extends': 'ENTENDS',
    'final': 'FINAL',
    'finally': 'FINALLY',
    'for': 'FOR',
    'foreach': 'FOREACH',
    'function': 'FUNCTION',
    'global': 'GLOBAL',
    'goto': 'GOTO',
    'if': 'IF',
    'implements': 'IMPLEMENTS',
    'include': 'INCLUDE',
    'include_once': 'INCLUDE_ONCE',
    'instanceof': 'INSTANCEOF',
    'insteadof': 'INSTEADOF',
    'interface': 'INTERFACE',
    'isset': 'ISSET',
    'list': 'LIST',
    'match': 'MATCH',
    'namespace': 'NAMESPACE',
    'new': 'NEW',
    'or': 'OR',
    'print': 'PRINT',
    'private': 'PRIVATE',
    'protected': 'PROTECTED',
    'require_once': 'REQUIRE_ONCE',
    'return': 'RETURN',
    'static': 'STATIC',
    'require': 'REQUIRE',
    'public': 'PUBLIC',
    'switch': 'SWITCH',
    'throw': 'THROW',
    'trait': 'TRAIT',
    'try': 'TRY',
    'unset': 'UNSET',
    'var': 'VAR',
    'while': 'WHILE',
    'yield': 'YIELD',
    'use': 'USE',
    'yieldfrom': 'YIELDFROM',
    'true': 'TRUE',
    'false': 'FALSE',
    'null': 'NULL',
    'void': 'VOID',
    'iterable': 'ITERABLE',
    'object': 'OBJECT'
}

# List of token names.   This is always required
tokens = ('NUMBER', 'MAS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN',
          'FLOTANTE', 'VARIABLE', 'STRING', 'EQUALS', 'SAME', 'MENORQUE',
          'MAYORQUE', 'DOUBLE') + tuple(reserved.values())

# Regular expression rules for simple tokens
t_MAS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NUMBER = r'\d+'
t_FLOTANTE = r'\d+\.\d+'
t_EQUALS = r'=='  #son iguales
t_SAME = '==='  #son iguales y del mismo tipo (el mismo objeto)
t_MAYORQUE = r'>'
t_MENORQUE = r'<'

# t_VARIABLE = r'[a-z]+'


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


#Define una variable
def t_VARIABLE(t):
    r'\$([a-zA-Z]|_)([a-zA-Z]|\d|_)*'
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
