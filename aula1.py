from tkinter import *
from tkinter import ttk
import mysql.connector # conecta o python ao mysql
from mysql.connector import errorcode

janela = Tk() #root

class Funcs():
    def limpa_tela(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.cidade_entry.delete(0, END)
    def conecta_bd(self):
        self.conexao = mysql.connector.connect( #precisa passar 4 parametros
            host='localhost',
            user='root',
            password='admin',
            database='clientes',
        ); print("Conectando ao banco de dados")
        self.cursor = self.conexao.cursor() # quem executa os comandos da minha conexão
    def desconecta_bd(self):
        self.cursor.close()   # no final do código precisa fechar ambos
        self.conexao.close(); print("Desconectando ao banco de dados")
    def monta_tabelas(self):
        try:
            # Conexão com o MySQL
            self.conexao = mysql.connector.connect(
                host='localhost',
                user='root',
                password='admin'
        ); print("Conectando ao banco de dados")
        
            self.cursor = self.conexao.cursor()
        
            # Criação do banco de dados
            self.cursor.execute("CREATE DATABASE IF NOT EXISTS clientes")
            self.cursor.execute("USE clientes")

            # Criação da tabela
            criar_tabela = """
            CREATE TABLE IF NOT EXISTS cadastro_clientes (
                cod INTEGER PRIMARY KEY,    
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40)
            )
            """
        
            self.cursor.execute(criar_tabela); print("Banco de dados e tabela criados com sucesso!")

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Erro: usuário ou senha inválidos")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Erro: banco de dados não existe")
            else:
                print(f"Erro: {err}")
        finally:
            # Fechando a conexão
            self.desconecta_bd()

class Application(Funcs):                            # uma classe que mantem a janela aberta em loop
    def __init__(self):
        self.janela = janela                    # como janela nao esta na classe, deve-se fazer uma equivalencia
        self.tela()                             # chama a funcao tela
        self.frames_da_tela()
        self.widtgets_frame1()
        self.widgets_frame2()
        self.monta_tabelas()
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
        ### Criação do botão limpar
        self.bt_limpar = Button(self.frame_1, text="Limpar", command=self.limpa_tela,  bd=2, bg='#107db2', fg='white')
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botão buscar
        self.bt_buscar = Button(self.frame_1, text="Buscar", bd=2, bg='#107db2', fg='white')
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botão novo
        self.bt_novo = Button(self.frame_1, text="Novo", bd=2, bg='#107db2', fg='white')
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botão alterar
        self.bt_Alterar = Button(self.frame_1, text="Alterar", bd=2, bg='#107db2', fg='white')
        self.bt_Alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botão apagar
        self.bt_Apagar = Button(self.frame_1, text="Apagar", bd=2, bg='#107db2', fg='white')
        self.bt_Apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        ### Criação da label e entrada do código
        self.lb_codigo = Label(self.frame_1, text="Código", bg='#dfe3ee', fg='#107db2')
        self.lb_codigo.place(relx=0.05, rely=0.05)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        ### Criação da label e entrada do nome
        self.lb_nome = Label(self.frame_1, text="Nome", bg='#dfe3ee', fg='#107db2')
        self.lb_nome.place(relx=0.05, rely=0.35)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.45, relwidth=0.8)

         ### Criação da label e entrada do telefone
        self.lb_telefone = Label(self.frame_1, text="Telefone", bg='#dfe3ee', fg='#107db2')
        self.lb_telefone.place(relx=0.05, rely=0.60)

        self.telefone_entry = Entry(self.frame_1)
        self.telefone_entry.place(relx=0.05, rely=0.7, relwidth=0.4)

         ### Criação da label e entrada da cidade
        self.lb_cidade = Label(self.frame_1, text="Cidade", bg='#dfe3ee', fg='#107db2')
        self.lb_cidade.place(relx=0.5, rely=0.6)

        self.cidade_entry = Entry(self.frame_1)
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



Application()