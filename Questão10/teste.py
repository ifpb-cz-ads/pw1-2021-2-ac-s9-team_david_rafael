from clientes import Cliente
from contas import ContaEspecial

maria = Cliente("Maria da Silva ", "555-4321")

conta = ContaEspecial([maria], 3432, 50000, 10000)
conta.extrato()
