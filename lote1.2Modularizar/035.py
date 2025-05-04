#Exercício 032 - Receba 2 números inteiros, verifique qual o maior entre eles. Calcule e mostre o resultado da somatória dos números ímpares entre esses valores.
def somar_numeros_impares(numero1, numero2):
    soma = 0
    if numero1 == numero2:
        print("Números iguais!")
    else:
        while numero1 > numero2:
            salvar = numero1
            numero1 = numero2
            numero2 = salvar
        print("Maior número ==> {}".format(numero2))
        if numero1 % 2 == 0:
            for i in range(numero1 + 1, numero2 + 1, +2):
                soma += i
        else:
            for i in range(numero1, numero2 + 1, 2):
                soma += i
    return print("Somatória dos números ímpares ==> {}".format(soma))

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
somar_numeros_impares(num1, num2)