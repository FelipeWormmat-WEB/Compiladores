import ply.lex as lex
import ply.yacc as yacc

# Definição dos tokens
tokens = (
    'INT',
    'REAL',
    'IDENTIFIER',
    'NUMBER',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'POWER',
    'LPAREN',
    'RPAREN',
    'LESSTHAN',
    'LESSEQUAL',
    'GREATERTHAN',
    'GREATEREQUAL',
    'EQUAL',
    'NOTEQUAL',
    'COMMA',
    'SEMICOLON',
    'VAR',
    'IF',
    'ELSE',
    'WHILE',
    'LBRACE',
    'RBRACE'
)

# Expressões regulares para os tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_POWER = r'\^'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LESSTHAN = r'<'
t_LESSEQUAL = r'<='
t_GREATERTHAN = r'>'
t_GREATEREQUAL = r'>='
t_EQUAL = r'=='
t_NOTEQUAL = r'<>'
t_COMMA = r','
t_SEMICOLON = r';'
t_VAR = r'var'
t_IF = r'if'
t_ELSE = r'else'
t_WHILE = r'while'
t_LBRACE = r'\{'
t_RBRACE = r'\}'

# Regra para ignorar espaços em branco e quebras de linha
t_ignore = ' \n\t'


# Expressões regulares com ações
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t


def t_REAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t


# Ignorar espaços em branco e tabulações
t_ignore = ' \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Tratamento de erros de token
def t_error(t):
    print(f"Caractere inválido: '{t.value[0]}' na linha {t.lineno}")
    t.lexer.skip(1)


lexer = lex.lex()


# Função para realizar a análise sintática
def parse(input_string):
    parser = yacc.yacc()
    result = parser.parse(input_string)
    return result


# Exemplo de uso
input_string = "var x, y; x = 5; while (x > 0) { x = x - 1; }"
result = parse(input_string)
print(result)