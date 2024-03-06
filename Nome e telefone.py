{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPiYFSovKH+m8K0xX8Ffrh/",
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
        "<a href=\"https://colab.research.google.com/github/Yann-Xavier/Python/blob/main/Nome%20e%20telefone.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def main():\n",
        "    nome = input(\"Digite o nome: \")\n",
        "    telefone = input(\"Digite o telefone: \")\n",
        "\n",
        "    # Verifica se o telefone é um número inteiro\n",
        "    try:\n",
        "        telefone = int(telefone)\n",
        "    except ValueError:\n",
        "        print(\"Erro: O telefone deve ser um número inteiro.\")\n",
        "        return\n",
        "\n",
        "    # Saída com vírgula\n",
        "    saida_virgula = nome + \",\" + str(telefone)\n",
        "    print(\"Saída com vírgula:\", saida_virgula)\n",
        "\n",
        "    # Saída com concatenação\n",
        "    saida_concatenacao = nome + \" \" + str(telefone)\n",
        "    print(\"Saída com concatenação:\", saida_concatenacao)\n",
        "\n",
        "    # Saída com f-string\n",
        "    saida_fstring = f\"{nome} {telefone}\"\n",
        "    print(\"Saída com f-string:\", saida_fstring)\n",
        "\n",
        "    # Saída com format\n",
        "    saida_format = \"{} {}\".format(nome, telefone)\n",
        "    print(\"Saída com format:\", saida_format)\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    main()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pwbDB_WFTNFf",
        "outputId": "14c3904a-7a9d-4a0f-f9e1-c392eb972ece"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o nome: Yann Xavier\n",
            "Digite o telefone: 81995139535\n",
            "Saída com vírgula: Yann Xavier,81995139535\n",
            "Saída com concatenação: Yann Xavier 81995139535\n",
            "Saída com f-string: Yann Xavier 81995139535\n",
            "Saída com format: Yann Xavier 81995139535\n"
          ]
        }
      ]
    }
  ]
}
