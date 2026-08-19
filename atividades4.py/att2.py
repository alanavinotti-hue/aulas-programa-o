class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.combustivel = 100 

    def acelerar(self):
        print(f"O {self.modelo} acelerou usando combustível.")

class CarroEletrico(Carro):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.bateria = 100


    def acelerar(self):
        if self.bateria >= 5:
            self.bateria -= 5
            print(f"O carro elétrico acelerou silenciosamente! Bateria restante: {self.bateria}%")
        else:
            print("Alerta: Carga insuficiente para acelerar. Por favor, recarregue.")

    
    def recarregar(self):
        self.bateria = 100
        print("Carga completa! A bateria agora está em 100%.")


    def painel(self):
        print("\n" + "="*30)
        print(f"   PAINEL ELÉTRICO: {self.marca.upper()} {self.modelo.upper()}")
        print("-" * 30)
        print(f" STATUS DA BATERIA: {self.bateria}%")
        print("="*30 + "\n")


meu_tesla = CarroEletrico("Tesla", "Model S")

meu_tesla.painel()
meu_tesla.acelerar()
meu_tesla.acelerar()
meu_tesla.painel() 
meu_tesla.recarregar()
meu_tesla.painel()