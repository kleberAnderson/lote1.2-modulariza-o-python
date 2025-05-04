#Exercício 032 - Receba um número inteiro. Calcule e mostre seu fatorial.
def calcular_fatorial(numero):
    resposta = 1
    for contador in range(numero, 1, -1):
        resposta = resposta * contador
    return resposta


num = int(input("Digite um número para calcular seu fatorial.\n : "))
print("Fatorial do número {} ==> {}".format(num, calcular_fatorial(num)))
