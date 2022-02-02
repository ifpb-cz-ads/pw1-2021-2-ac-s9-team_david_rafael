class Conta:
     def __init__(self, clientes, número, saldo = 0):
         self.saldo = 0
         self.clientes = clientes
         self.número = número
         self.operações = []
         self.deposito(saldo)
     def resumo(self):
         print("CC N°%s Saldo: %10.2f" %
               (self.número, self.saldo))
     def saque(self, valor):
         if self.saldo >= valor:
               self.saldo -= valor
               self.operações.append(["SAQUE", valor])
         else:
            print("Saldo insuficiente!")
            return False
     def deposito(self, valor):
         self.saldo += valor
         self.operações.append(["DEPÓSITO", valor])
     def extrato(self):
         print("Extrato CC N° %s\n" % self.número)
         for o in self.operações:
               print("%10s %10.2f" % (o[0],o[1]))
         print("\n       Saldo: %10.2f\n" % self.saldo)

class ContaEspecial(Conta):
     def __init__(self, clientes, número, saldo = 0, limite=0):
         Conta.__init__(self, clientes, número, saldo)
         self.limite = limite
     def saque(self, valor):
         if self.saldo + self.limite >= valor:
               self.saldo -= valor
               self.operações.append(["SAQUE", valor])
               return True
         else:
            return Conta.saque(self, valor)
     def extrato(self):
        Conta.extrato(self)
        print(f"\n     Limite: {self.limite:10.2f}\n")
        print(f"\n Disponivel: {self.limite + self.saldo:10.2f}\n")
        