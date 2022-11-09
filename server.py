from flask_app import app


#Importando Controlador
from flask_app.controller import user_controller, blog_controler, comentario_controller

if __name__=="__main__":
    app.run(debug=True)

