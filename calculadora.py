from functools import partial
from tkinter import *

#program by~ Welberthy Gustavo Developer

def calc(btn):
    if btn['text'].isdigit() or btn['text'] == '.':
        lbl['text'] += btn['text']
        

def soma():
    global sinal 
    sinal = 'soma'
    global valor1
    valor1 = lbl['text']
    lbl['text'] = ''


def sub():
    global sinal 
    sinal = 'sub'
    global valor1
    valor1 = lbl['text']
    lbl['text'] = ''


def mult():
    global sinal 
    sinal = 'mult'
    global valor1
    valor1 = lbl['text']
    lbl['text'] = ''


def div():
    global sinal 
    sinal = 'div'
    global valor1
    valor1 = lbl['text']
    lbl['text'] = ''


def raiz():
    global sinal 
    sinal = 'raiz'
    global valor1
    valor1 = lbl['text']
    lbl['text'] = '√'


def elev():
    global sinal 
    sinal = 'elev'
    global valor1
    valor1 = lbl['text']
    lbl['text'] = ''


def porc():
    global sinal 
    sinal = 'porc'
    global valor1
    valor1 = lbl['text']
    lbl['text'] = '%'


def ac():
    lbl['text'] = ''


def igual():
    if sinal == 'soma':
        valor2 = lbl['text']
        lbl['text'] = ''
        soma = float(valor1) + float(valor2)
        lbl['text'] = float(soma)
    elif sinal == 'sub':
        valor2 = lbl['text']
        lbl['text'] = ''
        subt = float(valor1) - float(valor2)
        lbl['text'] = float(subt)
    elif sinal == 'mult':
        valor2 = lbl['text']
        lbl['text'] = ''
        multi = float(valor1) * float(valor2)
        lbl['text'] = float(multi)
    elif sinal == 'div':
        valor2 = lbl['text']
        lbl['text'] = ''
        soma = float(valor1) / float(valor2)
        lbl['text'] = float(soma)
    elif sinal == 'raiz':
        lbl['text'] = ''
        rai = float(valor1) ** 0.5
        lbl['text'] = float(rai)
    elif sinal == 'elev':
        valor2 = lbl['text']
        lbl['text'] = ''
        eleva = float(valor1) ** float(valor2)
        lbl['text'] = float(eleva)
    elif sinal == 'porc':
        lbl['text'] = ''
        porcen = float(valor1) / 100
        lbl['text'] = float(porcen)
    else:
        lbl['text'] = 'Error!'


janela = Tk()
janela.title('Calculadora')
janela.iconbitmap('calculadoraProject/cal.ico')
janela['bg'] = 'gainsboro'
janela.geometry('400x450+400+100')
janela.resizable(0,0)

lbl = Label(janela,width=15, height=1, font='Arial 30', bd=1, relief='solid', justify=RIGHT, anchor=E, padx=15, pady=10)
lbl.place(x=100,y=100)
lbl.pack(side=TOP)

#Others buttons
btnab = Button(janela,width=8, height=2, font='Arial 11 bold', text='√', bg='gray80', command=raiz)
btnab.place(x=15,y=90)
btnfe = Button(janela,width=8, height=2, font='Arial 11 bold', text='x¹', bg='gray80', command=elev)
btnfe.place(x=110,y=90)
btnpor = Button(janela,width=8, height=2, font='Arial 11 bold', text='%', bg='gray80', command=porc)
btnpor.place(x=205,y=90)
btnac = Button(janela,width=8, height=2, font='Arial 11 bold', text='AC', bg='gray80', command=ac)
btnac.place(x=300,y=90)

#Numbers buttons
btn7 = Button(janela,width=8, height=2, font='Arial 12', text='7')
btn7['command'] = partial(calc, btn7)
btn7.place(x=15,y=160)
btn8 = Button(janela,width=8, height=2, font='Arial 12', text='8')
btn8['command'] = partial(calc, btn8)
btn8.place(x=110,y=160)
btn9 = Button(janela,width=8, height=2, font='Arial 12', text='9')
btn9['command'] = partial(calc, btn9)
btn9.place(x=205,y=160)

btn4 = Button(janela,width=8, height=2, font='Arial 12', text='4')
btn4['command'] = partial(calc, btn4)
btn4.place(x=15,y=230)
btn5 = Button(janela,width=8, height=2, font='Arial 12', text='5')
btn5['command'] = partial(calc, btn5)
btn5.place(x=110,y=230)
btn6 = Button(janela,width=8, height=2, font='Arial 12', text='6')
btn6['command'] = partial(calc, btn6)
btn6.place(x=205,y=230)

btn3 = Button(janela,width=8, height=2, font='Arial 12', text='3')
btn3['command'] = partial(calc, btn3)
btn3.place(x=15,y=300)
btn2 = Button(janela,width=8, height=2, font='Arial 12', text='2')
btn2['command'] = partial(calc, btn2)
btn2.place(x=110,y=300)
btn1 = Button(janela,width=8, height=2, font='Arial 12', text='1')
btn1['command'] = partial(calc, btn1)
btn1.place(x=205,y=300)

btn0 = Button(janela,width=8, height=2, font='Arial 12', text='0')
btn0['command'] = partial(calc, btn0)
btn0.place(x=15,y=370)
#Score button
btnp = Button(janela,width=8, height=2, font='Arial 11 bold', text='.')
btnp['command'] = partial(calc, btnp)
btnp.place(x=110,y=370)
#Equals button
btnig = Button(janela,width=8, height=2, font='Arial 11 bold', text='=', bg='blue2', fg='white', command=igual)
btnig.place(x=205,y=370)

#Operators button
btndiv = Button(janela,width=8, height=2, font='Arial 11 bold', text='÷', bg='gray80', command=div)
btndiv.place(x=300,y=160)
btnmul = Button(janela,width=8, height=2, font='Arial 11 bold', text='x',bg='gray80', command=mult)
btnmul.place(x=300,y=230)
btnsub = Button(janela,width=8, height=2, font='Arial 11 bold', text='-',bg='gray80', command=sub)
btnsub.place(x=300,y=300)
btnad = Button(janela,width=8, height=2, font='Arial 11 bold', text='+', bg='gray80', command=soma)
btnad.place(x=300,y=370)


janela.mainloop()