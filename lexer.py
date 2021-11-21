import ply.lex as lex

#LP asignado : PHP

#palabras reservadas

reserved = {
    'and': 'AND',
    'array': 'ARRAY',
    'break': 'BREAK',
    'class': 'CLASS',
    'continue': 'CONTINUE',
    'echo': 'ECHO',
    'else': 'ELSE',
    'elseif': 'ELSEIF',
    'for': 'FOR',
    'function': 'FUNCTION',
    'if': 'IF',
    'new': 'NEW',
    'or': 'OR',
    'private': 'PRIVATE',
    'protected': 'PROTECTED',
    'return': 'RETURN',
    'public': 'PUBLIC',
    'var': 'VAR',
    'while': 'WHILE',
    'true': 'TRUE',
    'false': 'FALSE',
    'null': 'NULL',
    'object': 'OBJECT',
    'php': "PHP",
    'this': "THIS"
    
}

# List of token names.   This is always required
tokens = ('ENTERO', 'MAS', 'MENOS', 'MULTIPLICACION', 'DIVISION', 'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET','NEGACION', "COMA","ASIGNACION2","PREGUNTA","DOLLAR","NUMERO","DOS_PUNTOS","AUTOINCREMENTO","AUTODECREMENTO","IDENTIFIER","CONCAT_ASIG",
    'FLOTANTE', 'VARIABLE', 'ASIGNACION', 'STRING1','STRING2', 'EQUALS', 'SAME', 'MENORQUE', 'FINAL_DE_LINEA', 'ID',"AMPERSANT","HASHTAG","DOT", "COMILLASIMPLE", "COMILLASDOBLES","ARROW",
          'MAYORQUE', 'DOUBLE','LLLAVE','RLLAVE', 'ASIGNACION_AUMENTADA', 'ASIGNACION_DISMINUIDA', 'DESIGUALDAD', 'MAYORIGUAL', 'MENORIGUAL', 'COMENTARIO') + tuple(reserved.values())

# Regular expression rules for simple tokens
#simbolor matematicos
t_AUTOINCREMENTO = r'\+\+'
t_AUTODECREMENTO = r'--'
t_MAS = r'\+'
t_MENOS = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_ASIGNACION_AUMENTADA = r'\+='
t_ASIGNACION_DISMINUIDA = r'-='

# simpbolos de agrupacion
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LLLAVE = r'\{'
t_RLLAVE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'

#primitivos
#  t_ENTERO = r'\d+'
#  t_FLOTANTE = r'\d+\.\d+'


# ASIGNACION
t_ASIGNACION = r'='
t_ASIGNACION2 = r'=>'
t_CONCAT_ASIG = r'\.='

# comparaciones
t_SAME = '==='  #son iguales y del mismo tipo (el mismo objeto)
t_EQUALS = r'=='  #son iguales
t_DESIGUALDAD = r'!='
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_MAYORQUE = r'>'
t_MENORQUE = r'<'
t_NEGACION = r'!'

# carateres 
t_DOLLAR = r'\$'
t_PREGUNTA = r'\?'
t_AMPERSANT = r'\&'
t_HASHTAG = r'\#'
t_DOT = r'\.'
t_COMA = r','
# t_COMILLASIMPLE = r'\''
# t_COMILLASDOBLES = r'\"'
t_FINAL_DE_LINEA = r';'
t_DOS_PUNTOS = r':'
t_ARROW =r'->'

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
#NUMERO, flotante o entero
def t_NUMERO(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t
#Define una variable
def t_VARIABLE(t):
    r'\$([a-zA-Z]|_)([a-zA-Z]|\d|_)*'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t
#Define una variable
def t_IDENTIFIER(t):
    r'([a-zA-Z]|_)([a-zA-Z]|\d|_)*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t
#Define ID
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# cadena que usa comillas dobles
def t_STRING1(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t

# cadena que usa comillas simples
def t_STRING2(t):
    r'\'([^\\\n]|(\\.))*?\''
    # r'\'([^\'].)*\''
    return t





def t_COMENTARIO(t):
  r'(//.*)|(/\*.*\*/)|(\#.*)'
  t.type = reserved.get(t.value, 'COMENTARIO')
  return t

# Error handling rule
def t_error(t):
    print("No se reconoce el siguiente componente léxico --->'%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test it out
f = open("index.php")
data = ''.join(f.readlines())

if __name__ =="__main__":
# Give the lexer some input
    lexer.input(data)

# Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)
