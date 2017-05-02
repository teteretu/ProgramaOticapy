'''
Created on 28 de abr de 2017

@author: Math
'''
from base.Endereco import Endereco
from base.Identificacao import Identificacao

class Cliente (Identificacao):
    """
    classdocs
    identificacao=0, nome='', cpf='', telefone=''
    sao da classe Identificacao
    """

    def __init__(self, identificacao=0, nome='', cpf='', telefone='', nascimento='', endereco=Endereco()):
        super(Cliente, self).__init__(identificacao, nome, cpf, telefone)
        self.nascimento = nascimento
        self.endereco = endereco
        
    def getIdentificacao(self):
        return Identificacao.getIdentificacao(self)
    
    def setIidentificacao(self, identificacao):
        Identificacao.setIidentificacao(self, identificacao)
        
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
        
    def getNascimento(self):
        return self.nascimento
    
    def setNascimento(self, nascimento):
        self.nascimento = nascimento
    
    def getEndereco(self):
        return self.endereco
    
    def setEndereco(self, endereco):
        self.endereco = endereco
        
    
        