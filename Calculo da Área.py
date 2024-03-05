{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPWJ55cjMxkGRSOPMzfKh7t",
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
        "<a href=\"https://colab.research.google.com/github/Yann-Xavier/Python/blob/main/Calculo%20da%20%C3%81rea.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import math\n",
        "\n",
        "def calcular_area_circulo(raio):\n",
        "    return math.pi * raio ** 2\n",
        "\n",
        "def calcular_area_retangulo(base, altura):\n",
        "    return base * altura\n",
        "\n",
        "def calcular_area_triangulo(base, altura):\n",
        "    return (base * altura) / 2\n",
        "\n",
        "def main():\n",
        "    while True:\n",
        "        print(\"\\nCALCULADORA DE ÁREAS DE FORMAS GEOMÉTRICAS\")\n",
        "        print(\"Escolha a forma geométrica para calcular a área:\")\n",
        "        print(\"1. Círculo\")\n",
        "        print(\"2. Retângulo\")\n",
        "        print(\"3. Triângulo\")\n",
        "        print(\"0. Sair\")\n",
        "\n",
        "        opcao = input(\"Digite o número correspondente à forma desejada: \")\n",
        "\n",
        "        if opcao == \"1\":\n",
        "            try:\n",
        "                raio = float(input(\"Digite o raio do círculo: \"))\n",
        "                area = calcular_area_circulo(raio)\n",
        "                print(\"A área do círculo é:\", area)\n",
        "            except ValueError:\n",
        "                print(\"Por favor, insira um valor numérico válido para o raio.\")\n",
        "        elif opcao == \"2\":\n",
        "            try:\n",
        "                base = float(input(\"Digite a base do retângulo: \"))\n",
        "                altura = float(input(\"Digite a altura do retângulo: \"))\n",
        "                area = calcular_area_retangulo(base, altura)\n",
        "                print(\"A área do retângulo é:\", area)\n",
        "            except ValueError:\n",
        "                print(\"Por favor, insira valores numéricos válidos para a base e altura.\")\n",
        "        elif opcao == \"3\":\n",
        "            try:\n",
        "                base = float(input(\"Digite a base do triângulo: \"))\n",
        "                altura = float(input(\"Digite a altura do triângulo: \"))\n",
        "                area = calcular_area_triangulo(base, altura)\n",
        "                print(\"A área do triângulo é:\", area)\n",
        "            except ValueError:\n",
        "                print(\"Por favor, insira valores numéricos válidos para a base e altura.\")\n",
        "        elif opcao == \"0\":\n",
        "            print(\"Obrigado por usar a calculadora de áreas. Até logo!\")\n",
        "            break\n",
        "        else:\n",
        "            print(\"Opção inválida. Por favor, escolha uma opção válida.\")\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    main()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7aERndcy4TPl",
        "outputId": "4b7abaec-ae3c-4b16-86b9-4dc22f1ca414"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "CALCULADORA DE ÁREAS DE FORMAS GEOMÉTRICAS\n",
            "Escolha a forma geométrica para calcular a área:\n",
            "1. Círculo\n",
            "2. Retângulo\n",
            "3. Triângulo\n",
            "0. Sair\n"
          ]
        }
      ]
    }
  ]
}
