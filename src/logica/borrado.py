from src.modelo.seccion import Seccion
from src.modelo.profesor import profesor
from src.modelo.estudiante import estudiante, Medio
from src.modelo.declarative_base import Session, engine, Base

if __name__ == '__main__':
    session = Session()

    seccion2 = session.query(Seccion).get(2)
    session.delete(seccion2)

    session.commit()
    session.close()