import ply.lex as lex

#LP asignado : PHP

#palabras reservadas

# Ejecutable: ventana.py

##################
# Viviana Vera: palabras reservadas, se hizo correcciones
##################

#resultado del analisis
resultado = []
errores = []

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
    'while': 'WHILE',
    'true': 'TRUE',
    'false': 'FALSE',
    'php': "PHP",
    'this': "THIS",
    'bool': "BOOL"
    
}

# List of token names.   This is always required
tokens = ( 'MAS', 'MENOS', 'MULTIPLICACION', 'DIVISION', 'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET','NEGACION', "COMA","ASIGNACION2","PREGUNTA", "NUMERO" ,"AUTOINCREMENTO","AUTODECREMENTO","IDENTIFIER","CONCAT_ASIG",
     'VARIABLE', 'ASIGNACION', 'STRING1','STRING2', 'EQUALS', 'SAME', 'MENORQUE', 'FINAL_DE_LINEA', "DOT", "ARROW",
          'MAYORQUE', 'LLLAVE','RLLAVE', 'ASIGNACION_AUMENTADA', 'ASIGNACION_DISMINUIDA', 'DESIGUALDAD', 'MAYORIGUAL', 'MENORIGUAL', 'COMENTARIO', 'NULL') + tuple(reserved.values())

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
#t_ENTERO = r'\d+'
#t_FLOTANTE = r'\d+\.\d+'

t_NULL = r'null'

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
t_PREGUNTA = r'\?'
t_DOT = r'\.'
t_COMA = r','
# t_COMILLASIMPLE = r'\''
# t_COMILLASDOBLES = r'\"'
t_FINAL_DE_LINEA = r';'
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

#Manejo de errores
def t_error(t):
    # con global puedo modificar resultado, una variable
    # que esta fuera del alcance de esta funcion
    global resultado
    advertencia = "No se reconoce el siguiente componente léxico --->'%s'" % t.value[0]
    errores.append(advertencia)
    t.lexer.skip(1)

# Funcion para probar el analizador
def prueba(data):
    #con global puedo modificar resultado, una variable
    #que esta fuera del alcance de esta funcion
    global resultado
    lexer = lex.lex()
    lexer.input(data)
    resultado.clear()
    errores.clear()
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        lectura = str(tok)
        #if lectura.startswith("No"):
        #    errores.append(lectura)
        resultado.append(lectura)
    return resultado

def analisiserrores(data):
    return errores

my_lexer = lex.lex()

f = open("index.php")
data = ''.join(f.readlines())

if __name__ =="__main__":
        prueba(data)
        print(resultado)


