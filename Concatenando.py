def obter_data_formatada(dia, mes, ano):
    # Formata a data no formato desejado (dd/mm/aaaa)
    data_formatada = f"{dia:02d}/{mes:02d}/{ano}"
    return data_formatada

# Solicita ao usuário que insira o dia, mês e ano de nascimento
dia_nascimento = int(input("Digite o dia de nascimento: "))
mes_nascimento = int(input("Digite o mês de nascimento: "))
ano_nascimento = int(input("Digite o ano de nascimento: "))

# Obtém a data formatada
data_formatada = obter_data_formatada(dia_nascimento, mes_nascimento, ano_nascimento)

# Exibe a data formatada na tela
print(f"Data de nascimento formatada: {data_formatada}")
