{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPIBhnWyZ4SVNpOy/N/xiKT",
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
        "<a href=\"https://colab.research.google.com/github/Yann-Xavier/Python/blob/main/Conversor%20de%20Temperatura.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def celsius_para_fahrenheit(celsius):\n",
        "    return (celsius * 9/5) + 32\n",
        "\n",
        "def fahrenheit_para_celsius(fahrenheit):\n",
        "    return (fahrenheit - 32) * 5/9\n",
        "\n",
        "def celsius_para_kelvin(celsius):\n",
        "    return celsius + 273.15\n",
        "\n",
        "def kelvin_para_celsius(kelvin):\n",
        "    return kelvin - 273.15\n",
        "\n",
        "def fahrenheit_para_kelvin(fahrenheit):\n",
        "    celsius = fahrenheit_para_celsius(fahrenheit)\n",
        "    return celsius_para_kelvin(celsius)\n",
        "\n",
        "def kelvin_para_fahrenheit(kelvin):\n",
        "    celsius = kelvin_para_celsius(kelvin)\n",
        "    return celsius_para_fahrenheit(celsius)\n",
        "\n",
        "def main():\n",
        "    print(\"Bem-vindo ao conversor de temperatura!\")\n",
        "    print(\"Selecione a unidade de temperatura de entrada:\")\n",
        "    print(\"1. Celsius\")\n",
        "    print(\"2. Fahrenheit\")\n",
        "    print(\"3. Kelvin\")\n",
        "\n",
        "    opcao_entrada = int(input(\"Digite o número da sua escolha: \"))\n",
        "\n",
        "    valor_entrada = float(input(\"Digite o valor da temperatura de entrada: \"))\n",
        "\n",
        "    print(\"Selecione a unidade de temperatura de saída:\")\n",
        "    print(\"1. Celsius\")\n",
        "    print(\"2. Fahrenheit\")\n",
        "    print(\"3. Kelvin\")\n",
        "\n",
        "    opcao_saida = int(input(\"Digite o número da sua escolha: \"))\n",
        "\n",
        "    if opcao_entrada == 1:  # Celsius\n",
        "        if opcao_saida == 1:\n",
        "            resultado = valor_entrada\n",
        "        elif opcao_saida == 2:\n",
        "            resultado = celsius_para_fahrenheit(valor_entrada)\n",
        "        elif opcao_saida == 3:\n",
        "            resultado = celsius_para_kelvin(valor_entrada)\n",
        "    elif opcao_entrada == 2:  # Fahrenheit\n",
        "        if opcao_saida == 1:\n",
        "            resultado = fahrenheit_para_celsius(valor_entrada)\n",
        "        elif opcao_saida == 2:\n",
        "            resultado = valor_entrada\n",
        "        elif opcao_saida == 3:\n",
        "            resultado = fahrenheit_para_kelvin(valor_entrada)\n",
        "    elif opcao_entrada == 3:  # Kelvin\n",
        "        if opcao_saida == 1:\n",
        "            resultado = kelvin_para_celsius(valor_entrada)\n",
        "        elif opcao_saida == 2:\n",
        "            resultado = kelvin_para_fahrenheit(valor_entrada)\n",
        "        elif opcao_saida == 3:\n",
        "            resultado = valor_entrada\n",
        "\n",
        "    print(\"O resultado da conversão é:\", resultado)\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    main()\n",
        "\n"
      ],
      "metadata": {
        "id": "svnJN1dH77x1",
        "outputId": "6efce35e-2d73-4fdf-ba4d-5826ed350cf0",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Bem-vindo ao conversor de temperatura!\n",
            "Selecione a unidade de temperatura de entrada:\n",
            "1. Celsius\n",
            "2. Fahrenheit\n",
            "3. Kelvin\n",
            "Digite o número da sua escolha: 1\n",
            "Digite o valor da temperatura de entrada: -273.5\n",
            "Selecione a unidade de temperatura de saída:\n",
            "1. Celsius\n",
            "2. Fahrenheit\n",
            "3. Kelvin\n",
            "Digite o número da sua escolha: 3\n",
            "O resultado da conversão é: -0.35000000000002274\n"
          ]
        }
      ]
    }
  ]
}