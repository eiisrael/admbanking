import csv
from time import sleep

def menu():
        print("~ PAXIS META.UNIVERSE ~")
        print('\n  [1]LOGIN [2]REGISTRO [3]SAIR')

        try:
            escolha = input("\n* Digite sua escolha: ")
            if escolha == '1':
                print("\n\n\n### MANUTENÇAO ###\n\n")
                sleep(1)
                print("\n" * 10)
                menu()
            elif escolha == '2':
                return registro()
            elif escolha == '3':
                print("Até breve. Vejo você mais tarde!")
                exit()
        except KeyboardInterrupt:
            exit()
        else:
            print("404 ERRO")

def registro():

    nome = input("Nome: ")
    cpf = input("CPF:")
    with open('registro.csv','r+') as database: #ABRIU CSV EM LEITURA
        lista = csv.reader(database)          #LEITOR LER O CSV NA DATABASE
        for linha in lista:
            if cpf in linha[0]:
                print("CPF já Existe no sistema. Tente novamente!")
                return registro()

    with open('registro.csv', 'a+') as database:
        senha = input("Senha:")
        database.writelines(f'{cpf},{senha}\n')
        print('Registrado com sucesso!\n'
              f'Seja bem vindo {nome.capitalize()}!')
        exit()

while True:
    menu()
