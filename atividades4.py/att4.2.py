class Usuario :
    def __init__(self, nome: str):
        self.nome = nome
        self.itens_emprestados = []

    def pegar_item(self, item):
        if item.disponivel :
            item.emprestar()
            self.itens_emprestados.append(item)
            print(f"Confirmação: {item.titulo} adicionado à conta de {self.nome}.")
        else:
            print(f"Aviso: O item '{item.titulo}' não pode ser pego agora.")


    def devolver_item(self, item):
        if item in self.itens_emprestados:
            item.devolver()
            self.itens_emprestados.remove(item)
            print(f"Confirmação: {item.titulo} removido da conta de {self.nome}.")
        else:
            print(f"Erro: O item '{item.titulo}' não consta nos empréstimos de {self.nome}.")

    def ver_historico(self):
        print(f"\n" + "="*35)
        print(f"USUÁRIO: {self.nome.upper()}")
        print(f"ITENS EM POSSE:")
        
        if not self.itens_emprestados:
            print("  - Nenhum item pendente.")
        else:
            for item in self.itens_emprestados:
                print(f"  • {item.titulo} (Código: {item.codigo})")
        print("="*35 + "\n")

livro1 = Livro ("Dom Casmurro", 2001, "Machado de Assis", 256) 
usuario1 = Usuario("Carlos Andrade")
usuario1.pegar_item(livro1) 
usuario1.pegar_item(livro2) 
usuario1.ver_historico()
usuario1.ver_historico()
   