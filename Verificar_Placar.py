{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP5cMwKzsz43BtKzvHpZtUW",
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
        "<a href=\"https://colab.research.google.com/github/Yann-Xavier/Python/blob/main/Verificar_Placar.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def verificar_resultado(gols_time1, gols_time2, nome_time1, nome_time2):\n",
        "    \"\"\"\n",
        "    Verifica o resultado do jogo com base nos gols de cada time.\n",
        "\n",
        "    Parâmetros:\n",
        "    gols_time1 (int): Gols marcados pelo primeiro time.\n",
        "    gols_time2 (int): Gols marcados pelo segundo time.\n",
        "    nome_time1 (str): Nome do primeiro time.\n",
        "    nome_time2 (str): Nome do segundo time.\n",
        "\n",
        "    Retorna:\n",
        "    str: O resultado do jogo no formato do placar.\n",
        "    \"\"\"\n",
        "    return f\"{nome_time1} {gols_time1}x{gols_time2} {nome_time2}\"\n",
        "\n",
        "def main():\n",
        "    \"\"\"\n",
        "    Função principal do programa.\n",
        "    \"\"\"\n",
        "    print(\"Bem-vindo ao verificador de resultado de jogo!\")\n",
        "\n",
        "    nome_time1 = input(\"Digite o nome do primeiro time: \")\n",
        "    nome_time2 = input(\"Digite o nome do segundo time: \")\n",
        "\n",
        "    while True:\n",
        "        try:\n",
        "            gols_time1 = int(input(f\"Digite os gols marcados pelo {nome_time1}: \"))\n",
        "            gols_time2 = int(input(f\"Digite os gols marcados pelo {nome_time2}: \"))\n",
        "\n",
        "            resultado = verificar_resultado(gols_time1, gols_time2, nome_time1, nome_time2)\n",
        "            print(\"Placar do jogo:\", resultado)\n",
        "            break\n",
        "        except ValueError:\n",
        "            print(\"Erro: Por favor, insira um número inteiro para os gols.\")\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    main()\n",
        "\n"
      ],
      "metadata": {
        "id": "yhjstwR89nOS"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
