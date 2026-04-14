import sqlite3

conexion = sqlite3.connect('universidad.db') #Crear la conexion a la base de datos, si no existe

conexion.execute('''
CREATE TABLE IF NOT EXISTS  aula(
    id INTEGER PRIMARY KEY,
    descripcion TEXT NOT NULL,
    horas INTEGER NOT NULL
)''')

conexion.execute('''
CREATE TABLE IF NOT EXISTS  universitario(
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellidos TEXT NOT NULL,
    fecha_nacimiento DATE NOT NULL
)''')

# conexion.execute('''
# INSERT INTO aula (descripcion, horas) 
# VALUES ('Programacion(Python)-I', 25)
# ''')

# conexion.execute('''
# INSERT INTO aula (descripcion, horas) 
# VALUES ('Programacion-Web(HTML, CSS, JavaScript)-I', 30)
# ''')

# conexion.execute('''
#     INSERT INTO universitario (nombre, apellidos, fecha_nacimiento)
#     VALUES ('Caleb', 'Acarapi', '1999-09-09')
# ''')


# conexion.commit()


conexion.execute('''
CREATE TABLE IF NOT EXISTS matriculacion(
    id INTEGER PRIMARY KEY,
    fecha_matriculacion DATE NOT NULL,
    curso_id INTEGER NOT NULL,
    universitario_id INTEGER NOT NULL,
    FOREIGN KEY (curso_id) REFERENCES aula(id),
    FOREIGN KEY (universitario_id) REFERENCES universitario(id)
)''')

conexion.execute('''
INSERT INTO matriculacion (fecha_matriculacion, curso_id, universitario_id)
VALUES ('2024-02-01', 1, 1)
''')
conexion.execute('''
INSERT INTO matriculacion (fecha_matriculacion, curso_id, universitario_id)
VALUES ('2024-02-01', 2, 1)
''')

conexion.commit()

print("Aulas:")
controlador = conexion.execute('SELECT * FROM aula')
for registro in controlador:
    print(registro)

print("\nUniversitarios:")
controlador = conexion.execute('SELECT * FROM universitario')
for registro in controlador:
    print(registro)

print("\nMatriculaciones:")
controlador = conexion.execute('SELECT * FROM matriculacion')
for registro in controlador:
    print(registro)