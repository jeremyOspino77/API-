from flask import Flask
from flask import jsonify
from flask import request
from config import config
from models import db
from models import ORD_MA_ESTADOS
from models import ORD_MA_CLIENTES
from models import ORD_MA_USUARIOS
from models import ORD_MV_DETALLES
from models import ORD_MV_ORDENES
from models import ORD_MV_PAISES


def create_app(enviroment):
    app = Flask(__name__)
    app.config.from_object(enviroment)
    with app.app_context():
        db.init_app(app)
    return app

enviroment = config['development']
app = create_app(enviroment)


@app.route('/estados', methods=['GET'])
def estados():
    
    estados = [ estado.json() for estado in ORD_MA_ESTADOS.query.all() ]
    return jsonify({'estados': estados })

@app.route('/estados/<id>', methods=['DELETE'])
def borrar_estado(id):
    """borrar estado
    """
    estado = ORD_MA_ESTADOS.query.filter_by(id=id).first()
    if estado is None:
        return jsonify({'message': 'no se encuantra regristrado ningun estado'}), 404

    estado.delete()

    return jsonify({'message': 'no tiene estado' })

@app.route('/clientes', methods=['GET'])
def clientes():
    """Listar clientes
    """
    clientes = [ clientes.json() for clientes in ORD_MA_CLIENTES.query.all() ]
    return jsonify({'clientes': clientes})

@app.route('/cliente', methods=['POST'])
def crear_cliente():
    data = request.get_json(force=True)
    
    nuevo_registro = ORD_MA_CLIENTES(
        id_estado =  data['id_estado'],
        fecha = data['fecha'],
        nombre = data['nombre'],
        direccion = data['direccion'],
        telefono = data['telefono'],
        email = data['email']
    )

    db.session.add(nuevo_registro)
    db.session.commit()

    return jsonify({'cliente': nuevo_registro.json()})

@app.route('/cliente/<id>', methods=['GET'])
def get_x_id_cliente(id):
    un_cliente = ORD_MA_CLIENTES.query.filter_by(id=id).first()

    if un_cliente is None:
        return jsonify({'message': 'El cliente no existe'}), 404

    return jsonify({'cliente': un_cliente.json()})

@app.route('/cliente/<id>', methods=['PUT'])
def actualizar_cliente(id):
    cliente = ORD_MA_CLIENTES.query.filter_by(id=id).first()
    
    if cliente is None:
       return jsonify({'message': 'El cliente no existe'}), 404

    data = request.get_json(force=True)
    cliente.id_estado =  data['id_estado'],
    cliente.fecha = data['fecha'],
    cliente.nombre = data['nombre'],
    cliente.direccion = data['direccion'],
    cliente.telefono = data['telefono'],
    cliente.email = data['email']

    db.session.add(cliente)
    db.session.commit()

    return jsonify(cliente.json())

@app.route('/cliente/<id>', methods=['DELETE'])
def borrar_cliente(id):
    cliente = ORD_MA_CLIENTES.query.filter_by(id=id).first()
    
    if cliente is None:
       return jsonify({'message': 'El cliente no existe'}), 404

    db.session.delete(cliente)
    db.session.commit()

    return jsonify({'message': 'el cliente ha sido eliminado' })


@app.route('/orden/nueva', methods=['POST'])
def nueva_orden():
    data = request.get_json(force=True)

    nueva_orden = ORD_MV_ORDENES(
        id = data['id'],
        uuid = data['uuid'],
        fecha = data['fecha'],
        id_digitador = data['id_digitador'],
        numero_orden = data['numero_orden'],
        id_cliente  = data['id_cliente'],
    )

    db.session.add(nueva_orden)
    db.session.commit()


    return jsonify({'orden/nueva': nueva_orden.json()})

@app.route('/ordenes', methods=['GET'])
def ver_ordenes():
    
    ordenes = [ ordenes.json() for ordenes in ORD_MV_ORDENES.query.all() ]
    return jsonify({'message':'vista de orden'})


@app.route('/orden/<id>', methods=['GET'])
def ver_orden_x_id():
    una_orden = ORD_MV_ORDENES.query.filter_by(id=id).first()

    if una_orden is None:
       return jsonify({'message': 'la orden no existe'}), 404

    return jsonify({'orden': una_orden.json()})

@app.route('/orden/<id>/aprobar', methods=['PUT'])
def aporbar_orden():
    orden_aprovada = ORD_MV_ORDENES.query.filter_by(id=id).first()
     
    if orden_aprovada is None:
       return jsonify({'message': 'la orden no existe'}), 404

    data = request.get_json(force=True)
    orden_aprovada.id_estado =  data['id_estado'],
    orden_aprovada.fecha = data['fecha'],
    orden_aprovada.uuid = data['uuid'],
    orden_aprovada.id = data['fecha'],
    orden_aprovada.numero_orden = data['numero_orden'],
    orden_aprovada.id_cliente  = data['id_cliente'],
    orden_aprovada.id_digitador = data['id_digitador'],


    db.session.add(orden_aprovada)
    db.session.commit()

    return jsonify(orden_aprovada.json())

@app.route('/orden/<id>/anular', methods=['DELETE'])
def anular_orden():
    orden_borrada = ORD_MV_ORDENES.query.filter_by(id=id).first()
    
    if orden_borrada is None:
       return jsonify({'message': 'la orden no existe'}), 404

    db.session.delete(orden_borrada)
    db.session.commit()

    return jsonify({'message': 'la orden fue eliminada' })


@app.route('/detalles', methods=['GET'])
def ver_detalles():
    
    detalles = [ detalles.json() for detalles in ORD_MV_DETALLES.query.all() ]
    return jsonify({'detalles': detalles })


if __name__ == '__main__':
    app.run(debug=True)


