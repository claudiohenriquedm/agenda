import os
import json
import random

def limpa():
    print('\n' * 130)

def menu():
    print('----------')
    print('Lista de contatos:')
    print('1 - Adicionar contato')
    print('2 - Remover contato')
    print('3 - Buscar contato')
    print('4 - Listar contatos')
    print('0 - Sair')
    print('----------')

def remcontato(id, lista):
    contato_encontrado = False
    for contato in lista:
        if contato['id'] == id:
            lista.remove(contato)
            contato_encontrado = True
            print('\nContato removido com sucesso.')
            break
    if contato_encontrado == False:
        print('\nContato não encontrado')
             
def buscacontato(nome, lista):
    encontrados = []
    for contato in lista:
        if contato['nomelow'].startswith(nome):
            encontrados.append(contato)
    if len(encontrados) == 0:
        print('\nNome não encontrado')    
    else:
        return listacontatos(encontrados)

def listacontatos(lista):
    for contato in lista:
        print('--------')
        print('Nome: ',contato['nome'])
        print('Telefone: ',contato['tel'])
        print('E-mail: ',contato['email'])
        print('ID: ',contato['id'])

def carregar():
    contatos = []
    if os.path.exists('contatos.json'):
        with open('contatos.json', 'r') as f:
            contatos = json.load(f)
    return contatos

def salvar(dicionario):
    with open('contatos.json', 'w') as f:
        json.dump(dicionario, f)

def geraid(lista):
    id = random.randint(1000,9999)
    for ctt in lista:
        if ctt['id'] == id:
            id = random.randint(1000,9999)
        return id