import math

def calcular_area_circulo(raio):
    return math.pi * raio ** 2

def calcular_area_retangulo(base, altura):
    return base * altura

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def main():
    while True:
        print("\nCALCULADORA DE ÁREAS DE FORMAS GEOMÉTRICAS")
        print("Escolha a forma geométrica para calcular a área:")
        print("1. Círculo")
        print("2. Retângulo")
        print("3. Triângulo")
        print("0. Sair")

        opcao = input("Digite o número correspondente à forma desejada: ")

        if opcao == "1":
            try:
                raio = float(input("Digite o raio do círculo: "))
                area = calcular_area_circulo(raio)
                print("A área do círculo é:", area)
            except ValueError:
                print("Por favor, insira um valor numérico válido para o raio.")
        elif opcao == "2":
            try:
                base = float(input("Digite a base do retângulo: "))
                altura = float(input("Digite a altura do retângulo: "))
                area = calcular_area_retangulo(base, altura)
                print("A área do retângulo é:", area)
            except ValueError:
                print("Por favor, insira valores numéricos válidos para a base e altura.")
        elif opcao == "3":
            try:
                base = float(input("Digite a base do triângulo: "))
                altura = float(input("Digite a altura do triângulo: "))
                area = calcular_area_triangulo(base, altura)
                print("A área do triângulo é:", area)
            except ValueError:
                print("Por favor, insira valores numéricos válidos para a base e altura.")
        elif opcao == "0":
            print("Obrigado por usar a calculadora de áreas. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
