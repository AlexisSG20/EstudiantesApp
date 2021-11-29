from src.modelo.seccion import Seccion
from src.modelo.profesor import Profesor
from src.modelo.estudiante import Estudiante, Medio
from src.modelo.declarative_base import Session, engine, Base

if __name__ == '__main__':
    session = Session()

    canciones = session.query(Seccion).all()

    print('Las estudiantes almacenadas son:')
    for seccion in secciones:
        print("Nombre: " + seccion.nombre + " (00:" +
        str(seccion.minutos) + ":" +
        str(seccion.segundos) + ")")

    print("profesor")
    for interprete in seccion.interpretes:
        print(" - " + interprete.nombre)

    for estudiante in seccion.estudiante:
        print(" -- la presente en la seccion: " + estudiante.nombre)
        print("")

    print('Los estudiantes almacenados en discos son:')
    estudiantes = session.query(estudiante).filter(Estudiante.medio == Medio.DISCO).all()
    for estudiante in estudiante:
        print("estudiante es: " + estudiante.nombre)

    session.close()