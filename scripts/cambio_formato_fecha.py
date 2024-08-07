from datetime import datetime
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

"""

Cambiar a formato de fecha

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




class Clustering:
    def __init__(self, dataframe, clusters, dataframeclustertets):
        self.dataframe=dataframe
        #self.user_code=user_code
        self.clusters=clusters
        self.dataframect=dataframeclustertets

    #def drop_user(self):
     #   self.dataframe=self.dataframe.drop(columns=self.user_code)

    def kmeans(self):
        optimal_k = 4
        kmeans = KMeans(n_clusters=optimal_k, random_state=0)
        self.dataframe[self.clusters]= kmeans.fit_predict(self.dataframe)
    
    def descalado(self):
        self.dataframe=pd.merge(self.dataframect, self.dataframe[self.clusters], left_index=True, right_index=True, how='inner')

    def ejec_Clustering(self):
        #self.drop_user()
        self.kmeans()
        self.descalado()
        #self.clusters_column()
        return self.dataframe
    



