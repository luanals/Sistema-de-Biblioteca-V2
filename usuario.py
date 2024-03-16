from datetime import datetime


class Usuario:
    def __init__(self, nome, email, telefone, filiacao, nascimento, categoria):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.filiacao = filiacao
        self.nascimento = nascimento
        self.categoria = categoria
        self.itens_emprestados = []

        if self.categoria == "Aluno de graduacao":
            self.dias_emprestimos = 7
            self.quantidade_itens_max = 5
        elif self.categoria == "Aluno de pós-graduacao":
            self.dias_emprestimos = 15
            self.quantidade_itens_max = 9
        elif self.categoria == "Professor":
            self.dias_emprestimos = 60
            self.quantidade_itens_max = 15

        with open("usuarios.txt", "a") as arquivo:
            arquivo.write(f"{self.nome},{self.email},{self.telefone},{self.filiacao},{self.nascimento},{self.categoria}\n")
        print(f'\nUsuário(a) {self.nome} foi cadastrado com sucesso.\n')

    def consultar(self):
        print(f'Informações do usuário {self.nome}:')
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")
        print(f"Filiação: {self.filiacao}")
        print(f"Nascimento: {self.nascimento}")
        print(f"Categoria: {self.categoria} \n")

    def adicionar_emprestimo(self, item):
        if len(self.itens_emprestados) < self.quantidade_itens_max:
            self.itens_emprestados.append(item)
            print("\nItem adicionado à lista de empréstimos do usuário.\n")
        else:
            print("Você atingiu o número máximo de itens. Não é possível adicionar mais itens.\n")

    def exibir_lista_do_usuario(self):
        print("\nRegistro de empréstimos do usuário:")
        for item in self.itens_emprestados:
            print(f"Título: {item.titulo} | ID: {item.id_item}")

    def exibir_lista_multas_do_usuario(self):
        print("\nRegistro de multas do usuário:")
        for item in self.itens_emprestados:
            if hasattr(item, 'valor_multa') and hasattr(item, 'situacao_multa'):
                if item.situacao_multa == "Paga":
                    print(f"Multas pagas para o item {item.titulo}: R${item.valor_multa:.2f}")
                elif item.situacao_multa == "Pendente":
                    print(f"Multas pendentes para o item {item.titulo}: R${item.valor_multa:.2f}")

    def tem_item_em_atraso(self):
        data_atual = datetime.now()
        for item in self.itens_emprestados:
            if hasattr(item, 'data_fim') and hasattr(item, 'data_devolucao'):
                if item.data_fim and item.data_fim < data_atual and item.data_devolucao is None:
                    return True
        return False

    def pesquisar_livro(self):
        # Lógica para pesquisar livros no sistema (?)
        pass
