Manual de instalación proyecto INFINITY ROL

Instalación y Configuración de Entorno Python con Flask y Django

1. Instalación de Python

   Opción 1: Desde la página oficial
   1. Visita la página de descargas de Python: https://www.python.org/downloads/
   2. Selecciona la versión de Python adecuada para tu sistema operativo y sigue las instrucciones de instalación.

   Opción 2: Desde la Microsoft Store
   1. Abre la Microsoft Store en tu equipo.
   2. Busca "Python 3.11" o una versión más reciente: https://www.microsoft.com/es-es/p/python-39/9p7qfqmjrfp7?activetab=pivot:overviewtab
   3. Haz clic en "Obtener" e instala Python desde la tienda.

2. Actualización de pip
   1. Abre una terminal (cmd en Windows, terminal en macOS/Linux).
   2. Ejecuta el siguiente comando para actualizar pip:
      python -m pip install --upgrade pip

3. Instalación de Flask
   1. En la misma terminal, instala Flask ejecutando:
      pip install flask

4. Creación del Entorno Virtual (Usando Django como ejemplo)

   ¿Qué es un Entorno Virtual?
   Un entorno virtual es un entorno de desarrollo aislado que permite instalar paquetes sin afectar el sistema global de Python.

   Pasos para Crear un Entorno Virtual

   1. Verificar Paquetes Instalados Globalmente:
      pip list

   2. Instalar virtualenv:
      pip install virtualenv

   3. Abrir Visual Studio Code como Administrador:
      - Abre Visual Studio Code.
      - Ejecuta como administrador.

   4. Crear un Entorno Virtual:
      virtualenv env

   5. Activar el Entorno Virtual:
      .\env\Scripts\activate

   6. Desactivar el Entorno Virtual (cuando sea necesario):
      deactivate

5. Instalación de Flask dentro del Entorno Virtual
   1. Con el entorno virtual activado, instala Flask:
      pip install flask

   2. Verifica que los paquetes necesarios están instalados:
      pip list

6. Descripción de Paquetes Relevantes

   - Werkzeug: Librería que permite manejar contraseñas de forma segura.
   - Jinja2: Motor de plantillas para Python.

7. Contenidos Online Adicionales

   Recursos
   - Bootstrap: Framework de CSS para desarrollar interfaces web responsivas.
   - FontAwesome: Biblioteca de íconos escalables.
   - jQuery: Biblioteca de JavaScript que simplifica la manipulación del DOM.

   Código de Ejemplo
   A continuación se muestra un código de ejemplo que utiliza varias de las herramientas mencionadas:

   from flask import Flask, request, jsonify, url_for, render_template, redirect
   from flask_cors import CORS  # Instala flask-cors con pip install flask-cors
   #from flask_mail import Mail, Message
   from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
   import pyodbc
   import os
   from datetime import timedelta
   from werkzeug.utils import secure_filename
   import json

   app = Flask(__name__)
   CORS(app)
   jwt = JWTManager(app)

   @app.route('/')
   def home():
       return render_template('index.html')

   if __name__ == '__main__':
       app.run(debug=True)

Este manual permite la instalacion de este programa usando Python, para gestionar un entorno virtual a traves de flask.
