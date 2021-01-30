import adivinhacao
import forca

def escolher_jogo():
    print("****************")
    print("Escolha seu jogo")
    print("****************")

    print("(1) Jogo da adivinhação -- (2) Jogo da forca")
    jogo = int(input())
    if (jogo == 1):
        print("Você está jogando o Jogo da adivinhação")
        adivinhacao.jogos()
    if (jogo == 2):
        print("Você está jogando o Jogo da forca")
        forca.jogos()
if (__name__ == "__main__"):
    escolher_jogo()