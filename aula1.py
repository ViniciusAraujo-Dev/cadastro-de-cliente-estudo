from modulos import*
from validEntry import Validadores
from funcionalidades import Funcs

janela = tix.Tk() #root
class Application(Funcs, Validadores):                            # uma classe que mantem a janela aberta em loop
    def __init__(self):
        self.janela = janela                    # como janela nao esta na classe, deve-se fazer uma equivalencia
        self.valida_entradas()
        self.tela()                             # chama a funcao tela
        self.frames_da_tela()
        self.widgets_frame1()
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
    def widgets_frame1(self):
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

        self.codigo_entry = Entry(self.aba1, validate = "key", validatecommand=self.valida3)
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

        #### Aba 2
        #labe optionMenu
        self.estado_civil_label = Label(self.aba2,text="Estado civil", bg='#dfe3ee', fg='#107db2')
        self.estado_civil_label.place(relx=0.025, rely=0.1, relwidth=0.2, relheight=0.2)

        ### drop down list
        self.estado_civil_var = StringVar()
        self.estado_civil_list = ("Solteiro(a)", "Casado(a)", "Divorciado(a)", "Viuvo(a)")
        self.estado_civil_var.set("Selecione")
        self.estado_civil_menu = OptionMenu(self.aba2, self.estado_civil_var, *self.estado_civil_list)
        self.estado_civil_menu.place(relx=0.2, rely=0.1, relwidth=0.2, relheight=0.2)
        self.estado_civil = self.estado_civil_var.get()

        # Botão para imprimir
        botao_imprimir = Button(self.aba2, text="Imprimir", command=self.imprimir_estado_civil)
        botao_imprimir.place(relx=0.2, rely=0.3, relwidth=0.2, relheight=0.2)
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
    def valida_entradas(self):
        self.valida3 = (self.janela.register(self.validate_entry3), "%P")

Application()

####### a fazer:  calendário, menus