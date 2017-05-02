'''
Created on 28 de abr de 2017

@author: Math
'''

class Endereco(object):
    '''
    classdocs
    '''


    def __init__(self, estado='', cidade='', rua='', cep=''):
        '''
        Constructor
        '''
    
    def setEstado(self, estado):
        self.estado = estado
    
    def getEstado(self):
        return self.estado
    
    def setCidade(self, cidade):
        self.cidade = cidade
    
    def getCidade(self):
        return self.cidade
    
    def setRua(self, rua):
        self.rua = rua
    
    def getRua(self):
        return self.estado
    
    
    def setCep(self, cep):
        if len(str(cep)) <= 10:
            self.cep = cep
        else:
            print ("Tamanho do cep invalido")
            
    def getCep(self):
        return self.cep
