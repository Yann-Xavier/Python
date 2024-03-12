def imprimir_menu():
    """
    Imprime o menu da lanchonete.
    """
    print('-' * 30)
    print('\t\tCardápio')
    print('-' * 30)
    print('Código\tEspecificação\t\tValores')
    print('100\tCachorro Quente\t\tR$ 5,00')
    print('101\tHamburguer\t\tR$ 10,00')
    print('102\tCoxinha\t\t\tR$ 4,00')
    print('-' * 30)

def calcular_valor(codigo, quantidade):
    """
    Calcula o valor a ser pago pelo item pedido.

    Parâmetros:
    codigo (int): Código do item pedido.
    quantidade (int): Quantidade do item pedido.

    Retorna:
    float: Valor total a ser pago pelo item.
    """
    if codigo == 100:
        valor_unitario = 5.00
    elif codigo == 101:
        valor_unitario = 10.00
    elif codigo == 102:
        valor_unitario = 4.00
    else:
        print('Código inválido!')
        return None

    valor_total = valor_unitario * quantidade
    return valor_total

def main():
    """
    Função principal do programa.
    """
    print('Bem-vindo à Lanchonete!')
    imprimir_menu()

    total_pagar = 0
    continuar_pedido = True

    while continuar_pedido:s
        try:
            codigo = int(input('Digite o código do item: '))
            quantidade = int(input('Digite a quantidade: '))
            valor_total_item = calcular_valor(codigo, quantidade)

            if valor_total_item is not None:
                total_pagar += valor_total_item
                print(f'Item adicionado ao pedido. Total a pagar: R$ {total_pagar:.2f}')

            continuar = input('Deseja adicionar mais itens ao pedido? (s/n): ')
            if continuar.lower() != 's':
                continuar_pedido = False

        except ValueError:
            print('Erro: Por favor, insira um número inteiro para o código e a quantidade.')

    print(f'Total a pagar pelo pedido: R$ {total_pagar:.2f}')

if __name__ == '__main__':
    main()
