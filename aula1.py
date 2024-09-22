from tkinter import *

janela = Tk() #root

class Application():                            # uma classe que mantem a janela aberta em loop
    def __init__(self):
        self.janela = janela                    # como janela nao esta na classe, deve-se fazer uma equivalencia
        self.tela()                             # chama a funcao tela
        self.frames_da_tela()
        self.widtgets_frame1()
        janela.mainloop()
    def tela(self):
        self.janela.title("Cadastro de Clientes") #função para as configurações da tela
        self.janela.configure(background='#1e3743')
        self.janela.geometry("700x500")
        self.janela.resizable(True, True)
        self.janela.maxsize(width="900", height="700")
        self.janela.minsize(width="400", height="300")
    def frames_da_tela(self):
        self.frame_1 = Frame(self.janela, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        # para relx e rely, e a posicao relativa do objeto em relacao a tela, vai de 0 a 1, onde 0 e totalmente a esquerda e 1 a direita
        # relwidth e relheight e a porcentagem que ocupara de largura e altura respectivamente
        self.frame_1.place(relx= 0.02, rely=0.02, relwidth=0.95, relheight=0.46)

        self.frame_2 = Frame(self.janela, bd=4, bg='#dfe3ee', highlightbackground='#759fe6', highlightthickness=3)
        self.frame_2.place(relx= 0.02, rely=0.5, relwidth=0.95, relheight=0.46)
    def widtgets_frame1(self):
        ### Criando o botão limpar
        self.bt_limpar = Button(self.frame_1, text="Limpar")
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criando o botão buscar
        self.bt_buscar = Button(self.frame_1, text="Buscar")
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criando o botão novo
        self.bt_novo = Button(self.frame_1, text="Novo")
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criando o botão alterar
        self.bt_Alterar = Button(self.frame_1, text="Alterar")
        self.bt_Alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criando o botão apagar
        self.bt_Apagar = Button(self.frame_1, text="Apagar")
        self.bt_Apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)
        

Application()