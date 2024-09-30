from tkinter import *
from tkinter import ttk
from tkinter import tix
import sqlite3

janela = tix.Tk() #root

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

class Application(Funcs):                            # uma classe que mantem a janela aberta em loop
    def __init__(self):
        self.janela = janela                    # como janela nao esta na classe, deve-se fazer uma equivalencia
        self.tela()                             # chama a funcao tela
        self.frames_da_tela()
        self.widtgets_frame1()
        self.widgets_frame2()
        self.monta_tabelas()
        self.select_lista()
        janela.mainloop()
    def tela(self):
        self.janela.title("Cadastro de Clientes") #função para as configurações da tela
        self.janela.configure(background='#1e3743')
        self.janela.geometry("700x500")
        self.janela.resizable(True, True)
        self.janela.maxsize(width="900", height="700")
        self.janela.minsize(width="500", height="400")
    def frames_da_tela(self):
        self.frame_1 = Frame(self.janela, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        # para relx e rely, e a posicao relativa do objeto em relacao a tela, vai de 0 a 1, onde 0 e totalmente a esquerda e 1 a direita
        # relwidth e relheight e a porcentagem que ocupara de largura e altura respectivamente
        self.frame_1.place(relx= 0.02, rely=0.02, relwidth=0.95, relheight=0.46)

        self.frame_2 = Frame(self.janela, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        self.frame_2.place(relx= 0.02, rely=0.5, relwidth=0.95, relheight=0.46)
    def widtgets_frame1(self):
        self.abas = ttk.Notebook(self.frame_1) #passa as abas para o frame_1 e os widgets do frame_1 para as abas
        self.aba1 = Frame(self.abas)
        self.aba1.configure(background= '#dfe3ee')
        self.abas.add(self.aba1, text="Aba 1")
        self.aba2 = Frame(self.abas)
        self.aba2.configure(background= '#dfe3ee')
        self.abas.add(self.aba2, text="Aba 2")
        self.abas.place(relx=0, rely=0, relwidth=0.98, relheight=0.98)

        ### Criação do botão limpar
        self.bt_limpar = Button(self.aba1, text="Limpar", command=self.limpa_tela,  bd=2, bg='#107db2', fg='white')
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botão buscar
        self.bt_buscar = Button(self.aba1, text="Buscar", command= self.busca_cliente, bd=2, bg='#107db2', fg='white')
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        text_balao_buscar = "Digite no campo nome o cliente que deseja pesquisar"
        self.balao_buscar = tix.Balloon(self.aba1)
        self.balao_buscar.bind_widget(self.bt_buscar, balloonmsg = text_balao_buscar)
        ### Criação do botão novo
        self.bt_novo = Button(self.aba1, text="Novo", command= self.add_cliente, bd=2, bg='#107db2', fg='white')
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botão alterar
        self.bt_Alterar = Button(self.aba1, text="Alterar", command= self.alterar_cliente, bd=2, bg='#107db2', fg='white')
        self.bt_Alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botão apagar
        self.bt_Apagar = Button(self.aba1, text="Apagar", command= self.deleta_cliente, bd=2, bg='#107db2', fg='white')
        self.bt_Apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        ### Criação da label e entrada do código
        self.lb_codigo = Label(self.aba1, text="Código", bg='#dfe3ee', fg='#107db2')
        self.lb_codigo.place(relx=0.05, rely=0.05)

        self.codigo_entry = Entry(self.aba1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        ### Criação da label e entrada do nome
        self.lb_nome = Label(self.aba1, text="Nome", bg='#dfe3ee', fg='#107db2')
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = Entry(self.aba1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.8)

         ### Criação da label e entrada do telefone
        self.lb_telefone = Label(self.aba1, text="Telefone", bg='#dfe3ee', fg='#107db2')
        self.lb_telefone.place(relx=0.05, rely=0.60)

        self.telefone_entry = Entry(self.aba1)
        self.telefone_entry.place(relx=0.05, rely=0.7, relwidth=0.4)

         ### Criação da label e entrada da cidade
        self.lb_cidade = Label(self.aba1, text="Cidade", bg='#dfe3ee', fg='#107db2')
        self.lb_cidade.place(relx=0.5, rely=0.6)

        self.cidade_entry = Entry(self.aba1)
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4)
    def widgets_frame2(self):
        self.lista_client = ttk.Treeview(self.frame_2, height=3, column=("col1", "col2", "col3", "col4"))
        self.lista_client.heading("#0", text="")
        self.lista_client.heading("#1", text="Código")
        self.lista_client.heading("#2", text="Nome")
        self.lista_client.heading("#3", text="Telefone")
        self.lista_client.heading("#4", text="Cidade")

        self.lista_client.column("#0", width=1)
        self.lista_client.column("#1", width=50)
        self.lista_client.column("#2", width=200)
        self.lista_client.column("#3", width=125)
        self.lista_client.column("#4", width=125)

        self.lista_client.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scroll_lista_c = Scrollbar(self.frame_2, orient='vertical')
        self.lista_client.configure(yscroll=self.scroll_lista_c.set)
        self.scroll_lista_c.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)

        # o bind indica que quando tiver alguma interação com o lista_client(treeview) do tipo double mouse 1, aciona o venento da função OnDoubleClick
        self.lista_client.bind ("<Double-1>", self.OnDoubleClick)  


Application()