import random

def jogos():
    print("*******************")
    print("Jogo da adivinhação")
    print("*******************")

    print("Qual modo você gostaria de jogar?")
    print("(Modo 1: + adivinhações) -- (Modo 2 + tentativas)")
    modo_str = input("Digite 1 ou 2: ")
    modo = int(modo_str)
    pontos = 1000
    if (modo == 1):
        print("Qual nível de dificuldade?")
        print("(1) Fácil -- (2) Médio -- (3) Difícil")
        dificuldade_str = input()
        dificuldade = int(dificuldade_str)
        total_de_tentativas = 3

        if (dificuldade == 1):
                print("Dificuldade = Fácil")
                numero_secreto = random.randrange(1, 10)
                for rodada in range(1, total_de_tentativas + 1):
                    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
                    chute_str = input("Digite um número entre 1 e 10: ")
                    chute = int(chute_str)

                    if chute < 1 or chute > 100:
                        print("Você deve digitar um número entre 1 e 100!")

                    acertou = chute == numero_secreto
                    menor = chute < numero_secreto
                    maior = chute > numero_secreto

                    if (acertou):
                        print("Você acertou e fez {} pontos!", format(pontos))
                        break
                    else:
                        if (maior):
                            print("Você errou, o número digitado é maior que o número secreto")
                        elif (menor):
                            print("Você errou, o número digitado é menor que o número secreto")
                        pontos_perdidos = abs(numero_secreto - chute)/ 3
                        pontos = pontos - pontos_perdidos
        elif (dificuldade == 2):
                print("Dificudade = Médio")
                numero_secreto = random.randrange(1, 50)
                for rodada in range(1, total_de_tentativas + 1):
                    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
                    chute_str = input("Digite um número entre 1 e 50: ")
                    chute = int(chute_str)

                    if chute < 1 or chute > 100:
                        print("Você deve digitar um número entre 1 e 100!")

                    acertou = chute == numero_secreto
                    menor = chute < numero_secreto
                    maior = chute > numero_secreto

                    if (acertou):
                        print("Você acertou e fez {} pontos!", format(pontos))
                        break
                    else:
                        if (maior):
                            print("Você errou, o número digitado é maior que o número secreto")
                        elif (menor):
                            print("Você errou, o número digitado é menor que o número secreto")
                        pontos_perdidos = abs(numero_secreto - chute)/ 3
                        pontos = pontos - pontos_perdidos
        elif (dificuldade == 3):
                print("Dificuldade = Difícil")
                numero_secreto = random.randrange(1, 100)
                for rodada in range(1, total_de_tentativas + 1):
                    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
                    chute_str = input("Digite um número entre 1 e 100: ")
                    chute = int(chute_str)

                    if chute < 1 or chute > 100:
                        print("Você deve digitar um número entre 1 e 100!")

                    acertou = chute == numero_secreto
                    menor = chute < numero_secreto
                    maior = chute > numero_secreto

                    if (acertou):
                        print("Você acertou e fez {} pontos!", format(pontos))
                        break
                    else:
                        if (maior):
                            print("Você errou, o número digitado é maior que o número secreto")
                        elif (menor):
                            print("Você errou, o número digitado é menor que o número secreto")
                        pontos_perdidos = abs(numero_secreto - chute)/ 3
                        pontos = pontos - pontos_perdidos
        else:
            print("Digite um valor válido")

        print("Fim do jogo!")
    elif (modo == 2):
        print("Qual nível de dificuldade?")
        print("(1) Fácil -- (2) Médio -- (3) Difícil")
        dificuldade_str = input()
        dificuldade = int(dificuldade_str)
        total_de_tentativas = 0
        if (dificuldade == 1):
            total_de_tentativas = 10
        elif (dificuldade == 2):
            total_de_tentativas = 5
        elif (dificuldade == 3):
            total_de_tentativas = 3
        numero_secreto = random.randrange(1, 100)
        for rodada in range(1, total_de_tentativas + 1):
            print("Tentativa {} de {}".format(rodada, total_de_tentativas))
            chute_str = input("Digite um número entre 1 e 100: ")
            chute = int(chute_str)

            if chute < 1 or chute > 100:
                print("Você deve digitar um número entre 1 e 100!")

            acertou = chute == numero_secreto
            menor = chute < numero_secreto
            maior = chute > numero_secreto
            if (acertou):
                print("Você acertou e fez {} pontos!", format(pontos))
                break
            else:
                if (maior):
                    print("Você errou, o número digitado é maior que o número secreto")
                elif (menor):
                    print("Você errou, o número digitado é menor que o número secreto")
                pontos_perdidos = abs(numero_secreto - chute)/ 3
                pontos = pontos - pontos_perdidos
    print("O número secreto era:", numero_secreto)
    print("Pontuação:", pontos)
if (__name__ == "__main__"):
    jogos()
