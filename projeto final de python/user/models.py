from datetime import datetime
from peewee import *
from database import db  # Importação corrigida

class Base(Model):
    criado_em = DateTimeField(default=datetime.now)

    class Meta:
        database = db

class Setores(Base):
    periodo = CharField(null=False)
    cod = CharField(null=True)
    nome= CharField(null=True)

class Obras(Base):
    nome = CharField(null=False)
    ano = DateField(null=True)
    artista = CharField(null=False)
    setore= CharField(null=False)
    
class Fucionarios(Base):
    nome = CharField(null=False)
    grau_ensino = CharField(null=False)
    setor_trabalho = CharField(null=False)
    cpf = CharField(null=False)
    cel = CharField(null=False)
    email = CharField(null=False)
    funcao = CharField(null=False)    


class Museu(Base):
    uf = CharField(max_length=2,null=False)
    horario = CharField(null=False)
    nome = CharField(null=False)    

class Passeio(Base):
    quan_pes = CharField(null=False)
    responsavel = CharField(null=False)

class Usuario(Base):
    nome = CharField(null=False)
    cpf = CharField(null=False)
    cel = CharField(null=False)
    email = CharField(null=False)

class marcar_visita(Base):
    horario = CharField(null=False)
    valor = CharField(null=False)
    numero_bilhete=CharField(null=False)
    nome_user= CharField(null=False)



