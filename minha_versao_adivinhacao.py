"""Replicar o jogo de adivinhação aprendido no curso, onde o jogador precisa acertar o número dentro de um
range de números de 0 a 100, com 20 - 10 - 5 tentativas, conforme nível escolhido pelo jogador."""

import random

def jogar_teste():
    numero_secreto = random.randrange(1,101)
    #print(numero_secreto)

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    print("Qual nível você quer jogar?")
    print("(1)Fácil (2)Médio (3)Difícil")

    escolha = False
    while(not escolha):
        nivel = int(input("Nível: "))
        if (nivel == 1 or nivel == 2 or nivel == 3):
            break

    if(nivel == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 10
    else:
        tentativas = 5

    contador = 1

    while(contador <= tentativas):
        print("Tentativa {} de {}".format(contador, tentativas))
        chute = int(input("Qual seu chute: "))
        print("Você digitou {}".format(chute))

        if(chute == numero_secreto):
            print("Parabéns Panaiiiiiiiiiiiiii, você acertou!")
            break
        else:
            if(chute < numero_secreto):
                print("Seu chute foi menor que o número secreto")
            elif(chute > numero_secreto):
                print("Seu chute foi maior que o número secreto")
        contador += 1
        if(contador > tentativas):
            print("Você perdeu. O número secreto era {}".format(numero_secreto))

    print("***** Fim de jogo! *****")

if(__name__ == "__main__"):
    jogar_teste()