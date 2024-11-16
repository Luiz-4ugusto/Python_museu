from tkinter import *
from tkinter.ttk import *


import tkinter as tk
from tkinter import ttk
from db_util import cadastrar_funcionario
from db_util import cadastrar_obra
from db_util import cadastrar_setores

from db_util import cadastrar_usuario
from db_util import cadastrar_passeio
from db_util import cadastrar_visitas
from db_util import cadastrar_museu
from db_util import getUsuarios
from db_util import getSETOR
from db_util import getSETOR1






# --funcionario----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
funcionarios = []


def submit_funcionario():
    nome = funcionarios[0].get()
    setor_trabalho = funcionarios[1].get()
    grau_ensino = funcionarios[2].get()
    cpf = funcionarios[3].get()
    cel = funcionarios[4].get()
    email = funcionarios[5].get()
    funcao= funcionarios[6].get()
    

    cadastrar_funcionario(nome_par=nome, setor_trabalho_par=setor_trabalho, grau_ensino_par=grau_ensino, cpf_par=cpf, cel_par=cel, email_par=email,funcao_par=funcao)
listfuncao=["Chefe", "Funcionario"]
def funcionario():
    funcionario = Toplevel()
    funcionario.geometry("400x400")
    funcionario.title("FUNCIONARIO")

    lblnome = Label(funcionario, text="Nome:")
    lblsetor_trabalho = Label(funcionario, text="Setor de trabalho:")
    lblgrau_ensino = Label(funcionario, text="Grau de ensino:")
    lblcpf = Label(funcionario, text="CPF:")
    lblcel = Label(funcionario, text="Telefone:")
    lblemail = Label(funcionario, text="Email:")
    lblfuncao = Label(funcionario, text="Funcao:")

    lblnome.grid(row=0, column=0, padx=5, pady=5)
    lblsetor_trabalho.grid(row=1, column=0, padx=5, pady=5)
    lblgrau_ensino.grid(row=2, column=0, padx=5, pady=5)
    lblcpf.grid(row=3, column=0, padx=5, pady=5)
    lblcel.grid(row=4, column=0, padx=5, pady=5)
    lblemail.grid(row=5, column=0, padx=5, pady=5)
    lblfuncao.grid(row=6, column=0, padx=5, pady=5)

    txtnome = Entry(funcionario)
    txtgrau_ensino = Entry(funcionario)
    txtsetor_trabalho = Entry(funcionario)
    txtcpf = Entry(funcionario)
    txtcel = Entry(funcionario)
    txtemail = Entry(funcionario)
    txtfuncao = Entry(funcionario)

    txtnome.grid(row=0, column=1, padx=5, pady=5)
    txtsetor_trabalho.grid(row=1, column=1, padx=5, pady=5)
    txtgrau_ensino.grid(row=2, column=1, padx=5, pady=5)
    txtcpf.grid(row=3, column=1, padx=5, pady=5)
    txtcel.grid(row=4, column=1, padx=5, pady=5)
    txtemail.grid(row=5, column=1, padx=5, pady=5)
    txtfuncao.grid(row=6, column=1, padx=5, pady=5)

    n = tk.StringVar()
    monthchoosen2 = Combobox(funcionario, width=17, textvariable=n, values=getSETOR1(), state="readonly")
    monthchoosen2.grid(column=1, row=1)


    o= tk.StringVar()
    lb_funcao=Combobox(funcionario,width=17, textvariable=o, values=listfuncao, state="readonly")
    lb_funcao.grid(row=6, column=1)

    funcionarios.append(txtnome)
    funcionarios.append(monthchoosen2)
    funcionarios.append(txtgrau_ensino)
    funcionarios.append(txtcpf)
    funcionarios.append(txtcel)
    funcionarios.append(txtemail)
    funcionarios.append(lb_funcao)

    btnSubmit = Button(funcionario, text="submit", command=submit_funcionario)
    btnSubmit.grid(column=1, row=10, padx=5, pady=5)

    funcionario.focus_set()
    funcionario.grab_set()
    funcionario.mainloop()
# --obras----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

obras = []


def submit_obra():
    nome = obras[0].get()
    ano = obras[1].get()
    artista = obras[2].get().upper()
    setore= obras[3].get()
    cadastrar_obra(ano_par=ano, artista_par=artista,nome_par=nome, setor_par=setore)


def obra():
    obra = Toplevel()
    obra.geometry("700x400")
    obra.title("OBRA")

    lblnome = Label(obra, text="Nome:")
    lblano = Label(obra, text="Ano:")
    lblartista = Label(obra, text="Artista:")
    lblsetor = Label(obra, text="Setor:")

    lblnome.grid(row=0, column=0, padx=5, pady=5)
    lblano.grid(row=1, column=0, padx=5, pady=5)
    lblartista.grid(row=2, column=0, padx=5, pady=5)
    lblsetor.grid(row=3, column=0, padx=5, pady=5)

    txtnome = Entry(obra)
    txtano = Entry(obra)
    txtartista = Entry(obra)

    txtnome.grid(row=0, column=1, padx=5, pady=5)
    txtano.grid(row=1, column=1, padx=5, pady=5)
    txtartista.grid(row=2, column=1, padx=5, pady=5)

    n = tk.StringVar()
    combo2 = Combobox(obra, width=17, textvariable=n, values=getSETOR(), state="readonly")
    combo2.grid(column=1, row=3)


    obras.append(txtnome)
    obras.append(txtano)
    obras.append(txtartista)
    obras.append(combo2)  


    btnSubmit = Button(obra, text="submit", command=submit_obra)
    btnSubmit.grid(column=1, row=10, padx=5, pady=5)

    obra.focus_set()
    obra.grab_set()
    obra.mainloop()

# --setores----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
setores = []


def submit_setor():
    cod = setores[0].get()
    Periodo = setores[1].get()
    nome=setores[2].get()
    cadastrar_setores( cod_par=cod, Periodo_par=Periodo,nome_par=nome)
    n=nome
    setores.append(n)

def setor():
    setor = Toplevel()
    setor.geometry("700x400")
    setor.title("SETOR")

    lblcod = Label(setor, text="Cod:")
    lblPeriodo = Label(setor, text="Periodo:")
    lblnome = Label(setor, text="Nome:")

    lblcod.grid(row=0, column=0, padx=5, pady=5)
    lblPeriodo.grid(row=1, column=0, padx=5, pady=5)
    lblnome.grid(row=2, column=0, padx=5, pady=5)

    txtcod = Entry(setor)
    txtPeriodo = Entry(setor)
    txtnome = Entry(setor)

    txtcod.grid(row=0, column=1, padx=5, pady=5)
    txtPeriodo.grid(row=1, column=1, padx=5, pady=5)
    txtnome.grid(row=2, column=1, padx=5, pady=5)

    setores.append(txtcod)
    setores.append(txtPeriodo)
    setores.append(txtnome)


    btnSubmit = Button(setor, text="submit", command=submit_setor)
    btnSubmit.grid(column=1, row=10, padx=5, pady=5)

    setor.focus_set()
    setor.grab_set()
    setor.mainloop()

# --Usuario----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

usuarios = []

def submit_usuario():
    nome = usuarios[0].get().upper()
    cpf = usuarios[1].get()
    cel = usuarios[2].get()
    email = usuarios[3].get()


    cadastrar_usuario(nome_par=nome, cpf_par=cpf, cel_par=cel, email_par=email)

    foda = nome

    usuarios.append(foda)

def usuario():
    usuario = Toplevel()
    usuario.geometry("700x400")
    usuario.title("usuario")

    lblnome = Label(usuario, text="Nome:")
    lblcpf = Label(usuario, text="Cpf:")
    lblcel = Label(usuario, text="Telefone:")
    lblemail = Label(usuario, text="Email:")

    lblnome.grid(row=0, column=0, padx=5, pady=5)
    lblcpf.grid(row=1, column=0, padx=5, pady=5)
    lblcel.grid(row=2, column=0, padx=5, pady=5)
    lblemail.grid(row=3, column=0, padx=5, pady=5)

    txtnome = Entry(usuario)
    txtcpf = Entry(usuario)
    txtcel = Entry(usuario)
    txtemail = Entry(usuario)

    txtnome.grid(row=0, column=1, padx=5, pady=5)
    txtcpf.grid(row=1, column=1, padx=5, pady=5)
    txtcel.grid(row=2, column=1, padx=5, pady=5)
    txtemail.grid(row=3, column=1, padx=5, pady=5)

    usuarios.append(txtnome)
    usuarios.append(txtcpf)
    usuarios.append(txtcel)
    usuarios.append(txtemail)

    btnSubmit = Button(usuario, text="submit", command=submit_usuario)
    btnSubmit.grid(column=1, row=10, padx=5, pady=5)

    usuario.focus_set()
    usuario.grab_set()
    usuario.mainloop()

# --exrcusão----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
excursoes = []

def submit_exrcusão():
    try:
        responsavel = excursoes[0].get()  
        quan_pes = excursoes[1].get()    
        cadastrar_passeio(quan_pes_par=quan_pes, responsavel_par=responsavel)
        print("Passeio cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro ao cadastrar passeio: {e}")
def passeio():
    passeio = Toplevel()
    passeio.geometry("700x400")
    passeio.title("passeio")

    lblquan_pes = Label(passeio, text="Quantidade Pessoas:")
    lblresponsavel = Label(passeio, text="Responsavel:")

    lblquan_pes.grid(row=1, column=0, padx=5, pady=5)
    lblresponsavel.grid(row=0, column=0, padx=5, pady=5)

    txtquan_pes = Entry(passeio)
    txtquan_pes.grid(row=1, column=1, padx=5, pady=5)

    n = tk.StringVar()
    monthchoosen = Combobox(passeio, width=17, textvariable=n, values=getUsuarios(), state="readonly")
    monthchoosen.grid(column=1, row=0)

    
    excursoes.clear()  
    excursoes.append(monthchoosen)  
    excursoes.append(txtquan_pes)  

    btnSubmit = Button(passeio, text="submit", command=submit_exrcusão)
    btnSubmit.grid(column=1, row=10, padx=5, pady=5)

    passeio.focus_set()
    passeio.grab_set()
    passeio.mainloop()

# --bilhete----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    

marcar_visita = []


def submit_bilhete():
    horario = marcar_visita[0].get()
    numero_bilhete = marcar_visita[1].get()
    valor = marcar_visita[2].get()
    nome_user=marcar_visita[3].get()
    cadastrar_visitas(horario_par=horario, numero_bilhete_par=numero_bilhete, valor_par=valor, nome_user_par=nome_user)


listhorario2=["2 HORAS", "3 HORAS", "4 HORAS", "5 HORAS"]
listvalor = ["35R$", "45R$", "55R$", "60R$", "70R$"] 
def bilhete():
    bilhete = Toplevel()
    bilhete.geometry("700x400")
    bilhete.title("Bilhete")

    lblhorario = Label(bilhete, text="Horario:")
    lblvalor = Label(bilhete, text="Valor:")
    lblnumero_bilhete = Label(bilhete, text="Numero bilhete:")
    lblnome_user = Label(bilhete, text="Dono:")

    lblhorario.grid(row=0, column=0, padx=5, pady=5)
    lblnumero_bilhete.grid(row=1, column=0, padx=5, pady=5)
    lblvalor.grid(row=2, column=0, padx=5, pady=5)
    lblnome_user.grid(row=4, column=0, padx=5, pady=5)


    txtnumero_bilhete = Entry(bilhete)


    txtnumero_bilhete.grid(row=1, column=1, padx=5, pady=5)


    
    d= tk.StringVar()
    lb_hora1=Combobox(bilhete,width=17, textvariable=d, values=listhorario2, state="readonly")
    lb_hora1.grid(row=0, column=1)
    
    n = tk.StringVar()
    combo = Combobox(bilhete, width=17, textvariable=n, values=getUsuarios(), state="readonly")
    combo.grid(column=1, row=4)



    a= tk.StringVar()
    lb_valor=Combobox(bilhete,width=17, textvariable=a, values=listvalor, state="readonly")
    lb_valor.grid(row=2, column=1)


    marcar_visita.append(lb_hora1)
    marcar_visita.append(lb_valor)
    marcar_visita.append(txtnumero_bilhete)    
    marcar_visita.append(combo)
    btnSubmit = Button(bilhete, text="submit", command=submit_bilhete)
    btnSubmit.grid(column=1, row=10, padx=5, pady=5)

    bilhete.focus_set()
    bilhete.grab_set()
    bilhete.mainloop()


# --museu----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

museus=[]
def submit_museu():

    uf = museus[0].get().upper()
    horario = museus[1].get()
    nome=museus[2].get().upper()
    cadastrar_museu(uf_par=uf, horario_par=horario, nome_par=nome)
listhorario=["10:00 até 18:00", "08:30 até 18:00", "8:00 até 17:00", "07:30 até 19:00","14:00 até 20:00", "09:30 até 19:00"]
    
def museu():
    museu = Toplevel()
    museu.geometry("400x400")
    museu.title("museu")

    lbluf = Label(museu, text="UF:")
    lblhorario = Label(museu, text="Horario:")
    lblnome = Label(museu, text="Nome:")

    lbluf.grid(row=0, column=0, padx=5, pady=5)
    lblhorario.grid(row=1, column=0, padx=5, pady=5)
    lblnome.grid(row=2, column=0, padx=5, pady=5)

    txtuf = Entry(museu)
    txthorario = Entry(museu)
    txtnome = Entry(museu)
    


    txtuf.grid(row=0, column=1, padx=5, pady=5)
    txthorario.grid(row=1, column=1, padx=5, pady=5)
    txtnome.grid(row=2, column=1, padx=5, pady=5)
    p= tk.StringVar()
    lb_hora=Combobox(museu,width=17, textvariable=p, values=listhorario, state="readonly")
    lb_hora.grid(row=1, column=1)
    museus.append(txtuf)
    museus.append(lb_hora)
    museus.append(txtnome)

    btnSubmit = Button(museu, text="submit", command=submit_museu)
    btnSubmit.grid(column=1, row=10, padx=5, pady=5)

    museu.focus_set()
    museu.grab_set()
    museu.mainloop()

#--Main----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

import os
diretorio_atual = os.path.dirname(__file__)
caminho_tema = os.path.join(diretorio_atual, "Forest-ttk-theme-master", "forest-dark.tcl")
def main():
    janela_principal = Tk()
    janela_principal.geometry("400x600")
    janela_principal.title("janela")
    janela_principal.tk.call("source", caminho_tema)

    style = ttk.Style(janela_principal)

    style.theme_use("forest-dark")
    fonte_personalizada = ("Times New Roman", 12)

    btn = Button(janela_principal, text="Museu",style='Accent.TButton', command=museu) 
    btn1 = Button(janela_principal, text="Obra",style='Accent.TButton', command=obra)
    btn2 = Button(janela_principal, text="Setor",style='Accent.TButton', command=setor)

    btn4 = Button(janela_principal, text="Funcionario",style='Accent.TButton', command=funcionario)
    btn5 = Button(janela_principal, text="Usuario",style='Accent.TButton', command=usuario)
    btn6 = Button(janela_principal, text="Bilhete",style='Accent.TButton', command=bilhete)
    btn7 = Button(janela_principal, text="Passeio",style='Accent.TButton', command=passeio)
    lbl_museu = Label(janela_principal, text="MUSEU",font=fonte_personalizada)

    lbl_museu.grid(row=2, column=0, padx=10, pady=5)
    btn.grid(row=3, column=0, padx=10, pady=10)

    lbl_funcionario = Label(janela_principal, text="FUNCIONARIO",font=fonte_personalizada)
    lbl_funcionario.grid(row=2, column=1, padx=10, pady=5)

    btn1.grid(row=4, column=1, padx=10, pady=10)
    btn2.grid(row=3, column=1, padx=10, pady=10)
    btn4.grid(row=5, column=1, padx=10, pady=10)

    lbl_usuario = Label(janela_principal, text="USUARIO",font=fonte_personalizada)
    lbl_usuario.grid(row=2, column=2, padx=10, pady=5)

    btn5.grid(row=3, column=2, padx=10, pady=10)
    btn6.grid(row=4, column=2, padx=10, pady=10)
    btn7.grid(row=5, column=2, padx=10, pady=10)
    
    
    janela_principal.mainloop()

if __name__ == '__main__':
    main()



