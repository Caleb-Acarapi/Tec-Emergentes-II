from flask import Flask, request, jsonify

app = Flask(__name__)

carrito = [
    {'id': 1, 'producto': 'Manzana',  'cantidad': 3},
    {'id': 2, 'producto': 'Pan',      'cantidad': 2},
]

# GET - Obtener todos los productos del carrito
@app.route('/api/carrito', methods=['GET'])
def listar_carrito():
    return jsonify(carrito), 200


# GET - Obtener un producto específico del carrito
@app.route('/api/carrito/<int:id>', methods=['GET'])
def obtener_producto(id):
    producto = None
    for p in carrito:
        if p['id'] == id:
            producto = p
            break
    if producto:
        return jsonify(producto), 200
    return jsonify({'error': 'Producto no encontrado'}), 404


# POST - Agregar un producto al carrito
@app.route('/api/carrito', methods=['POST'])
def agregar_producto():
    nuevo_producto = {
        'id':       len(carrito) + 1,
        'producto': request.json.get('producto', ''),
        'cantidad': request.json.get('cantidad', 1)
    }
    carrito.append(nuevo_producto)
    return jsonify(nuevo_producto), 201


# PUT - Actualizar cantidad de un producto
@app.route('/api/carrito/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    producto = None
    for p in carrito:
        if p['id'] == id:
            producto = p
            break
    if producto is None:
        return jsonify({'error': 'Producto no encontrado'}), 404

    producto['producto'] = request.json.get('producto', producto['producto'])
    producto['cantidad'] = request.json.get('cantidad', producto['cantidad'])
    return jsonify(producto), 200


# DELETE - Eliminar un producto del carrito
@app.route('/api/carrito/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    global carrito
    carrito = [p for p in carrito if p['id'] != id]
    return jsonify({'mensaje': 'Producto eliminado del carrito'}), 200


if __name__ == '__main__':
    app.run(debug=True)
