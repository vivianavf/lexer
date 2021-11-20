import ply.yacc as yacc
from lexer import tokens
import lexer
# import lexer

VERBOSE =1

def p_program(p):
	'program : header_declaration declaration_list footer_declaration'
	pass

def p_declaration_list_1(p):
	'declaration_list : declaration_list  declaration'
	pass

def p_declaration_list_2(p):
	'declaration_list : declaration'
	pass

def p_declaration(p):
	'''declaration : var_declaration
                    | selection_stmt
                    | iteration_stmt
				    | fun_declaration
                    | show_in_screen
                    | expression_stmt'''

	pass

def p_header_declaration(p):
    'header_declaration : MENORQUE PREGUNTA PHP'
    pass

def p_footer_declaration(p):
    'footer_declaration : PREGUNTA MAYORQUE'
    pass

def p_show_in_screen_1(p):
    'show_in_screen : ECHO var_val FINAL_DE_LINEA'
    pass

def p_show_in_screen_2(p):
    'show_in_screen : ECHO STRING1 FINAL_DE_LINEA'
    pass

def p_show_in_screen_3(p):
    'show_in_screen : ECHO STRING2 FINAL_DE_LINEA'
    pass
def p_show_in_screen_4(p):
    'show_in_screen : ECHO selection_stmt'
    pass

def p_var_declaration_1(p):
	'var_declaration : var_declaration2 FINAL_DE_LINEA'
	pass

def p_var_declaration_2(p):
	'var_declaration : VARIABLE LBRACKET NUMERO RBRACKET FINAL_DE_LINEA'
	pass

def p_var_declaration_3(p):                     
	'''var_declaration2 : VARIABLE
                        | VARIABLE COMA var_declaration2
                        | VARIABLE ASIGNACION NUMERO COMA var_declaration2
                        | VARIABLE ASIGNACION NUMERO
                        | VARIABLE ASIGNACION VARIABLE COMA var_declaration2
                        | VARIABLE ASIGNACION VARIABLE
                        | COMA 
                        | VARIABLE ASIGNACION VARIABLE simple_expression
                        | VARIABLE ASIGNACION LBRACKET NUMERO COMA var_declaration2
                        | NUMERO COMA var_declaration2
                        | NUMERO RBRACKET
                        | VARIABLE ASIGNACION LBRACKET STRING1 COMA var_declaration2
                        | STRING1 COMA var_declaration2
                        | STRING1 RBRACKET
        '''
	pass

def p_fun_declaration(p):
	'fun_declaration : FUNCTION IDENTIFIER LPAREN params RPAREN statement'
	pass

def p_params_1(p):
	'params : param_list'
	pass

def p_param_list_1(p):
	'param_list : param_list COMA param'
	pass

def p_param_list_2(p):
	'param_list : param'
	pass

def p_param_1(p):
	'param : VARIABLE'
	pass

def p_param_2(p):
	'param : VARIABLE LBRACKET RBRACKET'
	pass 

def p_param_3(p):
    'param : empty_function'
    pass

def p_compount_stmt(p):
	'compount_stmt : LLLAVE local_declarations statement_list RLLAVE'
	pass

def p_local_declarations_1(p):
	'local_declarations : local_declarations var_declaration'
	pass

def p_local_declarations_1(p):
    'local_declarations : var_declaration'
    pass

def p_local_declarations_2(p):
	'local_declarations : empty_function'
	pass

def p_statement_list_1(p):
	'statement_list : statement_list statement'
	pass

def p_statement_list_2(p):
	'statement_list : statement'
	pass
def p_statement_list_3(p):
	'statement_list : empty_function'
	pass

def p_statement(p):
	'''statement : expression_stmt
				| compount_stmt
				| selection_stmt
				| iteration_stmt
                | show_in_screen
				| return_stmt
	'''
	pass

def p_expression_stmt_1(p):
	'expression_stmt : expression FINAL_DE_LINEA'
	pass

def p_expression_stmt_2(p):
	'expression_stmt : FINAL_DE_LINEA'
	pass

def p_selection_stmt_1(p):
    'selection_stmt : IF LPAREN expression RPAREN statement'
    pass

def p_selection_stmt_2(p):
    'selection_stmt : IF LPAREN expression RPAREN statement ELSE statement'
    pass

def p_selection_stmt_3(p):
    'selection_stmt : IF LPAREN expression RPAREN statement ELSEIF statement'
    pass

def p_selection_stmt_4(p):
	'selection_stmt : SWITCH LPAREN var_val RPAREN statement'
	pass

def p_selection_stmt_5(p):
	'selection_stmt : CASE NUMERO DOS_PUNTOS statement BREAK FINAL_DE_LINEA'
	pass

def p_selection_stmt_6(p):
	'selection_stmt : DEFAULT DOS_PUNTOS statement BREAK FINAL_DE_LINEA'
	pass

def p_selection_stmt_7(p):
    'selection_stmt : VARIABLE relop VARIABLE PREGUNTA expression DOS_PUNTOS expression FINAL_DE_LINEA'
    pass

def p_iteration_stmt_1(p):
	'iteration_stmt : WHILE LPAREN expression RPAREN statement'
	pass

def p_iteration_stmt_2(p):
	'iteration_stmt : FOR LPAREN var_declaration2 FINAL_DE_LINEA expression FINAL_DE_LINEA additive_expression RPAREN statement'
	pass

def p_iteration_stmt_3(p):
    'iteration_stmt : FOREACH LPAREN var_val AS var_val RPAREN statement'
    pass

def p_return_stmt_1(p):
	'return_stmt : RETURN FINAL_DE_LINEA'
	pass

def p_return_stmt_2(p):
	'return_stmt : RETURN expression FINAL_DE_LINEA'
	pass

def p_expression_1(p):
	'expression : var_val ASIGNACION expression'
	pass

def p_expression_2(p):
	'expression : simple_expression'
	pass

def p_var_1(p):
	'var_val : VARIABLE'
	pass

def p_var_2(p):
	'var_val : VARIABLE LBRACKET expression RBRACKET'
	pass

def p_simple_expression_1(p):
	'simple_expression : additive_expression relop additive_expression'
	pass

def p_simple_expression_2(p):
	'simple_expression : additive_expression'
	pass


def p_relop(p):
	'''relop : MENORQUE 
			| MENORIGUAL
			| MAYORQUE
			| MAYORIGUAL
			| DESIGUALDAD
			| NEGACION
			| EQUALS
	'''
	pass

def p_additive_expression_1(p):
	'''additive_expression : additive_expression addop term
                                              
        '''
	pass

def p_additive_expression_2(p):
	'additive_expression : term'
	pass


def p_additive_expression_3(p):
	'additive_expression : term AUTODECREMENTO'
	pass

def p_additive_expression_4(p):
	'additive_expression : term AUTOINCREMENTO'
	pass

def p_additive_expression_5(p):
    '''additive_expression : addop term
                                            
    '''
    pass

def p_addop(p):
	'''addop : MAS 
			| MENOS
	'''
	pass

def p_term_1(p):
	'term : term mulop factor'
	pass

def p_term_2(p):
	'term : factor'
	pass

def p_term_3(p):
    'term : STRING1'
    pass

def p_term_4(p):
    'term : STRING2'
    pass


def p_mulop(p):
	'''mulop : 	MULTIPLICACION
				| DIVISION
	'''
	pass

def p_factor_1(p):
	'factor : LPAREN expression RPAREN'
	pass

def p_factor_2(p):
	'factor : var_val'
	pass

def p_factor_3(p):
	'factor : call'
	pass

def p_factor_4(p):
	'factor : NUMERO' 
	pass

def p_call_1(p):
	'call : IDENTIFIER LPAREN args RPAREN'
	pass


def p_args(p):
	'''args : args_list
			| empty_function
	'''
	pass

def p_args_list_1(p):
	'args_list : args_list COMA expression'
	pass

def p_args_list_2(p):
	'args_list : expression'
	pass

def p_empty_function(p):
	'empty_function :'
	pass


def p_error(p):
	if VERBOSE:
		if p is not None:
			print ("ERROR SINTACTICO EN LA LINEA " + str(p.lexer.lineno) + " NO SE ESPERABA EL Token  " + str(p.value))
		else:
			pass
	else:
		raise Exception('syntax', 'error')
		


parser = yacc.yacc()
if __name__ == "__main__":
    parser.parse(lexer.data,debug=True)
    
