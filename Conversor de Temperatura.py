def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_para_kelvin(fahrenheit):
    celsius = fahrenheit_para_celsius(fahrenheit)
    return celsius_para_kelvin(celsius)

def kelvin_para_fahrenheit(kelvin):
    celsius = kelvin_para_celsius(kelvin)
    return celsius_para_fahrenheit(celsius)

def main():
    print("Bem-vindo ao conversor de temperatura!")
    print("Selecione a unidade de temperatura de entrada:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")

    opcao_entrada = int(input("Digite o número da sua escolha: "))

    valor_entrada = float(input("Digite o valor da temperatura de entrada: "))

    print("Selecione a unidade de temperatura de saída:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")

    opcao_saida = int(input("Digite o número da sua escolha: "))

    if opcao_entrada == 1:  # Celsius
        if opcao_saida == 1:
            resultado = valor_entrada
        elif opcao_saida == 2:
            resultado = celsius_para_fahrenheit(valor_entrada)
        elif opcao_saida == 3:
            resultado = celsius_para_kelvin(valor_entrada)
    elif opcao_entrada == 2:  # Fahrenheit
        if opcao_saida == 1:
            resultado = fahrenheit_para_celsius(valor_entrada)
        elif opcao_saida == 2:
            resultado = valor_entrada
        elif opcao_saida == 3:
            resultado = fahrenheit_para_kelvin(valor_entrada)
    elif opcao_entrada == 3:  # Kelvin
        if opcao_saida == 1:
            resultado = kelvin_para_celsius(valor_entrada)
        elif opcao_saida == 2:
            resultado = kelvin_para_fahrenheit(valor_entrada)
        elif opcao_saida == 3:
            resultado = valor_entrada

    print("O resultado da conversão é:", resultado)

if __name__ == "__main__":
    main()
