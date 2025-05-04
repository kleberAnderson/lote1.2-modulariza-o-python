#Exercício 036 - Receba um número N. Calcule e mostre a série 1 + 1/1! + 1/2! + ... +1/N!
def calcular_serie(numero):
    soma = 0
    for i in range(0, numero + 1):
        print("{} / {} ==> {}".format(1, calcular_fatorial(i), 1 / calcular_fatorial(i)))
        soma += (1 / calcular_fatorial(i))
    return print("Resultado da somatória ==> {}".format(soma))

def calcular_fatorial(numero):
    multi = 1
    for i in range(numero, 1, -1):
        multi *= i
    return multi

num = int(input("Digite um número para calcular a série: "))
calcular_serie(num)