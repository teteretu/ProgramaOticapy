'''
Created on 6 de mai de 2017

@author: Math
'''
from base.Funcionario import Funcionario

class RepositorioFuncionarioArray(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.funcionario = []
        
        
    def inserirFuncionario(self, funcionario=Funcionario()):
        try:
            self.funcionario.append(funcionario)
        
        except:
            print("Erro na insersao!!")
        
        print("Funcionario inserido com sucesso!!")
    
    
    def removerFuncionario(self, funcionario=Funcionario()):
        try:
            self.funcionario.remove(funcionario)
            
        except:
            print ("Erro na remocao!!")
            
        print ("Funcionario removido com sucesso!!")   
    
    
    def atualizarFuncionario(self, funcionario=Funcionario()):
        try:
            self.funcionario.remove(funcionario.getIdentificacao())
            self.funcionario.append(funcionario)
        except:
            print ("Erro na atualizacao")
        
        print ("Funcionario atualizado com sucesso!!")
    
    
    def procurarFuncionario(self, identificacao):
        for i in range(len(self.funcionario)):
            if self.funcionario[i].getIdentificacao() == identificacao:
                return self.funcionario[i]
        
        print ("Funcionario nao encontrado")
    
    
    def todosFuncionarios(self):
        return self.funcionario
    