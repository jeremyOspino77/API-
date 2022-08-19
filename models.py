from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ORD_MA_ESTADOS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(50)) 
    fecha = db.Column(db.String(30)) 
    nombre = db.Column(db.String(20)) 
    id_estado  = db.Column(db.Integer)
    id_digitador = db.Column(db.Integer)

    def json(self):
        return {
            'id': self.id,
            'uuid' : self.uuid,
            'fecha' : self.fecha,
            'nombre' : self.nombre,
            'id_estado' : self.id_estado,
            'id_digitador' : self.id_digitador
        }

    def delete(self):
        try:
                db.session.delete(self)
                db.session.commit()
                return True
        except:
                return False

class ORD_MA_CLIENTES(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(50)) 
    fecha = db.Column(db.String(30)) 
    nombre = db.Column(db.String(20)) 
    id_estado  = db.Column(db.Integer)
    id_digitador = db.Column(db.Integer)
    identificacion = db.Column(db.String(30))
    direccion = db.Column(db.String(30))
    telefono = db.Column(db.String(30))
    email = db.Column(db.String(250))

    def json(self):
        return {
            'id': self.id,
            'uuid' : self.uuid,
            'fecha' : self.fecha,
            'nombre' : self.nombre,
            'id_estado' : self.id_estado,
            'id_digitador' : self.id_digitador,
            'identificacion' : self.identificacion,
            'direccion' : self.direccion,
            'telefono' : self.telefono,
            'email' : self.email

        }

    

class ORD_MA_USUARIOS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(50)) 
    fecha = db.Column(db.String(30)) 
    nombre = db.Column(db.String(20)) 
    id_estado  = db.Column(db.Integer)
    id_digitador = db.Column(db.Integer)
    usuario = db.Column(db.String(250))
    password = db.Column(db.String(300))


    def json(self):
        return {
            'id': self.id,
            'uuid' : self.uuid,
            'fecha' : self.fecha,
            'nombre' : self.nombre,
            'id_estado' : self.id_estado,
            
        }


class ORD_MV_DETALLES(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_orden = db.Column(db.Integer)
    largo = db.Column(db.String(20)) 
    ancho = db.Column(db.String(20)) 
    id_estado  = db.Column(db.Integer)
    

    def json(self):
        return {
            'id': self.id,
            'id_orden' : self.id_orden,
            'largo' : self.largo,
            'ancho' : self.ancho,
            'id_estado' : self.id_estado,
            
        }

class ORD_MV_ORDENES(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(50)) 
    fecha = db.Column(db.String(30))  
    id_estado  = db.Column(db.Integer)
    id_digitador = db.Column(db.Integer)
    numero_orden = db.Column(db.String(30)) 
    id_cliente  = db.Column(db.Integer)

    def json(self):
        return {
            'id': self.id,
            'uuid' : self.uuid,
            'fecha' : self.fecha,
            'id_estado' : self.id_estado,
            'id_digitador' : self.id_digitador,
        }


class ORD_MV_PAISES(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(50)) 
    fecha = db.Column(db.String(30)) 
    nombre = db.Column(db.String(20)) 
    id_estado  = db.Column(db.Integer)
    id_digitador = db.Column(db.Integer)
    codigo = db.Column(db.String(5)) 


    def json(self):
        return {
            'id': self.id,
            'uuid' : self.uuid,
            'fecha' : self.fecha,
            'nombre' : self.nombre,
            'id_estado' : self.id_estado,
            'id_digitador' : self.id_digitador
        }




