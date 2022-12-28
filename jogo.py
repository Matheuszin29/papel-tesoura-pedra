import tkinter
from tkinter import * 
from tkinter import ttk

#import random

import random

#import pillow

from PIL import Image, ImageTk

# cores --------------------------------
co0 = "#FFFFFF"  # white / branca
co1 = "#333333"  # black / preta
co2 = "#fcc058"  # orange / laranja
co3 = "#fff873"  # yellow / amarela
co4 = "#34eb3d"   # green / verde
co5 = "#e85151"   # red / vermelha

fundo = "#3b3b3b"

#configurações de janela -------------
janela = Tk()
janela.title('')
janela.geometry('260x200')
janela.configure(bg=fundo)

# dividindo janela 

frame_cima = Frame(janela, width=260, height=100, bg=co1, relief='raised')
frame_cima.grid(row=0, column=0, sticky=NW) 

frame_baixo = Frame(janela, width=260, height=300, bg=co0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NW) 

estilo = ttk.Style(janela)
estilo.theme_use('clam')

#configurando frame_cima

app_1 = Label(frame_cima, text="Voce" ,height=1, anchor='center' , font=('Ivy 10 bold') ,  bg=co1 , fg=co0 )
app_1.place(x=25 , y=70 )
app_1_linha = Label(frame_cima , text="" ,height=10, anchor='center' , font=('Ivy 10 bold') ,  bg=co0 , fg=co0 )
app_1_linha.place(x=0 , y=0)
app_1_pontos = Label(frame_cima , text="0" ,height=1, anchor='center' , font=('Ivy 30 bold') ,  bg=co1 , fg=co0 )
app_1_pontos.place(x=50 , y=20)

app_ =Label(frame_cima, text=':' ,height=1 , anchor='center' , font=('Ivy 30 bold') ,  bg=co1 , fg=co0  ) 
app_.place(x=125 , y=20)

app_2_pontos = Label(frame_cima , text="0" ,height=1, anchor='center' , font=('Ivy 30 bold') ,  bg=co1 , fg=co0 )
app_2_pontos.place(x=170 , y=20)
app_2 = Label(frame_cima, text="PC" ,height=1, anchor='center' , font=('Ivy 10 bold') ,  bg=co1 , fg=co0 )
app_2.place(x=205 , y=70 )
app_2_linha = Label(frame_cima , text="" ,height=10, anchor='center' , font=('Ivy 10 bold') ,  bg=co0 , fg=co0 )
app_2_linha.place(x=255 , y=0)

app_linha =Label(frame_cima, text='' ,width=255 , anchor='center' , font=('Ivy 30 bold') ,  bg=co4 , fg=co0  ) 
app_linha.place(x=0 , y=95)

app_pc = Label(frame_baixo , text="" ,height=1, anchor='center' , font=('Ivy 10 bold') ,  bg=co0 , fg=co1 )
app_pc.place(x=170 , y=20)

global voce
global pc 
global ronda 
global ponto_voce
global pontos_pc

pontos_pc = 0
ponto_voce = 0
ronda = 5

#função logica do jogo

def jogar(i): 
    global ronda
    global ponto_voce
    global pontos_pc

    if ronda > 0 :
        print(ronda)
        option = ["pedra" , "papel"  , "tesoura"]
        pc = random.choice(option)
        voce = i

        print(voce , pc)
        if voce== "papel" and pc=="papel":
            print("empate")
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co0
            app_linha['bg'] = co0

        elif voce== "pedra" and pc=="pedra":
            print("empate")
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co0
            app_linha['bg'] = co0

        elif voce== "tesoura" and pc=="tesoura":
            print("empate")
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co0
            app_linha['bg'] = co0   

        elif voce== "papel" and pc=="pedra":
            print("voce ganhou")
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co0
            app_linha['bg'] = co0  
            ponto_voce +=10 

        elif voce== "pedra" and pc=="tesoura":
            print("voce ganhou")
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co0
            app_linha['bg'] = co0 
            ponto_voce +=10      

        elif voce== "tesoura" and pc=="papel":
            print("voce ganhou")
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co0
            app_linha['bg'] = co0 
            ponto_voce +=10

        elif voce== "papel" and pc=="tesoura":
            print("voce perdeu")
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co0
            app_linha['bg'] = co0  

            pontos_pc += 10

        elif voce== "tesoura" and pc=="pedra":
            print("voce perdeu")
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co0
            app_linha['bg'] = co0 
            pontos_pc += 10 

        elif voce== "pedra" and pc=="papel":
            print("voce perdeu")
            app_1_linha['bg'] = co4
            app_2_linha['bg'] = co0
            app_linha['bg'] = co0 
            pontos_pc += 10  

        #atualizando a pontuação
        app_1_pontos['text']= ponto_voce
        app_2_pontos['text']= pontos_pc          

        #rondas
        ronda -= 1

    else:   
        app_1_pontos['text']= ponto_voce
        app_2_pontos['text']= pontos_pc          

        #fim_de_jogo() 

#função iniciar jogo
#configuirando o frame_biaxo
def iniciar_jogo():
    global icon_1
    global icon_2
    global icon_3
    global b_icon_1
    global b_icon_2
    global b_icon_3

    icon_1 = Image.open('dedos.png')
    icon_1 = icon_1.resize((50,50),Image.ANTIALIAS)
    icon_1 = ImageTk.PhotoImage(icon_1)
    b_icon_1 = Button(frame_baixo, command=lambda:jogar('papel') ,width=50, image=icon_1, compound=CENTER , bg=co0 , fg=co0 ,font=('Ivy 10 bold') , anchor=CENTER , relief=FLAT)
    b_icon_1.place(x=15 , y=60)

    icon_2 = Image.open('rock.png')
    icon_2 = icon_2.resize((50,50),Image.ANTIALIAS)
    icon_2 = ImageTk.PhotoImage(icon_2)
    b_icon_2 = Button(frame_baixo, command=lambda:jogar('pedra') ,width=50, image=icon_2, compound=CENTER , bg=co0 , fg=co0 ,font=('Ivy 10 bold') , anchor=CENTER , relief=FLAT)
    b_icon_2.place(x=95 , y=60)

    icon_3 = Image.open('tesoura.png')
    icon_3 = icon_3.resize((50,50),Image.ANTIALIAS)
    icon_3 = ImageTk.PhotoImage(icon_3)
    b_icon_3 = Button(frame_baixo, command=lambda:jogar('tesoura') ,width=50, image=icon_3, compound=CENTER , bg=co0 , fg=co0 ,font=('Ivy 10 bold') , anchor=CENTER , relief=FLAT)
    b_icon_3.place(x=170 , y=60)




#função terminar jogo
def  fim_de_jogo():
    global ronda
    global ponto_voce
    global pontos_pc

    pontos_pc = 0
    ponto_voce = 0
    ronda = 5

    b_icon_1.destroy()
    b_icon_2.destroy()
    b_icon_3.destroy()

    jogador_voce =  int(app_1_pontos['text'])
    jogador_pc =  int(app_2_pontos['text'])

    if jogador_voce > jogador_pc:
        app_vencedor = Label(frame_baixo , text="parabens" ,height=1, anchor='center' , font=('Ivy 10 bold') ,  bg=co0 , fg=co4 )
        app_vencedor.place(x=5 , y=60)
    elif jogador_voce < jogador_pc:    
        app_vencedor = Label(frame_baixo , text="perdeu ze" ,height=1, anchor='center' , font=('Ivy 10 bold') ,  bg=co0 , fg=co5 )
        app_vencedor.place(x=5 , y=60)
    else:    
        app_vencedor = Label(frame_baixo , text="empate" ,height=1, anchor='center' , font=('Ivy 10 bold') ,  bg=co0 , fg=co1 )
        app_vencedor.place(x=5 , y=60)
      
    def jogar_denovo():
        app_1_pontos['text'] = '0'
        app_1_pontos['text'] = '0'
        app_vencedor.destroy()

        iniciar_jogo()

    b_jogar_denovo = Button(frame_baixo,command=jogar_denovo, width = 30 , text= "jogar de novo" , bg=fundo , fg=co0 , font=('Ivy 10 bold') , anchor=CENTER , relief=RAISED , overrelief=RIDGE)
    b_jogar_denovo.place(x=5 , y=151)



print('jogo terminou')

b_jogar = Button(frame_baixo,command=iniciar_jogo, width=30, text="jogar", bg=fundo , fg=co0 ,font=('Ivy 10 bold') , anchor=CENTER , relief=RAISED , overrelief=RIDGE)
b_jogar.place(x=5 , y=151)



janela.mainloop()