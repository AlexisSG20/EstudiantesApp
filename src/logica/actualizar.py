from src.modelo.seccion import Seccion
from src.modelo.profesor import Profesor
from src.modelo.estudiante import Estudiante, Medio
from src.modelo.declarative_base import Session, engine, Base

if __name__ == '__main__':
    session = Session()

    seccion = session.query(Seccion).get(2)

    profesor = session.query(Profesor).get(4)
    Seccion.Grado=5
    Seccion.Clase = "A"
    Seccion.profesor = "Pedro Pérez"
    Seccion.profesores.append(Profesor)
    session.add(Seccion)
    session.commit()

    session.close()