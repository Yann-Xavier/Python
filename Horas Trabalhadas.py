{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPjbvjYuxLrWG9AaVPU8qcp",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Yann-Xavier/Python/blob/main/Horas%20Trabalhadas.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def validar_input(mensagem):\n",
        "    while True:\n",
        "        try:\n",
        "            entrada = input(mensagem)\n",
        "            if ',' in entrada:\n",
        "                print(\"Caracteres inválidos. Use apenas ponto (.) para separar decimais.\")\n",
        "            else:\n",
        "                return float(entrada)\n",
        "        except ValueError:\n",
        "            print(\"Entrada inválida. Por favor, digite um número válido.\")\n",
        "\n",
        "def calcular_salario():\n",
        "    valor_hora = validar_input(\"Digite o valor ganho por hora de trabalho: \")\n",
        "    horas_trabalhadas = validar_input(\"Digite o valor de horas trabalhadas neste mês: \")\n",
        "    pagamento = valor_hora * horas_trabalhadas\n",
        "    print(\"Você trabalhou por\", horas_trabalhadas, \"horas.\")\n",
        "    print(\"O valor da hora trabalhada é de R$\", valor_hora)\n",
        "    print(\"O pagamento que deve ser recebido é de: R$\", pagamento)\n",
        "    return pagamento\n",
        "\n",
        "def main():\n",
        "    while True:\n",
        "        calcular_salario()\n",
        "        resposta = input(\"Deseja realizar um novo cálculo? (s/n) \")\n",
        "        if resposta != 's':\n",
        "            break\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    main()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "m3PENS9u82SZ",
        "outputId": "39ef701c-5eb7-4181-bc84-4daa4f13101c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o valor ganho por hora de trabalho: 12,33\n",
            "Caracteres inválidos. Use apenas ponto (.) para separar decimais.\n",
            "Digite o valor ganho por hora de trabalho: 13.36\n",
            "Digite o valor de horas trabalhadas neste mês: 244\n",
            "Você trabalhou por 244.0 horas.\n",
            "O valor da hora trabalhada é de R$ 13.36\n",
            "O pagamento que deve ser recebido é de: R$ 3259.8399999999997\n"
          ]
        }
      ]
    }
  ]
}
