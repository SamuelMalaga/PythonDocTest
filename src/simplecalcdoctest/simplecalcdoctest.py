def soma(a, b):

    return a + b

def subtracao(a, b):

    return a - b

def multiplicacao(a, b):

    return a * b

def divisao(a, b):
    """
    Realiza a divisão entre dois números.

    Parâmetros:
    - a (float ou int): O numerador.
    - b (float ou int): O denominador.

    Retorna:
    - float ou str: O resultado da divisão (ou mensagem de erro se b for zero).
    """
    if b != 0:
        return a / b
    else:
        return "Erro: divisão por zero"
