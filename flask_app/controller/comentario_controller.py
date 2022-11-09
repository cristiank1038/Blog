from flask import render_template, redirect, session, request, flash #importaciones de módulos de flask
from flask_app import app

#Importar el modelo de User
from flask_app.models.users import User     #

#Importar el modelo de Post
from flask_app.models.post import Post  #
from flask_app.models.comentarios import Comentarios

@app.route('/coment/blog/<int:id>') #Recibo el identificador de el blog que quiero editar
def coment_blog(id):
    if 'usuario_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    
    formulario = {
        "id": session['usuario_id']
    }

    user = User.get_by_id(formulario) #Usuario que inició sesión

    comentario_blog = { "id": id }
    #llamar a una función y debo de recibir el blog
    post = Post.get_by_id(comentario_blog)

    return render_template('comentarios.html', user=user, post=post)
    


@app.route('/comentarios/blog', methods=['POST'])
def comenta_blog():
    if 'usuario_id' not in session: #Solo puede ver la página si ya inició sesión 
        return redirect('/')
    
    #Tengo que validar mi comentario
    if not Comentarios.valida_comentario(request.form): #Comentarios.valida_comentario(ENVIA FORMULARIO). SI NO ES VALIDO
        return redirect('/show/blog/'+ request.form['post_id'])

    Comentarios.save(request.form)
    return redirect('/dashboard')