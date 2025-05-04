#Exercício 021 - Receba 4 notas bimestrais de um aluno. Calcule e mostre a média aritmética. Mostre a mensagem de acordo com a média.
def procedure_media_nota(nota1, nota2, nota3, nota4):
    m = (nota1 + nota2+ nota3 + nota4)/4
    print("Média Bimestral: {}".format(m))

def procedure_mostra_mensagem(nota1, nota2, nota3, nota4):
    m = (nota1 + nota2 + nota3 + nota4) / 4
    if m >= 6:
        print("APROVADO!")
    elif 6 > m >= 3:
        print("EXAME")
    elif m < 3:
        print("RETIDO")

n1 = float(input("Digite a 1º nota bimestral: "))
n2 = float(input("Digite a 2º nota bimestral: "))
n3 = float(input("Digite a 3º nota bimestral: "))
n4 = float(input("Digite a 4º nota bimestral: "))

procedure_media_nota(n1, n2, n3, n4)
procedure_mostra_mensagem(n1, n2, n3, n4)

