import pandas as pd
import pickle

#Dataset : https://www.kaggle.com/code/pratik1120/penguin-dataset-eda-classification-and-clustering/data
penguins = pd.read_csv("penguins_classification.csv")

df = penguins.copy()
#Ordinal Feature encoding
target = 'species'
encode = ['sex','island']

for i in encode:
    dummy = pd.get_dummies(df[i], prefix=i)
    df = pd.concat([df,dummy],axis=1)
    del df[i]

target_map = {'Adelie':0, 'Chinstrap':1, 'Gentoo':2}
def target_encode(val):
    return target_map[val]

df['species'] = df['species'].apply(target_encode)

#X and y
X = df.drop('species', axis= 1)
y =df.species

#build Model
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier()
#fit the model
clf.fit(X,y)

#Save the model
pickle.dump(clf,open('penguin_model.pkl','wb'))