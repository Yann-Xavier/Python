{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN7tcMzGfr4TiZj3wmj1bsi",
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
        "<a href=\"https://colab.research.google.com/github/Yann-Xavier/Python/blob/main/Concatenando.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def obter_data_formatada(dia, mes, ano):\n",
        "    # Formata a data no formato desejado (dd/mm/aaaa)\n",
        "    data_formatada = f\"{dia:02d}/{mes:02d}/{ano}\"\n",
        "    return data_formatada\n",
        "\n",
        "# Solicita ao usuário que insira o dia, mês e ano de nascimento\n",
        "dia_nascimento = int(input(\"Digite o dia de nascimento: \"))\n",
        "mes_nascimento = int(input(\"Digite o mês de nascimento: \"))\n",
        "ano_nascimento = int(input(\"Digite o ano de nascimento: \"))\n",
        "\n",
        "# Obtém a data formatada\n",
        "data_formatada = obter_data_formatada(dia_nascimento, mes_nascimento, ano_nascimento)\n",
        "\n",
        "# Exibe a data formatada na tela\n",
        "print(f\"Data de nascimento formatada: {data_formatada}\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zDjpF9vMRC3z",
        "outputId": "9c04a3c4-c5a3-4e7d-d765-0d4c963b6661"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o dia de nascimento: 25\n",
            "Digite o mês de nascimento: 10\n",
            "Digite o ano de nascimento: 1988\n",
            "Data de nascimento formatada: 25/10/1988\n"
          ]
        }
      ]
    }
  ]
}
