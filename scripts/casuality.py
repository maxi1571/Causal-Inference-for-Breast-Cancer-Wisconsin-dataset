import pandas as pd
from causalnex.plots import plot_structure, NODE_STYLE, EDGE_STYLE
from causalnex.structure.notears import from_pandas, from_pandas_lasso
from causalnex.structure import StructureModel
from IPython.display import Image
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.simplefilter(action='ignore', category=Warning)



class casuality:

    def __init__(self, df):
        self.df = df


    def jaccard_similarity(g, h):

        i = set(g).intersection(h)
        return round(len(i) / (len(g) + len(h) - len(i)),3)

    def get_connect(self, sm, parent_node:str):
    
        sm_tuple = list(sm.edges)
        sm_list = [list(tuple) for tuple in sm_tuple]
        Diagnosis_edge = []
        feature_list = []
        for i in sm_list:
            if i[0]==parent_node or i[1]==parent_node:
                if i[0]!=parent_node:
                    feature_list.append(i[0])
                else:feature_list.append(i[1])  
                Diagnosis_edge.append(i)
            else:continue
        return feature_list
    
    def create_sm(self):

        sm = StructureModel()
        sm = from_pandas(self.df, w_threshold=0.8)

    def visualize(self,sm):

        viz = plot_structure(
            sm,
            graph_attributes={"scale": "2"},
            all_node_attributes=NODE_STYLE.WEAK,
            all_edge_attributes=EDGE_STYLE.WEAK)
        Image(viz.draw(format='png'))  

    def get_similarity(self):

        sm = StructureModel()
        sm = from_pandas(self.df, w_threshold=0.8)

        edges = []
        similarity = []
        sm_total = [sm]
        count = 0
        cor = {0:9, 1:8, 2:7, 3:6, 4:5, 5:4, 6:3, 7:2, 8:1}

        for i in range(3, 0, -1):
                
            df_ = self.df.head(int(i*0.25*len(self.df)))
            sm1 = StructureModel()
            sm1 = from_pandas(df_, w_threshold=0.8)
            sm_total.append(sm1)
            
            if i == 3:
                similarity.append(self.jaccard_similarity(sm.edges(),sm1.edges()))
                edges.append(sm1.edges())
                continue
                
            similarity.append(self.jaccard_similarity(edges[count], sm1.edges()))
            count+=1
            edges.append(sm1.edges())

        sm_final = sm_total[cor[similarity.index(max(similarity))]]

        return sm_final

