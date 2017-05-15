'''
Created on 6 de mai de 2017

@author: Math
'''

from base.Venda import Venda

class RepositorioVendaArray(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.venda = []
        
        
    def inserirVenda(self, venda=Venda()):
        try:
            venda.setIdentificacao(len(self.venda) + 1)
            self.venda.append(venda)
        
        except:
            print("Erro na insersao!!")
        
        print("venda inserido com sucesso!!")
    
    
    def removerVenda(self, venda=Venda()):
        try:
            self.venda.remove(venda)
            
        except:
            print ("Erro na remocao!!")
            
        print ("venda removido com sucesso!!")   
    
    
    def atualizarVenda(self, venda=Venda()):
        try:
            self.venda.remove(venda.getIdentificacao())
            self.venda.append(venda)
        except:
            print ("Erro na atualizacao")
        
        print ("venda atualizado com sucesso!!")
    
    
    def procurarvenda(self, identificacao):
        for i in self.venda:
            if int(i.getIdentificacao()) == int(identificacao):
                return i
        
        print ("venda nao encontrado")
    
    
    def todasvendas(self):
        return self.venda
        