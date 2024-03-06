{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMKwSIIVmlQ/pHuXYJEOY9H",
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
        "<a href=\"https://colab.research.google.com/github/Yann-Xavier/Python/blob/main/Checagem_de_dados.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mprthjNNe9z0",
        "outputId": "d25173f8-bad3-48e5-c2a2-3fd308ca0d12"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o salário atual do funcionário: 500\n",
            "O novo salário do funcionário é: R$575.00\n"
          ]
        }
      ],
      "source": [
        "def obter_nome():\n",
        "    while True:\n",
        "        nome = input(\"Digite seu nome: \")\n",
        "        if len(nome) > 3:\n",
        "            return nome\n",
        "        else:\n",
        "            print(\"O nome deve ter mais de 3 caracteres.\")\n",
        "\n",
        "def obter_idade():\n",
        "    while True:\n",
        "        try:\n",
        "            idade = int(input(\"Digite sua idade: \"))\n",
        "            if 0 <= idade <= 150:\n",
        "                return idade\n",
        "            else:\n",
        "                print(\"A idade deve estar entre 0 e 150.\")\n",
        "        except ValueError:\n",
        "            print(\"Por favor, insira um número inteiro para a idade.\")\n",
        "\n",
        "def obter_salario():\n",
        "    while True:\n",
        "        try:\n",
        "            salario = float(input(\"Digite seu salário: \"))\n",
        "            if salario >= 0:\n",
        "                return salario\n",
        "            else:\n",
        "                print(\"O salário não pode ser negativo.\")\n",
        "        except ValueError:\n",
        "            print(\"Por favor, insira um valor numérico para o salário.\")\n",
        "\n",
        "def main():\n",
        "    print(\"Bem-vindo ao programa de cadastro!\")\n",
        "\n",
        "    while True:\n",
        "        nome = obter_nome()\n",
        "        idade = obter_idade()\n",
        "        salario = obter_salario()\n",
        "\n",
        "        # Se todas as condições forem atendidas, exiba os dados e encerre o programa.\n",
        "\n",
        "        print(\"\\nDados cadastrados com sucesso:\")\n",
        "        print(f\"Nome: {nome}\")\n",
        "        print(f\"Idade: {idade}\")\n",
        "        print(f\"Salário: R${salario:.2f}\")\n",
        "\n",
        "        resposta = input(\"\\nDeseja cadastrar outra pessoa? (s/n): \")\n",
        "        if resposta.lower() != 's':\n",
        "            print(\"Programa encerrado.\")\n",
        "            break\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    main()\n"
      ]
    }
  ]
}