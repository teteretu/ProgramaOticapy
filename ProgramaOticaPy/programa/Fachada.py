'''
Created on 30 de abr de 2017

@author: Math
'''
from repositorios.RepositorioClienteArray import RepositorioClienteArray
from base.Cliente import Cliente
from repositorios.RepositorioFuncionarioArray import RepositorioFuncionarioArray
from base.Funcionario import Funcionario
from repositorios.RepositorioItemVendaArray import RepositorioItemVendaArray
from base.ItemVenda import ItemVenda
from repositorios.RepositorioProdutoArray import RepositorioProdutoArray
from base.Produto import Produto
from repositorios.RepositorioVendaArray import RepositorioVendaArray
from base.Venda import Venda


class Fachada(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.clientes = RepositorioClienteArray()
        self.funcionarios = RepositorioFuncionarioArray()
        self.itensVenda = RepositorioItemVendaArray()
        self.produtos = RepositorioProdutoArray()
        self.vendas = RepositorioVendaArray()
        
    """=============
    ====CLIENTE=====
    ============="""
    
    def inserirCliente(self, cliente=Cliente()):
        self.clientes.inserirCliente(cliente)
    
    
    def removerCliente(self, cliente=Cliente()):
        self.clientes.removerCliente(cliente)
    
    
    def atualizarCliente(self, cliente=Cliente()):
        self.clientes.atualizarCliente(cliente)
    
    
    def procurarCliente(self, identificacao):
        return self.clientes.procurarCliente(identificacao)
    
    
    def todosClientes(self):
        try:
            return self.clientes.todosClientes()
        except:
            print("Nao existem clientes cadastrados!!")

    """=============
    ==FUNCIONARIO===
    ============="""

    def inserirFuncionario(self, funcionario=Funcionario()):
        self.funcionarios.inserirFuncionario(funcionario)
    
    
    def removerFuncionario(self, funcionario=Funcionario()):
        self.funcionarios.removerFuncionario(funcionario)
    
    
    def atualizarFuncionario(self, funcionario=Funcionario()):
        self.funcionarios.atualizarFuncionario(funcionario)
    
    
    def procurarFuncionario(self, identificacao):
        return self.funcionarios.procurarFuncionario(identificacao)
    
    
    def todosFuncionarios(self):
        try:
            return self.funcionarios.todosFuncionarios()
        except:
            print("Nao existem funcionarios cadastrados!!")
            
    """=============
    ===ITEM VENDA===
    ============="""

    def inserirItemVenda(self, itemVenda=ItemVenda()):
        self.itensVenda.inserirItemVenda(itemVenda)
    
    
    def removerItemVenda(self, itemVenda=ItemVenda()):
        self.itensVenda.removerItemVenda(itemVenda)
    
    
    def atualizarItemVenda(self, itemVenda=ItemVenda()):
        self.itensVenda.atualizarItemVenda(itemVenda)
    
    
    def procurarItemVenda(self, identificacao):
        return self.itensVenda.procurarItemVenda(identificacao)
    
    
    def todosItensVenda(self):
        try:
            return self.itensVenda.todosItensVenda()
        except:
            print("Nao existem itens Vendidos cadastrados!!")

    
    """=============
    ====PRODUTO=====
    ============="""

    def inserirProduto(self, produto=Produto()):
        self.produtos.inserirProduto(produto)
    
    
    def removerProduto(self, produto=Produto()):
        self.produtos.removerProduto(produto)
    
    
    def atualizarProduto(self, produto=Produto()):
        self.produtos.atualizarProduto(produto)
    
    
    def procurarProduto(self, identificacao):
        return self.produtos.procurarProduto(identificacao)
    
    
    def todosProdutos(self):
        try:
            return self.produtos.todosproduto()
        except:
            print("Nao existem produtos cadastrados!!")


    """=============
    =====VENDA======
    ============="""

    def inserirVenda(self, venda=Venda()):
        self.vendas.inserirVenda(venda)
    
    
    def removerVenda(self, venda=Venda()):
        self.vendas.removerVenda(venda)
    
    
    def atualizarVenda(self, venda=Venda()):
        self.vendas.atualizarVenda(venda)
    
    
    def procurarVenda(self, identificacao):
        return self.vendas.procurarVenda(identificacao)
    
    
    def todasVendas(self):
        try:
            return self.vendas.todasvendas()
        except:
            print("Nao existem vendas cadastrados!!")

