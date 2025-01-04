# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 19:49:26 2025

@author: shukl
"""

import numpy as np
import streamlit as st
import pickle

#loading the saved model
loaded_model=pickle.load(open("D:/GLA University MCA/MCA SEM 3 MINI PROJECT/DATASETS/trained_model.sav",'rb'))

#Creating a function for Prediction

def diabetes_prediction(input_data):

    #changing the input_data to a numpy array

    input_data_as_numpy_array=np.asarray(input_data)

    #reshaping the array as we're predicting for one instance

    input_data_reshape=input_data_as_numpy_array.reshape(1,-1)

    prediction=loaded_model.predict(input_data_reshape)
    print(prediction)

    if (prediction[0]==0):
      return "The person is not diabetic"
    else:
      return 'The person is diabetic'
  

def main():
    
    #giving a title
    st.title("Diabetes Prediction Web App")
    
    #getting the input data from the user
    Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome
    
    Pregnancies=st.text_input('Number Of Pregnancies')
    Glucose=st.text_input('Glucose Level')
    BloodPressure=st.text_input('Blood Pressure Value')
    SkinThickness=st.text_input('Skin Thickness value')
    Insulin=st.text_input('Insulin value')
    BMI=st.text_input('BMI value')
    DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function value')
    Age=st.text_input('Age of the person')
    
    #code for prediction
    diagnosis=''
    
    #creating a button for prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis=diabetes_prediction([Pregnancies,Glucose,BloodPressure,
                                       SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
    st.success(diagnosis)
    
    if __name__=='__main__':
        main()
    
        
        
        
        
        