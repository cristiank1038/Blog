from turtle import update
from flask import render_template, redirect, session, request, flash #importaciones de módulos de flask
from flask_app import app
from flask_app.models.comentarios import Comentarios

#Importar el modelo de User
from flask_app.models.users import User     #

#Importar el modelo de Post
from flask_app.models.post import Post  #

@app.route('/new/blog')
def new_blog():
    if 'usuario_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')

    formulario = {
        "id": session['usuario_id']
    }

    user = User.get_by_id(formulario)
    
    return render_template('new_blog.html', user=user)

@app.route('/create/blog', methods=['POST'])
def create_blog():
    if 'usuario_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    
    #Tengo que validar mi blog
    if not Post.valida_post(request.form): #Post.valida_post(ENVIA FORMULARIO). SI NO ES VALIDO
        return redirect('/new/blog')

    Post.save(request.form)
    return redirect('/dashboard')

@app.route('/show/blog/<int:id>') #A través de la URL recibimos el ID de el blog
def show_blog(id):
    if 'usuario_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')

    formulario = {
        "id": session['usuario_id']
    }

    user = User.get_by_id(formulario) #Usuario que inició sesión


    formulario_blog = { "id": id }
    #llamar a una función y debo de recibir el blog
    posts = Post.get_by_id(formulario_blog)

    comentarios = Comentarios.get_all(formulario_blog)

    return render_template('ver_blog.html', user=user, posts=posts, comentarios=comentarios)

@app.route('/edit/blog/<int:id>') #Recibo el identificador de el blog que quiero editar
def edit_blog(id):
    if 'usuario_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    
    formulario = {
        "id": session['usuario_id']
    }

    user = User.get_by_id(formulario) #Usuario que inició sesión

    formulario_blog = { "id": id }
    #llamar a una función y debo de recibir el blog
    post = Post.get_by_id(formulario_blog)

    return render_template('edit_blog.html', user=user, post=post)

@app.route('/update/blog', methods=['POST'])
def update_blog():
    if 'usuario_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    
    if not Post.valida_post(request.form):
        return redirect('/edit/blog/'+request.form['id']) #/edit/blog/1

    print( request.form )
    Post.update_post(request.form) 

    return redirect('/dashboard')

@app.route('/delete/blog/<int:id>')
def delete_blog(id):
    if 'usuario_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    
    formulario = {"id": id}
    Post.delete_post(formulario)

    return redirect('/dashboard')


# Ruta para likes, al boton se le agreda esa ruta,  se llama al metodo en post.py
@app.route('/post_like/<int:id>')
def post_like(id):
    if 'usuario_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    
    formulario = {"id": id}
    likes = Post.get_likes(formulario).post_like
    likes=likes+1
    print(likes)
    formulario_like = { 'id' : id, 'post_like': likes}
    Post.update_like(formulario_like )

    return redirect('/dashboard')