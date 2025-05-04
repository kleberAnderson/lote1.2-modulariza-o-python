#Exercício 026 - Receba 2 números inteiros. Verifique e mostre se o maior número é multiplo do menor.
def verificar_multiplicidade(n1, n2):
    if n1 > n2:
        if n1 % n2 == 0:
            print("{} é multiplo de {}.".format(n1,n2))
        else:
            print("Não existe multiplicidade")
    elif n2 > n1:
        if n2 % n1 == 0:
            print("{} é multiplo de {}".format(n2, n1))
        else:
            print("Não existe multiplicidade")
    else:
        print("Números iguais!")


num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
verificar_multiplicidade(num1, num2)