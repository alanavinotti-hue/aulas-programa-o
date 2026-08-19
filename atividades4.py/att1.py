class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def fazer_som(self):
        print("Este animal faz um som genérico.")


class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, "Canino")
        self.raca = raca


    def fazer_som(self):
        print(f"{self.nome} ({self.raca}) faz: Au Au!")

class Gato(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, "Felino")
        self.raca = raca

    def fazer_som(self):
        print(f"{self.nome} ({self.raca}) faz: Miau!")

class Vaca(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, "Bovino")
        self.raca = raca

    def fazer_som(self):
        print(f"{self.nome} ({self.raca}) faz: Muuu!")


dog = Cachorro("Buddy", "Pastor Alemão")
cat = Gato("Mia", "Siamês")
cow = Vaca("Mimosa", "Holandesa")


animais = [dog, cat, cow]

print("=== Demonstração de Polimorfismo ===")
for bicho in animais:
    bicho.fazer_som()