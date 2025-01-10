from os import system
system('cls')

import csv

entrada = open('./brasileirao.csv', 'r', encoding="utf-8")

arquivo = csv.reader(entrada, delimiter=',')
m=0
v=0
op="s"
times_brasileirao_2011 = [
    "América-MG", "Atlético-GO", "Atlético-MG", "Botafogo", "Ceará", "Corinthians",
    "Cruzeiro", "Flamengo", "Fluminense", "Figueirense", "Grêmio", "Internacional", 
    "Palmeiras", "Paraná", "Santos", "São Paulo", "Vasco da Gama", "Vitória", "Fluminense", "Coritiba"
]
while op == "s":
    time=input("Digite um time\n")
    while time == "" not in times_brasileirao_2011 or len(time)<4:
        time=input("Digite um time válido\n")

    for coluna in arquivo:    
        if coluna[7]==time and coluna[17]>coluna[18]:
            m=m+1
        elif coluna[8]==time and coluna[17]<coluna[18]:
            v=v+1
    print(m+v,"vitórias")
    op=input("Deseja procurar outro time? s/n\n").lower()

entrada.close()
print("Fim do código")
