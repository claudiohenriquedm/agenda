from funcoes import buscacontato, listacontatos, menu, remcontato, limpa
from contatosteste import contatosteste

contatos = []
id = 0
while True:
    menu()
    opt = input('\nDigite uma opção: ')
    
    if opt == '1': # Adicionar
        limpa()
        nome = input('Digite o nome do contato: ').strip()
        tel = input('Digite o telefone do contato: ').strip()
        email = input('Digite o email do contato: ').strip()
        nomelow = nome.lower()
        limpa()
        print('\nContato adicionado com sucesso!')
        input('\nPressione qualquer tecla para voltar ao menu...')
        contato = {'id':id, 'nome': nome, 'tel': tel, 'email':email, 'nomelow':nomelow}
        id += 1
        contatos.append(contato)
    
    elif opt == '2': # Remover
        limpa()
        id_apagar = int(input('Digite o ID do contato a ser apagado: '))
        remcontato(id_apagar, contatos)
        input('\nPressione qualquer tecla para voltar ao menu...')

    elif opt == '3': # Buscar
        nome = input('Digite o nome do contato que deseja procurar: ')
        buscacontato(nome, contatos)
    
    elif opt == '4': #Listar
        limpa()
        listacontatos(contatos)
        input('\nPressione qualquer tecla para voltar ao menu...')
    
    elif opt == '0': # Sair
        break
