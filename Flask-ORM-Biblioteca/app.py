from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///biblioteca.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#Crear la tabla intermedia libro - generos
libro_genero = db.Table(
    'libro_genero',
    db.Column('libro_id',
              db.Integer,
              db.ForeignKey('libros.id'),
              primary_key = True),
    db.Column('genero_id',
              db.Integer,
              db.ForeignKey('generos.id'),
              primary_key = True)
)
#Creando el Modelo autor
class Autor(db.Model):
    __tablename__ = 'autor'

    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.Integer, nullable = False)
    nacionalidad = db.Column(db.String(100), nullable = False)

    #Definiendo la relacion autor - libros
    libros = db.relationship('Libros', back_populates = 'autor', cascade = 'all, delete-orphan')

    def __repr__(self):
        return f'Autor: {self.nombre}, con nacionalidad: {self.nacionalidad}'

#Creando del Modelo Libros
class Libros(db.Model):
    __tablename__ = "libros"

    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(100), nullable = False)
    anio = db.Column(db.Integer, nullable = False)

    #Definiendo la relacion para autores - libros
    autor_id = db.Column(db.Integer, db.ForeignKey("autor.id"), nullable = False)
    autor = db.relationship('Autor', back_populates = 'libros')

    #Definiendo la relacion para libro - genero
    generos = db.relationship('Generos', secondary = libro_genero, back_populates = 'libros')

    def __repr__(self):
        return f'Libro: {self.titulo}, Anio: {self.anio}, Autor: {self.autor.nombre}'
#Creando el Modelo de Generos
class Generos(db.Model):
    __tablename__ = 'generos'
    
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50), nullable = False)

    #Definiendo la relacion entre genero - libro
    libros = db.relationship('Libros', secondary = libro_genero, back_populates = 'generos')

    def __repr__(self):
        return f'Genero: {self.nombre}'
    
def init_db():
    with app.app_context():
        db.create_all()
        print("Base de datos creada exitosamente")

def insertar_datos():
    with app.app_context():
        #Crear Autores
        autor1 = Autor(nombre = 'Linus Torvalds', nacionalidad = 'Estados Unidos')
        autor2 = Autor(nombre = 'Elliot Anderson', nacionalidad = 'Reino Unido')
        autor3 = Autor(nombre = 'Richar Endricks', nacionalidad = 'Canada')

        #Crear Libros
        libro1 = Libros(titulo = 'Linux la base de todo', anio = 2004, autor = autor1)
        libro2 = Libros(titulo = 'El internet no es seguro', anio = 2010, autor = autor2)
        libro3 = Libros(titulo = 'El algoritmo que cambio todo', anio = 2015, autor = autor3)
        libro4 = Libros(titulo = 'El mundo de el Pentesting', anio = 2020, autor = autor2)
        libro5 = Libros(titulo = 'El poder de Linux', anio = 2011, autor = autor1)

        #Crear Generos
        genero1 = Generos(nombre = 'Seguridad')
        genero2 = Generos(nombre = 'Ciencia')
        genero3 = Generos(nombre = 'Tecnologia')
        genero4 = Generos(nombre = 'Ciberseguridad')

        #Asociar Libros con Generos
        libro1.generos.extend([genero2, genero3])
        libro2.generos.append(genero1)
        libro3.generos.extend([genero2, genero3])
        libro4.generos.append(genero4)
        libro5.generos.extend([genero1, genero3, genero4, genero2])

        db.session.add_all([autor1, autor2, autor3, 
                            libro1, libro2, libro3, libro4, libro5, 
                            genero1, genero2, genero3, genero4
                        ])
        #Registrar cambios
        db.session.commit()
        print("Datos insertados exitosamente")

def consultar_datos():
    with app.app_context():
        #Listar de autores con sus libros
        print("=================Lista de Autores=====================\n")
        autores = Autor.query.all()
        for autor in autores:
            print(f'\n {autor}')
            for libro in autor.libros:
                print(f'\n*  {libro}')
        #Listar generos con sus libros
        print('========================Lista de Generos============================\n')
        generos = Generos.query.all()
        for genero in generos:
            print(f'\n {genero}')
            for libro in genero.libros:
                print(f'\n* {libro}')

def actualizar_datos():
    #Actualizar el titulo de un libro
    with app.app_context():
        libro = Libros.query.filter_by(id = 5).first()
        if libro:
            libro.titulo = "El Pentesting las vulnerabilidades expuestas"
            db.session.commit()
            print('\nLibro actualizado exitosamente')
            consultar_datos()
        else:
            print('\nLibro no encontrado')

def eliminar_datos():
    with app.app_context():
        #Eliminar un autor(sus libros deben eliminarse en cascada)
        autor = Autor.query.filter_by(id = 2).first()
        if autor:
            db.session.delete(autor)
            db.session.commit()
            print('\nAutor eliminado exitosamente')
            consultar_datos()
        else:
            print('\nAutor no encontrado')

if __name__ == '__main__':
    # init_db()
    # insertar_datos()
    # consultar_datos()
    # actualizar_datos()
    # eliminar_datos()
    pass













