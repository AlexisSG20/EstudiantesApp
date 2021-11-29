import random
from datetime import datetime
from datetime import timedelta
from src.modelo.album import Medio
from faker import Faker
from faker.providers import BaseProvider

class EstudianteApellidoPaternoProvider(BaseProvider):
    def estudianteApellidoPaterno(self):
        estudiantesApellidoPaterno = ['Gonzales', 'Lopez', 'Ramirez', 'Soto']
        return random.choice(estudiantesApellidoPaterno)

class EstudianteApellidoMaternoProvider(BaseProvider):
    def estudianteApellidoMaterno(self):
        estudiantesApellidoMaterno = ['Morales', 'Gomez', 'Quispe', 'Bernaola']
        return random.choice(estudiantesApellidoMaterno)

class EstudianteNombresProvider(BaseProvider):
    def estudianteNombres(self):
        estudiantesNombres = ["Maria", "Juan","Jose","Esteban"]
        return random.choice(estudiantesNombres)

class EstudianteMedioProvider(BaseProvider):
    def estudianteMedio(self):
        self.medios = [ Medio.NOTA, Medio.CICLO, Medio.GRADO]
        return random.choice(self.medios)

class EstudianteFechaProvider(BaseProvider):
    def EstudianteFecha(self):
        new_date = datetime(2015,2016,2015,2018,2016)
        fecha = [new_date, new_date + timedelta(days=-1), new_date + timedelta(days=-2)]
        return random.choice(fecha)
