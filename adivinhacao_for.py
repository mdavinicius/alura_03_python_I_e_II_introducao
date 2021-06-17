"""
Fazer um jogo de avinhar o número secreto, indo de 1 a 100.
O jogador poderá escolher a dificuldade (facil - 20 tentativas, medio - 10 e dificil 5)
Tera uma pontuação maxima de 1000 pontos e a cada erro, sera subtratido do total de pontos
a diferença entre o chute e o numero secreto
A cada chute, mostrar se a aposta do usuário foi maior ou menor que o número secreto
Transformar em uma função para usar em outro projeto, mas também deixar habilitado para funcionar
caso o arquivo .py seja inicializado diretamente
Essa versão devera ser feita com loop for
"""

import random


def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    rodada = 1
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Nível: "))
    if (nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou", chute)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos

            if (maior):
                print("O seu chute foi maior que o número secreto.")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {} pontos.".format(numero_secreto, pontos))
            elif (menor):
                print("O seu chute foi menor que o número secreto.")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {} pontos.".format(numero_secreto, pontos))

    print("Fim do jogo!")


if (__name__ == "__main__"):
    jogar()
