from flask import Flask, render_template, request, redirect, url_for
import sqlite3

main = Flask(__name__)

def iniciar_base_de_datos():
    conexion = sqlite3.connect('kardex.db')
    conexion.execute('''
        CREATE TABLE IF NOT EXISTS estudiantes (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            telefono TEXT NOT NULL,
            fecha_nacimiento DATE NOT NULL
        )
    ''')
    conexion.commit()
    conexion.close()    
 
iniciar_base_de_datos()

@main.route('/')
def index():
    conexion = sqlite3.connect('kardex.db')
    conexion.row_factory = sqlite3.Row
    controlador = conexion.cursor()
    controlador.execute('SELECT * FROM estudiantes')
    estudiantes = controlador.fetchall()
    return render_template('index.html', estudiantes=estudiantes)


@main.route("/crear")
def crear(): 
    return render_template("crear.html")

@main.route("/guardar", methods=["POST"])
def guardar():
    nombre = request.form["nombre"]
    telefono = request.form["telefono"]
    fecha_nacimiento = request.form["fecha_nacimiento"]

    conexion = sqlite3.connect('kardex.db')
    controlador = conexion.cursor()
    controlador.execute('''
        INSERT INTO estudiantes (nombre, telefono, fecha_nacimiento)
        VALUES (?, ?, ?)
    ''', (nombre, telefono, fecha_nacimiento))
    conexion.commit()
    conexion.close()

    return redirect("/")

@main.route("/editar/<int:id>")
def estudiante_editar(id):
    conexion = sqlite3.connect("kardex.db")
    conexion.row_factory = sqlite3.Row
    controlador = conexion.cursor()
    controlador.execute("SELECT * FROM estudiantes WHERE id = ?", (id,))
    estudiante = controlador.fetchone()
    return render_template("editar.html", estudiante=estudiante)

@main.route("/actualizar/<int:id>", methods=["POST"])
def actualizar(id):
    id = request.form["id"]
    nombre = request.form["nombre"]
    telefono = request.form["telefono"]
    fecha_nacimiento = request.form["fecha_nacimiento"]

    conexion = sqlite3.connect("kardex.db")
    controlador = conexion.cursor()
    controlador.execute('''
        UPDATE estudiantes
        SET nombre = ?, telefono = ?, fecha_nacimiento = ?
        WHERE id = ?
    ''', (nombre, telefono, fecha_nacimiento, id))
    conexion.commit()
    conexion.close()

    return redirect("/")

@main.route("/eliminar/<int:id>")
def eliminar(id):
    conexion = sqlite3.connect("kardex.db")
    controlador = conexion.cursor()
    controlador.execute('DELETE FROM estudiantes WHERE id = ?', (id,))
    conexion.commit()
    conexion.close()
    return redirect("/")

if __name__ == '__main__':
    main.run(debug=True)