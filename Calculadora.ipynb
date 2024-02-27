# Constantes
OPERACOES = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}

# Funções de conversão (não definidas no código fornecido)
def decimal_para_binario(numero):
    return bin(numero)[2:]

def decimal_para_octal(numero):
    return oct(numero)[2:]

def decimal_para_hexadecimal(numero):
    return hex(numero)[2:]

def binario_para_decimal(numero):
    return int(numero, 2)

def octal_para_decimal(numero):
    return int(numero, 8)

def hexadecimal_para_decimal(numero):
    return int(numero, 16)

CONVERSOES = {
    'D': {
        '1': decimal_para_binario,
        '2': decimal_para_octal,
        '3': decimal_para_hexadecimal
    },
    'B': binario_para_decimal,
    'O': octal_para_decimal,
    'H': hexadecimal_para_decimal
}

def ler_numero(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
            return numero
        except ValueError:
            print("Ops! Por favor, insira um número válido.")

def ler_operacao_conversao():
    while True:
        operacao = input('''
Por favor, digite a operação matemática ou a conversão que deseja realizar:
+ para adição
- para subtração
* para multiplicação
/ para divisão
D para converter decimal em binário, octal ou hexadecimal
B para converter binário em decimal
O para converter octal em decimal
H para converter hexadecimal em decimal
''').upper()

        if operacao in OPERACOES or operacao in CONVERSOES:
            return operacao
        else:
            print("Operação inválida!")

def calcular():
    try:
        operacao = ler_operacao_conversao()

        if operacao in CONVERSOES:
            if operacao == 'D':
                numero = ler_numero('Digite o número decimal que deseja converter: ')
                opcao = input('''
Escolha a base de conversão:
1 para binário
2 para octal
3 para hexadecimal
''')

                if opcao in CONVERSOES['D']:
                    print("O número convertido é: ", CONVERSOES['D'][opcao](int(numero)))
                else:
                    print("Opção inválida!")
            else:
                numero = ler_numero('Digite o número que deseja converter em decimal: ')
                print("O número convertido é: ", CONVERSOES[operacao](numero))
        else:
            numero_1 = ler_numero('Digite seu primeiro número: ')
            numero_2 = ler_numero('Digite seu segundo número: ')

            if operacao == '+':
                resultado = OPERACOES[operacao](numero_1, numero_2)
                print("O resultado é: ", resultado)
            elif operacao == '-':
                resultado = OPERACOES[operacao](numero_1, numero_2)
                print("O resultado é: ", resultado)
            elif operacao == '*':
                resultado = OPERACOES[operacao](numero_1, numero_2)
                print("O resultado é: ", resultado)
            elif operacao == '/':
                try:
                    resultado = OPERACOES[operacao](numero_1, numero_2)
                    print("O resultado é: ", resultado)
                except ZeroDivisionError:
                    print("Não é possível dividir por zero!")
            else:
                print("Operação inválida!")

    except Exception as e:
        print("Ops! Algo deu errado.", e)

# Defina novamente() fora da função calcular()
def novamente():
    calc_novamente = input('''
Deseja calcular novamente?
Por favor, digite S para SIM ou N para NÃO.
''')

    if calc_novamente.upper() == 'S':
        calcular()
    elif calc_novamente.upper() == 'N':
        print('Até logo.')
    else:
        novamente()

calcular()
