from datetime import datetime

"""

Cambiar a formato de fecha

"""

class date_format ():

    def __init__(self, columna):
        self.columna=columna

    def fecha(self):
        self.columna=self.columna.apply(lambda x: datetime.fromisoformat(x.replace('Z','+00:00')))
        return self.columna
    
