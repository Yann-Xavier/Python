{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNAuXQDqVD7gbCL0qpZBKAw",
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
        "<a href=\"https://colab.research.google.com/github/Yann-Xavier/Python/blob/main/Desafio%205%20-%20Conversor.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def main():\n",
        "  \"\"\"\n",
        "  Solicita ao usuário três tipos de números (inteiro, decimal e texto)\n",
        "  e converte entre eles, imprimindo o resultado e a classificação de cada um.\n",
        "  \"\"\"\n",
        "\n",
        "  # Solicitando ao usuário um número qualquer inteiro\n",
        "  numero_inteiro = int(input(\"Digite um número inteiro: \"))\n",
        "\n",
        "  # Solicitando ao usuário um número decimal\n",
        "  numero_decimal = float(input(\"Digite um número decimal: \"))\n",
        "\n",
        "  # Solicitando ao usuário um número do tipo texto\n",
        "  numero_texto = input(\"Digite um número do tipo texto: \")\n",
        "\n",
        "  # Convertendo o número inteiro para decimal\n",
        "  numero_inteiro_para_decimal = float(numero_inteiro)\n",
        "\n",
        "  # Convertendo o número decimal para texto\n",
        "  numero_decimal_para_texto = str(numero_decimal)\n",
        "\n",
        "  # Convertendo o número texto para inteiro\n",
        "  numero_texto_para_inteiro = int(numero_texto.strip()) if numero_texto.strip().isdigit() else None\n",
        "\n",
        "  # Imprimindo o resultado e sua classificação\n",
        "  print(f\"Número inteiro: {numero_inteiro:d}\")\n",
        "  print(f\"Número decimal: {numero_decimal:f}\")\n",
        "  print(f\"Número texto: {numero_texto}\")\n",
        "  print(f\"Número inteiro convertido para decimal: {numero_inteiro_para_decimal:f}\")\n",
        "  print(f\"Número decimal convertido para texto: {numero_decimal_para_texto}\")\n",
        "\n",
        "  if numero_texto_para_inteiro is not None:\n",
        "    print(f\"Número texto convertido para inteiro: {numero_texto_para_inteiro:d}\")\n",
        "  else:\n",
        "    print(f\"O texto '{numero_texto}' não é um número inteiro válido.\")\n",
        "\n",
        "  print(f\"Classificação do número inteiro: {type(numero_inteiro)}\")\n",
        "  print(f\"Classificação do número decimal: {type(numero_decimal)}\")\n",
        "  print(f\"Classificação do número texto: {type(numero_texto)}\")\n",
        "  print(f\"Classificação do número inteiro convertido para decimal: {type(numero_inteiro_para_decimal)}\")\n",
        "  print(f\"Classificação do número decimal convertido para texto: {type(numero_decimal_para_texto)}\")\n",
        "\n",
        "  if numero_texto_para_inteiro is not None:\n",
        "    print(f\"Classificação do número texto convertido para inteiro: {type(numero_texto_para_inteiro)}\")\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "  main()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cV2seXQmOX0J",
        "outputId": "8d681a47-8d05-483a-b69a-23a5bc577cdb"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite um número inteiro: 10\n",
            "Digite um número decimal: 100\n",
            "Digite um número do tipo texto: casa\n",
            "Número inteiro: 10\n",
            "Número decimal: 100.000000\n",
            "Número texto: casa\n",
            "Número inteiro convertido para decimal: 10.000000\n",
            "Número decimal convertido para texto: 100.0\n",
            "O texto 'casa' não é um número inteiro válido.\n",
            "Classificação do número inteiro: <class 'int'>\n",
            "Classificação do número decimal: <class 'float'>\n",
            "Classificação do número texto: <class 'str'>\n",
            "Classificação do número inteiro convertido para decimal: <class 'float'>\n",
            "Classificação do número decimal convertido para texto: <class 'str'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "n0gYe3FjOo3R"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
