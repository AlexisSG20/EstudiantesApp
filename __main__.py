from src.modelo.seccion import Seccion
from src.modelo.profesor import Profesor
from src.modelo.estudiante import Estudiante, Medio
from src.modelo.declarative_base import Session, engine, Base
from src.logica.destacados import Coleccion


def anadir_estudiante (ApellidoPaterno , ApellidoMaterno , Nombres , medio) :
   # Crea la BD
   Base.metadata.create_all ( engine )

   # Abre la sesion
   session = Session ( )
   coleccion = Coleccion ( )

   if coleccion.agregar_estudiante ( ApellidoPaterno , ApellidoMaterno , Nombres , medio ) :
      print ( f"Se añadio el estudiante: {ApellidoPaterno} {ApellidoMaterno} {Nombres}" )
   else :
      print ( f"El alumno: {ApellidoPaterno} {ApellidoMaterno} {Nombres}, ya existe" )
   session.close()

def editar_estudiante (estudiante_id, ApellidoPaterno ,  ApellidoMaterno , Nombres , medio) :
   # Crea la BD
   Base.metadata.create_all ( engine )

   # Abre la sesion
   session = Session ( )
   coleccion = Coleccion ( )

   if coleccion.editar_estudiante ( estudiante_id , ApellidoPaterno , ApellidoMaterno , Nombres , medio ) :
      print ( f"Se modifico el album con id: {estudiante_id}" )
   else :
      print ( f"El estudiante '{ApellidoPaterno}' '{ApellidoMaterno}' '{Nombres}' con el id: {estudiante_id}, ya existe" )
   session.close()



def mostrar_estudiante (estudiante_id) :
   # Crea la BD
   Base.metadata.create_all ( engine )

   # Abre la sesion
   session = Session ( )
   coleccion = Coleccion ( )

   estudiante=coleccion.dar_estudiante_por_id(estudiante_id)
   # print(album)
   print ( f"=======================================" )
   print ( f"Id Estudiante   : {estudiante[ 'id' ]}" )
   print ( f"Apellido Paterno del Estudiante: {estudiante[ 'apellido paterno' ]}" )
   print ( f"Apellido Materno del Estudiante: {estudiante[ 'apellido materno' ]}" )
   print ( f"Nombres : {estudiante[ 'nombres' ]}" )
   print ( f"Medio       : {estudiante[ 'medio' ]}" )
   print ( f"=======================================" )
   session.close()

def Anadir_registros():
   # Crea la BD
   Base.metadata.create_all(engine)

   # Abre la sesion
   session = Session()

   # crear profesores
   profesor1 = Profesor(ApellidoPaterno="Roni", ApellidoMaterno="Elias", Nombres="Maria")
   profesor2 = Profesor(ApellidoPaterno="Quispe", ApellidoMaterno="Ticse", Nombres="Esteban")
   profesor3 = Profesor(ApellidoPaterno="Rojas", ApellidoMaterno="Loes", Nombres="Alvaro")
   profesor4 = Profesor(ApellidoPaterno="Ramires", ApellidoMaterno="Gonzales", Nombres="Ana")
   session.add(profesor1)
   session.add(profesor2)
   session.add(profesor3)
   session.add(profesor4)
   session.commit()

   # Crear estudiantes
   estudiante1 = Estudiante(ApellidoPaterno="Lopez", ApellidoMaterno="Gonzales", Nombres="Esteban", medio=Medio.GRADO)
   estudiante2 = Estudiante(ApellidoPaterno="Roman", ApellidoMaterno="Flores", Nombres="Jose", medio=Medio.GRADO)
   session.add(estudiante1)
   session.add(estudiante2)

   # Crear secciones
   seccion1 = Seccion(Nombre="GHGA", Cantidad=30, Tutor="Roman")
   seccion2 = Seccion(Nombre="GHGB", Cantidad=35, Tutor="Samuel")
   seccion3 = Seccion(Nombre="GHGC", Cantidad=45, Tutor="Felipe")
   session.add(seccion1)
   session.add(seccion2)
   session.add(seccion3)

   # Relacionar estudiantes con secciones
   estudiante1.secciones = [seccion1, seccion2]
   estudiante2.secciones = [seccion1, seccion2]

   # Relacionar secciones con profesores
   seccion1.profesores = [profesor1]
   seccion2.profesores = [profesor2]
   seccion3.profesores = [profesor3, profesor4]
   session.commit()

   session.commit()
   session.close()

if __name__ == '__main__':
   Anadir_registros ( )

   anadir_estudiante ( "Rojas" , "Alvares" , "Juan" , Medio.CD )

   for i in [ 1 ] :
      mostrar_estudiante ( i )

   i = 1
   while i <= 4:
      mostrar_estudiante(i)
      i=i+1

