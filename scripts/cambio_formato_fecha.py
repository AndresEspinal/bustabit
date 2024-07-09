from datetime import datetime

"""

Cambiar a formato de fecha

"""

class DateFormat ():

    def __init__(self, columna, dataframe):
        self.columna=columna
        self.dataframe=dataframe

    def fecha(self):
        self.dataframe[self.columna]=self.dataframe[self.columna].apply(lambda x: datetime.fromisoformat(x.replace('Z','+00:00')))
        return self.columna
    
    
