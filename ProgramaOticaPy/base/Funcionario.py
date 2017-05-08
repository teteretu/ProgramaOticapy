'''
Created on 6 de mai de 2017

@author: Math
'''

from base.Identificacao import Identificacao

class Funcionario(Identificacao):
    '''
    classdocs
    '''

    def __init__(self, identificacao=0, nome='', cpf='', telefone=''):
        '''
        Constructor
        '''
        super(Funcionario, self).__init__(identificacao, nome, cpf, telefone)
    
    
    def getIdentificacao(self):
        return Identificacao.getIdentificacao(self)
    
    def setIdentificacao(self, identificacao):
        Identificacao.setIdentificacao(self, identificacao)
    
    def getNome(self):
        return Identificacao.getNome(self)
    
    def setNome(self, nome):
        Identificacao.setNome(self, nome)
    
    def getCpf(self):
        return Identificacao.getCpf(self)
    
    def setCpf(self, cpf):
        Identificacao.setCpf(self, cpf)
    
    def getTelefone(self):
        return Identificacao.getTelefone(self)
    
    def setTelefone(self, telefone):
        Identificacao.setTelefone(self, telefone)
        