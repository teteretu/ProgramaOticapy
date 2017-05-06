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
        self.clientes.inserir(cliente)
    
    
    def removerCliente(self, cliente=Cliente()):
        self.clientes.remover(cliente)
    
    
    def atualizarCliente(self, cliente=Cliente()):
        self.clientes.atualizar(cliente)
    
    
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
        self.funcionarios.inserir(funcionario)
    
    
    def removerFuncionario(self, funcionario=Funcionario()):
        self.funcionarios.remover(funcionario)
    
    
    def atualizarFuncionario(self, funcionario=Funcionario()):
        self.funcionarios.atualizar(funcionario)
    
    
    def procurarfuncionario(self, identificacao):
        return self.funcionarios.procurar(identificacao)
    
    
    def todosfuncionarios(self):
        try:
            return self.funcionarios.todosFuncionarios()
        except:
            print("Nao existem funcionarios cadastrados!!")
            
    """=============
    ===ITEM VENDA===
    ============="""

    def inserirItemVenda(self, itemVenda=ItemVenda()):
        self.itensVenda.inserir(itemVenda)
    
    
    def removerItemVenda(self, itemVenda=ItemVenda()):
        self.itensVenda.remover(itemVenda)
    
    
    def atualizarItemVenda(self, itemVenda=ItemVenda()):
        self.itensVenda.atualizar(itemVenda)
    
    
    def procurarItemVenda(self, identificacao):
        return self.itensVenda.procurar(identificacao)
    
    
    def todosItensVenda(self):
        try:
            return self.itensVenda.todosItensVenda()
        except:
            print("Nao existem itens Vendidos cadastrados!!")

    
    """=============
    ====PRODUTO=====
    ============="""

    def inserirProduto(self, produto=Produto()):
        self.produtos.inserir(produto)
    
    
    def removerProduto(self, produto=Produto()):
        self.produtos.remover(produto)
    
    
    def atualizarProduto(self, produto=Produto()):
        self.produtos.atualizar(produto)
    
    
    def procurarProduto(self, identificacao):
        return self.produtos.procurar(identificacao)
    
    
    def todosProdutos(self):
        try:
            return self.produtos.todosproduto()
        except:
            print("Nao existem produtos cadastrados!!")


    """=============
    =====VENDA======
    ============="""

    def inserirVenda(self, venda=Venda()):
        self.vendas.inserir(venda)
    
    
    def removerVenda(self, venda=Venda()):
        self.vendas.remover(venda)
    
    
    def atualizarVenda(self, venda=Venda()):
        self.vendas.atualizar(venda)
    
    
    def procurarVenda(self, identificacao):
        return self.vendas.procurar(identificacao)
    
    
    def todosVendas(self):
        try:
            return self.vendas.todasvendas()
        except:
            print("Nao existem vendas cadastrados!!")

