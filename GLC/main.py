from parser1 import parser


# Função para analisar uma sentença de entrada
def parse(input_string):
    parser.parse(input_string)


# Código principal
input_string = '''
var
    int cont, num
    real cont2

num = 0
while(cont < 10) {
    cont2 = 3.1415 * cont ^ 2
    if (cont < 5) {
       num = num + cont2
    }
    else {
       cont = 0
    }
    cont = cont + 1
}
'''

parse(input_string)

# Adicionar uma nova linha vazia no final do arquivo
print()
