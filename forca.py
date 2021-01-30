def jogos():
    print("***************************")
    print("Bem vindo ao Jogo da forca!")
    print("***************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    acertou = False
    enforcou = False

    print(letras_acertadas)
    while (not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)

    print("Fim do jogo!")

if (__name__ == "__main__"):
    jogos()
