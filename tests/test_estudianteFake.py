import datetime
import unittest
import random

from faker import Faker

from src.logica.coleccion import Coleccion
from src.modelo.estudiante import Estudiante,Medio
from src.modelo.seccion import Seccion,EstudianteSeccion
from src.modelo.profesor import Profesor
from src.modelo.declarative_base import Session
from fake_providers import EstudianteApellidoPaternoProvider, EstudianteApellidoMaternoProvider,EstudianteNombresProvider,EstudianteMedioProvider

class EstudianteTestCaseFake(unittest.TestCase):
    def setUp ( self ) :
        self.logica = Coleccion()
        self.session = Session ( )
        self.data_factory = Faker ( )

        # Generación de datos con libreria Faker
        self.data_factory.add_provider ( EstudianteApellidoPaternoProvider )
        self.data_factory.add_provider ( EstudianteApellidoMaternoProvider )
        self.data_factory.add_provider ( EstudianteNombresProvider )
        self.data_factory.add_provider ( EstudianteMedioProvider )

        self.data=[]
        self.estudiantes=[]
        for i in range ( 0 , 2 ) :
            self.data.append(
                (
                    self.data_factory.unique.estudianteApellidoPaterno ( ),
                    self.data_factory.estudianteApellidoMaterno  ( ),
                    self.data_factory.estudianteNombres  ( ),
                    self.data_factory.estudianteMedio ()
                )
            )
            self.estudiantes.append(
                Estudiante(
                    EstudianteApellidoPaterno = self.data[ -1 ][ 0 ] ,
                    EstudianteApellidoMaterno= self.data[ -1 ][ 1 ] ,
                    EstudiantesNombres = self.data[ -1 ][ 2 ] ,
                    Estudiantemedio = self.data[ -1 ][ 3 ] ,
                    secciones = [ ]
                )
            )
            self.session.add ( self.estudiantes[ -1 ] )

        '''
            Persiste los objetos
            En este setUp no se cierra la sesión para usar
            los estudiantes en las pruebas
        '''
        self.session.commit ( )
        #self.session.close()

    def tearDown ( self ) :
        self.session = Session ( )

        busqueda_estudiante = self.session.query ( Album ).all ( )
        for estudiante in busqueda_estudiante :
            self.session.delete ( estudiante )

        self.session.commit()
        self.session.close()

    def test_constructor ( self ) :
        for estudiante , dato in zip ( self.estudiantes , self.data ) :
            self.assertEqual ( estudiante.ApellidoPaterno , dato[ 0 ] )
            self.assertEqual ( estudiante.ApellidoMaterno , dato[ 1 ] )
            self.assertEqual ( estudiante.Nombres , dato[ 2 ] )
            self.assertEqual ( estudiante.Medio , dato[ 3 ] )

    def test_agregar_estudiante ( self ) :
        estudianteApellidoPaterno=self.data_factory.unique.estudianteApellidoPaterno ( )
        estudianteApellidoMaterno=self.data_factory.unique.estudianteApellidoMaterno ( )
        estudianteNombres=self.data_factory.estudianteNombres ( )
        estudianteMedio=self.data_factory.estudianteMedio()

        resultado=self.logica.agregar_estudiante(estudianteApellidoPaterno,estudianteApellidoMaterno,estudianteNombres,estudianteMedio)

        self.assertEqual ( resultado , True )

    def test_agregar_estudiante1 ( self ) :
        self.data.append (
            (
                self.data_factory.unique.estudianteApellidoPaterno ( ) ,
                self.data_factory.unique.estudianteApellidoMaterno ( ) ,
                self.data_factory.estudianteNombres ( ),
                self.data_factory.estudianteMedio()
            )
        )
        resultado = self.logica.agregar_estudiante (
            estudianteApellidoPaterno = self.data[ -1 ][ 0 ] ,
            estudianteApellidoMaterno = self.data[ -1 ][ 1 ] ,
            estudianteNombres = self.data[ -1 ][ 2 ] ,
            estudiantemedio = self.data[ -1 ][ 3 ] )
        self.assertEqual ( resultado , True )