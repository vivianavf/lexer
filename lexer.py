import ply.lex as lex

#LP asignado : PHP

#palabras reservadas

reserved = {
    'and': 'AND',
    'as': 'AS',
    'array': 'ARRAY',
    'break': 'BREAK',
    'class': 'CLASS',
    'continue': 'CONTINUE',
    'declare': 'DECLARE',
    'default': 'DEFAULT',
    'echo': 'ECHO',
    'else': 'ELSE',
    'elseif': 'ELSEIF',
    'for': 'FOR',
    'foreach': 'FOREACH',
    'function': 'FUNCTION',
    'if': 'IF',
    'isset': 'ISSET',
    'list': 'LIST',
    'match': 'MATCH',
    'new': 'NEW',
    'or': 'OR',
    'print': 'PRINT',
    'private': 'PRIVATE',
    'protected': 'PROTECTED',
    'return': 'RETURN',
    'static': 'STATIC',
    'public': 'PUBLIC',
    'unset': 'UNSET',
    'var': 'VAR',
    'while': 'WHILE',
    'true': 'TRUE',
    'false': 'FALSE',
    'null': 'NULL',
    'void': 'VOID',
    'object': 'OBJECT'
    
}

# List of token names.   This is always required
tokens = ('ENTERO', 'MAS', 'MENOS', 'MULTIPLICACION', 'DIVISION', 'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET','NEGACION', "COMA",
          'FLOTANTE', 'VARIABLE', 'ASIGNACION', 'STRING1','STRING2', 'EQUALS', 'SAME', 'MENORQUE', 'FINAL_DE_LINEA', 'ID',"AMPERSANT","HASHTAG","DOT", "COMILLASIMPLE", "COMILLASDOBLES",
          'MAYORQUE', 'DOUBLE','LLLAVE','RLLAVE', 'ASIGNACION_AUMENTADA', 'ASIGNACION_DISMINUIDA', 'DESIGUALDAD', 'MAYORIGUAL', 'MENORIGUAL', 'COMENTARIO') + tuple(reserved.values())

# Regular expression rules for simple tokens
#simbolor matematicos
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
t_RBRACKET = r'\['

#primitivos
t_ENTERO = r'\d+'
t_FLOTANTE = r'\d+\.\d+'

#operadores
t_ASIGNACION = r'='

# comparaciones
t_EQUALS = r'=='  #son iguales
t_SAME = '==='  #son iguales y del mismo tipo (el mismo objeto)
t_DESIGUALDAD = r'!='
t_MAYORQUE = r'>'
t_MENORQUE = r'<'
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='

# carateres 
t_AMPERSANT = r'\&'
t_HASHTAG = r'\#'
t_DOT = r'\.'
t_COMA = r','
t_COMILLASIMPLE = r'\''
t_COMILLASDOBLES = r'\"'
t_FINAL_DE_LINEA = r';'

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#Define una variable
def t_VARIABLE(t):
    r'\$([a-zA-Z]|_)([a-zA-Z]|\d|_)*'
    t.type = reserved.get(t.value, 'VARIABLE')
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
data = '''
$flot = 1.222;
$a = 3;
$b = 2;
$c = $a+$b;
$d = $a-$b;
$cadena = "hola"
$cadena = 'hola/''

if($c>$d){
  echo "la variable a es mayor a b";
}elseif($c===$d){
  echo "la variable a es igual a b";
}else{
  echo "la variable a es menor a b";
}

if ($a == $b and $c == $d){
  echo "a y b son iguales, c y d son iguales"
}
//Varios tipos de creación de arrays
array("foo", "bar", "hello", "world")
array("foo" => "bar", "bar" => "foo", 100   => -100, -100  => 100,)
array(1 => "a", "1" => "b", 1.5 => "c", true => "d")
array("foo" => "bar", "bar" => "foo")
array("a", "b", 6 => "c", "d")
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
