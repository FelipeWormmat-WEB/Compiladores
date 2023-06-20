import ply.yacc as yacc


# Definição das regras de produção
def p_program(p):
    p[0] = p[1]


def p_statement(p):
    p[0] = p[1]


def p_declaration(p):
    p[0] = ('declaration', p[2])


def p_variable_declaration(p):
    p[0] = (p[1], p[2])


def p_type(p):
    p[0] = p[1]


def p_variable_list(p):
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]


def p_variable(p):
    p[0] = p[1]


def p_assignment(p):
    p[0] = (p[1], p[3])


def p_expression(p):
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]


def p_term(p):
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        if p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]


def p_factor(p):
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = p[2]


def p_add_op(p):
    print("p_add_op")
    p[0] = p[1]


def p_mult_op(p):
    print("p_mult_op")
    p[0] = p[1]


def p_loop(p):
    print("p_loop")
    p[0] = ('loop', p[3], p[6])


def p_conditional(p):
    print("p_conditional")
    if len(p) == 8:
        p[0] = ('conditional', p[3], p[6], None)
    else:
        p[0] = ('conditional', p[3], p[6], p[10])


def p_error(p):
    if p:
        print("Erro de sintaxe: token '{0}' inválido na linha {1}"
              .format(p.value, p.lineno))
    else:
        print("Erro de sintaxe: final de entrada inesperado")


parser = yacc.yacc()