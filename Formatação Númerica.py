def formatar_com_zeros(numero, tamanho):
    # Converte o número inteiro para uma string
    numero_str = str(numero)

    # Calcula quantos zeros precisam ser adicionados
    zeros_faltantes = tamanho - len(numero_str)

    # Formata a string com zeros à esquerda
    numero_formatado = f"{zeros_faltantes * '0'}{numero_str}"

    return numero_formatado

# Exemplo de uso
numero_inteiro = int(input("Digite um número inteiro: "))
tamanho_desejado = int(input("Digite o tamanho desejado: "))

numero_formatado = formatar_com_zeros(numero_inteiro, tamanho_desejado)
print(f"Número formatado: {numero_formatado}")
