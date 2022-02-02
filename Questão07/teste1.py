from clientes import Cliente
from contas import Conta

maria = Cliente("Maria", "1243-3321")
joão = Cliente("João", "5554-3322")

conta = Conta([maria, joão], 7894, 10000)
conta.resumo()