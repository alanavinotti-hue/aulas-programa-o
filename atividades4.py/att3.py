# 1. Classe Mãe: Funcionario
class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = float(salario)

    def exibir_dados(self):
        """Exibe os dados formatados utilizando f-strings [3, 4]."""
        print("\n--- DADOS DO FUNCIONÁRIO ---")
        print(f"Nome:    {self.nome}")
        print(f"CPF:     {self.cpf}")
        print(f"Salário: R$ {self.salario:,.2f}")

    def aumentar_salario(self, percentual):
        """Aumenta o salário com base no percentual informado."""
        aumento = self.salario * (percentual / 100)
        self.salario += aumento
        print(f"Salário de {self.nome} aumentado em {percentual}%. Novo valor: R$ {self.salario:,.2f}")


class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, setor):
        super().__init__(nome, cpf, salario) 
        self.setor = setor

    def receber_bonificacao(self):
        """Aumento fixo de 10% e mensagem comemorativa."""
        self.aumentar_salario(10)
        print(f"🎉 Parabéns! O Gerente do setor {self.setor} recebeu sua bonificação anual!")

    def exibir_dados(self):
        """Sobrescrita para incluir o setor (Polimorfismo)."""
        super().exibir_dados()
        print(f"Setor:   {self.setor}")


func1 = Funcionario("João Silva", "123.456.789-00", 3000.00)
func1.exibir_dados()
func1.aumentar_salario(5)

gerente1 = Gerente("Maria Souza", "987.654.321-11", 8000.00, "Tecnologia")
gerente1.exibir_dados()
gerente1.receber_bonificacao()