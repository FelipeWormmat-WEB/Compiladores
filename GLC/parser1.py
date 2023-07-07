import ply.yacc as yacc
from lexer import tokens
import lexer

intermediate_code = []
temp_count = 1
label_count = 1


# Definição das regras de produção
def p_program(p):
    'program : declaration_list SEMICOLON'
    p[0] = ('program', p[1])

    for token in p[1]:
        if tokens in lexer.tokens:
            print('The token `{:0}` is defined in the '
                  'lexer.tokens module'.format(token))
        else:
            print('The token `{0}` is not defined in the '
                  'lexer.tokens module'.format(token))


def p_statement(p):
    '''declaration_list : declaration
                        | declaration_list declaration'''
    p[0] = p[1]


def p_declaration(p):
    'declaration : VAR variable_list SEMICOLON'
    p[0] = ('declaration', p[2])


def p_variable_declaration(p):
    'variable_declaration : type IDENTIFIER'
    p[0] = (p[1], p[2])


def p_type(p):
    '''type : INT
            | REAL'''
    p[0] = p[1]


def p_variable_list(p):
    '''variable_list : variable
                     | variable_list COMMA variable'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]


def p_variable(p):
    'variable : IDENTIFIER'
    p[0] = p[1]


def p_assignment(p):
    '''statement : assignment
       statement : conditional
    '''
    p[0] = (p[1], p[3])
    intermediate_code.append(p[0])


def p_expression(p):
    '''expression : expression PLUS term
       expression : expression MINUS term
       expression : term
       '''
    if len(p) <= 2:
        p[0] = p[1]
        return
    p[0] = geraTemp()
    print(p[0], "=", p[1], p[2], p[3])


def p_term(p):
    '''term : term MULTIPLY factor
        term: term DIVIDE factor
        term: factor
        '''
    if len(p) <= 2:
        p[0] = p[1]
        return
    p[0] = geraTemp()
    print(p[0], "=", p[1], p[2], p[3])


def geraTemp(p):
    global cont
    cont += 1
    return "T" + str(cont)


def geraLabel(p):
    global cont1
    cont1 += 1
    return "T" + str(cont1)


def p_factor(p):
    '''factor : NUMBER
       factor: IDENTIFIER
       factor: LPAREN expression RPAREN
       '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = p[2]


def p_add_op(p):
    '''add_op : PLUS
              | MINUS'''
    print("p_add_op")
    p[0] = p[1]


def p_mult_op(p):
    '''mult_op : MULTIPLY
               | DIVIDE'''
    print("p_mult_op")
    p[0] = p[1]


def p_loop(p):
    'loop : WHILE LPAREN expression RPAREN LBRACE statement RBRACE'
    print("p_loop")
    p[0] = ('loop', p[3], p[6])


def p_conditional(p):
    '''conditional : IF LPAREN expression RPAREN LBRACE statement RBRACE \
                   | ELSE LBRACE statement RBRACE
    '''
    p[0] = geraLabel()
    print("p_conditional")
    if len(p) == 8:
        p[0] = ('conditional', p[3], p[6], None)
    else:
        p[0] = ('conditional', p[3], p[6], p[10])


def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression MULTIPLY expression
                  | expression DIVIDE expression
                  | expression POWER expression'''
    p[0] = f"t{temp_count}"
    intermediate_code.append(f"{p[0]} = {p[1]} {p[2]} {p[3]};")


def p_expression_relational(p):
    '''expression : expression LESSTHAN expression
       expression : expression LESSEQUAL expression
       expression : expression GREATERTHAN expression
       expression : expression GREATEREQUAL expression
       expression : expression EQUAL expression
       expression : expression NOTEQUAL expression
    '''
    p[0] = f"t{temp_count}"
    intermediate_code.append(f"{p[0]} = {p[1]} {p[2]} {p[3]};")
    

def p_looping(p):
    'loop : WHILE LPAREN expression RPAREN LBRACE COM_L RBRACE'
    global label_count
    label_start = f"WHILE{label_count}:"
    label_end = f"END{label_count}:"
    label_count += 1

    intermediate_code.append(label_start)
    intermediate_code.append(f"IF {p[3]} GOTO {label_end}")

    for statement in p[6]:
        intermediate_code.append(statement)

    intermediate_code.append(f"GOTO {label_start}")
    intermediate_code.append(label_end)


def p_error(p):
    if p:
        print("Erro de sintaxe: token '{0}' inválido na linha {1}"
              .format(p.value, p.lineno))
    else:
        print("Erro de sintaxe: final de entrada inesperado")


parser = yacc.yacc()
cont = 0
cont1 = 0