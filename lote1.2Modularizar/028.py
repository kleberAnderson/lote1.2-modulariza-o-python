#Exercício 028 - Receba o preço atual e a média mensal de um produto. Calcule e mostre o novo preço sabendo que:
#   Venda Mensal         Preço Atual       Preço      Novo
#   < 500                < 30              +          10%
#   >= 500 e < 1000      >= 30 e < 80      +15%
#   >= 1000              >= 80             -          5%
#   obs: para outras condições, preço novo será igual ao preço atual.
def calcular_novo_preco(v, m):
    if v >= 80:
        if m >= 1000:
            v = v * 0.95
            print("Preço atualizado ==> {} R$".format(v))
        else:
            print("Preço atual ==> {} R$".format(v))
    elif v >= 30:
        if 1000 > m >= 500:
            v = v * 1.15
            print("Preço atualizado ==> {} R$".format(v))
        else:
            print("Preço atual ==> {} R$".format(v))
    elif m < 500:
        v = v * 1.1
        print("Preço atualizado ==> {} R$".format(v))
    else:
        print("Preço atual ==> {}".format(v))

preco = float(input("Digite o preço atual do produto: "))
media = float(input("Digite a média de vendas do produto: "))
calcular_novo_preco(preco, media)