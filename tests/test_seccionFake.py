import datetime
import unittest
import random

from faker import Faker

from src.logica.destacados import Coleccion
from src.modelo.estudiante import Estudiante,Medio
from src.modelo.seccion import Seccion,EstudianteSeccion
from src.modelo.profesor import Interprete
from src.modelo.declarative_base import Session
from fake_providers import *

class SeccionTestCaseFake(unittest.TestCase):
    def setUp ( self ) :
        self.logica = Coleccion()
        self.session = Session ( )
        self.data_factory = Faker ( )

        # Generación de datos con libreria Faker
        self.data_factory.add_provider (SeccionNombreseccionProvider )
        self.data_factory.add_provider (SeccionCantidad )
        self.data_factory.add_provider (SeccionTutor )

        self.data=[]
        self.secciones=[]
        for i in range ( 0 , 2 ) :
            self.data.append(
                (
                    self.data_factory.unique.seccionNombreseccion ( ),
                    self.data_factory.seccionCantidad ( ),
                    self.data_factory.seccionTutor ( ),
                    self.data_factory.cancionCompositor ()
                )
            )

            self.secciones.append(
                Cancion(
                    nombreseccion = self.data[ -1 ][ 0 ] ,
                    cantidad = self.data[ -1 ][ 1 ] ,
                    tutor = self.data[ -1 ][ 2 ] ,
                    estudiantes=[],
                    profesores=[]
                 )
            )
            self.session.add ( self.secciones[ -1 ] )

        '''
            Persiste los objetos
            En este setUp no se cierra la sesión para usar
            los estudiantes en las pruebas
        '''
        self.session.commit ( )
        #self.session.close()

    def tearDown ( self ) :
        self.session = Session ( )

        busqueda_secciones = self.session.query ( Cancion ).all ( )
        for seccion in busqueda_secciones :
            self.session.delete ( seccion )

        self.session.commit()
        self.session.close()

    def test_constructor ( self ) :
        for seccion , dato in zip ( self.secciones , self.data ) :
            self.assertEqual ( seccion.nombreseccion , dato[ 0 ] )
            self.assertEqual ( seccion.cantidad , dato[ 1 ] )
            self.assertEqual ( seccion.tutor , dato[ 2 ] )

    def test_agregar_seccion ( self ) :
        self.data.append (
            (
                self.data_factory.unique.seccionNombreseccion ( ) ,
                self.data_factory.seccionCantidad ( ) ,
                self.data_factory.seccionTutor ( ),
            )
        )

        resultado = self.logica.agregar_seccion (
            nombreseccion = self.data[ -1 ][ 0 ] ,
            cantidad = self.data[ -1 ][ 1 ] ,
            tutor = self.data[ -1 ][ 2 ] )
        self.assertEqual ( resultado , True )

