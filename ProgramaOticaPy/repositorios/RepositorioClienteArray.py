'''
Created on 30 de abr de 2017

@author: Math
'''
from base.Cliente import Cliente

class RepositorioClienteArray(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.cliente = Cliente()
        self.clienteLista = [self.cliente]
        
    
    def inserir(self, cliente=Cliente()):
        self.clienteLista.append(cliente)
    
    def remover(self, identificacao):
        try:
            self.clienteLista.remove(identificacao)
            
        except:
            print ("Cliente nao existe!!")
            
        print ("Cliente removido com sucesso!!")   
    
    def atualizar(self, cliente=Cliente()):
        self.clienteLista.remove(cliente.getIdentificacao())
        self.clienteLista.append(cliente)
        