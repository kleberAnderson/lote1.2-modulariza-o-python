#Exercício 043 - Calcule e mostre quantos anos serão necessários para que Ana seja maior que Maria sabendo que Ana tem 1.10m
# e cresce 3 cm ao ano e Maria tem 1.5 m e cresce 2 cm ao ano.
def calcular_anos(ano1, ano2):
    ano = 0
    while ano2 >= ano1:
        ano1 += 0.03
        ano2 += 0.02
        ano += 1
    return ano

ana = float(input("Digite a altura de Ana: "))
maria = float(input("Digite a altura de Maria: "))
print("São necessários {} anos para que Ana seja maior que Maria".format(calcular_anos(ana, maria)))
