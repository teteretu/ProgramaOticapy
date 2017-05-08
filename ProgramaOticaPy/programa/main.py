'''
Created on 28 de abr de 2017

@author: Math
'''
from base.Cliente import Cliente
from base.Endereco import Endereco
from programa.Fachada import Fachada
from base.Funcionario import Funcionario
from base.Produto import Produto
from base.Venda import Venda
from base.ItemVenda import ItemVenda

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
    
    fachada.inserirCliente(cliente)


def atualizarCliente():
    idCliente = input("Qual o id do cliente?")
    cliente = fachada.procurarCliente(idCliente)
    endereco = cliente.getEndereco()
    
    cliente.setNome(input("Qual o seu nome?\n"))
    cliente.setNascimento(input("Qual sua data de nascimento?\n"))
    cliente.setCpf(input("Qual o seu cpf?\n"))
    cliente.setTelefone(input("Qual o seu telefone?\n"))
    endereco.setCep(input("Qual o seu cep?\n"))
    endereco.setEstado(input("Qual o seu estado?\n"))
    endereco.setCidade(input("Qual a sua cidade\n?"))
    endereco.setRua(input("Qual a sua rua\n?"))
    cliente.setEndereco(endereco)
    
    fachada.atualizarCliente(cliente)


def removerCliente():
    identificacao = input("Qual id do cliente que voce deseja remover?\n")
    removerCliente = fachada.procurarCliente(identificacao)
    
    fachada.removerCliente(removerCliente)


def procurarCliente():
    identificacao = input("Qual id do cliente que voce deseja procurar?\n")
    
    procurarCliente = fachada.procurarCliente(identificacao)
    print (procurarCliente)


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

def inserirFuncionario():
    funcionario = Funcionario()
    
    funcionario.setNome(input("Qual o seu nome?"))
    funcionario.setCpf(input("Qual o seu cpf?"))
    funcionario.setTelefone(input("Qual o seu telefone?"))
    
    fachada.inserirFuncionario(funcionario)


def atualizarFuncionario():
    idFuncionario = input("Qual o id do funcionario?")
    funcionario = fachada.procurarFuncionario(idFuncionario)

    funcionario.setNome(input("Qual o seu nome?"))
    funcionario.setCpf(input("Qual o seu cpf?"))
    funcionario.setTelefone(input("Qual o seu telefone?"))
    
    fachada.AtualizarFuncionario(funcionario)


def removerFuncionario():
    identificacao = input("Qual id do funcionario que voce deseja remover?\n")
    removerFuncionario = fachada.procurarFuncionario(identificacao)
    
    fachada.removerFuncionario(removerFuncionario)
    

def procurarFuncionario():
    identificacao = input("Qual id do funcionario que voce deseja remover?\n")
    procurarFuncionario = fachada.procurarFuncionario(identificacao)
    
    print (procurarFuncionario)


def todosFuncionarios():
    todosFuncionarios = fachada.todosFuncionarios()
    print (todosFuncionarios)


def openFuncionario():
    run = True
    while run:
        opcaoFuncionario = input("    FUNCIONARIO\n 1. Inserir\n 2. Atualizar\n 3. Remover\n 4. Procurar\n 5. Todos\n 0. Voltar Menu\n")
        
        if opcaoFuncionario == '1':
            inserirFuncionario()
        elif opcaoFuncionario == '2':
            atualizarFuncionario()
        elif opcaoFuncionario == '3':
            removerFuncionario()
        elif opcaoFuncionario == '4':
            procurarFuncionario()
        elif opcaoFuncionario == '5':
            todosFuncionarios()
        elif opcaoFuncionario == '0':
            run = False
        else:
            print("Opcao nao confere")

"""=============
===ITEM VENDA===
============="""

"""=============
====PRODUTO=====
============="""

def inserirProduto():
    produto = Produto()
    
    produto.setNome(input("Qual o nome?"))
    produto.setMarca(input("Qual a marca?"))
    produto.setValorCompra(input("Qual o Valor de Compra?"))
    produto.setValorVenda(input("Qual o Valor de Venda?"))
    produto.setQuantidade(input("Qual a quantidade?"))
    
    fachada.inserirProduto(produto)
    

def atualizarProduto():
    idProduto = input("Qual o id do produto?")
    produto = fachada.procurarProduto(idProduto)
    
    produto.setNome(input("Qual o nome?"))
    produto.setMarca(input("Qual a marca?"))
    produto.setValorCompra(input("Qual o Valor de Compra?"))
    produto.setValorVenda(input("Qual o Valor de Venda?"))
    produto.setQuantidade(input("Qual a quantidade?"))
    
    fachada.atualizarProduto(produto)


def removerProduto():
    identificacao = input("Qual id do produto que voce deseja remover?\n")
    removerProduto = fachada.procurarProduto(identificacao)
    
    fachada.removerProduto(removerProduto)


def procurarProduto():
    identificacao = input("Qual id do produto que voce deseja remover?\n")
    procurarProduto = fachada.procurarProduto(identificacao)
    
    print (procurarProduto)


def todosProdutos():
    todosProdutos = fachada.todosProdutos()
    print (todosProdutos)


def openProduto():
    run = True
    while run:
        opcaoProduto = input("    PRODUTO\n 1. Inserir\n 2. Atualizar\n 3. Remover\n 4. Procurar\n 5. Todos\n 0. Voltar Menu\n")
        
        if opcaoProduto == '1':
            inserirProduto()
        elif opcaoProduto == '2':
            atualizarProduto()
        elif opcaoProduto == '3':
            removerProduto()
        elif opcaoProduto == '4':
            procurarProduto()
        elif opcaoProduto == '5':
            todosProdutos()
        elif opcaoProduto == '0':
            run = False
        else:
            print("Opcao nao confere")

"""=============
=====VENDA======
============="""

def inserirVenda():
    venda = Venda()
    itensVenda = []
    itemVenda = ItemVenda() 
    op = 1
    
    venda.setIdCliente(input("Qual o id do cliente?"))
    venda.setTotal(input("Qual o total da venda?"))
    venda.setData(input("Qual a data da venda?"))
    while op == 1:
        itemVenda.setIdProduto(input("Qual o id do produto a comprar?"))
        itemVenda.setQuantidade(input("Quantos desse produto voce deseja comprar?"))
        
        fachada.inserirItemVenda(itemVenda)
        
        itensVenda.append(itemVenda)
        
        op = input("Deseja comprar outro produto?  1. Sim\t 0. Nao")
    
    venda.setVendas(itensVenda)
    
    fachada.inserirVenda(venda)


def atualizarVenda():
    idVenda = input("Qual o id da Venda?")
    venda = fachada.procurarVenda(idVenda)
    
    itensVenda = venda.getVendas()
    itemVenda = ItemVenda() 
    op = 1
    
    venda.setIdCliente(input("Qual o id do cliente?"))
    venda.setTotal(input("Qual o total da venda?"))
    venda.setData(input("Qual a data da venda?"))
    while op == 1:
        itemVenda.setIdProduto(input("Qual o id do produto a comprar?"))
        itemVenda.setQuantidade(input("Quantos desse produto voce deseja comprar?"))
        
        fachada.inserirItemVenda(itemVenda)
        
        itensVenda.append(itemVenda)
        
        op = input("Deseja comprar outro produto?  1. Sim\t 0. Nao")
    
    venda.setVendas(itensVenda)
    
    fachada.atualizarVenda(venda)


def removerVenda():
    identificacao = input("Qual id da venda que voce deseja remover?\n")
    removerVenda = fachada.procurarVenda(identificacao)
    
    fachada.removerVenda(removerVenda)


def procurarVenda():
    identificacao = input("Qual id da venda que voce deseja remover?\n")
    procurarVenda = fachada.procurarVenda(identificacao)
    
    print(procurarVenda)


def todasVendas():
    todasVendas = fachada.todasVendas()
    print (todasVendas)


def openVenda():
    run = True
    while run:
        opcaoVenda = input("    VENDA\n 1. Inserir\n 2. Atualizar\n 3. Remover\n 4. Procurar\n 5. Todos\n 0. Voltar Menu\n")
        
        if opcaoVenda == '1':
            inserirVenda()
        elif opcaoVenda == '2':
            atualizarVenda()
        elif opcaoVenda == '3':
            removerVenda()
        elif opcaoVenda == '4':
            procurarVenda()
        elif opcaoVenda == '5':
            todasVendas()
        elif opcaoVenda == '0':
            run = False
        else:
            print("Opcao nao confere")

"""=============
===PROGRAMA=====
============="""

run = True

while run:
    global fachda 
    fachada = Fachada()
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
