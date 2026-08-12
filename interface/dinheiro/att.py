class aluno ():
    def _init_( self, nome, idade):
        """ Função de inicializção padrão , deve ser usada para criar variáveis que são exclusivas de um objeto """
        self.nome = nome
        self.idade = idade 

        print("O aluno" + self.nome + " tem " + str(self.idade) + " anos. ")

    aluno1 = aluno("Alberto", 25)



   









