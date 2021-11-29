import enum

from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship

from .declarative_base import Base


class Medio(enum.Enum):
    GRADO = 1
    CICLO = 2
    NOTA = 3


class Estudiante(Base):
    __tablename__ = 'estudiante'

    id = Column(Integer, primary_key=True)
    ApellidoPaterno = Column(String)
    ApellidoMaterno = Column(String)
    Nombres = Column(String)
    medio = Column(Enum(Medio))
    secciones = relationship('Seccion', secondary='estudiante_seccion')