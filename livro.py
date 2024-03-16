from item import Item
from exemplar import Exemplar

class Livro(Item):
    def __init__(self, titulo, isbn, editora, ano, autores, id_livro):
        super().__init__(titulo, ano, id_livro)
        self.isbn = isbn
        self.editora = editora
        self.autores = autores
        self.exemplares = []

    def cadastrar(self, exemplares):
        self.exemplares.extend(exemplares)
        # Lógica para cadastrar um livro no sistema
        with open("livros.txt", "a") as arquivo:
            arquivo.write(f"{self.titulo},{self.isbn},{self.editora},{self.ano},{','.join(self.autores)},{self.id_item}\n")
        print(f'\nO livro "{self.titulo}" foi cadastrado com sucesso com {len(exemplares)} exemplares. \n')

    def consultar(self):
        # Lógica para consultar informações de um livro
        print(f'Informações do livro "{self.titulo}":')
        print(f"Título: {self.titulo}")
        print(f"ISBN: {self.isbn}")
        print(f"Editora: {self.editora}")
        print(f"Ano: {self.ano}")
        print(f"Autores: {', '.join(self.autores)}")
        print(f"ID: {self.id_item}")
        print("Exemplares disponíveis:")

        for exemplar in self.exemplares:
            if exemplar.disponivel:
                print(f"- ID do exemplar: {exemplar.id_exemplar} (Disponível)")
            else:
                print(f"- ID do exemplar: {exemplar.id_exemplar} (Indisponível)")

    
    @staticmethod
    def procurar_por_id(id_livro):
        return super().procurar_por_id(id_livro, "livros.txt", 0)
            