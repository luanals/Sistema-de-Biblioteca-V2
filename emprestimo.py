import datetime
from datetime import timedelta
from exemplar import Exemplar
from usuario import Usuario
from fila_espera import FilaDeEspera
from item import Item

class Emprestimo:
    itens_emprestados = {}
    emprestimos = []

    def __init__(self, exemplar, usuario, data_inicio, data_fim=None, data_devolucao=None, valor_multa=0, situacao_multa=None):
        if exemplar.esta_disponivel():
            if isinstance(usuario, Usuario):
                data_fim = data_inicio + timedelta(days=usuario.dias_emprestimos)
                if len(usuario.itens_emprestados) < usuario.quantidade_itens_max:
                    if usuario.tem_item_em_atraso():
                        print("Você possui pelo menos um item em atraso. Não é possível emprestar o item.")
                    else:
                        self.exemplar = exemplar
                        self.usuario = usuario
                        self.categoria_user = usuario.categoria
                        self.data_inicio = data_inicio
                        self.data_fim = data_fim
                        self.data_devolucao = data_devolucao
                        self.valor_multa = valor_multa
                        self.situacao_multa = situacao_multa

                        if self not in self.itens_emprestados:
                            self.itens_emprestados[self] = 1
                        else:
                            self.itens_emprestados[self] += 1

                        self.emprestimos.append(self)

                        print("Item emprestado com sucesso.\n")

                else:
                    print("Você atingiu o número máximo de itens. Não é possível emprestar o item.\n")
        else:
            print("Este exemplar não está disponível para empréstimo.\n")

    def __str__(self):
        return f"Exemplar: {self.exemplar}, Usuário: {self.usuario}, Data de início: {self.data_inicio}, Data de fim: {self.data_fim}, Data de devolução: {self.data_devolucao}, Valor da multa: {self.valor_multa}, Situação da multa: {self.situacao_multa}"

    @staticmethod
    def listar_itens_emprestados():
        for emprestimo in Emprestimo.emprestimos:
            print(f"Usuário: {emprestimo.usuario.nome}")
            print(f"Título: {emprestimo.exemplar.titulo}")
            print(f"ID do item emprestado: {emprestimo.exemplar.id_item}")
            print(f"Data de início do empréstimo: {emprestimo.data_inicio}")
            print(f"Data de fim do empréstimo: {emprestimo.data_fim}")
            if emprestimo.data_devolucao:
                print(f"Data de devolução: {emprestimo.data_devolucao}\n")
            else:
                print("Item ainda não devolvido.\n")
        print("\n")

    @classmethod
    def listar_50_mais_emprestados(cls):
        itens_sorted = sorted(cls.itens_emprestados.items(), key=lambda x: x[1], reverse=True)
        ids_50_mais_emprestados = [item[0].exemplar.id_item for item in itens_sorted[:50]]

        titulos_50_mais_emprestados = []
        for id_item in ids_50_mais_emprestados:
            titulo = Item.procurar_item_por_id(id_item)
            if titulo:
                titulos_50_mais_emprestados.append(titulo)

        return titulos_50_mais_emprestados

    @staticmethod
    def quantidade_itens_emprestados_mes():
        mes_atual = datetime.datetime.now().month
        contador_emprestimos_mes = 0
        for emprestimo in Emprestimo.emprestimos:
            if emprestimo.data_inicio.month == mes_atual:
                contador_emprestimos_mes += 1
        return contador_emprestimos_mes

    @staticmethod
    def quantidade_itens_emprestados_semana():
        data_atual = datetime.datetime.now()
        semana_atual = data_atual.isocalendar()[1]
        emprestimos_por_semana = {}
        for emprestimo in Emprestimo.emprestimos:
            semana_emprestimo = emprestimo.data_inicio.isocalendar()[1]
            if semana_emprestimo not in emprestimos_por_semana:
                emprestimos_por_semana[semana_emprestimo] = 1
            else:
                emprestimos_por_semana[semana_emprestimo] += 1
        return emprestimos_por_semana

    @staticmethod
    def quantidade_itens_emprestados_dia():
        emprestimos_por_dia = {}
        for emprestimo in Emprestimo.emprestimos:
            dia_semana = emprestimo.data_inicio.strftime("%A")
            if dia_semana not in emprestimos_por_dia:
                emprestimos_por_dia[dia_semana] = 1
            else:
                emprestimos_por_dia[dia_semana] += 1
        return emprestimos_por_dia

    @staticmethod
    def quantidade_dias_atraso_por_item():
        dias_atraso_por_item = {}
        data_atual = datetime.datetime.now()
        for emprestimo in Emprestimo.emprestimos:
            if emprestimo.data_devolucao and emprestimo.data_devolucao > emprestimo.data_fim:
                dias_atraso = (emprestimo.data_devolucao - emprestimo.data_fim).days
                id_item_emprestado = emprestimo.exemplar.id_item
                titulo_item = Item.procurar_item_por_id(id_item_emprestado)
                if titulo_item:
                    if titulo_item not in dias_atraso_por_item:
                        dias_atraso_por_item[titulo_item] = dias_atraso
                    else:
                        dias_atraso_por_item[titulo_item] += dias_atraso
        if dias_atraso_por_item == {}:
            print("Não há itens em atraso.\n")
        return dias_atraso_por_item
