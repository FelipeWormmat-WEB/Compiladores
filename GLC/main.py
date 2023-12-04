from parser1 import parser
from lexer import lexer


# Função para analisar uma sentença de entrada
def parse(input_string):
    parser.parse(input_string)


# Código principal
input_string = '''
var
    int cont, num;
    real cont2;

num = 0;
while(cont < 10) {
    cont2 = 3.1415 * contador ^ 2;
    if (cont < 5) {
       num = num + cont2;
    }
    else {
       cont = 0;
    }
    cont = cont + 1;
}
'''
input_string = "var x, y; x = 5; while (x > 0) { x = x - 1; }"
lexer.input(input_string)
result = parse(input_string)
print(result)

if result is not None:
    print('Análise bem sucedida')
else:
    print('Análise não foi bem sucedida')

# Print the generated three-address code
print("\nGenerated Three-Address Code:")
for code in parser.intermediate_code:
    print(code)
