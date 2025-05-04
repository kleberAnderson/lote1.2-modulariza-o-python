#Receba a quantidade de horas trabalhadas, o valor por hora, o percentual de desconto e o número de descendentes.
#Calcule  salário que serão as horas trabalhadas X o valor por hora. Calcule o salário líquido ( = Saário Bruto - desconto).
def calculo(qtdhoras, valorhora, percentd, numdep):
    #Calculo do salário bruto
    salb = (qtdHoras * valorHora)
    #Calculo percentual de desconto
    desc = salb * percentD
    #Calculo do salário líquido e nº de descendente
    sall = salb - desc
    sall = sall + (numDep * 100)
    return sall

#A cada dependente será acrescido R$ 100,00 no Salário Líquido. Exiba o salário a receber.
qtdHoras = int(input("Digite a quantidade de horas trabalhadas: "))
valorHora = float(input("Digite o valor por hora: "))
percentD = float(input("Digite o percentual de desconto: "))
numDep = int(input("Digite o nº de dependente: "))
print("Salário a receber: R$ {}".format(calculo(qtdHoras, valorHora, percentD, numDep)))
