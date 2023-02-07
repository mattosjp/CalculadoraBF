from tkinter import *

from math import log

import matplotlib.pyplot as plt

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from time import sleep



class App:

    def __init__(self):

        self.root = root

        self.configura_tela()

        self.widgets()

        self.frames()

        root.mainloop()

    def configura_tela(self):

        self.root.title('Researt')

        #centralizar o programa na tela

        self.larguraT, self.alturaT = 1000, 725

        self.largura_display = self.root.winfo_screenwidth()

        self.altura_display = self.root.winfo_screenheight()

        self.posx = self.largura_display/2-1000/2

        self.posy = self.altura_display/2-700/2

        self.root.geometry('%dx%d+%d+%d' % (self.larguraT, self.alturaT, self.posx, self.posy))

        self.root.resizable(False, False)



        self.root.configure(bg='#353535')

    def widgets(self):

        pass



    def frames(self):

        #Frame do quadrado do menu------------------------------------------------------------------------------------------------------------------

        self.quadrado_menu = Frame(self.root)

        self.quadrado_menu.place(x=310, y=100)

        

        self.titulo = Label(self.quadrado_menu, bg='#353535', width=20, height=1, bd=9, text='RESEART', fg='white', font='Arial 20 bold').grid(row=0, column=0)

        self.vazio2 = Label(self.quadrado_menu,bg='#353535', width=50, bd=4, height='4').grid(row=1, column=0)

        self.quadrado0 = Label(self.quadrado_menu, bg='#535353', width=50, height=25, bd=4, relief='solid').grid(row=2, column=0)

        #Frame do menu ----------------------------------------------------------------------------------------------------------------------

        self.frame0 = Frame(self.root, bg='#353535')

        self.frame0.place(x=433, y=300)

        self.btn_bf = Button(self.frame0, text='Calcular BF', font='Arial 15', command=self.acessar_bf)

        self.btn_quiz = Button(self.frame0, text='Quiz')

        self.btn_bf.grid(row=0, column=0)

        

        #Frame do quadrado do bf -----------------------------------------------------------------------------------------------------------

        self.quadrado_bf = Frame(self.root)

        

        self.quadrado1 = Label(self.quadrado_bf, bg='#535353', width=100, height=14, bd=3, relief='solid').grid(row=0, column=0)

        

        #Frame do bf --------------------------------------------------------------------------------------------------------------------

        self.frame1 = Frame(self.root, bg='#535353')

        



        #LABEL-bf

        

        self.l1 = Label(self.frame1, text='Digite sua altura (cm):', bg='#535353', fg='white', font='Arial, 16').grid(row=0, column=0)

        self.l2 = Label(self.frame1, text='Circunferência da sua cintura(cm):', bg='#535353', fg='white', font='Arial, 16').grid(row=1, column=0)

        self.l3 = Label(self.frame1, text='Circunferência do seu pescoço(cm): ', bg='#535353', fg='white', font='Arial, 16').grid(row=2, column=0)

        self.l3 = Label(self.frame1, text='Quadril (somente para mulheres): ', bg='#535353', fg='white', font='Arial, 16').grid(row=3, column=0)

        self.resultado = Label(self.frame1, text='', bg='#535353', fg='black', font='Arial, 16')

        self.resultado.grid(row=7, column=0, sticky=N)

        self.vazio = Label(self.frame1, text='', bg='#535353').grid(row=6, column=3)

        #ENTRY-bf

        self.t1 = Entry(self.frame1, font='Arial, 16')

        self.t2 = Entry(self.frame1, font='Arial, 16')

        self.t3 = Entry(self.frame1, font='Arial, 16')

        self.t4 = Entry(self.frame1, font='Arial, 16')

        self.t1.grid(row=0, column=1)

        self.t2.grid(row=1, column=1)

        self.t3.grid(row=2, column=1)

        self.t4.grid(row=3, column=1)

        self.t1.focus()

        #BUTTON-bf

        self.b = Button(self.frame1, text='CALCULAR', command=self.calcular).grid(row=7, column=1, sticky='NE')

        #MENU-bf

        self.meuMenu = Menu(self.frame1)

        

        self.fileMenu = Menu(self.meuMenu, tearoff=0)

        self.fileMenu.add_command(label='Menu principal', command=self.acessar_menu)

        self.fileMenu.add_separator()

        self.fileMenu.add_command(label='Calculadora de BF')

        self.meuMenu.add_cascade(label='Menu', menu=self.fileMenu)

        



    def calcular(self):

        #BF masculino -------------------------------------------------

        if self.t4.get() == '':
                
            self.altura = float(self.t1.get())/2.54

            self.cintura = float(self.t2.get())/2.54

            self.pescoco = float(self.t3.get())/2.54

            self.bf = ((log(self.cintura-self.pescoco, 10)*86.010)-(log(self.altura, 10)*70.041))+36

            self.bf = round(self.bf)

            self.resultado['text']=f'Gordura corporal = {self.bf}%'

            self.resultado['bd']=3

            self.resultado['relief']='solid'

            self.resultado['bg']='white'

            #APARECER GRÁFICO - Homem 

            self.grafico_h = Frame(self.root, bd='4', relief='solid')

            self.grafico_h.place(x=234, y=320)

            self.bfhomem = ['Essencial', 'Atleta', 'Regular', 'Média', 'Acima do peso']

            self.valores_homem = [2, 6, 14, 18, 25]

            self.figura=plt.Figure(figsize=(9, 6), dpi=60)

            self.figura.suptitle('Resultado BF - Masculino')

            self.grafico=self.figura.add_subplot(111)

            self.grafico.axhline(self.bf, 0, 1, color='r', **{'ls':'--', 'lw':2})

            canva=FigureCanvasTkAgg(self.figura, self.grafico_h)

            canva.draw()

            canva.get_tk_widget().grid(row=9, column=0)

            #CONDIÇÕES PARA MUDANÇA DE COR DAS BARRAS

            if self.bf < 2:

                self.grafico.bar(self.bfhomem, self.valores_homem, color=['#FAAC58', '#58ACFA', '#58ACFA', '#58ACFA', '#58ACFA'])

            elif self.bf < 6:

                self.grafico.bar(self.bfhomem, self.valores_homem, color=['#58ACFA', '#FAAC58', '#58ACFA', '#58ACFA', '#58ACFA'])

            elif self. bf < 14:

                self.grafico.bar(self.bfhomem, self.valores_homem, color=['#58ACFA', '#58ACFA', '#FAAC58', '#58ACFA', '#58ACFA'])

            elif self. bf < 18:

                self.grafico.bar(self.bfhomem, self.valores_homem, color=['#58ACFA', '#58ACFA', '#58ACFA', '#FAAC58', '#58ACFA'])

            elif self. bf < 25:

                self.grafico.bar(self.bfhomem, self.valores_homem, color=['#58ACFA', '#58ACFA', '#58ACFA', '#58ACFA', '#FAAC58'])

            else:

                self.grafico.bar(self.bfhomem, self.valores_homem, color=['#58ACFA', '#58ACFA', '#58ACFA', '#58ACFA', '#FAAC58'])

            

        

            

        #BF feminino -----------------------------------------------------

        elif self.t4.get() != '':

            self.altura = float(self.t1.get())/2.54

            self.cintura = float(self.t2.get())/2.54

            self.pescoco = float(self.t3.get())/2.54

            self.quadril = float(self.t4.get())/2.54

            self.bf = ((log(self.cintura+self.quadril-self.pescoco, 10)*163.205))-(log(self.altura, 10)*97.684)- 78.387

            self.bf = round(self.bf)

            self.resultado['text']=f'Gordura corporal = {self.bf}%'

            self.resultado['bd']=3

            self.resultado['relief']='solid'

            self.resultado['bg']='white'

        #APARECER GRÁFICO - Mulher

            self.grafico_m = Frame(self.root, bd='4', relief='solid')

            self.grafico_m.place(x=234, y=320)

            self.bfhomem = ['Essencial', 'Atletas', 'Regular', 'Média', 'Acima do peso']

            self.valores_homem = [10, 14, 21, 25, 32]

            self.figura=plt.Figure(figsize=(9, 6), dpi=60)

            self.figura.suptitle('Resultado BF - Feminino')

            self.grafico=self.figura.add_subplot(111)

            self.grafico.axhline(self.bf, 0, 1, color='r', **{'ls':'--', 'lw':2})

            canva=FigureCanvasTkAgg(self.figura, self.grafico_m)

            canva.draw()

            canva.get_tk_widget().grid(row=9, column=0)

            #CONDIÇÕES PARA MUDANÇA DE COR DAS BARRAS

            if self.bf < 10:

                self.grafico.bar(self.bfhomem, self.valores_homem, color=['#FAAC58', '#58ACFA', '#58ACFA', '#58ACFA', '#58ACFA'])

            elif self.bf < 14:

                self.grafico.bar(self.bfhomem, self.valores_homem, color=['#58ACFA', '#FAAC58', '#58ACFA', '#58ACFA', '#58ACFA'])

            elif self.bf < 21:

                self.grafico.bar(self.bfhomem, self.valores_homem, color=['#58ACFA', '#58ACFA', '#FAAC58', '#58ACFA', '#58ACFA'])

            elif self.bf < 25:

                self.grafico.bar(self.bfhomem, self.valores_homem, color=['#58ACFA', '#58ACFA', '#58ACFA', '#FAAC58', '#58ACFA'])

            elif self.bf < 32:

                self.grafico.bar(self.bfhomem, self.valores_homem, color=['#58ACFA', '#58ACFA', '#58ACFA', '#58ACFA', '#FAAC58'])

            else:

                self.grafico.bar(self.bfhomem, self.valores_homem, color=['#58ACFA', '#58ACFA', '#58ACFA', '#58ACFA', '#FAAC58'])



    def acessar_bf(self):

        #Guardar menu

        self.frame0.place_forget()

        self.quadrado_menu.place_forget()

        #Aparecer bf

        sleep(0.2)

        self.frame1.place(x=165, y=90)

        self.quadrado_bf.place(x=150, y=50)

        #Aparecer barra do menu

        self.root.config(menu=self.meuMenu)

    def acessar_menu(self):

        #Guardar outras páginas

        self.frame1.place_forget()

        self.quadrado_bf.place_forget()

        self.meuMenu.forget()

        self.grafico_h.place_forget()



          

        #Aparecer menu

        self.frame0.place(x=433, y=300)

        self.quadrado_menu.place(x=310, y=100)



            





#RROGRAMA PRINCIPAL

root = Tk()

App()