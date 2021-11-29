from sqlalchemy import Column, Integer, String, ForeignKey
from .declarative_base import Base

class Profesor(Base):
  __tablename__ = 'profesor'
  id = Column(Integer, primary_key=True)
  ApellidoPaterno = Column(String)
  ApellidoMaterno = Column(String)
  Nombres = Column(String)
  Seccion = Column(Integer, ForeignKey('seccion.id'))
