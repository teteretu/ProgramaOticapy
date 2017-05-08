'''
Created on 6 de mai de 2017

@author: Math
'''
from base.Identificacao import Identificacao

class Venda(Identificacao):
    '''
    classdocs
    '''


    def __init__(self, identificacao=0, idCliente=0, total=0, data="", vendas=[]):
        '''
        Constructor
        '''
        super(Venda, self).__init__(identificacao)
        self.idCliente = idCliente
        self.total = total
        self.data = data
        self.vendas = vendas
    
    def getIdentificacao(self):
        return Identificacao.getIdentificacao(self)
    
    def setIdentificacao(self, identificacao):
        Identificacao.setIdentificacao(self, identificacao)
    
    def getIdCliente(self):
        return self.idCliente()
    
    def setIdCliente(self, idCliente):
        self.idCliente = idCliente
    
    def getTotal(self):
        return self.total
    
    def setTotal(self, total):
        self.total = total

    def getData(self):
        return self.data
    
    def setData(self, data):
        self.data = data

    def getVendas(self):
        return self.vendas
    
    def setVendas(self, vendas):
        self.vendas.append(vendas)
    