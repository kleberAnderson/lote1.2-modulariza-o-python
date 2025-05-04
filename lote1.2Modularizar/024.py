#Exercício 024 - Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3:
def verificar_numero(n):
    if n % 2 == 0 and num % 3 == 0:
        print("{} é divisível por 2 e 3.".format(n))
    elif n % 2 != 0:
        print("{}, não é divisível por 2".format(n))
    elif n % 3 != 0:
        print("{}, não é divisível por 3".format(n))

num = int(input("Digite um valor inteiro: "))
verificar_numero(num)