from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
DATABASE = 'usuarios.db'

# Crear tabla de usuarios si no existe
def init_db():
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        usuario TEXT UNIQUE NOT NULL,
                        contraseña TEXT NOT NULL)''')
        conn.commit()

@app.route('/registro', methods=['POST'])
def registro():
    data = request.get_json()
    usuario = data.get('usuario')
    contraseña = data.get('contraseña')
    
    if not usuario or not contraseña:
        return jsonify({'error': 'Datos incompletos'}), 400

    hash_contraseña = generate_password_hash(contraseña)
    
    try:
        with sqlite3.connect(DATABASE) as conn:
            c = conn.cursor()
            c.execute('INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)', (usuario, hash_contraseña))
            conn.commit()
        return jsonify({'mensaje': 'Usuario registrado exitosamente'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'El usuario ya existe'}), 409

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = data.get('usuario')
    contraseña = data.get('contraseña')
    
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute('SELECT contraseña FROM usuarios WHERE usuario = ?', (usuario,))
        result = c.fetchone()
        if result and check_password_hash(result[0], contraseña):
            return jsonify({'mensaje': 'Login exitoso'}), 200
        else:
            return jsonify({'error': 'Credenciales inválidas'}), 401

@app.route('/tareas', methods=['GET'])
def tareas():
    return '''
    <html>
        <head><title>Bienvenido</title></head>
        <body><h1>Bienvenido a tu sistema de tareas</h1></body>
    </html>
    '''

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
