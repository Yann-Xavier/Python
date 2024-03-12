def obter_nota():
    """
    Solicita uma nota ao usuário e valida se está entre zero e dez.

    Retorna:
    float: A nota inserida pelo usuário.
    """
    while True:
        try:
            nota = float(input("Digite uma nota entre zero e dez: "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Erro: A nota deve estar entre zero e dez.")
        except ValueError:
            print("Erro: Por favor, insira um valor numérico para a nota.")

def main():
    """
    Função principal do programa.
    """
    print("Bem-vindo ao programa de verificação de nota!")

    nota = obter_nota()
    print(f"A nota digitada foi: {nota}")

if __name__ == "__main__":
    main()
