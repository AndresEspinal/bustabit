import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

"""
Agrupamiento de clientes y escalamiento
"""

class GroupbyCostumers:

    def __init__(self, dataframe, columna, user_code, bet, co, porcentaje, profit, bustedat, result):
        self.dataframe=dataframe
        self.date_columna=columna
        self.user_code=user_code
        self.bet_columna=bet
        self.co_columna=co
        self.porc_columna=porcentaje
        self.prof_columna=profit
        self.ba=bustedat
        self.result_columna=result
        #self.clustertest=clustertest
        #self.dataframemm=dataframemm


    def dropcolumns(self):
        self.dataframe=self.dataframe.drop(columns=[self.date_columna], axis=1)

    def group_by(self):
        self.dataframe=self.dataframe.groupby(self.user_code).agg({self.bet_columna:'mean',self.co_columna:'mean',self.porc_columna:'mean', self.prof_columna:'sum',self.ba:'mean',self.result_columna:'sum'}).reset_index()

    def minmaxscaler(self):
        scaler = MinMaxScaler()
        a=scaler.fit_transform(self.dataframe[[self.bet_columna, self.co_columna, self.porc_columna, self.prof_columna, self.ba, self.result_columna]])
        self.dataframe= pd.DataFrame(a, columns=[self.bet_columna, self.co_columna, self.porc_columna, self.prof_columna, self.ba, self.result_columna])

    def ejec_GroupByCustomer(self):
        self.dropcolumns()
        self.group_by()
        self.minmaxscaler()
        return self.dataframe