def obter_nome():
    while True:
        nome = input("Digite seu nome: ")
        if len(nome) > 3:
            return nome
        else:
            print("O nome deve ter mais de 3 caracteres.")

def obter_idade():
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if 0 <= idade <= 150:
                return idade
            else:
                print("A idade deve estar entre 0 e 150.")
        except ValueError:
            print("Por favor, insira um número inteiro para a idade.")

def obter_salario():
    while True:
        try:
            salario = float(input("Digite seu salário: "))
            if salario >= 0:
                return salario
            else:
                print("O salário não pode ser negativo.")
        except ValueError:
            print("Por favor, insira um valor numérico para o salário.")

def main():
    print("Bem-vindo ao programa de cadastro!")

    while True:
        nome = obter_nome()
        idade = obter_idade()
        salario = obter_salario()

        # Se todas as condições forem atendidas, exiba os dados e encerre o programa.

        print("\nDados cadastrados com sucesso:")
        print(f"Nome: {nome}")
        print(f"Idade: {idade}")
        print(f"Salário: R${salario:.2f}")

        resposta = input("\nDeseja cadastrar outra pessoa? (s/n): ")
        if resposta.lower() != 's':
            print("Programa encerrado.")
            break

if __name__ == "__main__":
    main()
