from bottle import Bottle

app = Bottle()

from app.controllers import default

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