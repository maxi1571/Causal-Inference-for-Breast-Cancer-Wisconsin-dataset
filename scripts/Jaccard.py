import pandas as pd
from causalnex.structure.notears import from_pandas
from sklearn.preprocessing import LabelEncoder
df = pd.read_csv("../data/data.csv")
df['diagnosis'] = LabelEncoder().fit_transform(df["diagnosis"])
causal_df = df[['diagnosis','area_mean', 'concavity_mean', 'concave points_mean', 'radius_worst',
       'perimeter_worst', 'area_worst', 'concavity_worst'
                    ,'concave points_worst']].copy()
def jaccard_similarity_index(g, h):

    i = set(g).intersection(h)
    return round(len(i) / (len(g) + len(h) - len(i)),3)

def Jaccar_score(g, h):    
    i = set(g).intersection(set(h))
    u = set(g).union(set(h))
    return len(i) / float(len(u))

df_1 = causal_df.iloc[:150,:]
df_2 = causal_df.iloc[:300,:]
sm_df1 = from_pandas(df_1, w_threshold=0.8)
sm_df2 = from_pandas(df_2, w_threshold=0.8)

print("jaccard_similarity_index : "+str(jaccard_similarity_index(sm_df1.edges(), sm_df2.edges())))
print("Jaccar_score : "+ str(Jaccar_score(sm_df1.edges(), sm_df2.edges())))