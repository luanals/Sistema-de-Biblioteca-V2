class Item:
    def __init__(self, titulo, ano, id_item):
        self.titulo = titulo
        self.ano = ano
        self.id_item = id_item

    @staticmethod
    def procurar_por_id(id_item, arquivo, indice_titulo):
        with open(arquivo, "r") as arquivo:
            for linha in arquivo:
                dados_item = linha.strip().split(",")
                if int(dados_item[-1]) == int(id_item):
                    return dados_item[indice_titulo]
        return f"O item com o ID {id_item} especificado não foi encontrado."