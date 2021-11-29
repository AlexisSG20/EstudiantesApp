from faker import Faker
import random
import unittest
from src.logica.coleccion import Coleccion
from src.modelo.estudiante import Estudiante, Medio
from src.modelo.seccion import Seccion, EstudianteSeccion
from src.modelo.profesor import Profesor
from src.modelo.declarative_base import Session

class EstudianteTestCase(unittest.TestCase):
    def setUp(self):
        '''Crea una colección para hacer las pruebas'''
        self.coleccion = Coleccion()

        '''Abre la sesión'''
        self.session = Session()

        '''Crea una instance de Faker'''
        self.data_factory = Faker ( )

        '''Se programa para que Faker cree los mismos datos cuando se ejecuta'''
        Faker.seed ( 1000 )

        '''Genera 10 datos en data y creamos los estudiantes'''
        self.data = [ ]
        self.estudiantes = [ ]
        self.medios = [ Medio.NOTA , Medio.CICLO , Medio.GRADO ]
        for i in range ( 0 , 10 ) :
            self.data.append ( (
                self.data_factory.unique.name ( ) ,
                self.data_factory.random_int ( 1800 , 2021 ) ,
                self.data_factory.text ( ) ,
                random.choice ( self.medios )) )
            self.estudiantes.append (
                Estudiante (
                    ApellidoPaterno = self.data[ -1 ][ 0 ] ,
                    ApellidoMaterno = self.data[ -1 ][ 1 ] ,
                    Nombres = self.data[ -1 ][ 2 ] ,
                    medio = self.data[ -1 ][ 3 ] ,
                    secciones = [ ]
                ) )
            self.session.add ( self.estudiantes[ -1 ] )

        '''Persiste los objetos
        En este setUp no se cierra la sesión para usar los estudiantes en las pruebas'''
        self.session.commit ( )

    def tearDown(self) :
        self.session = Session ( )
        busqueda = self.session.query ( Album ).all ( )

        for estudiante in busqueda :
            self.session.delete ( estudiante )

        self.session.commit ( )
        self.session.close ( )

    def test_constructor(self):
        for estudiante, dato in zip(self.estudiantes, self.data):
            self.assertEqual(estudiante.ApellidoPaterno, dato[0])
            self.assertEqual(estudiante.ApellidoMaterno, dato[1])
            self.assertEqual(estudiante.nombres, dato[2])
            self.assertEqual(estudiante.medio, dato[3])

    def test_agregar_estudiante ( self ) :
        '''Prueba la adición de un estudiante'''

        self.data.append ( (self.data_factory.unique.name ( ) , self.data_factory.random_int ( 1800 , 2021 ) ,
                            self.data_factory.text ( ) , random.choice ( self.medios )) )
        resultado = self.coleccion.agregar_estudiante (
            ApellidoPaterno = self.data[ -1 ][ 0 ] ,
            ApellidoMaterno=self.data[-1][1],
            Nombres = self.data[ -1 ][ 2 ] ,
            medio = self.data[ -1 ][ 3 ] )
        self.assertEqual ( resultado , True )