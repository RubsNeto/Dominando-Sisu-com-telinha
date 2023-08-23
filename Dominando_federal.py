import os

print('Bem Vindo ao Dominando a Federal!\nEste é um programa criado por Rubens Gonçalves, professor do Guia: Dominando o sisu')
print('com o intuito de ajudar jovens a conseguirem uma vaga na federal de seus sonhos!\n')

print("Digite os valores sem o ponto/virgula!")

nota_linguagens = input('Digite sua nota de Linguagens, Códigos e suas Tecnologias: ')

while nota_linguagens.isnumeric()==False or float(nota_linguagens) < 3000 or float(nota_linguagens) > 10000:
    nota_linguagens = input('Valor inválido. Digite novamente. ')

nota_linguagens = float(nota_linguagens)/10


nota_humanas    = input('Digite sua nota de Ciências Humanas e suas Tecnologias: ')

while nota_humanas.isnumeric()==False or float(nota_humanas) < 3000 or float(nota_humanas) > 10000:
    nota_humanas = input('Valor inválido. Digite novamente. ')

nota_humanas=float(nota_humanas)/10

nota_natureza   = input('Digite sua nota de Ciências da Natureza e suas Tecnologias: ')

while nota_natureza.isnumeric()==False or float(nota_natureza) < 3000 or float(nota_natureza) > 10000:
    nota_natureza = input('Valor inválido. Digite novamente. ')

nota_natureza= float(nota_natureza)/10

nota_matematica = input('Digite sua nota de Matemática e suas Tecnologias: ')

while nota_matematica.isnumeric()==False or float(nota_matematica) < 3000 or float(nota_matematica) > 10000:
    nota_matematica = input('Valor inválido. Digite novamente. ')

nota_matematica=float(nota_matematica)/10

nota_redacao    = input('Digite sua nota de Redação: ')

while nota_redacao.isnumeric()==False or float(nota_redacao) < 3000 or float(nota_redacao) > 10000:
    nota_redacao = input('Valor inválido. Digite novamente. ')

nota_redacao =float(nota_redacao )/10


peso_linguagens = [ 2, 2, 2, 2, 2, 2.5, 2.5, 3 ]
peso_humanas = [ 1, 1, 1, 1.5, 1, 3, 2, 2.5 ]
peso_natureza = [ 2.5, 1.5, 1, 3, 3, 1, 1, 1 ]
peso_matematica = [ 3, 4, 4, 1.5, 2, 1, 2, 1 ]
peso_redacao = [ 1.5, 1.5, 2, 2, 2, 2.5, 2.5, 2.5 ]


roda=0
nota_final = list()

while roda != len(peso_linguagens):
    validando_casas_decimanis = (nota_linguagens * float(peso_linguagens[roda]) +  nota_humanas * float(peso_humanas[roda])  +  nota_natureza * float(peso_natureza[roda])  +  nota_matematica * float(peso_matematica[roda])  +  nota_redacao * float(peso_redacao[roda]))/10 
    nota_final.append(round(validando_casas_decimanis,2))
    roda+=1

for numero_grupo in range(1,9):

    print(f'\nSua nota no grupo {numero_grupo} é: ',nota_final[numero_grupo-1])
    print("\nChamada regular: ")

    with open(f"nota/G{numero_grupo}/G{numero_grupo}_media_chamada_regular.txt", mode="r", encoding="utf-8") as media_regular:
        for linha in media_regular:
            tira_traco = linha.split('-')
            media_nota_antiga = float(tira_traco[4].split('\n')[0])

            if nota_final[numero_grupo - 1] >= media_nota_antiga:
                print('Curso:',tira_traco[0],'Turno:',tira_traco[1],'Grau:',tira_traco[2],'Cidade:',tira_traco[3],' Nota média: ',tira_traco[4])

    print('\nSegunda chamada:')

    with open(f"nota/G{numero_grupo}/G{numero_grupo}_media_segunda_chamada.txt", mode="r", encoding="utf-8") as media_regular:
        for ver in media_regular:
            tira_traco = ver.split('-')
            media_nota_antiga = float(tira_traco[4].split('\n')[0])

            if nota_final[numero_grupo - 1] >= media_nota_antiga:
                print('Curso:',tira_traco[0],'Turno:',tira_traco[1],'Grau:',tira_traco[2],'Cidade:',tira_traco[3],' Nota média: ',tira_traco[4])

os.system("Pause")
