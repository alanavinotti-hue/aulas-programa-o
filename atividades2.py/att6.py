class Aplicativo:
    def __init__(self, nome, consumo_bateria):
        pass


class Celular:
    def __init__(self, marca, modelo, bateria=100):
        self.marca = marca
        self.modelo = modelo
        self.bateria = bateria
        self.ligado = False

    def ligar(self):
        self.ligado = True
        print(f"O {self.marca} {self.modelo} foi ligado.")

    def executar_app(self, app):
        if not self.ligado:
            print(f"Erro: Não é possível executar '{app.nome}' com o celular desligado.")
            return

        if self.bateria >= app.consumo_bateria:
            self.bateria -= app.consumo_bateria
            print(f"Usando aplicativo: {app.nome}. Bateria restante: {self.bateria}%")
        else:
            print(f"Bateria insuficiente para rodar '{app.nome}'.")


whatsapp = Aplicativo("WhatsApp", 5)
jogo_pesado = Aplicativo("Genshin Impact", 40)


meu_celular = Celular("Apple", "iPhone 15")

print(f"Status inicial: Bateria {meu_celular.bateria}%")
meu_celular.ligar()

meu_celular.executar_app(whatsapp)
meu_celular.executar_app(jogo_pesado)

print(f"Status final: Bateria {meu_celular.bateria}%")