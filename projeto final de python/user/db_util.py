from peewee import SqliteDatabase

db=SqliteDatabase("museu.db")

from models import Usuario, Setores, Obras, Fucionarios, Museu, Passeio, marcar_visita

tabelas = [Usuario, Setores, Obras, Fucionarios, Museu, Passeio,marcar_visita]

def cria_db():
    db.create_tables(tabelas)

def exclui_tabelas():
    db.drop_tables(tabelas)

def cadastrar():
    db.connect()
    cria_db()
    
    museu= Museu(uf= 'SC', horario='10:00 ate 20:00', nome='museu')

    usuario1 = Usuario.create(nome='Jason', cpf='FADBG', telefone=40228922, email='Jason@tata@gmail.com')

    Obra1 = Obras.create(nome='Ladrilha', ano='3/05/2011', artista='xuxa', setor='pre-historco')

    setore1 = Setores.create(cod=1, Periodo=2001, nome='antigo')

    funcionario1 = Fucionarios.create(nome='james', setor_trabalho='setore1', grau_d_ensino='Sabo muito', cpf='FADBG', telefone=40228922, email='Jason@tata@gmail.com', funcao='chefe')

    db.close()
 
def cadastrar_funcionario(nome_par,grau_ensino_par,setor_trabalho_par,cpf_par, cel_par, email_par, funcao_par):
    funcionario = Fucionarios.create(nome=nome_par, grau_ensino=grau_ensino_par, setor_trabalho=setor_trabalho_par,cpf=cpf_par, cel=cel_par,  email=email_par, funcao=funcao_par)
    
def cadastrar_obra(ano_par, artista_par,nome_par, setor_par):
    obra = Obras.create(ano=ano_par, artista=artista_par, nome=nome_par, setore=setor_par)
    
def cadastrar_setores(Periodo_par, cod_par,nome_par):
    setor = Setores.create(cod=cod_par,periodo=Periodo_par, nome=nome_par)
  
    
def cadastrar_usuario(nome_par, cpf_par, cel_par, email_par):
    usuario = Usuario.create(nome=nome_par, cpf=cpf_par, cel=cel_par,  email=email_par)
##====
def cadastrar_passeio(quan_pes_par, responsavel_par):
    passeio = Passeio.create(quan_pes=quan_pes_par , responsavel=responsavel_par)

def cadastrar_visitas(horario_par, numero_bilhete_par, valor_par, nome_user_par):
    bilhete = marcar_visita.create(horario=horario_par, numero_bilhete=numero_bilhete_par, valor=valor_par, nome_user =nome_user_par)


def cadastrar_museu(uf_par, horario_par,nome_par):
    museu = Museu.create(uf=uf_par, horario=horario_par,nome=nome_par)

def getUsuarios():
    lista = []
    requi = Usuario.select()
    for i in requi:
        lista.append(i.nome)
    return lista
def getSETOR():
    lista1 = []
    requisi = Setores.select()
    for i in requisi:
        lista1.append(i.nome)
    return lista1

def getSETOR1():
    lista2 = []
    requisi = Setores.select()
    for i in requisi:
        lista2.append(i.nome)
    return lista2