from lexer import tokens
import lexer
import ply.yacc as yacc


def p_php_code (p):
    'php_code : php_heading statements php_end'
    pass

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
    pass
        
# statements match every posible php line of code
def p_php_statements_many(p):
    'statements : statements statement' 
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
                    | echo
    '''
    pass

#######################################################################################################3
# global scope
#######################################################################################################3
def p_var_declaration_base(p):
    'var_declaration : var_dcl FINAL_DE_LINEA'

def p_var_modification_base(p):
    'var_modification : var_modi FINAL_DE_LINEA'

def p_function_declaration (p):
    'function : func '

def p_function_call (p):
    'function_call : func_call FINAL_DE_LINEA'

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
    pass

######################################
# strings aporte de Jorge Vulgarin
######################################
# TODO: faltan metodos de string
# concatenacion de strings

# string_concat es [1 o mas] instancias de (. string | . variable)
def p_string_concats0(p):
    ' string_concats :  string_concat '
    pass
def p_string_concats1(p):
    ' string_concats : string_concats string_concat '
    pass

# match (. <cadnea>)
def p_string_concat2(p):
    ' string_concat :  DOT string  '
    pass

# match ( . <variable> ) 
def p_string_concat3(p):
    ' string_concat : DOT VARIABLE'
    pass
# match ( . <function>(...args) ) 
def p_string_concat4(p):
    ' string_concat : DOT func_call'
    pass
def p_string_concat5(p):
    ' string_concat : DOT var_accs'
    pass

# match strings con "" y con ''
def p_string_1 (p): 
    '''string : STRING1 
                | STRING2
    '''
    pass

# se define como string a un "" seguido por multiples concatenaciones
def p_string_2 (p): 
    ' string : string string_concats'
    pass

# se define como estring a una variable seguida de multiples concatenaciones
def p_string_3 (p): 
    ' string : VARIABLE string_concats'
    pass

# asignnar un string a una variable
def p_var_dcl_s (p): 
    'var_dcl : VARIABLE ASIGNACION string '   
    pass

# concatenacion assigncacion (operador .=)
def p_var_modi_CONCAT (p): 
    'var_modi : VARIABLE CONCAT_ASIG string '
    pass

# concatenacion assigncacion (operador .=)
def p_var_modi_CONCAT2 (p):
    'var_modi : VARIABLE CONCAT_ASIG VARIABLE '
    pass

######################################
# number 
######################################

# match for +-
def p_signo_mas_menos0(p):
    ' signo_mas_menos : MAS MENOS '
#mathch for +-+-+-+-...+-
def p_signo_mas_menos1(p):
    ' signo_mas_menos : MAS MENOS signo_mas_menos '
# #mathch for +-+-+-+-...+
# def p_signo_mas_menos2(p):
#     ' signo_mas_menos_mas : signo_mas_menos MAS'

#match for -+
def p_signo_menos_mas (p):
    ' signo_menos_mas : MENOS MAS '
#mathch for -+-+-...+
def p_signo_menos_mas1(p):
    ' signo_menos_mas : MENOS MAS signo_menos_mas '
# #mathch for -+-+-+-...-
# def p_signo_menos_mas2(p):
#     ' signo_menos_mas_menos : signo_menos_mas MENOS'


# math con signos para los nuumeros
def p_signo (p) :
    '''signo :    MAS
                | MENOS'''
    pass
def p_signo1 (p):
    '''signo :    signo_mas_menos
                | signo_menos_mas
    '''
    pass

def p_math_operator (p):
    ''' math_oper :   MAS
                    | MENOS
                    | MULTIPLICACION
                    | DIVISION
    '''

######################################
# expresiones matermaticas aporte de jorge vulgarin
# componentes sintanticos y semanticos
######################################
#math numeros idividuales
def p_math_expr1 (p):
    'math_expr : NUMERO '
    pass
#math numeros idividuales cons signos
def p_math_expr2 (p):
    'math_expr : signo NUMERO '
    pass
#math variables idividuales
def p_math_expr3 (p):
    'math_expr : VARIABLE '
    pass
#math vaiables idividuales cons signos
def p_math_expr4 (p):
    'math_expr : signo VARIABLE '
    pass
def p_math_expr5 (p):
    'math_expr : var_accs '
    pass
#math vaiables idividuales cons signos
def p_math_expr6 (p):
    'math_expr : signo var_accs '
    pass
def p_math_expr7(p):
    'math_expr : math_expr operaciones_mat'
    pass

# match (operador con numero) ej. + 125
def p_oper__mat0 (p):
    'operacion_mat : math_oper NUMERO'
    pass
# match (operador con variable) ej. + $uno
def p_oper__mat1 (p): 
    'operacion_mat : math_oper VARIABLE'
    pass
def p_oper__mat2 (p): 
    'operacion_mat : math_oper var_accs'
    pass
def p_oper__mat3 (p):
    'operacion_mat : signo NUMERO'
    pass
# match (operador con variable) ej. + $uno
def p_oper__mat4 (p): 
    'operacion_mat : signo VARIABLE'
    pass
def p_oper__mat5 (p): 
    'operacion_mat : signo var_accs'
    pass
# operaciones, define la lista de operaciones matematicas continuas
def p_operaciones1 (p):
    'operaciones_mat : operacion_mat'
    pass
def p_operaciones2 (p):
    'operaciones_mat : operacion_mat operaciones_mat'
    pass

def p_var_dcl_n (p):
    'var_dcl : VARIABLE ASIGNACION math_expr '
    pass

def p_var_modi1 (p):
    'var_modi : VARIABLE AUTOINCREMENTO '
    pass
def p_var_modi2 (p):
    'var_modi : VARIABLE AUTODECREMENTO '
    pass
def p_var_modi3 (p):
    'var_modi : VARIABLE ASIGNACION_AUMENTADA math_expr '
def p_var_modi4 (p):
    'var_modi : VARIABLE ASIGNACION_DISMINUIDA math_expr '
#######################################################################################################3
#  if statement
#######################################################################################################3

# siingle if
def p_if_statement0(p):
    'if_statement : main_if_statement scope '
# if con else
def p_if_statement1(p):
    'if_statement : main_if_statement scope else scope'
# if con elseif
def p_if_statement2(p):
    'if_statement : main_if_statement scope many_elseif'
#if con elseif con else
def p_if_statement3(p):
    'if_statement : main_if_statement scope many_elseif else scope'

# if con elseif con else
def p_many_elseif(p):
    'many_elseif : elseif_statement scope'
    pass
def p_many_elseif1(p):
    'many_elseif : elseif_statement scope many_elseif'
    pass

######################################
# boolean operations
######################################

# comparaciones que reciben 2 argumentos y retornan booleans
def p_comp_binary_operator (p):
    '''comp_bin_oprs : MAYORQUE
                        | MENORQUE
                        | MAYORIGUAL
                        | MENORIGUAL
                        | SAME
                        | EQUALS
                        | DESIGUALDAD
                        | AND
                        | OR'''
# operaciones que reciben un boolean y retornan otro
def p_bool_unary_oprs(p):
    '''bool_unary_oprs : negacion'''

# match !
def p_negacion0 (p):
    'negacion : NEGACION'
# match !!!! ... !
def p_negacion1 (p):
    'negacion : NEGACION negacion'

######################################
# condicion, aka. boolean, 
######################################
def p_boolean_constant (p):
    '''boolean : TRUE
                | FALSE'''

def p_boolean0 (p):
    'boolean : expresion comp_bin_oprs expresion'
def p_boolean1 (p):
    'boolean : bool_unary_oprs boolean'
# def p_boolean2 (p): 
#     'boolen : LPAREN bolean RPAREN'

######################################
# main_if statement
######################################
def p_main_if_statement (p):
    'main_if_statement : IF LPAREN boolean RPAREN '
    pass

######################################
# elseif
######################################
def p_elseif_statement (p):
    ' elseif_statement : ELSEIF LPAREN boolean RPAREN'
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
def p_scope_empty (p):
    'scope : LLLAVE RLLAVE'

def p_scope_break (p):
    'scope : LLLAVE statements BREAK FINAL_DE_LINEA RLLAVE'
def p_scope_just_break (p):
    'scope : LLLAVE BREAK FINAL_DE_LINEA RLLAVE'

def p_scope_continue (p):
    'scope : LLLAVE statements CONTINUE FINAL_DE_LINEA RLLAVE'
def p_scope_just_continue (p):
    'scope : LLLAVE CONTINUE FINAL_DE_LINEA RLLAVE'

def p_scope_return (p):
    'scope : LLLAVE statements return FINAL_DE_LINEA RLLAVE'
def p_scope_just_return (p):
    'scope : LLLAVE return FINAL_DE_LINEA RLLAVE'
######################################
# return
######################################
def p_return_void (p):
    ' return : RETURN'
def p_return_value (p):
    ' return : RETURN expresion'

#######################################################################################################3
# while loop
#######################################################################################################3

def p_while_loop (p):
    'while_lopp : WHILE LPAREN boolean RPAREN scope'

#######################################################################################################3
# for loop
#######################################################################################################3
def p_for_loop (p):
    'for_loop : FOR LPAREN var_dcl FINAL_DE_LINEA boolean FINAL_DE_LINEA var_modi RPAREN scope'

#######################################################################################################3
# array, contribucion de jorge Vugarin
# semantica de arrays, Viviana Vera
#######################################################################################################

def p_array_clave(p):
  """array_clave : string  
                  | boolean 
                  | math_expr
                     """
def p_array_elemento(p):
  """array_elemento : math_expr
                    | string
                    | boolean
                    | array
                  | NULL"""

def p_asignacionArrow(p):
    ' asignacionArrow : array_clave ASIGNACION2 array_elemento'

def p_arrayItem (p):
    ''' array_item : asignacionArrow 
                    | array_elemento'''

def p_arrayItems_single (p):
    ' array_items : array_item '
def p_arrayItems (p):
    ' array_items : array_item COMA array_items'

def p_array(p):
    ' array : ARRAY LPAREN array_items RPAREN'

def p_array_declaration(p):
    'var_dcl : VARIABLE ASIGNACION array'

######################################
# indexing
######################################
def p_array_indexing(p):
    ' var_accs : VARIABLE LBRACKET array_clave RBRACKET'
    
# def p_copy_array_element (p):
#     ' var_accs : indexing'
#######################################################################################################3
# booleans, contribucion de Adriana Guilindro
#######################################################################################################3
#asignar el valor de false a una variable
def p_boolean_false(p):
    ' boolean_false : VARIABLE ASIGNACION FALSE'
#asignar el valor de true a una variable
def p_boolean_true(p):
    ' boolean_true : VARIABLE ASIGNACION TRUE'
#conversion de una variable a booleano
def p_boolean_conv(p):
    ' boolean : LPAREN BOOL RPAREN VARIABLE'

#######################################################################################################3
# functions
#######################################################################################################3
# arguments for a function definition
def p_arguments_single (p):
    'arguments : VARIABLE'
def p_arguments_many (p):
    'arguments : VARIABLE COMA arguments'
def p_fn_no_args (p):
    'args : LPAREN RPAREN'
def p_fn_args (p):
    'args : LPAREN arguments RPAREN'

# function argument values list, for a function call
def p_fun_argument_value (p):
    ' value : expresion'
def p_func_argument_values_single (p):
    ' values : value'
def p_func_argument_values_many (p):
    ' values :  value COMA values'

# defincion de una funcion
def p_func(p):
    ' func : FUNCTION IDENTIFIER args scope'

# definition de una llamada a una funcion
def p_func_call_no_arguments (p):
    ' func_call : IDENTIFIER LPAREN RPAREN'
def p_func_call_with_arguments (p):
    ' func_call : IDENTIFIER LPAREN values RPAREN '

#######################################################################################################3
# clas, contribucion de Jorge Vulgarin
#######################################################################################################3
######################################
# self reference, using "this->"
######################################
def p_self_ref(p):
    ' var_modi : THIS ARROW IDENTIFIER ASIGNACION expresion'
def p_member_modification(p):
    ' var_modi : VARIABLE ARROW IDENTIFIER ASIGNACION expresion'
def p_member_access(p):
    ' var_accs : VARIABLE ARROW IDENTIFIER '
def p_member_copy(p):
    ' var_dcl : VARIABLE ASIGNACION var_accs'
def p_member_func_call(p):
    ' func_call : VARIABLE ARROW func_call'
def p_var_modif_acso (p):
    ''' modf_acso : PUBLIC 
                    | PRIVATE
                    | PROTECTED
    '''
def p_class (p):
    ' class : CLASS IDENTIFIER LLLAVE mem_vars mem_funcs  RLLAVE'
######################################
# class member variables
######################################
def p_member_var_dcl (p):
    ' mem_var_dcl : modf_acso VARIABLE FINAL_DE_LINEA '
def p_member_var_dcl_comentario (p):#TODO: esto no debe hacerse asi, los comentarios deben ser ignorados
    ' mem_var_dcl : COMENTARIO'
def p_member_variables_base (p):
    ' mem_vars : mem_var_dcl' 
def p_member_variables_many (p):
    ' mem_vars : mem_var_dcl mem_vars'

######################################
# class member functions
######################################

def p_mem_func_acs_mod(p):
    ' mem_func : modf_acso FUNCTION IDENTIFIER args scope'
def p_mem_func_default(p):
    ' mem_func : FUNCTION IDENTIFIER args scope'
def p_mem_funcs_single (p):
    ' mem_funcs : mem_func'
def p_mem_funcs_many (p):
    ' mem_funcs : mem_func mem_funcs'

######################################
# class instanciacion 
######################################
def p_instanciacion(p):
    'var_dcl : VARIABLE ASIGNACION NEW func_call'

# printing to the console
def p_echo (p):
    'echo : ECHO expresion FINAL_DE_LINEA'
    pass
## comentarios 
def p_comment (p):
    'comentario : COMENTARIO '
    pass




def p_error(p):
    if p is not None:
        print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value) + "de tipo " + str(p))
    else:
        pass



parser = yacc.yacc()
if __name__ == "__main__":
    parser.parse(lexer.data)
