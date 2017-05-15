'''
Created on 6 de mai de 2017

@author: Math
'''
from base.Produto import Produto

class RepositorioProdutoArray(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.produto = []
        
        
    def inserirProduto(self, produto=Produto()):
        try:
            produto.setIdentificacao(len(self.produto) + 1)
            self.produto.append(produto)
        
        except:
            print("Erro na insersao!!")
        
        print("produto inserido com sucesso!!")
    
    
    def removerProduto(self, produto=Produto()):
        try:
            self.produto.remove(produto)
            
        except:
            print ("Erro na remocao!!")
            
        print ("produto removido com sucesso!!")   
    
    
    def atualizarProduto(self, produto=Produto()):
        try:
            self.produto.remove(produto.getIdentificacao())
            self.produto.append(produto)
        except:
            print ("Erro na atualizacao")
        
        print ("produto atualizado com sucesso!!")
    
    
    def procurarproduto(self, identificacao):
        for i in self.produto:
            if int(i.getIdentificacao()) == int(identificacao):
                return i
        
        print ("produto nao encontrado")
    
    
    def todosproduto(self):
        return self.produto
                    