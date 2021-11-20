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
tokens = ('ENTERO', 'MAS', 'MENOS', 'MULTIPLICACION', 'DIVISION', 'LPAREN', 'RPAREN',
          'FLOTANTE', 'VARIABLE', 'ASIGNACION', 'STRING', 'EQUALS', 'SAME', 'MENORQUE', 'FINAL_DE_LINEA',
          'MAYORQUE', 'DOUBLE','LLLAVE','RLLAVE', 'ASIGNACION_AUMENTADA', 'ASIGNACION_DISMINUIDA', 'DESIGUALDAD', 'MAYORIGUAL', 'MENORIGUAL', 'COMENTARIO') + tuple(reserved.values())

# Regular expression rules for simple tokens
t_MAS = r'\+'
t_MENOS = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ENTERO = r'\d+'
t_FLOTANTE = r'\d+\.\d+'
t_FINAL_DE_LINEA = r';'
t_ASIGNACION = r'='
t_ASIGNACION_AUMENTADA = r'\+='
t_ASIGNACION_DISMINUIDA = r'-='
t_EQUALS = r'=='  #son iguales
t_SAME = '==='  #son iguales y del mismo tipo (el mismo objeto)
t_DESIGUALDAD = r'!='
t_MAYORQUE = r'>'
t_MENORQUE = r'<'
t_AND = r'\band\b'
t_OR = r'\bor\b'
t_IF = r'if\b'
t_ELSE = r'else\b'
t_ELSEIF = r'elseif\b'
# t_NEGACION_LOGICA = r'!'
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_LLLAVE = r'\{'
t_RLLAVE = r'\}'


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
    r'("|\').*("|\')'
    t.type = reserved.get(t.value, 'STRING')
    return t

def t_ARRAY(t):
  r'array\((.+,?)\)'
  t.type = reserved.get(t.value, 'STRING')
  return t

def t_DOUBLE(t):
    r'(\d+,\d+)+'
    t.type = reserved.get(t.value, 'DOUBLE')
    return t

def t_WHILE(t):
  r'while\(.+\)'
  t.type = reserved.get(t.value, 'WHILE')
  return t

def t_FOR(t):
  r'for\(.+\)'
  t.type = reserved.get(t.value, 'FOR')
  return t

def t_ECHO(t):
    r'echo .+'
    t.type = reserved.get(t.value, 'ECHO')
    return t


def t_RETURN(t):
    r'return[\s]*.*'
    t.type = reserved.get(t.value, 'RETURN')
    return t

def t_USE(t):
    r'use .+'
    t.type = reserved.get(t.value, 'USE')
    return t

def t_LIST(t):
    r'list\($([a-zA-Z]|_)([a-zA-Z]|\d|_)*,+\)'
    t.type = reserved.get(t.value, 'LIST')
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
