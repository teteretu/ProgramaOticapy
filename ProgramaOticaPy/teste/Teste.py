'''
Created on 30 de abr de 2017

@author: Math
'''

from base.Cliente import Funcionario

if __name__ == '__main__':
    pass

cliente1 = Funcionario()
cliente1.setCpf(123123123)
cliente2 = Funcionario()
cliente2.setNome("amsdasid")
cliente3 = Funcionario()
cliente3.setTelefone(9811911122)

lista = [cliente1, cliente2]
print (lista[0].getCpf() , "\n" , lista[1].getNome())
lista.append(cliente3)

print (lista[0].getCpf(), "\n", lista[1].getNome(), "\n", lista[2].getTelefone())