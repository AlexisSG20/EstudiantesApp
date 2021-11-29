from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .declarative_base import Base



class Seccion(Base):
    __tablename__ = 'seccion'

    id = Column(Integer, primary_key=True)
    nombreseccion = Column(String)
    cantidad = Column(Integer)
    tutor = Column(String)
    estudiantes = relationship('Estudiante', secondary='estudiante_seccion')
    profesores = relationship('Profesor', cascade='all, delete, delete-orphan')


class EstudianteSeccion(Base):
    __tablename__ = 'estudiante_seccion'

    seccion_id = Column(
        Integer,
        ForeignKey('seccion.id'),
        primary_key=True)

    estudiante_id = Column(
        Integer,
        ForeignKey('estudiante.id'),
        primary_key=True)

