#Exercício 044 - Receba o número da base e do expoente. Calcule e mostre o valor da potência.
def calcular_potencia(base, expoente):
    resultado = 1
    for i in range(1, expoente + 1):
        resultado *= base
    return resultado


bas = int(input("Digite o número da base: "))
exp = int(input("Digite o número do expoente: "))
print("{} ^ {} ==> {}".format(bas, exp, calcular_potencia(bas, exp)))