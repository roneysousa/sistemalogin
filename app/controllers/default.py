from app import app
from bottle import request, template
from bottle import static_file
from app.models.default import insert_user

# static routes
@app.get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')

@app.get('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static/js')

@app.get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='static/img')

@app.get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='static/fonts')

@app.route('/') # @get('/login')
def login():
    return template('login.html')

@app.route('/cadastro')
def cadastro():
    return template('cadastro.html')

@app.route('/cadastro', method='POST')
def acao_cadastro():
    username = request.forms.get('username')
    password = request.forms.get('password')
    insert_user(username, password)
    return template('verificacao_cadastro.html', nome=username)

'''def check_login(username, password):
    d = {'roney':'delphi', 'joao':'123', 'bono': 'python'}
    if username in d.keys() and d[username] == password:
        return True
    return False'''

'''@route('/')
def index():
    return template('view/index.html')'''

@app.route('/', method='POST') # @post('/')
def acao_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    return template('verificacao_login.html', sucesso=True)
    #return template('views/verificacao_login', sucesso=check_login(username, password), nome=username)

@app.error(404)
def error404(error):
    return template('pagina404.html')