from flask import Flask, request, jsonify, url_for, render_template, jsonify, redirect, url_for
from flask_cors import CORS # instala flask-cors con pip install flask-cors
#from flask_mail import Mail, Message
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import pyodbc
import os
from datetime import timedelta
from werkzeug.utils import secure_filename


import json

app = Flask(__name__)
### coneccion a la base de datos
app.config['JWT_SECRET_KEY'] = 'ClaveUltraSecreta'
jwt = JWTManager(app)

def conectar():
    try:
        server = 'IDEPAD3\SQLEXPRESS'
        bd = 'PROYECTO_ROL'
        conexion = pyodbc.connect(
            'DRIVER={ODBC Driver 18 for SQL Server};SERVER=' + server + ';DATABASE=' + bd + ';Encrypt=no;Trusted_Connection=yes;'
        )
        print("Conexión exitosa")
        return conexion
    except Exception as e:
        print("Ocurrió un error al conectar a SQL Server: ", e)
        return None

def verificacion_usuario(usuario, contraseña):
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM USUARIO WHERE USR_USUARIO = ? AND USR_PASS_USUARIO = ?', (usuario, contraseña))
        usuario = cursor.fetchone()
        conn.close()
        if usuario:
            print(f"Usuario encontrado: {usuario}")
        else:
            print("Usuario no encontrado o contraseña incorrecta")
        return usuario
    print("Error en la conexión a la base de datos")
    return None

def registrar_usuario(usuario, correo, contraseña):
    conn = conectar()
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO USUARIO (USR_USUARIO, USR_CORREO, USR_PASS_USUARIO) VALUES (?, ?, ?)',
            (usuario, correo, contraseña)
        )
        conn.commit()
        conn.close()
        print("Usuario registrado exitosamente")
        return True
    print("Error en la conexión a la base de datos")
    return False

def generar_token(email):
    expires = timedelta(hours=1)
    return create_access_token(identity=email, expires_delta=expires)

def enviar_correo_recuperacion(correo, token):
    url = url_for('reset_password', token=token, _external=True)
    html = f'<p>Para restablecer tu contraseña, haz clic en el siguiente enlace:</p><p><a href="{url}">{url}</a></p>'
    msg = Message('Recuperación de contraseña', recipients=[correo], html=html)
    mail.send(msg)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        usuario = data.get('usuario')
        contraseña = data.get('contraseña')
        recuerdame = data.get('recuerdame')

        print(f"Intentando iniciar sesión con usuario: {usuario}")

        usuario_verificado = verificacion_usuario(usuario, contraseña)
        if usuario_verificado:
            additional_claims = {'usuario': usuario}

            if recuerdame:
                expires = timedelta(days=30)
            else:
                expires = timedelta(hours=1)

            access_token = create_access_token(identity=usuario, additional_claims=additional_claims, expires_delta=expires)
            response = jsonify({'login': True, 'token': access_token})
            return response, 200
        else:
            print("Inicio de sesión fallido")
            return jsonify({'login': False}), 401
    else:
        return render_template('login.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    usuario = data.get('usuario')
    correo = data.get('correo')
    contraseña = data.get('contraseña')

    if registrar_usuario(usuario, correo, contraseña):
        return jsonify({'register': True}), 200
    else:
        return jsonify({'register': False}), 500
### fin ###

## carga imagenes

# Configuración para la carga de archivos
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/creadorPersonaje', methods=['GET', 'POST'])
def creadorPersonaje():
    if request.method == 'POST':
        # Obtener otros datos del formulario
        nombre_real = request.form['nombreReal']
        nombre_personaje = request.form['nombrePersonaje']
        
        # Manejar la carga del archivo
        if 'avatar' not in request.files:
            return redirect(request.url)
        file = request.files['avatar']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # Aquí puedes guardar el nombre del archivo en la base de datos asociado al personaje

        # Procesar otros datos del formulario y guardar en la base de datos

        return redirect(url_for('success'))

    return render_template('creadorPersonaje.html')
@app.route('/success')
def success():
    return 'Personaje creado con éxito!'

@app.route('/plataformaJuego')
def plataformaJuego():
    return render_template('plataformaJuego.html')



@app.route('/registro')
def registro():

    return render_template('registro.html')

@app.route('/creadorObjetos')
def creadorObjetos():
    return render_template('creadorObjetos.html')
@app.route('/historial')
def historial():

    return render_template('historial.html')
@app.route('/dados')
def dados():

    return render_template('dados.html')


# json esta en static/data/data.json
@app.route('/data')
def get_data():
    file_path = os.path.join(app.root_path, 'static', 'data', 'data.json')
    with open(file_path, encoding='utf-8') as file:
        data = json.load(file)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)  # debug=True para que se reinicie el servidor automáticamente al guardar cambios en el códigofrom flask import Flask, render_template, jsonify, request


