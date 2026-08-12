class Carro:
    def __init__(self, modelo, marca, combustivel=0):
        self.modelo = modelo
        self.marca = marca
        self.combustivel = combustivel
        
        self.quilometragem = 0 

    
    def abastecer(self, quantidade):
        if self.combustivel + quantidade > 100:
            self.combustivel = 100
            print("Atenção: O tanque atingiu o limite máximo de 100 litros.")
        else:
            self.combustivel += quantidade
            print(f"Foram adicionados {quantidade}L. Nível atual: {self.combustivel}L.")

   
    def acelerar(self):
        if self.combustivel > 0:
            self.combustivel -= 5 # Simulação de consumo
            self.quilometragem += 15 # Aumento de 15 km por aceleração
            print(f"O {self.modelo} acelerou! +15km percorridos.")
        else:
            print("Falha: O carro não tem combustível para acelerar.")

    
    def painel(self):
        print("\n" + "="*20)
        print(f"      PAINEL - {self.marca} {self.modelo}")
        print("="*20)
        print(f"Combustível:  {self.combustivel}L")
        print(f"Quilometragem: {self.quilometragem}km")
        print("="*20 + "\n")



meu_carro = Carro("Uno", "Fiat")

meu_carro.abastecer(50)  
meu_carro.acelerar()     
meu_carro.acelerar()     
meu_carro.painel()       

meu_carro.abastecer(80) 
meu_carro.painel()       