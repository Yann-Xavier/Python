{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMWgAH2TX9ZjCF0otu0qRil",
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
        "<a href=\"https://colab.research.google.com/github/Yann-Xavier/Python/blob/main/Reajuste_salarial.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def calcular_novo_salario(salario_atual):\n",
        "    \"\"\"\n",
        "    Calcula o novo salário do funcionário com base no salário atual.\n",
        "\n",
        "    Parâmetros:\n",
        "    salario_atual (float): Salário atual do funcionário.\n",
        "\n",
        "    Retorna:\n",
        "    float: Novo salário do funcionário após o reajuste.\n",
        "    \"\"\"\n",
        "    if salario_atual < 500:\n",
        "        reajuste = 0.15\n",
        "    elif 500 <= salario_atual <= 1000:\n",
        "        reajuste = 0.10\n",
        "    else:\n",
        "        reajuste = 0.05\n",
        "\n",
        "    novo_salario = salario_atual * (1 + reajuste)\n",
        "    return novo_salario\n",
        "\n",
        "def main():\n",
        "    \"\"\"\n",
        "    Função principal do programa.\n",
        "    \"\"\"\n",
        "    print(\"Bem-vindo ao programa de cálculo de novo salário!\")\n",
        "\n",
        "    try:\n",
        "        salario_atual = float(input(\"Digite o salário atual do funcionário: \"))\n",
        "        novo_salario = calcular_novo_salario(salario_atual)\n",
        "\n",
        "        print(f\"O novo salário do funcionário é: R${novo_salario:.2f}\")\n",
        "    except ValueError:\n",
        "        print(\"Erro: Por favor, insira um valor numérico para o salário.\")\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    main()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yhjstwR89nOS",
        "outputId": "d96258fc-a161-44e3-9e90-6121d86f4c64"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Bem-vindo ao programa de verificação de nota!\n",
            "Digite uma nota entre zero e dez: 10\n",
            "A nota digitada foi: 10.0\n"
          ]
        }
      ]
    }
  ]
}
