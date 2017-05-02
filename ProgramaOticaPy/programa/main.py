'''
Created on 28 de abr de 2017

@author: Math
'''
from base.Cliente import Cliente
from base.Endereco import Endereco

if __name__ == '__main__':
    pass

"""=============
====CLIENTE=====
============="""

def inserirCliente():
    cliente = Cliente()
    endereco = Endereco()
    
    cliente.setNome(input("Qual o seu nome?\n"))
    cliente.setNascimento(input("Qual sua data de nascimento?"))
    cliente.setCpf(input("Qual o seu cpf?"))
    cliente.setTelefone(input("Qual o seu telefone?"))
    endereco.setCep(input("Qual o seu cep?"))
    endereco.setEstado(input("Qual o seu estado?"))
    endereco.setCidade(input("Qual a sua cidade?"))
    endereco.setRua(input("Qual a sua rua?"))
    cliente.setEndereco(endereco)

def atualizarCliente():
    cliente = Cliente()
    endereco = Endereco()
    
    cliente.setNome(input("Qual o seu nome?\n"))
    cliente.setNascimento(input("Qual sua data de nascimento?"))
    cliente.setCpf(input("Qual o seu cpf?"))
    cliente.setTelefone(input("Qual o seu telefone?"))
    endereco.setCep(input("Qual o seu cep?"))
    endereco.setEstado(input("Qual o seu estado?"))
    endereco.setCidade(input("Qual a sua cidade?"))
    endereco.setRua(input("Qual a sua rua?"))
    cliente.setEndereco(endereco)


def removerCliente():
    pass

def procurarCliente():
    pass

def todosClientes():
    cliente = Cliente()
    todosClientes = [cliente.getNome, cliente.getNascimento(), cliente.getCpf, cliente.getTelefone(), cliente.getEndereco().getCep(), cliente.getEndereco().getEstado(), cliente.getEndereco().getCidade(), cliente.getEndereco().getRua()]
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
    opcao = input(" 1. Cliente\n 2. Funcionario\n 3. Produto\n 4. Venda\n 0. Encerrar Programa\n")
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
