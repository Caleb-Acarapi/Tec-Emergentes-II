from flask import Flask, request, jsonify

app = Flask(__name__)

productos = [
    {'id': 1, 'nombre': 'Laptop',   'precio': 1500.00, 'cantidad': 5},
    {'id': 2, 'nombre': 'Mouse',    'precio':   25.00, 'cantidad': 10},
    {'id': 3, 'nombre': 'Teclado',  'precio':   45.00, 'cantidad': 8},
]


# GET - Obtener todos los productos con su total por producto
@app.route('/api/productos', methods=['GET'])
def listar_productos():
    resultado = []
    for p in productos:
        item = {
            'id':       p['id'],
            'nombre':   p['nombre'],
            'precio':   p['precio'],
            'cantidad': p['cantidad'],
            'total':    p['precio'] * p['cantidad']
        }
        resultado.append(item)

    # Calcular el gran total de todos los productos
    gran_total = 0
    for p in productos:
        gran_total += p['precio'] * p['cantidad']

    return jsonify({'productos': resultado, 'gran_total': gran_total}), 200


# GET - Obtener un producto específico
@app.route('/api/productos/<int:id>', methods=['GET'])
def obtener_producto(id):
    producto = None
    for p in productos:
        if p['id'] == id:
            producto = p
            break
    if producto is None:
        return jsonify({'error': 'Producto no encontrado'}), 404

    resultado = {
        'id':       producto['id'],
        'nombre':   producto['nombre'],
        'precio':   producto['precio'],
        'cantidad': producto['cantidad'],
        'total':    producto['precio'] * producto['cantidad']
    }
    return jsonify(resultado), 200


# POST - Crear un producto
@app.route('/api/productos', methods=['POST'])
def crear_producto():
    precio   = request.json.get('precio', 0)
    cantidad = request.json.get('cantidad', 0)

    nuevo_producto = {
        'id':       len(productos) + 1,
        'nombre':   request.json.get('nombre', ''),
        'precio':   precio,
        'cantidad': cantidad
    }
    productos.append(nuevo_producto)

    nuevo_producto['total'] = precio * cantidad
    return jsonify(nuevo_producto), 201


# PUT - Actualizar un producto
@app.route('/api/productos/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    producto = None
    for p in productos:
        if p['id'] == id:
            producto = p
            break
    if producto is None:
        return jsonify({'error': 'Producto no encontrado'}), 404

    producto['nombre']   = request.json.get('nombre',   producto['nombre'])
    producto['precio']   = request.json.get('precio',   producto['precio'])
    producto['cantidad'] = request.json.get('cantidad', producto['cantidad'])

    resultado = {
        'id':       producto['id'],
        'nombre':   producto['nombre'],
        'precio':   producto['precio'],
        'cantidad': producto['cantidad'],
        'total':    producto['precio'] * producto['cantidad']
    }
    return jsonify(resultado), 200


# DELETE - Eliminar un producto
@app.route('/api/productos/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    global productos
    productos = [p for p in productos if p['id'] != id]
    return jsonify({'mensaje': 'Producto eliminado'}), 200


if __name__ == '__main__':
    app.run(debug=True)
