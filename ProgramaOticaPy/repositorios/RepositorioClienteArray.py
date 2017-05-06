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
        self.cliente = []
        
        
    def inserirCliente(self, cliente=Cliente()):
        try:
            self.cliente.append(cliente)
        
        except:
            print("Erro na insersao!!")
        
        print("Cliente inserido com sucesso!!")
    
    
    def removerCliente(self, cliente=Cliente()):
        try:
            self.cliente.remove(cliente)
            
        except:
            print ("Erro na remocao!!")
            
        print ("Cliente removido com sucesso!!")   
    
    
    def atualizarCliente(self, cliente=Cliente()):
        try:
            self.cliente.remove(cliente.getIdentificacao())
            self.cliente.append(cliente)
        except:
            print ("Erro na atualizacao")
        
        print ("Cliente atualizado com sucesso!!")
    
    
    def procurarCliente(self, identificacao):
        for i in range(len(self.cliente)):
            if self.cliente[i].getIdentificacao() == identificacao:
                return self.cliente[i]
        
        print ("Cliente nao encontrado")
    
    
    def todosClientes(self):
        return self.cliente
    