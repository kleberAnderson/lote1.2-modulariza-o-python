#Exercício 039 - Calcule a quantidade de grãos contidos em um tabuleiro de xadrez onde:
#Casa: 1 2 3 4 ... 64
#Qtde: 1 2 4 8 ... N

def calcular_graos(c):
    soma = 0
    for i in range(c):
        qtde = 2 ** i
        print("Casa ({}) ==> {} grãos".format(i + 1, qtde))
        soma += qtde
    print("Total ==> {} grãos".format(soma))

casa = int(input("Digite a quantidade de casas de um tabuleiro:"))
calcular_graos(casa)