
from sklearn.cluster import KMeans
import pandas as pd


"""
Clusterización por kmeans
"""


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