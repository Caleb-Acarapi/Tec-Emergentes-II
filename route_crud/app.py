from flask import Flask, request, jsonify

app = Flask(__name__)

tareas = [
    {'id':1,'tarea':'Aprender Flask','completada':False},
    {'id':2,'tarea':'Practicar Flask','completada':False}
]

# GET - Obtener todas las tareas
@app.route("/api/tareas", methods=['GET'])
def listar_tareas():
    return jsonify(tareas), 200

# GET - Obtener una tarea específica
@app.route("/api/tareas/<int:id>")
def obtener_tarea(id):
    tarea = None
    for t in tareas:
        if t['id'] == id:
            tarea = t
            break
    if tarea: 
        return jsonify(tarea), 200
    return jsonify({'error':'Tarea no encontrada'}), 404

# POST - Crear una tarea
@app.route("/api/tareas", methods=['POST'])
def crear_tarea():
    nueva_tarea = {
        'id': len(tareas)+1,
        'tarea': request.json.get('tarea',''),
        'completada': request.json.get('completada',False)
    }
    tareas.append(nueva_tarea)
    return jsonify(nueva_tarea), 201

# DELETE - Eliminar tarea
@app.route('/api/tareas/<int:id>', methods=['DELETE'])
def eliminar_tarea(id):
    global tareas

    tareas = [ t for t in tareas if t['id']!= id]
    return jsonify({ 'mensaje': 'tarea eliminada'}), 200


if __name__ == "__main__":
    app.run(debug = True)
