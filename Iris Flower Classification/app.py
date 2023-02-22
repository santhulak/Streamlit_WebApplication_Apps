import pandas as pd
import streamlit as st
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Iris Flower Prediction App
""")

st.sidebar.header("User Input Parameters")

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal Length',4.3, 7.9, 5.4)
    sepal_width =st.sidebar.slider('Sepal Width', 2.0, 4.4, 3.4 )
    petal_length = st.sidebar.slider('Petal Length', 1.0,6.9,1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1,2.5,0.2)
    data = {'sepal_length':sepal_length,
            'sepal_width':sepal_width,
            'petal_length':petal_length,
            'petal_width':petal_width
            }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader("User Input Parameters")
st.write(df)

#Loading the dataset
iris = datasets.load_iris()

# Store the data as independent and dependent variable
X = iris.data
y = iris.target

clf = RandomForestClassifier()
clf.fit(X,y)

prediction = clf.predict(df)
predict_prob = clf.predict_proba(df)


# st.subheader('Class Labels With Index Numbers')
# st.write(iris.target_names)

col1,col2 = st.columns(2)
with col1:
    st.subheader('Prediction')
    st.write(iris.target_names[prediction])

with col2:
    st.subheader('Prediction Probability')
    st.write(predict_prob)