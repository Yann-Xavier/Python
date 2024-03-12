def validar_input(mensagem):
    while True:
        try:
            entrada = input(mensagem)
            if ',' in entrada:
                print("Caracteres inválidos. Use apenas ponto (.) para separar decimais.")
            else:
                return float(entrada)
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

def calcular_salario():
    valor_hora = validar_input("Digite o valor ganho por hora de trabalho: ")
    horas_trabalhadas = validar_input("Digite o valor de horas trabalhadas neste mês: ")
    pagamento = valor_hora * horas_trabalhadas
    print("Você trabalhou por", horas_trabalhadas, "horas.")
    print("O valor da hora trabalhada é de R$", valor_hora)
    print("O pagamento que deve ser recebido é de: R$", pagamento)
    return pagamento

def main():
    while True:
        calcular_salario()
        resposta = input("Deseja realizar um novo cálculo? (s/n) ")
        if resposta != 's':
            break

if __name__ == "__main__":
    main()
