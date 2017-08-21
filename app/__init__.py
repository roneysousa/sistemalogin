import bottle_session
from bottle import Bottle, TEMPLATE_PATH
from bottle.ext import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///database.db', echo=True)

app = Bottle()
TEMPLATE_PATH.insert(0, 'app/views/')
plugin = sqlalchemy.Plugin(
    engine,
    Base.metadata,
    keyword='db',
    create=True,
    commit=True,
    use_kwargs=False
)


plugin_session = bottle_session.SessionPlugin(cookie_lifetime=120)


app.install(plugin)
app.install(plugin_session)

from app.controllers import default
from app.models import tables

'''@route('/')
@route('/user/<nome>')
def index(nome='Desconhecido'):
    return '<center><h1>Olá '+nome+ '!!!</h1></center>'

@route('/artigo/<id>')
def artigo(id):
    return '<h1>Você está lendo o artigo '+ id +'</h1>'

@route('/pagina/<id>/<nome>')
def pagina(id, nome):
    return '<h1>Você está vendo a página '+ id + ' com o nome '+nome+'</h1>'


@route('/python')
def python():
    return '<h1>Curso de Python</h1>'''