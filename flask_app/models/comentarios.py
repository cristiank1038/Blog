from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Comentarios:

    def __init__(self, data):
        self.id = data['id']
        
        self.comentario = data['comentario']
        
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id'] 
        self.post_id = data['post_id'] 

        self.first_name = data['first_name'] 
        self.last_name = data['last_name'] 

    @staticmethod
    def valida_comentario(formulario):
        es_valido = True

        if len(formulario['comentario']) < 3:
            flash("El comentario del blog debe tener al menos 3 caracteres", "comentar")
            es_valido = False
                
        return es_valido 

    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO comentarios (comentario, user_id, post_id) VALUES ( %(comentario)s, %(user_id)s, %(post_id)s )" 
        nuevoId = connectToMySQL('proyecto_blog').query_db(query, formulario)
        return nuevoId
    
    @classmethod
    def get_all(cls, formulario_blog):
        query = "SELECT comentarios.*, users.first_name, users.last_name FROM comentarios LEFT JOIN users ON comentarios.user_id = users.id WHERE comentarios.post_id = %(id)s" #LEFT JOIN users
        print(formulario_blog)
        results = connectToMySQL('proyecto_blog').query_db(query, formulario_blog) #Lista de diccionarios
        comentarios = []
        for comenta in results:
            comentarios.append(cls(comenta)) #cls(post) -> Instancia de post, Agregamos la instancia a mi lista de comentarios
        return comentarios
    
    

    
