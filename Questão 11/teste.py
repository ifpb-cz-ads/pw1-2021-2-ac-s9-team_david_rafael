from clientes import Cliente
from contas import ContaEspecial

maria = Cliente("Maria da Silva", "1243-3321")

conta = ContaEspecial([maria], 3432, 5000, 1000)
conta.extrato()
conta.saque(6000)
conta.saque(3000)
conta.saque(1000)
conta.extrato()