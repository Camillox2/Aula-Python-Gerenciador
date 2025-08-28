from flask import render_template, redirect, url_for, request
from config import app

from models import *
from formulario import FormularioEvento

"""
pip install flask, flask-wtf
flask_sqlalchemy, flask_login

"""


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    from formulario import FormularioCriarconta

    formulario = FormularioCriarconta()

    if formulario.validate_on_submit():
        nome = formulario.nome.data
        email = formulario.email.data
        senha = formulario.senha.data

        usu_ex = User.query.filter_by(username=email).first()

        if usu_ex:
            print('Usuario ja existe')
        else:
            novo_usuario = User(username=email, password=senha)
            db.session.add(novo_usuario)
            db.session.commit()
            print('Usuario Criado')
            return redirect(url_for('login'))

    return render_template('register.html', form=formulario)


@app.route('/login', methods=['GET', 'POST'])
def login():
    from formulario import FormularioCriarconta
    from flask_login import login_user
    
    formulario = FormularioCriarconta()
    
    if formulario.validate_on_submit():
        email = formulario.email.data
        senha = formulario.senha.data
        
        user = User.query.filter_by(username=email).first()
        
        if user and user.password == senha:
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            print('Login inválido')
    
    return render_template('login.html', form=formulario)


@app.route('/logout')
def logout():
    from flask_login import logout_user
    logout_user()
    return redirect(url_for('home'))


@app.route('/dashboard')
def dashboard():
    from flask_login import login_required, current_user
    
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    
    todos_eventos = Evento.query.all()
    meus_eventos = Evento.query.filter_by(id_usuario=current_user.id).all()
    
    return render_template('dashboard.html', todos_eventos=todos_eventos, meus_eventos=meus_eventos)


@app.route('/create_event', methods=['GET', 'POST'])
def create_event():
    from flask_login import current_user
    
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    
    formulario = FormularioEvento()

    if formulario.validate_on_submit():
        nome = formulario.nome.data
        desc = formulario.descricao.data
        dat = formulario.data.data

        novoEvento = Evento(nome=nome, descricao=desc, dataEvento=dat, id_usuario=current_user.id)
        db.session.add(novoEvento)
        db.session.commit()

        return redirect(url_for('dashboard'))

    return render_template('create_event.html', form=formulario)


@app.route('/edit_event/<int:event_id>', methods=['GET', 'POST'])
def edit_event(event_id):
    from flask_login import current_user
    
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    
    evento = Evento.query.get_or_404(event_id)
    formulario = FormularioEvento()
    
    if formulario.validate_on_submit():
        evento.nome = formulario.nome.data
        evento.descricao = formulario.descricao.data
        evento.dataEvento = formulario.data.data
        db.session.commit()
        return redirect(url_for('dashboard'))
    
    formulario.nome.data = evento.nome
    formulario.descricao.data = evento.descricao
    formulario.data.data = evento.dataEvento
    
    return render_template('edit_event.html', form=formulario, evento=evento)


@app.route('/delete_event/<int:event_id>', methods=['POST'])
def delete_event(event_id):
    from flask_login import current_user
    
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    
    evento = Evento.query.get_or_404(event_id)
    db.session.delete(evento)
    db.session.commit()
    return redirect(url_for('dashboard'))


if __name__ == '__main__':
    app.run(debug=True)
