'''
Created on 28 de abr de 2017

@author: Math
'''

class Identificacao(object):
    '''
    classdocs
    '''


    def __init__(self, identificacao=0, nome='', cpf='', telefone=''):
        '''
        Constructor
        '''
        super(Identificacao, self).__init__()
        self.identificacao = identificacao
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        
    def getIdentificacao(self):
        return self.identificacao
    
    def setIidentificacao(self, identificacao):
        self.identificacao = identificacao
        
    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome = nome
        
    def getCpf(self):
        return self.cpf
    
    def setCpf(self, cpf):
        self.cpf = cpf
        
    def getTelefone(self):
        return self.telefone
    
    def setTelefone(self, telefone):
        self.telefone = telefone
    