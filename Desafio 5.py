{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOJo0kXqndLP38iq4XRQTAw",
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
        "<a href=\"https://colab.research.google.com/github/Yann-Xavier/Python/blob/main/Desafio%205.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def main():\n",
        "    nome = input(\"Digite seu nome: \")\n",
        "    idade = int(input(\"Digite sua idade: \"))\n",
        "    nacionalidade = input(\"Digite sua nacionalidade: \")\n",
        "    hobby = input(\"Digite seu hobby: \")\n",
        "\n",
        "    # Corrigindo o erro na formatação\n",
        "    resultado = f\"{nome}, {idade}, {nacionalidade}, {hobby}\"\n",
        "\n",
        "    # Imprimindo o resultado\n",
        "    print(resultado)\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    main()"
      ],
      "metadata": {
        "id": "HOwMANZk801x",
        "outputId": "f84b07fd-62ad-4047-962f-36e158d98908",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite seu nome: Yann Xavier\n",
            "Digite sua idade: 35\n",
            "Digite sua nacionalidade: Brasileiro\n",
            "Digite seu hobby: Gamer\n",
            "Yann Xavier, 35, Brasileiro, Gamer\n"
          ]
        }
      ]
    }
  ]
}
