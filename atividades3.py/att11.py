class CofreDigital :
    def __init__(self, titular, senha):
        self.titular = titular
        self.__senha = senha
        self.__saldo = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado. Titular: {self.titular}")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor, senha_informada):
        if senha_informada == self.__senha:
            if self.__saldo >= valor:
                self.__saldo -= valor
                print(f"Saque de R$ {valor:.2f} autorizado. Novo saldo: R$ {self.__saldo:.2f}")
            else:
                print(f"Saldo insuficiente para realizar o saque de R$ {valor:.2f}.")
        else:
            print("Senha incorreta! Acesso negado.")

    def consultar_saldo_seguro(self):
        """Método público para acessar dado privado com segurança."""
        return f"Saldo atual de {self.titular}: R$ {self.__saldo:.2f}"


meu_cofre = CofreDigital("Marcos", "4321")
meu_cofre.depositar(500.0)
meu_cofre.sacar(100.0, "4321") 

print("\n--- Tentando quebrar o Encapsulamento ---")
meu_cofre.__saldo = 1000000.0 
meu_cofre.__senha = "0000"


print(f"Valor da variável externa '__saldo': {meu_cofre.__saldo}") 
print(meu_cofre.consultar_saldo_seguro()) 

meu_cofre.sacar(50.0, "0000") 
