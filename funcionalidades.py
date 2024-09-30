from modulos import*

class Funcs():
    def limpa_tela(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
    def conecta_bd(self):
        self.conexao = sqlite3.connect("clientes.bd")
        self.cursor = self.conexao.cursor(); print("Conectando ao banco de dados")
        # quem executa os comandos da minha conexão
    def desconecta_bd(self):
        self.conexao.close(); print("Desconectando ao banco de dados")
    def monta_tabelas(self):
        self.conecta_bd()
        ### Criar tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS cadastro_clientes (
                cod INTEGER PRIMARY KEY,    
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40)
            );
        """)
        self.conexao.commit(); print("Banco de dados criado")
        self.desconecta_bd()
    def variaveis_entry(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.cidade = self.cidade_entry.get()
    def add_cliente(self):
        self.variaveis_entry()
        if self.nome_entry.get() == "":
            mensagem = "Para cadastrar um novo cliente é necessário que o campo nome não esteja vazio"
            messagebox.showinfo("Cadastro de Cliente - Aviso!", mensagem)
        else:
            self.conecta_bd()
            self.cursor.execute(""" INSERT INTO cadastro_clientes (nome_cliente, telefone, cidade) VALUES (?, ?, ?)""", (self.nome, self.telefone, self.cidade))
            self.conexao.commit()
            self.desconecta_bd()
            self.select_lista() # limpa a listagem atual e chama a função de listagem com o novo valor add
            self.limpa_tela() # limpa todas as entrys do frame 1
    def select_lista(self):
        self.lista_client.delete(*self.lista_client.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM cadastro_clientes
                ORDER BY nome_cliente ASC; """)
        for i in lista:
            self.lista_client.insert("", END, values=i)
        self.desconecta_bd()
    def OnDoubleClick(self, event):
        self.limpa_tela()
        self.lista_client.selection()

        for n in self.lista_client.selection():
            col1, col2, col3, col4 = self.lista_client.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.telefone_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)
    def deleta_cliente(self):
        self.variaveis_entry()
        self.conecta_bd()
        self.cursor.execute("""DELETE FROM cadastro_clientes WHERE cod = ? """, (self.codigo))
        self.conexao.commit()
        self.desconecta_bd()
        self.limpa_tela()
        self.select_lista()
    def alterar_cliente(self):
        self.variaveis_entry()
        self.conecta_bd()
        self.cursor.execute(""" UPDATE cadastro_clientes SET nome_cliente = ?, telefone = ?, cidade = ? WHERE cod = ? 
            """, (self.nome, self.telefone, self.cidade, self.codigo))
        self.conexao.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()
    def busca_cliente(self):
        self.conecta_bd()
        self.lista_client.delete(*self.lista_client.get_children())

        self.nome_entry.insert(END, '%') #adciona forçadamente um '%' na entry nome para que na pesquisa inclua tudo que tem o trecho que foi digitado(se digitar 'mar', apare por exemplo, maria, marcos, mariana, marina)
        nome = self.nome_entry.get()
        self.cursor.execute(
            """ SELECT cod, nome_cliente, telefone, cidade FROM cadastro_clientes
            WHERE nome_cliente LIKE '%s' ORDER BY nome_cliente ASC""" % nome)
        busca_nome_cli = self.cursor.fetchall() # fecha o laço da pesquisa e para usar no laço for
        for i in busca_nome_cli:
            self.lista_client.insert("", END, values=i)
        self.limpa_tela()
        self.desconecta_bd()
    def imprimir_estado_civil(self):
        self.estado_civil = self.estado_civil_var.get()
        print(self.estado_civil)
