"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os 

lista_menu = 'i', 'a', 'l' # menu de opções disponíveis para o usuário utilizar
lista_compras = [] # define uma lista de compras vazia

while True:
    print ('Escolha uma opção: ')
    opcao = input ('[i]nserir [a]pagar [l]listar: ')
    
    # inserir elemento na lista
    if opcao == 'i':
        os.system('clear')
        novo_elemento = input('Valor: ')
        lista_compras.append(novo_elemento)

    # listar todos os elementos da lista
    elif opcao == 'l':
        if len(lista_compras) < 1:
            print ('Lista de compras está vazia!')
            continue

        os.system('clear')
        for indice, item in enumerate(lista_compras):
            print(indice, item)

    # apagar um elemento da lista
    elif opcao == 'a':
        if len(lista_compras) == 0:
            print('Lista de compras está vazia')
            continue

        os.system('clear')
        indice_a_remover= input ('Índice: ')
        try:
            indice = int(indice_a_remover)
            del lista_compras[indice]
        except ValueError:
            print ('Valor inválido! Digite um número inteiro.')
        except IndexError:
            print ('Índice não existe na lista de compras atual')
        except Exception:
            print ('Erro desconhecido')    
    else:
        print ('Você deve escolher uma das opções disponíveis')

