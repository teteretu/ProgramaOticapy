'''
Created on 28 de abr de 2017

@author: Math
'''
from base.Cliente import Cliente
from base.Endereco import Endereco
from programa.Fachada import Fachada

if __name__ == '__main__':
    pass

"""=============
====CLIENTE=====
============="""

def inserirCliente():
    cliente = Cliente()
    endereco = Endereco()
    
    cliente.setNome(input("Qual o seu nome?\n"))
    cliente.setNascimento(input("Qual sua data de nascimento?\n"))
    cliente.setCpf(input("Qual o seu cpf?\n"))
    cliente.setTelefone(input("Qual o seu telefone?\n"))
    endereco.setCep(input("Qual o seu cep?\n"))
    endereco.setEstado(input("Qual o seu estado?\n"))
    endereco.setCidade(input("Qual a sua cidade?\n"))
    endereco.setRua(input("Qual a sua rua?\n"))
    cliente.setEndereco(endereco)
    
    fachada.inserir(cliente)


def atualizarCliente():
    cliente = Cliente()
    endereco = Endereco()
    
    cliente.setNome(input("Qual o seu nome?\n"))
    cliente.setNascimento(input("Qual sua data de nascimento?\n"))
    cliente.setCpf(input("Qual o seu cpf?\n"))
    cliente.setTelefone(input("Qual o seu telefone?\n"))
    endereco.setCep(input("Qual o seu cep?\n"))
    endereco.setEstado(input("Qual o seu estado?\n"))
    endereco.setCidade(input("Qual a sua cidade\n?"))
    endereco.setRua(input("Qual a sua rua\n?"))
    cliente.setEndereco(endereco)
    
    fachada.atualizar(cliente)


def removerCliente():
    identificacao = input("Qual id do cliente que voce deseja remover?\n")
    removerCliente = fachada.procurar(identificacao)
    
    fachada.remover(removerCliente)


def procurarCliente():
    identificacao = input("Qual id do cliente que voce deseja procurar?\n")
    
    fachada.procurarCliente(identificacao)
    

def todosClientes():
    
    todosClientes = fachada.todosClientes()
    print (todosClientes)

def openCliente():
    run = True
    while run:
        opcaoCliente = input("    CLIENTE\n 1. Inserir\n 2. Atualizar\n 3. Remover\n 4. Procurar\n 5. Todos\n 0. Voltar Menu\n")
        
        if opcaoCliente == '1':
            inserirCliente()
        elif opcaoCliente == '2':
            atualizarCliente()
        elif opcaoCliente == '3':
            removerCliente()
        elif opcaoCliente == '4':
            procurarCliente()
        elif opcaoCliente == '5':
            todosClientes()
        elif opcaoCliente == '0':
            run = False
        else:
            print("Opcao nao confere")
    

"""=============
==FUNCIONARIO===
============="""

def openFuncionario():
    pass

"""=============
===ITEM VENDA===
============="""

def openItemVenda():
    pass

"""=============
====PRODUTO=====
============="""

def openProduto():
    pass 

"""=============
=====VENDA======
============="""

def openVenda():
    pass

"""=============
===PROGRAMA=====
============="""

run = True

while run:
    global fachada
    fachada = Fachada()
    opcao = input(" 1. Funcionario\n 2. Funcionario\n 3. Produto\n 4. Venda\n 0. Encerrar Programa\n")
    if opcao == '0':
        run = False
        print ("Programa fechado\n\n\t BYE!!")
    elif opcao == '1':
        openCliente()
    elif opcao == '2':
        openFuncionario()
    elif opcao == '3':
        openProduto()
    elif opcao == '4':
        openVenda()
    else:
        print("Opcao nao confere")
