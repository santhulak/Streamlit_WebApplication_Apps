import pandas as pd
import numpy as np
import streamlit as st
import pickle
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Penguin Species Classification App
Data obtained from the [palmerpenguins library](https://github.com/allisonhorst/palmerpenguins) in R by Allison Horst.
""")

st.sidebar.header("User Input")
st.sidebar.markdown("""
[Example CSV File](https://raw.githubusercontent.com/santhulak/Streamlit_WebApplication_Apps/main/Penguin%20Classification%20Streamlit%20App/penguins_classification.csv)
""")
#upload your file in csv format
upload_file = st.sidebar.file_uploader("Upload your csv file", type=['csv'])

if upload_file is not None:
    input_df = pd.read_csv(upload_file)

else:
    def user_input():
        island = st.sidebar.selectbox('Island',('Biscoe','Dream','Torgersen'))
        sex = st.sidebar.selectbox('Sex',('male','female'))
        bill_length_mm = st.sidebar.slider('Bill Length(mm)',32.1,59.6,43.9)
        bill_depth_mm = st.sidebar.slider('Bill Depth(mm)',13.1,21.5,17.2)
        flipper_length_mm = st.sidebar.slider('Flipper Length(mm)',172.0,231.0,201.0)
        body_mass_g = st.sidebar.slider('Body Mass (g)', 2700.0,6300.0,4207.0)
        data = {'island':island,
                
                'bill_length_mm':bill_length_mm,
                'bill_depth_mm':bill_depth_mm,
                'flipper_length_mm':flipper_length_mm,
                'body_mass_g':body_mass_g,
                'sex':sex}
        features = pd.DataFrame(data, index=[0])
        return features
    input_df = user_input()

# combine user input features with the entire penguins dataset

penguin_raw = pd.read_csv('penguins_classification.csv')
penguin = penguin_raw.drop(columns=['species'])
df = pd.concat([input_df,penguin],axis=0)

#Encoding ordinal features
encode = ['sex','island']
for i in encode:
    dummy = pd.get_dummies(df[i], prefix=i)
    df = pd.concat([df,dummy],axis=1)
    del df[i]
    #selects only the first row
df =df[:1]

#Display the User input
st.subheader('User Input')

if upload_file is not None:
    st.write(df)
else:
    st.write('Awaiting csv file')
    st.write(df)

#load pickle model
loaded_model =pickle.load(open('penguin_model.pkl','rb'))

#Predict
prediction = loaded_model.predict(df)
prediction_prob = loaded_model.predict_proba(df)

st.subheader("Prediction")
penguins_species = np.array(['Adelie','Chinstrap','Gentoo'])
st.write(penguins_species[prediction])

st.subheader('Prediction Probability')
st.write(prediction_prob)