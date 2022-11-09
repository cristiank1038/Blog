from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Post:

    def __init__(self, data):
        self.id = data['id']
        self.nombre_blog = data['nombre_blog']
        self.contenido = data['contenido']
        self.date_made = data['date_made']
        self.post_like = data['post_like']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

        self.first_name = data['first_name'] 
        self.last_name = data['last_name'] 

    @staticmethod
    def valida_post(formulario):
        es_valido = True

        if len(formulario['nombre_blog']) < 3:
            flash("El nombre_blog de la blog debe tener al menos 3 caracteres", "blog")
            es_valido = False

        if len(formulario['contenido']) < 3:
            flash("El contenido de la blog debe tener al menos 3 caracteres", "blog")
            es_valido = False
        
        if formulario['date_made'] == "":
            flash("Ingrese una fecha", "blog")
            es_valido = False
        
        return es_valido 

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO posts (nombre_blog, contenido, date_made, user_id) VALUES ( %(nombre_blog)s, %(contenido)s, %(date_made)s,  %(user_id)s )"
        nuevoId = connectToMySQL('proyecto_blog').query_db(query, formulario)
        return nuevoId
    
    @classmethod
    def get_all(cls):
        query = "SELECT posts.*, first_name, last_name FROM posts LEFT JOIN users ON users.id = posts.user_id" #LEFT JOIN users
        results = connectToMySQL('proyecto_blog').query_db(query) #Lista de diccionarios
        posts = []
        for post in results:
            posts.append(cls(post)) #cls(post) -> Instancia de post, Agregamos la instancia a mi lista de posts
        return posts

    @classmethod
    def get_by_id(cls, formulario): #recibir formulario_blog
        query = "SELECT posts.*, first_name, last_name FROM posts LEFT JOIN users ON users.id = posts.user_id WHERE posts.id = %(id)s" #LEFT JOIN users
        result = connectToMySQL('proyecto_blog').query_db(query, formulario) #recibimos una lista 
        post = cls(result[0]) #Creamos una instancia de post
        return post

    @classmethod
    def update_post(cls, formulario): #Recibir el formulario. OJO con todo y el ID de los posts
        query = "UPDATE proyecto_blog.posts  SET nombre_blog = %(nombre_blog)s, contenido = %(contenido)s, date_made = %(date_made)s WHERE posts.id = %(id)s"
        result = connectToMySQL('proyecto_blog').query_db(query, formulario)
        return result
    
    @classmethod
    def delete_post(cls, formulario): #Recibe formulario con id de blog a borrar
        query = "DELETE FROM posts WHERE id = %(id)s"
        result = connectToMySQL('proyecto_blog').query_db(query, formulario)
        return result



    @classmethod
    def get_likes(cls, formulario):
        query = "SELECT posts.*, first_name, last_name FROM posts LEFT JOIN users ON users.id = posts.user_id WHERE posts.id = %(id)s" #LEFT JOIN users
        results = connectToMySQL('proyecto_blog').query_db(query, formulario) #Lista de diccionarios
        post = cls(results[0]) #Creamos una instancia de post
        return post

    @classmethod
    def update_like(cls, formulario): #Recibir el formulario. OJO con todo y el ID de los posts
        query = "UPDATE posts SET post_like = %(post_like)s WHERE id = %(id)s"
        result = connectToMySQL('proyecto_blog').query_db(query, formulario)
        return result