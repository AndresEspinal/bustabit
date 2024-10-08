from datetime import datetime
import numpy as np


"""

Cambiar a formato de fecha, imputación, nueva columna y eliminación de columnas

"""

class DateFormat:

    def __init__(self, columna, dataframe, porcentaje, profit, bet, co, result, dropid, dropgameid):
        self.date_columna=columna
        self.dataframe=dataframe
        self.porc_columna=porcentaje
        self.prof_columna=profit
        self.bet_columna=bet
        self.co_columna=co
        self.result_columna=result
        self.drop_id=dropid
        self.drop_gameid=dropgameid


    def fecha(self):
        self.dataframe[self.date_columna]=self.dataframe[self.date_columna].apply(lambda x: datetime.fromisoformat(x.replace('Z','+00:00')))
        return self.date_columna
    
    def porcentaje(self):
        self.dataframe[self.porc_columna]=self.dataframe[self.porc_columna]/100
        return self.porc_columna

    def imputacion(self):
        self.dataframe[self.prof_columna].fillna(-self.dataframe[self.bet_columna], inplace=True)
        self.dataframe[self.porc_columna].fillna(0, inplace=True)
        self.dataframe[self.co_columna].fillna(0, inplace=True)
        return self.dataframe

    def new_column(self):
        self.dataframe[self.result_columna] = np.where(self.dataframe[self.prof_columna] > 0, 1, 0)
        return self.dataframe
    
    def dropcolumns(self):
        self.dataframe=self.dataframe.drop(columns=[self.drop_id, self.drop_gameid], axis=1)
    
    def ejec_dateformat(self):
        self.fecha()
        self.porcentaje()
        self.imputacion()
        self.new_column()
        self.dropcolumns()
        return self.dataframe
        






    



