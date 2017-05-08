'''
Created on 6 de mai de 2017

@author: Math
'''
from base.Identificacao import Identificacao

class ItemVenda(Identificacao):
    '''
    classdocs
    '''


    def __init__(self, identificacao=0, idProduto=0, idVenda=0, quantidade=0):
        '''
        Constructor
        '''
        super(ItemVenda, self).__init__(identificacao)
        self.idProduto = idProduto
        self.idVenda = idVenda
        self.quantidade = quantidade
    
    def getIdentificacao(self):
        return Identificacao.getIdentificacao(self)
    
    def setIdentificacao(self, identificacao):
        Identificacao.setIdentificacao(self, identificacao)
    
    def getIdProduto(self):
        return self.idProduto
    
    def setIdProduto(self, idProduto):
        self.idProduto = idProduto
    
    def getIdVenda(self):
        return self.idVenda
    
    def setIdVenda(self, idVenda):
        self.idVenda = idVenda
    
    def getQuantidade(self):
        return self.quantidade
    
    def setQuantidade(self, quantidade):
        self.quantidade = quantidade