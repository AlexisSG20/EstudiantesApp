from src.modelo.declarative_base import engine, Base, session
from src.modelo.estudiante import Estudiante

class Coleccion():
    def __init__(self):
        Base.metadata.create_all(engine)

    def agregar_estudiante(self, nombre, anio, medio):
        busqueda = session.query(Estudiante).filter(Estudiante.nombre == nombre).all()
        if len(busqueda) == 0:
            estudiante = Estudiante(nombre=nombre, anio=anio,  medio=medio)
            session.add(estudiante)
            session.commit()
            return True
        else:
            return False

    def dar_medios(self):
        return [medio.name for medio in Medio]

    def editar_estudiante(self, estudiante_id, nombre, anio, medio):
        busqueda = session.query(Estudiante).filter(Estudiante.nombre == nombre, Estudiante.id != estudiante_id).all()
        if len(busqueda) == 0:
            estudiante = session.query(Estudiante).filter(Estudiante.id == estudiante_id).first()
            estudiante.nombre = nombre
            estudiante.anio = anio
            estudiante.medio = medio
            session.commit()
            return True
        else:
            return False

    def eliminar_estudiante(self, estudiante_id):
        try:
            estudiante = session.query(Estudiante).filter(Estudiante.id == estudiante_id).first()
            session.delete(estudiante)
            session.commit()
            return True
        except:
            return False

    def dar_estudiante_por_id(self, album_id):
        return session.query(Estudiante).get(album_id).__dict__
