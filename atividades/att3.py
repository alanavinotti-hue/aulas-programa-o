class contabancaria:


    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
       
        self.limite_negativo = -60.00

    def adicionar_saldo(self, valor):
        """Aumenta o saldo da conta."""
        self.saldo += valor

    def transferir(self, valor, conta_destino):
        """Transfere valores entre contas com validação de limite negativo."""
        print("-- STATUS PRÉ-TRANSFERÊNCIA --")
        print(f"Origem ({self.titular}): R$ {self.saldo:.2f}")
        print(f"Destino ({conta_destino.titular}): R$ {conta_destino.saldo:.2f}")

       
        if (self.saldo - valor) < self.limite_negativo:
            print(f"\n>>> OPERAÇÃO BLOQUEADA: Valor de R$ {valor:.2f} excede o limite de crédito de R$ 500,00.")
        else:
            
            conta_destino.adicionar_saldo(valor)
            print(f"\n>>> SUCESSO: R$ {valor:.2f} transferidos para {conta_destino.titular}.")

       
        print("-- STATUS PÓS-TRANSFERÊNCIA --")
        print(f"Origem ({self.titular}): R$ {self.saldo:.2f}")
        print(f"Destino ({conta_destino.titular}): R$ {conta_destino.saldo:.2f}\n")
