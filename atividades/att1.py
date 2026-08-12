class Animal:
    def __int__(self, nome, especie, som , idade = 0):
        self.nome = nome
        self.especie = especie
        self.idade = idade 
        self.som = som 


    def emitir_som(self):
        print(f" O {self.especie} chamado {self.nome} faz: {self.som}")

    def aniversario(self):
        self.idade += 1
        print(f" comemorção: O {self.nome} fez {self.idade} anos")

def main():
    animal1 = Animal( "Amora", "Gata", "miau" ,  2 )    
    animal2 = Animal( "Buddy" , "Cachorro" , "AU AU",  4)
    animal3 = Animal( "Zuzu " , "passarinho" , " piu piu",  5)

    animal = [animal1, animal2, animal3]

    for bicho in animal:
        print(f"\n- Interagindo com {bicho.nome} -")
        bicho.emitir_som()
    
    
    bicho.aniversario()
    bicho.aniversario()




            