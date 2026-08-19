class ItemBiblioteca:
    def __init__(self, titulo: str, codigo: int):
        self.titulo = titulo
        self.codigo = codigo
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"Sucesso: O item '{self.titulo}' (Código: {self.codigo}) foi emprestado.")
        else:
            print(f"Falha: O item '{self.titulo}' não está disponível no momento.")

    
    def devolver(self):
        self.disponivel = True
        print(f"Sucesso: O item '{self.titulo}' foi devolvido e está disponível para novo uso.")


class Livro(ItemBiblioteca):
    def __init__(self, titulo: str, codigo: int, autor: str, num_paginas: int):
        super().__init__(titulo, codigo)
        self.autor = autor
        self.num_paginas = num_paginas

    def __str__(self):
        """Representação amigável do objeto [Histórico]."""
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"Livro: {self.titulo} | Autor: {self.autor} | Páginas: {self.num_paginas} | Status: {status}"

meu_livro = Livro("O Programador Pragmático", 1001, "Andrew Hunt", 352)
print(meu_livro)
meu_livro.emprestar()
meu_livro.emprestar()
meu_livro.devolver()
print(meu_livro)