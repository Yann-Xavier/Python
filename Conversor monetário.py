def formatar_valor_monetario(valor_decimal):
    # Arredonda o valor para 2 casas decimais
    valor_arredondado = round(valor_decimal, 2)

    # Transforma o valor arredondado em uma string
    valor_formatado = f"{valor_arredondado:.2f}"

    # Substitui o ponto decimal pela vírgula
    valor_formatado = valor_formatado.replace('.', ',')

    # Adiciona o símbolo de moeda (R$) e espaços para melhor legibilidade
    valor_final = f"R$ {valor_formatado}"

    return valor_final


numero_decimal = float(input("Digite um número decimal: "))
valor_monetario_formatado = formatar_valor_monetario(numero_decimal)
print(f"Valor formatado: {valor_monetario_formatado}")
