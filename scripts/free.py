import pandas as pd

class DataFrameModifier ():
    def __init__(self, dataframe, date_column):
        self.dataframe = dataframe.copy()
        self.date_column = date_column

    def modify_dataframe(self):
        # Convertir la columna de fecha a tipo datetime
        self.dataframe[self.date_column] = pd.to_datetime(self.dataframe[self.date_column])

        # Extraer año, mes, día y hora
        self.dataframe['year'] = self.dataframe[self.date_column].dt.year
        self.dataframe['month'] = self.dataframe[self.date_column].dt.month
        return self.dataframe
        