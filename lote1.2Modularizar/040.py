#Exercício 040 - Receba 2 números inteiros. Verifique e mostre todos os números primos existentes entre eles.
def mostrar_numeros_primos(num1,num2):
    while num1 > num2:
        save = num1
        num1 = num2
        num2 = save
    cont = 0
    while num1 <= num2:
        for i in range(1, num1 + 1):
            res = num1 % i
            if res == 0:
                cont = cont + 1
        if cont == 2:
            print(num1)
            num1 = num1 + 1
            cont = 0
        else:
            num1 = num1 + 1
            cont = 0

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
mostrar_numeros_primos(numero1, numero2)

