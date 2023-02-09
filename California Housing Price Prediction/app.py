import streamlit as st
import pickle
import pandas as pd


def main():
    style = """<div style='background-color:#12164F; padding:12px'>
              <h1 style='color:white'><center>House Price Prediction App</center></h1>
       </div>"""
    st.markdown(style, unsafe_allow_html=True)
    left, right = st.columns((2,2))
    longitude = left.number_input('Enter the Longitude in negative number',
                                  step =1.0, format="%.2f", value=-21.34)
    latitude = right.number_input('Enter the Latitude in positive number',
                                  step=1.0, format='%.2f', value= 35.84)
    housing_median_age = left.number_input('Enter the median age of the building',
                                           step=1.0, format='%.1f', value=25.0)
    total_rooms = right.number_input('How many rooms are there in the house?',
                                     step=1.0, format='%.1f', value=56.0)
    total_bedrooms = left.number_input('How many bedrooms are there in the house?',
                                       step=1.0, format='%.1f', value=15.0)
    population = right.number_input('Population of people within a block',
                                    step=1.0, format='%.1f', value=250.0)
    households = left.number_input('Poplulation of a household',  step=1.0,
                                   format='%.1f',value=43.0)
    median_income = right.number_input('Median_income of a household in Dollars',
                                       step=1.0, format='%.1f', value=3000.0)    
    ocean_proximity = st.selectbox('How close to the sea is the house?',
                    ('<1H OCEAN', 'INLAND', 'NEAR OCEAN', 'NEAR BAY', 'ISLAND'))
    button = st.button('Predict')
    
    # if button is pressed
    if button:
        
        # make prediction
        result = predict(longitude, latitude, housing_median_age,
                         total_rooms,total_bedrooms, population,
                         households, median_income, ocean_proximity)
        st.success(f'The value of the house is ${result}')

#load the train model
with open('rf_model.pkl','rb') as rf:
    model = pickle.load(rf)

#load the standard scaler
with open('std_scale_model.pkl','rb') as std:
    scaler = pickle.load(std)
    
def predict(longitude, latitude, housing_median_age,
                         total_rooms,total_bedrooms, population,
                         households, median_income, ocean_pro):
    ocean = 0 if ocean_pro == '<1H OCEAN' else 1 if ocean_pro == 'INLAND' else 2 if ocean_pro == 'ISLAND' else 3 if ocean_pro == 'NEAR BAY' else 4
    med_income = median_income / 5
    lists = [longitude, latitude, housing_median_age, total_rooms,
             total_bedrooms, population, households, med_income, ocean]
    
    df = pd.DataFrame(lists).transpose()
    # scaling the data
    scaler.transform(df)
    # making predictions using the train model
    prediction = model.predict(df)
    result = int(prediction)
    return result

if __name__ == '__main__':
    main()