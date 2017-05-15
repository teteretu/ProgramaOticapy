'''
Created on 6 de mai de 2017

@author: Math
'''

from base.ItemVenda import ItemVenda

class RepositorioItemVendaArray(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.itemVenda = []
        
        
    def inserirItemVenda(self, itemVenda=ItemVenda()):
        try:
            itemVenda.setIdentificacao(len(self.itemVenda) + 1)
            self.itemVenda.append(itemVenda)
        
        except:
            print("Erro na insersao!!")
        
        print("itemVenda inserido com sucesso!!")
    
    
    def removerItemVenda(self, itemVenda=ItemVenda()):
        try:
            self.itemVenda.remove(itemVenda)
            
        except:
            print ("Erro na remocao!!")
            
        print ("itemVenda removido com sucesso!!")   
    
    
    def atualizarItemVenda(self, itemVenda=ItemVenda()):
        try:
            self.itemVenda.remove(itemVenda.getIdentificacao())
            self.itemVenda.append(itemVenda)
        except:
            print ("Erro na atualizacao")
        
        print ("itemVenda atualizado com sucesso!!")
    
    
    def procurarItemVenda(self, identificacao):
        for i in self.itemVenda:
            if int(i.getIdentificacao()) == int(identificacao):
                return i
        
        print ("itemVenda nao encontrado")
    
    
    def todosItensVenda(self):
        return self.itemVenda
            