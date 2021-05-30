"""Replicar o jogo de forca aprendido no curso, puxando a palavra secreta de forma aletaróia de um
arquivo como forma de banco de dados. As tentativas do jogador serão o mesmo número de caracteres
que a palavra secreta possuir."""

import random

def jogar_teste_2():
    print("*********************************")
    print("***Bem vindo ao jogo de Forca!***")
    print("*********************************")

    lista_de_palavras = []

    with open("palavras.txt", "r") as banco_de_palavras:
        for palavra in banco_de_palavras:
            lista_de_palavras.append(palavra.strip().upper())
    palavra_secreta = lista_de_palavras[random.randint(0,3)]

    palavra_forca = []
    for x in palavra_secreta:
        palavra_forca.append("_")
    print(palavra_forca)

    contador = 0
    tentativas = len(palavra_secreta)

    while(tentativas > 0):
        chute = str(input("Qual letra? ")).strip().upper()
        contador = 0

        for x in palavra_secreta:
            if(chute == x):
                palavra_forca[contador] = chute
            contador += 1

        if(chute not in palavra_secreta):
            tentativas -= 1
            print("Errou! Tentativa(s) {}".format(tentativas))

        if(tentativas == 0):
            print("Você perdeu! A palavra secreta era {}!".format(palavra_secreta))
        print(palavra_forca)

        if("_" not in palavra_forca):
            print("Você ganhou! A palavra secreta era {}!".format(palavra_secreta))
            break

    print("***** Fim de jogo! *****")

if(__name__ == "__main__"):
    jogar_teste_2()