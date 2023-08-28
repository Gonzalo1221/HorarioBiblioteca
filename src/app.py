from flask import Flask,  redirect, request, jsonify, json, session, render_template, Blueprint
from config.db import db, app, ma



#importar routes 
from api.user import routes_user
from api.roles import routes_roles
from api.reservacion import routes_reservacion
#rutas


#ubicacion del api 
app.register_blueprint(routes_roles, url_prefix="/api")
app.register_blueprint(routes_user, url_prefix="/api")
app.register_blueprint(routes_reservacion, url_prefix="/api")


#------------------------------------------------
@app.route("/")
def index():
    titulo= "Pagina Princiapl"
    return render_template('/main/login.html', titles=titulo)

# Datos de la tabla de Editoriales
if __name__ == '__main__':
   # load_dotenv()
    app.run(debug=True, port=5000, host='0.0.0.0')
    
