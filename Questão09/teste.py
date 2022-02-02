from clientes import Cliente
from contas import Conta
from contas import ContaEspecial

joão = Cliente("João da Silva", "777-1234")
maria = Cliente("Maria da Silva", "555-4321")

conta = Conta([joão, maria], 7894, 500)
conta.resumo()
print(conta.saque(1000))
print(conta.saque(100))
conta.resumo()

conta2 = ContaEspecial([maria], 3432, 50000, 10000)
conta2.resumo()
print(conta2.saque(100000))
print(conta2.saque(500))
conta2.resumo()
