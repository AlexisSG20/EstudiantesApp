from src.modelo.seccion import Seccion
from src.modelo.profesor import Profesor
from src.modelo.estudiante import Estudiante, Medio
from src.modelo.declarative_base import Session, engine, Base

if __name__ == '__main__':
    #Crea la BD
    Base.metadata.create_all(engine)

    #Abre la sesión
    session = Session()

    #crear profesor
    profesor1 = Profesor(nombre = "Samuel Torres")
    profesor2 = Profesor(nombre = "Aldo Gavilan")
    profesor3 = Profesor(nombre = "Buena Vista Social club")
    profesor4 = Profesor(nombre = "Arturo Sandoval")
    session.add(profesor1)
    session.add(profesor2)
    session.add(profesor3)
    session.add(profesor4)
    session.commit()

    # Crear Estudiantes
    estudiante1 = Estudiante(Nombre = "Jose Suares Colchones ", anio = "5", medio = Medio.DISCO)
    estudiante2 = Estudiante(Nombre = "Paty Suares Domar ", anio = "6", medio = Medio.DISCO)
    estudiante3 = Estudiante(Nombre="Laure Pausini Dolorier ", anio="4", medio=Medio.DISCO)
    session.add(estudiante1)
    session.add(estudiante2)
    session.commit()

    # Crear Seccion
    seccion1 = Seccion(Seccion = "A", anio = 3, profesor = "Samuel Torres")
    seccion2 = Seccion(Seccion = "B", anio = 3,  profesor = "Paul Roman")
    seccion3 = Seccion(Seccion = "C", anio = 4,  profesor = "Gaby Herreros")
    session.add(seccion1)
    session.add(seccion2)
    session.add(seccion3)
    session.commit()

    # Relacionar estudiante con seccion
    estudiante1.seccion = [seccion1, estudiante2]
    estudiante2.seccion = [seccion2, estudiante3]

    # Relacionar seccion con profesores
    seccion1.profesor = [profesor1]
    seccion2.profesor = [profesor2]
    seccion3.profesor = [profesor3, profesor4]

    session.commit()
    session.close()