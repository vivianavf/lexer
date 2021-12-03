import ply.lex as lex

import lexer
from lexer import tokens
from lexer import my_lexer
import ply.yacc as yacc

symbols = {}# se usa para validar que simbols existen

#resultado_parser = []
errores_parser = []

def format_parser_tree(str_tree):
    output = ""
    tab_count = 0
    for l in str_tree:
        if l == '(': 
            output +="\n"+"    "*tab_count +"("
            tab_count += 1
        elif l == ')': 
            tab_count -= 1
            output += "    "*tab_count+")\n"
        else: output +=l
    return output

def p_php_code (p):
    'php_code : php_heading statements php_end'
    p[0] = ("php_code" , p[2])
    errores_parser.append(format_parser_tree(str(p[0])))

# php header: todos los programas php empiezan con estos tokens
def p_php_heading (p):
    'php_heading : MENORQUE PREGUNTA PHP'
    pass

# php end: todos los programas php terminan con estos tokens
def p_php_end(p):
    'php_end : PREGUNTA MAYORQUE'
    pass
# statements match every posible php line of code
def p_php_statements_single(p):
    'statements : statement'
    p[0] = ("statements", p[1])
        
# statements match every posible php line of code
def p_php_statements_many(p):
    'statements : statement statements' 
    p[0]= ("statements",p[1],p[2])

    # defincion recursiva statements "statements" es igual a uno o varios "statement"
    pass

# php statement can be, variable declarion, if_statement, for loop, while loop, 
def p_php_statement_0 (p):
    ''' statement : var_declaration
                    | var_modification
                    | if_statement
                    | for_loop
                    | while_lopp
                    | class
                    | comentario
                    | function
                    | function_call
                    | echo_statement
                    | expresion_linea
                    | error_sintax
    '''
    p[0] = ("statement", p[1])
    pass

#######################################################################################################3
# global scope
#######################################################################################################3
def p_var_declaration_base(p):
    'var_declaration : var_dcl FINAL_DE_LINEA'
    p[0] = ("var_declaration",p[1])

def p_var_modification_base(p):
    'var_modification : var_modi FINAL_DE_LINEA'
    p[0] = ("var_modification",p[1])

def p_function_declaration (p):
    'function : func '
    p[0] = ("funcion_definition",p[1])

def p_function_call (p):
    'function_call : func_call FINAL_DE_LINEA'
    p[0] = ("funcion_call",p[1])
def p_echo_statement (p):
    'echo_statement : echo FINAL_DE_LINEA'
    p[0] = ("echo_statement",p[1])
def p_expresion_main (p):
    'expresion_linea : expresion FINAL_DE_LINEA'
    p[0] = ("expresion_linea",p[1])

#######################################################################################################3
# declaracion y modficacion de variable
#######################################################################################################3
######################################
# expresion, everithing that can be stored in a vaiable 
######################################

def p_expresion (p):
    ''' expresion : math_expr 
                    | string
                    | boolean
                    | array
                    | var_accs
                    | func_call
    '''
    p[0] = ("expresion", p[1])
    pass

######################################
# strings aporte de Jorge Vulgarin
######################################
# TODO: faltan metodos de string
# concatenacion de strings

# string_concat es [1 o mas] instancias de (. string | . variable)
def p_string_concats0(p):
    ' string_concats :  string_concat '
    p[0] = ("string_concats ", p[1])
    pass
def p_string_concats1(p):
    ' string_concats : string_concat string_concats '
    p[0] = ("string_concats ", p[1], p[2])
    pass

# match (. <cadnea>)
def p_string_concat2(p):
    ' string_concat :  DOT string  '
    p[0] = ("string_concat ", p[2])
    pass

# match ( . <variable> ) 
def p_string_concat3(p):
    ' string_concat : DOT VARIABLE'
    #TODO: variable debe exisit
    p[0] = ("string_concat ", p[2])

    pass
# match ( . <function>(...args) ) 
def p_string_concat4(p):
    ' string_concat : DOT func_call'
    p[0] = ("string_concat ", p[2])
    pass
def p_string_concat5(p):
    ' string_concat : DOT var_accs'
    p[0] = ("string_concat ", p[2])
    pass

# match strings con "" y con ''
def p_string_1 (p): 
    '''string : STRING1 
                | STRING2
    '''
    p[0] = ("string", p[1])
    pass

# se define como string a un "" seguido por multiples concatenaciones
def p_string_2 (p): 
    ' string : string string_concats'
    p[0] = ("string", p[1],p[2])
    pass

# se define como estring a una variable seguida de multiples concatenaciones
def p_string_3 (p): 
    ' string : VARIABLE string_concats'
    p[0] = ("string", p[1],p[2])
    pass

# asignnar un string a una variable
def p_var_dcl_s (p): 
    'var_dcl : VARIABLE ASIGNACION string '   
    p[0] = ("var_dcl","string", p[1],p[3])
    pass

# concatenacion assigncacion (operador .=)
def p_var_modi_CONCAT (p): 
    'var_modi : VARIABLE CONCAT_ASIG string '
    p[0] = ("self_concat","string", p[1],p[3])
    pass

# concatenacion assigncacion (operador .=)
def p_var_modi_CONCAT2 (p):
    'var_modi : VARIABLE CONCAT_ASIG VARIABLE '
    p[0] = ("self_concat","string", p[1],p[3])
    pass

######################################
# number 
######################################

# match for +-
def p_signo_mas_menos0(p):
    ' signo_mas_menos : MAS MENOS '
    p[0] = ("signo_mas_menos",p[1],p[2])
#mathch for +-+-+-+-...+-
def p_signo_mas_menos1(p):
    ' signo_mas_menos : MAS MENOS signo_mas_menos '
    p[0] = ("signo_mas_menos",p[1],p[2],p[3])
# #mathch for +-+-+-+-...+
# def p_signo_mas_menos2(p):
#     ' signo_mas_menos_mas : signo_mas_menos MAS'

#match for -+
def p_signo_menos_mas (p):
    ' signo_menos_mas : MENOS MAS '
    p[0] = ("signo_menos_mas",p[1],p[2])
#mathch for -+-+-...+
def p_signo_menos_mas1(p):
    ' signo_menos_mas : MENOS MAS signo_menos_mas '
    p[0] = ("signo_menos_mas",p[1],p[2],p[3])
# #mathch for -+-+-+-...-
# def p_signo_menos_mas2(p):
#     ' signo_menos_mas_menos : signo_menos_mas MENOS'


# math con signos para los nuumeros
def p_signo (p) :
    '''signo :    MAS
                | MENOS'''
    p[0] = ("signo", p[1])
    pass
def p_signo1 (p):
    '''signo :    signo_mas_menos
                | signo_menos_mas
    '''
    p[0] = ("signo", p[1])
    pass

def p_math_operator (p):
    ''' math_oper :   MAS
                    | MENOS
                    | MULTIPLICACION
                    | DIVISION
    '''
    p[0] = ("math_oper", p[1])

######################################
# expresiones matermaticas aporte de jorge vulgarin
# componentes sintanticos y semanticos
######################################
#math numeros idividuales
def p_math_expr1 (p):
    'math_expr : NUMERO '
    p[0] = ("math_expr", p[1])
    pass
#math numeros idividuales cons signos
def p_math_expr2 (p):
    'math_expr : signo NUMERO '
    p[0] = ("math_expr",p[1], p[2])
    pass
#math variables idividuales
def p_math_expr3 (p):
    'math_expr : VARIABLE '
    p[0] = ("math_expr",p[1])
    pass
#math vaiables idividuales cons signos
def p_math_expr4 (p):
    'math_expr : signo VARIABLE '
    p[0] = ("math_expr",p[1],p[2])
    pass
def p_math_expr5 (p):
    'math_expr : var_accs '
    p[0] = ("math_expr",p[1])
    pass
#math vaiables idividuales cons signos
def p_math_expr6 (p):
    'math_expr : signo var_accs '
    p[0] = ("math_expr",p[1],p[2])
    pass
def p_math_expr7(p):
    'math_expr : math_expr operaciones_mat'
    p[0] = ("math_expr",p[1],p[2])
    pass

# match (operador con numero) ej. + 125
def p_oper__mat0 (p):
    'operacion_mat : math_oper NUMERO'
    p[0] = ("operacion_mat",p[1],p[2])
    pass
# match (operador con variable) ej. + $uno
def p_oper__mat1 (p): 
    'operacion_mat : math_oper VARIABLE'
    p[0] = ("operacion_mat",p[1],p[2])
    pass
def p_oper__mat2 (p): 
    'operacion_mat : math_oper var_accs'
    p[0] = ("operacion_mat",p[1],p[2])
    pass
def p_oper__mat3 (p):
    'operacion_mat : signo NUMERO'
    p[0] = ("operacion_mat",p[1],p[2])
    pass
# match (operador con variable) ej. + $uno
def p_oper__mat4 (p): 
    'operacion_mat : signo VARIABLE'
    p[0] = ("operacion_mat",p[1],p[2])
    pass
def p_oper__mat5 (p): 
    'operacion_mat : signo var_accs'
    p[0] = ("operacion_mat",p[1],p[2])
    pass
# operaciones, define la lista de operaciones matematicas continuas
def p_operaciones1 (p):
    'operaciones_mat : operacion_mat'
    p[0] = ("operaciones_mat",p[1])
    pass
def p_operaciones2 (p):
    'operaciones_mat : operacion_mat operaciones_mat'
    p[0] = ("operaciones_mat",p[1],p[2])
    pass

def p_var_dcl_n (p):
    'var_dcl : VARIABLE ASIGNACION math_expr '
    p[0] = ("var_dcl","number",p[1],p[3])
    symbols[p[1]] = p[3]
    pass

def p_var_modi1 (p):
    'var_modi : VARIABLE AUTOINCREMENTO '
    p[0] = ("autoincremento",p[1])
    pass
def p_var_modi2 (p):
    'var_modi : VARIABLE AUTODECREMENTO '
    p[0] = ("autodecremento",p[1])
    pass
def p_var_modi3 (p):
    'var_modi : VARIABLE ASIGNACION_AUMENTADA math_expr '
    p[0] = ("asignacion_aumentada",p[1],p[3])
def p_var_modi4 (p):
    'var_modi : VARIABLE ASIGNACION_DISMINUIDA math_expr '
    p[0] = ("asignacion_disminuida",p[1],p[3])
#######################################################################################################3
#  if statement
#######################################################################################################3

# siingle if
def p_if_statement0(p):
    'if_statement : main_if_statement scope '
    p[0] = ("if_statement",p[1],p[2])
# if con else
def p_if_statement1(p):
    'if_statement : main_if_statement scope else scope'
    p[0] = ("if_statement_else",p[1],p[2],p[3],p[4])
# if con elseif
def p_if_statement2(p):
    'if_statement : main_if_statement scope many_elseif'
    p[0] = ("if_statement_elseifs",p[1],p[2],p[3])
#if con elseif con else
def p_if_statement3(p):
    'if_statement : main_if_statement scope many_elseif else scope'
    p[0] = ("if_statement_elseifs_else",p[1],p[2],p[3],p[4],p[5])

# if con elseif con else
def p_many_elseif(p):
    'many_elseif : elseif_statement scope'
    p[0] = ("many_elseifs",p[1],p[2])
    pass
def p_many_elseif1(p):
    'many_elseif : elseif_statement scope many_elseif'
    p[0] = ("many_elseifs",p[1],p[2],p[3])
    pass

######################################
# boolean operations
######################################

# comparaciones que reciben 2 argumentos y retornan booleans
def p_comp_binary_operator (p):
    '''comp_bin_oprs :  MAYORQUE
                        | MENORQUE
                        | MAYORIGUAL
                        | MENORIGUAL
                        | SAME
                        | EQUALS
                        | DESIGUALDAD
                        | AND
                        | OR'''

    p[0] = ("comp_bin_oprs",p[1])
# operaciones que reciben un boolean y retornan otro
def p_bool_unary_oprs(p):
    '''bool_unary_oprs : negacion'''
    p[0] = ("bool_unary_oprs",p[1])

# match !
def p_negacion0 (p):
    'negacion : NEGACION'
    p[0] = ("negacion")

# match !!!! ... !
def p_negacion1 (p):
    'negacion : NEGACION negacion'
    p[0] = ("negacion",p[2])

######################################
# condicion, aka. boolean, 
######################################
def p_boolean_constant (p):
    '''boolean : TRUE
                | FALSE'''
    p[0] = ("boolean", p[1])

def p_boolean0 (p):
    'boolean : expresion comp_bin_oprs expresion'
    p[0] = ("binary_comp", p[1], p[2],p[3])
def p_boolean1 (p):
    'boolean : bool_unary_oprs boolean'
    p[0] = ("bool_unary_operation", p[1], p[2])
# def p_boolean2 (p): 
#     'boolen : LPAREN bolean RPAREN'

######################################
# main_if statement
######################################
def p_main_if_statement (p):
    'main_if_statement : IF LPAREN boolean RPAREN '
    p[0] = ("main_if_statement",p[3])
    pass

######################################
# elseif
######################################
def p_elseif_statement (p):
    ' elseif_statement : ELSEIF LPAREN boolean RPAREN'
    p[0] = ("elseif_statement",p[3])
######################################
# else
######################################
def p_else_statement (p):
    ' else : ELSE'
######################################
# scope, codigo dentre de {}, puede ser el cuerp de una funcion o de un if , etc
######################################
def p_scope_base (p):
    'scope : LLLAVE statements RLLAVE'
    p[0] = ("scope",p[2])
def p_scope_empty (p):
    'scope : LLLAVE RLLAVE'
    p[0] = ("empty_scope")

def p_scope_break (p):
    'scope : LLLAVE statements BREAK FINAL_DE_LINEA RLLAVE'
    p[0] = ("break_scope",p[2])
def p_scope_just_break (p):
    'scope : LLLAVE BREAK FINAL_DE_LINEA RLLAVE'
    p[0] = ("break_scope_empty")

def p_scope_continue (p):
    'scope : LLLAVE statements CONTINUE FINAL_DE_LINEA RLLAVE'
    p[0] = ("continue_scope", p[2])
def p_scope_just_continue (p):
    'scope : LLLAVE CONTINUE FINAL_DE_LINEA RLLAVE'
    p[0] = ("continue_scope_empty")

def p_scope_return (p):
    'scope : LLLAVE statements return FINAL_DE_LINEA RLLAVE'
    p[0] = ("return_scope", p[2],p[3])
def p_scope_just_return (p):
    'scope : LLLAVE return FINAL_DE_LINEA RLLAVE'
    p[0] = ("return_scope_empty",p[2])
######################################
# return
######################################
def p_return_void (p):
    ' return : RETURN'
    p[0] = ("void_return")
def p_return_value (p):
    ' return : RETURN expresion'
    p[0] = ("resturn",p[1])

#######################################################################################################3
# while loop
#######################################################################################################3

def p_while_loop (p):
    'while_lopp : WHILE LPAREN boolean RPAREN scope'
    p[0] = ("while_lopp", p[3],p[5])

#######################################################################################################3
# for loop
#######################################################################################################3
def p_for_loop (p):
    'for_loop : FOR LPAREN var_dcl FINAL_DE_LINEA boolean FINAL_DE_LINEA var_modi RPAREN scope'
    p[0] = ("for_loop", p[3],p[5],p[7], p[9])

#######################################################################################################3
# array, contribucion de jorge Vugarin
# semantica de arrays, Viviana Vera
#######################################################################################################

def p_array_clave(p):
  """array_clave : string  
                  | boolean 
                  | math_expr
                     """
  p[0] = ("array_clave", p[1])
def p_array_elemento(p):
  """array_elemento : math_expr
                    | string
                    | boolean
                    | array
                    | NULL"""
  p[0] = ("array_elemento", p[1])

def p_asignacionArrow(p):
    ' asignacionArrow : array_clave ASIGNACION2 array_elemento'
    p[0] = ("asignacionArrow", p[1],p[3])

def p_arrayItem (p):
    ''' array_item : asignacionArrow 
                    | array_elemento'''
    p[0] = ("array_item", p[1])


def p_arrayItems_single (p):
    ' array_items : array_item '
    p[0] = ("array_items", p[1])
def p_arrayItems (p):
    ' array_items : array_item COMA array_items'
    p[0] = ("array_items", p[1],p[2])

def p_array(p):
    ' array : ARRAY LPAREN array_items RPAREN'
    p[0] = ("array", p[1])

def p_array_declaration(p):
    'var_dcl : VARIABLE ASIGNACION array'
    p[0] = ("var_dcl", p[1],p[3])
def p_cast_to_array (p):
    'array : LPAREN ARRAY RPAREN VARIABLE'
    p[0] = ("casting_to_array",p[4])

######################################
# indexing
######################################
def p_array_indexing(p):
    ' var_accs : VARIABLE LBRACKET array_clave RBRACKET'
    p[0] = ("indexing",p[1],p[3])
    
# def p_copy_array_element (p):
#     ' var_accs : indexing'
#######################################################################################################3
# booleans, contribucion de Adriana Guilindro
#######################################################################################################3
#asignar el valor de false a una variable
def p_boolean_false(p):
    ' var_dcl : VARIABLE ASIGNACION FALSE'
    p[0] = ("var_dcl","bool",p[1], p[3])
#asignar el valor de true a una variable
def p_boolean_true(p):
    ' var_dcl : VARIABLE ASIGNACION TRUE'
    p[0] = ("var_dcl","bool",p[1], p[3])
#conversion de una variable a booleano
def p_boolean_conv(p):
    ' boolean : LPAREN BOOL RPAREN expresion'
    p[0] = ("casting",p[1], p[3])

#######################################################################################################3
# functions
#######################################################################################################3
# arguments for a function definition
def p_arguments_single (p):
    'arguments : VARIABLE'
    p[0]=("arguments",p[1])
def p_arguments_many (p):
    'arguments : VARIABLE COMA arguments'
    p[0]=("arguments",p[1],p[3])
def p_fn_no_args (p):
    'args : LPAREN RPAREN'
    p[0]=("no_arguments")
def p_fn_args (p):
    'args : LPAREN arguments RPAREN'
    p[0]=("args",p[2])

# function argument values list, for a function call
def p_fun_argument_value (p):
    ' value : expresion'
    p[0] = ("value", p[1])
def p_func_argument_values_single (p):
    ' values : value'
    p[0] = ("values", p[1])
def p_func_argument_values_many (p):
    ' values :  value COMA values'
    p[0] = ("values", p[1],p[3])

# defincion de una funcion
def p_func(p):
    ' func : FUNCTION IDENTIFIER args scope'
    p[0] = ("function", p[2],p[3],p[4])

# definition de una llamada a una funcion
def p_func_call_no_arguments (p):
    ' func_call : IDENTIFIER LPAREN RPAREN'
    p[0] = ("function_call_no_arguments", p[1])
def p_func_call_with_arguments (p):
    ' func_call : IDENTIFIER LPAREN values RPAREN '
    p[0] = ("function_call", p[1],p[3])

#######################################################################################################3
# clas, contribucion de Jorge Vulgarin
#######################################################################################################3
######################################
# self reference, using "this->"
######################################
def p_self_ref(p):
    ' var_modi : THIS ARROW IDENTIFIER ASIGNACION expresion'
    p[0] = ("internal_member_modification",p[3],p[5])
def p_member_modification(p):
    ' var_modi : VARIABLE ARROW IDENTIFIER ASIGNACION expresion'
    p[0] = ("external_member_modification",p[1],p[3],p[5])
def p_member_access(p):
    ' var_accs : VARIABLE ARROW IDENTIFIER '
    p[0] = ("read_member", p[1],p[3])
def p_member_copy(p):
    ' var_dcl : VARIABLE ASIGNACION var_accs'
    p[0] = ("copy_resource", p[1],p[3])
def p_member_func_call(p):
    ' func_call : VARIABLE ARROW func_call'
    p[0] = ("member_function_call", p[1],p[3])
def p_var_modif_acso (p):
    ''' modf_acso : PUBLIC 
                    | PRIVATE
                    | PROTECTED
    '''
    p[0] = ("modificador_acceso", p[1])
def p_class (p):
    ' class : CLASS IDENTIFIER LLLAVE mem_vars mem_funcs  RLLAVE'
    p[0] = ("class", p[2],p[4],p[5])
######################################
# class member variables
######################################
def p_member_var_dcl (p):
    ' mem_var_dcl : modf_acso VARIABLE FINAL_DE_LINEA '
    p[0] = ("member_variable_declaration", p[1], p[2],p[3])
def p_member_var_dcl_comentario (p):#TODO: esto no debe hacerse asi, los comentarios deben ser ignorados
    ' mem_var_dcl : COMENTARIO'
def p_member_variables_base (p):
    ' mem_vars : mem_var_dcl' 
    p[0] = ("member_variables", p[1])
def p_member_variables_many (p):
    ' mem_vars : mem_var_dcl mem_vars'
    p[0] = ("member_variables", p[1],p[2])

######################################
# class member functions
######################################

def p_mem_func_acs_mod(p):
    ' mem_func : modf_acso FUNCTION IDENTIFIER args scope'
    p[0] = ("member_function", p[1],p[3],p[4],p[5])
def p_mem_func_default(p):
    ' mem_func : FUNCTION IDENTIFIER args scope'
    p[0] = ("public_member_function", p[1],p[3],p[4])
def p_mem_funcs_single (p):
    ' mem_funcs : mem_func'
    p[0] = ("member_functions",p[1])
def p_mem_funcs_many (p):
    ' mem_funcs : mem_func mem_funcs'
    p[0] = ("member_functions",p[1],p[2])

######################################
# class instanciacion 
######################################
def p_instanciacion(p):
    'var_dcl : VARIABLE ASIGNACION NEW func_call'
    p[0] = ("instanciacion", p[1], p[4])

# printing to the console
def p_echo (p):
    'echo : ECHO expresion '
    p[0] = ("echo", p[2])
    pass
## comentarios 
def p_comment (p):
    'comentario : COMENTARIO '
    pass

#Manejo de errores
def p_termina_punto_y_coma(p):
    '''falta_punto_y_coma : expresion
                             | var_dcl
                             | echo
    '''
    print("requiere_punto_y_coma detectado",str(p))
def p_error_falta_punto_y_coma (p):
    'error_sintax : falta_punto_y_coma'
    print ("error detectado")
    global errores_parser 
    error = "Falta ';' en linea #" + str(p.lineno(1)) + '\n'
    print(error)
    errores_parser.append(error)
    raise SyntaxError


def p_error(p):
    global errores_parser
    if p:
        mensaje = "ERROR EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value) + "de tipo " + str(p)
        errores_parser.append(mensaje)
    else:
        pass

#Construir el parser
parser = yacc.yacc()

def pruebasyntax(datos):
    my_lexer_clone = my_lexer.clone() #objeto ply.lex.lexer
    global errores_parser
    errores_parser.clear()
    parser.parse(datos, tracking=True, lexer= my_lexer_clone)
    if len(errores_parser)<1:
        errores_parser.append("No hay errores ☺")
    parser.restart()
    return errores_parser #una lista


def errorsyntax():
    return errores_parser

if __name__ == "__main__":
    pruebasyntax(lexer.data)
    print(pruebasyntax(lexer.data))

