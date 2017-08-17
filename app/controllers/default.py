from app import app
from app.models.tables import User
from bottle import request, template, static_file, redirect

# static routes
@app.get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='app/static/css')

@app.get('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='app/static/js')

@app.get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='app/static/img')

@app.get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='app/static/fonts')

@app.route('/') # @get('/login')
def login():
    return template('login', sucesso=True)

@app.route('/cadastro')
def cadastro():
    return template('cadastro')

@app.route('/cadastro', method='POST')
def acao_cadastro(db):
    username = request.forms.get('username')
    password = request.forms.get('password')
    new_user = User(username, password)
    db.add(new_user)
    #return template('lista_usuarios')
    return redirect('/usuarios')

@app.route('/', method='POST') # @post('/')
def acao_login(db):
    username = request.forms.get('username')
    password = request.forms.get('password')
    result = db.query(User).filter((User.username==username) \
        & (User.password==password)).all()
    if result:
        return redirect('/usuarios')
        #return template('lista_usuarios')
    return template('login', sucesso=False)
    #return template('verificacao_login', sucesso=True, nome=username)
    #return template('views/verificacao_login', sucesso=check_login(username, password), nome=username)

@app.route('/usuarios')
def usuarios(db):
    usuarios = db.query(User).all()
    return template('lista_usuarios', usuarios=usuarios)

@app.error(404)
def error404(error):
    return template('pagina404')