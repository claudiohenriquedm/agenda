from funcoes import buscacontato, listacontatos, menu, remcontato, limpa, carregar, salvar, geraid

contatos = carregar()

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
        id = geraid(contatos)
        contato = {'nome': nome, 'tel': tel, 'email':email, 'nomelow':nomelow, 'id': id}
        contatos.append(contato)
        salvar(contatos)
    
    elif opt == '2': # Remover
        id_apagar = int(input('Digite o ID do contato a ser apagado: '))
        remcontato(id_apagar, contatos)
        salvar(contatos)

    elif opt == '3': # Buscar
        nome = input('Digite o nome do contato que deseja procurar: ')
        buscacontato(nome, contatos)
    
    elif opt == '4': #Listar
        limpa()
        listacontatos(contatos)
    
    elif opt == '0': # Sair
        break