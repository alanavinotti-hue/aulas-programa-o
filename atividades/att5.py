class Produto:

    def __init__(self, nome: str, preco: float, estoque: int):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

   
    def reduzir_estoque(self, quantidade: int):
        if self.estoque >= quantidade:
            self.estoque -= quantidade
        else:
            print(f"Aviso: Estoque insuficiente de {self.nome}. Restam apenas {self.estoque} unidades.")
            return False
        return True

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

   
    def adicionar_ao_carrinho(self, produto, quantidade):
         if produto.reduzir_estoque(quantidade):
            self.produtos.append((produto, quantidade))
            print(f"{quantidade}x {produto.nome} adicionado ao carrinho.")

    
    def mostrar_carrinho(self):
        if not self.produtos:
            print("O carrinho está vazio.")
            return

        print("\n--- ITENS NO CARRINHO ---")
        total_compra = 0
        for item, qtd in self.produtos:
            subtotal = item.preco * qtd
            total_compra += subtotal
            print(f"Produto: {item.nome:.<15} | Qtd: {qtd:>2} | Preço Un.: R$ {item.preco:>7.2f} | Subtotal: R$ {subtotal:>7.2f}")
        
        print("-" * 65)
        print(f"TOTAL DA COMPRA: R$ {total_compra:.2f}\n")


p1 = Produto("Notebook", 3500.00, 10)
p2 = Produto("Mouse", 120.00, 50)
p3 = Produto("Teclado", 250.00, 5)


meu_carrinho = CarrinhoDeCompras()

meu_carrinho.adicionar_ao_carrinho(p1, 1) 
meu_carrinho.adicionar_ao_carrinho(p2, 2)
meu_carrinho.adicionar_ao_carrinho(p3, 10) 

meu_carrinho.mostrar_carrinho()