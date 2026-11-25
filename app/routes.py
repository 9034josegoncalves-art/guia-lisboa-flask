from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Restaurante, Local


# Rota da Página Inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota de Locais a Visitar
@app.route('/locais')
def locais():
    lista_locais = Local.query.all()
    return render_template('locais.html', locais=lista_locais)

# Rota de Gastronomia Típica
@app.route('/gastronomia')
def gastronomia():
    lista_restaurantes = Restaurante.query.all()
    return render_template('gastronomia.html', restaurantes=lista_restaurantes)


# ---------------- RESTAURANTES ----------------

# Rota para Gerir a Tabela de Restaurantes
@app.route('/restaurantes', methods=['GET', 'POST'])
def restaurantes():
    if request.method == 'POST':
        novo = Restaurante(
            nome=request.form['nome'],
            zona=request.form['zona'],
            especialidade=request.form['especialidade'],
            preco=request.form['preco']
        )
        db.session.add(novo)
        db.session.commit()
        return redirect(url_for('restaurantes'))

    lista_restaurantes = Restaurante.query.all()
    return render_template('restaurantes.html', restaurantes=lista_restaurantes)

# Rota para Apagar um Restaurante pelo ID
@app.route('/apagar_restaurante/<int:id>', methods=['POST'])
def apagar_restaurante(id):
    restaurante = Restaurante.query.get_or_404(id)
    db.session.delete(restaurante)
    db.session.commit()
    return redirect(url_for('restaurantes'))

# Rota para Editar um Restaurante pelo ID
@app.route('/editar_restaurante/<int:id>', methods=['GET', 'POST'])
def editar_restaurante(id):
    restaurante = Restaurante.query.get_or_404(id)
    if request.method == 'POST':
        restaurante.nome = request.form['nome']
        restaurante.zona = request.form['zona']
        restaurante.especialidade = request.form['especialidade']
        restaurante.preco = request.form['preco']
        db.session.commit()
        return redirect(url_for('restaurantes'))

    return render_template('editar_restaurante.html', restaurante=restaurante)


# ---------------- LOCAIS ----------------

# Rota para Gerir a Tabela de Locais
@app.route('/gerir_locais', methods=['GET', 'POST'])
def gerir_locais():
    if request.method == 'POST':
        novo = Local(
            nome=request.form['nome'],
            descricao=request.form['descricao'],
            link=request.form['link'],
            imagem=request.form['imagem']
        )
        db.session.add(novo)
        db.session.commit()
        return redirect(url_for('gerir_locais'))

    lista_locais = Local.query.all()
    return render_template('gerir_locais.html', locais=lista_locais)

# Rota para Apagar um Local pelo ID
@app.route('/apagar_local/<int:id>', methods=['POST'])
def apagar_local(id):
    local = Local.query.get_or_404(id)
    db.session.delete(local)
    db.session.commit()
    return redirect(url_for('gerir_locais'))

# Rota para Editar um Local pelo ID
@app.route('/editar_local/<int:id>', methods=['GET', 'POST'])
def editar_local(id):
    local = Local.query.get_or_404(id)
    if request.method == 'POST':
        local.nome = request.form['nome']
        local.descricao = request.form['descricao']
        local.link = request.form['link']
        local.imagem = request.form['imagem']
        db.session.commit()
        return redirect(url_for('gerir_locais'))

    return render_template('editar_local.html', local=local)
