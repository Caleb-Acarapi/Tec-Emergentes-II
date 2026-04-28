from flask import Flask, request, jsonify

app = Flask(__name__)

contactos = [
    {'id': 1, 'nombre': 'Ana García',   'correo': 'ana@ejemplo.com',    'celular': '70000001'},
    {'id': 2, 'nombre': 'Carlos López', 'correo': 'carlos@ejemplo.com', 'celular': '70000002'},
    {'id': 3, 'nombre': 'María Torres', 'correo': 'maria@ejemplo.com',  'celular': '70000003'},
]

# GET - Obtener todos los contactos
@app.route('/api/contactos', methods=['GET'])
def listar_contactos():
    return jsonify(contactos), 200


# GET - Obtener un contacto específico
@app.route('/api/contactos/<int:id>', methods=['GET'])
def obtener_contacto(id):
    contacto = None
    for c in contactos:
        if c['id'] == id:
            contacto = c
            break
    if contacto:
        return jsonify(contacto), 200
    return jsonify({'error': 'Contacto no encontrado'}), 404


# POST - Crear un contacto
@app.route('/api/contactos', methods=['POST'])
def crear_contacto():
    nuevo_contacto = {
        'id':      len(contactos) + 1,
        'nombre':  request.json.get('nombre', ''),
        'correo':  request.json.get('correo', ''),
        'celular': request.json.get('celular', '')
    }
    contactos.append(nuevo_contacto)
    return jsonify(nuevo_contacto), 201


# PUT - Actualizar un contacto
@app.route('/api/contactos/<int:id>', methods=['PUT'])
def actualizar_contacto(id):
    contacto = None
    for c in contactos:
        if c['id'] == id:
            contacto = c
            break
    if contacto is None:
        return jsonify({'error': 'Contacto no encontrado'}), 404

    contacto['nombre']  = request.json.get('nombre',  contacto['nombre'])
    contacto['correo']  = request.json.get('correo',  contacto['correo'])
    contacto['celular'] = request.json.get('celular', contacto['celular'])
    return jsonify(contacto), 200


# DELETE - Eliminar un contacto
@app.route('/api/contactos/<int:id>', methods=['DELETE'])
def eliminar_contacto(id):
    global contactos
    contactos = [c for c in contactos if c['id'] != id]
    return jsonify({'mensaje': 'Contacto eliminado'}), 200


if __name__ == '__main__':
    app.run(debug=True)
