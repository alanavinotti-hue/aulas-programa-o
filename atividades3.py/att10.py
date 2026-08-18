# Crie uma classe OrdemDeServico com os atributos: cliente e descricao;
# Crie um atributo de classe chamado total_os_criadas = 0 e um atributo chamado os_abertas = 0;
# Sempre que uma nova OrdemDeServico for instanciada (__init__), o atributo de classe total_os_criadas e os_abertas devem ser incrementadas em 1, e o objeto ordem de serviço atual deve receber o valor de total_os_criadas como seu id_os;
# Crie o atributo status que inicia como "Aberta";
# Crie o método finalizar_os() que altera o status para "Concluída" e diminua em 1 o valor de os_abertas;
# Instancie 3 ordens de serviço e conclua uma;
# Crie um método capaz de verificar quantas ordens estão abertas.

class OrdemDeServiço:
    total_os_criadas = 0
    os_abertas = 0

    def __init__(self, cliente, descricao):
        OrdemDeServiço.total_os_criadas += 1
        OrdemDeServiço.os_abertas += 1
        self.id_os = OrdemDeServiço.total_os_criadas
        self.cliente = cliente
        self.descricao = descricao
        self.status = "aberta"

        def finalizar_os(self):
            if self.status == "aberta":
                self.status = "concluída"
                OrdemDeServiço.os_abertas -= 1
            else:
                print("A ordem de serviço ja foi concluida.")

                




            
