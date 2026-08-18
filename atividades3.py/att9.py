# Crie uma classe Livro com os atributos: titulo:str, autor:str e paginas:int;
# Implemente o método especial def __str__(self): para retornar uma string formatada:
# "Livro: '[titulo]' por [autor] [paginas] pgs"
# Crie o método comparar_tamanho(outro_livro) que recebe outro objeto Livro e imprime qual dos dois livros tem mais páginas;
# Instancie 2 livros, use o print() direto nas variáveis para testar o __str__ e compare o tamanho entre eles.



class Livro :
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo 
        self.autor = autor 
        self.paginas = paginas 

    def __str__(self):
        return f"Livro: '{self.titulo}' por {self.autor} ({self.paginas} pgs)"

    def comparar_tamanho(self, outro_livro):
        if self.paginas > outro_livro.paginas:
            print(f"{self.titulo} tem mais páginas que {outro_livro.titulo}")
        elif self.paginas < outro_livro.paginas:
            print(f"{outro_livro.titulo} tem mais páginas que {self.titulo}")
        else:
            print(f"{self.titulo} e {outro_livro.titulo} têm o mesmo número de páginas")

Livro1 = Livro("O senhor dos Aneis " , "J.R.R. Tolkien", 1216)
Livro2 = Livro("A Hipotese do Amor" , "Ali Hazelwood" , 400)

print(Livro1)
print(Livro2)
Livro1.comparar_tamanho(Livro2)

