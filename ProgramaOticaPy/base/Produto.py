'''
Created on 6 de mai de 2017

@author: Math
'''
from base.Identificacao import Identificacao

class Produto(Identificacao):
    '''
    classdocs
    '''


    def __init__(self, identificacao=0, nome="", marca="", valorCompra=0.0, valorVenda=0.0, quantidade=0):
        '''
        Constructor
        '''
        super(Produto, self).__init__(identificacao, nome)
        self.marca = marca
        self.valorCompra = valorCompra
        self.valorVenda = valorVenda
        self.quantidade = quantidade
    
    def getIdentificacao(self):
        return Identificacao.getIdentificacao(self)
    
    def setIdentificacao(self, identificacao):
        Identificacao.setIdentificacao(self, identificacao)
    
    def getNome(self):
        return Identificacao.getNome(self)
    
    def setNome(self, nome):
        Identificacao.setNome(self, nome)
    
    def getMarca(self):
        return self.marca
    
    def setMarca(self, marca):
        self.marca = marca
    
    def getValorCompra(self):
        return self.valorCompra
    
    def setValorCompra(self, valorCompra):
        self.valorCompra = valorCompra
        
    def getValorVenda(self):
        return self.valorVenda
    
    def setValorVenda(self, valorVenda):
        self.valorVenda = valorVenda
    
    def getQuantidade(self):
        return self.quantidade
    
    def setQuantidade(self, quantidade):
        self.quantidade = quantidade