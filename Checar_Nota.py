{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOUxQ95IOaEz3UUtrpJfcpF",
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
        "<a href=\"https://colab.research.google.com/github/Yann-Xavier/Python/blob/main/Checar_Nota.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def obter_nota():\n",
        "    \"\"\"\n",
        "    Solicita uma nota ao usuário e valida se está entre zero e dez.\n",
        "\n",
        "    Retorna:\n",
        "    float: A nota inserida pelo usuário.\n",
        "    \"\"\"\n",
        "    while True:\n",
        "        try:\n",
        "            nota = float(input(\"Digite uma nota entre zero e dez: \"))\n",
        "            if 0 <= nota <= 10:\n",
        "                return nota\n",
        "            else:\n",
        "                print(\"Erro: A nota deve estar entre zero e dez.\")\n",
        "        except ValueError:\n",
        "            print(\"Erro: Por favor, insira um valor numérico para a nota.\")\n",
        "\n",
        "def main():\n",
        "    \"\"\"\n",
        "    Função principal do programa.\n",
        "    \"\"\"\n",
        "    print(\"Bem-vindo ao programa de verificação de nota!\")\n",
        "\n",
        "    nota = obter_nota()\n",
        "    print(f\"A nota digitada foi: {nota}\")\n",
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