def adicionar_aspas(citacao):
    # Adiciona aspas simples no início e no fim da citação
    citacao_formatada = f"'{citacao}'"
    return citacao_formatada

# Solicita ao usuário que insira uma citação
citacao_usuario = input("Digite uma citação: ")

# Obtém a citação formatada com aspas
citacao_com_aspas = adicionar_aspas(citacao_usuario)

# Exibe a citação formatada na tela
print(f"Citação com aspas: {citacao_com_aspas}")
