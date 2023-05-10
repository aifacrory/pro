import pickle
import streamlit as st
from streamlit_option_menu import option_menu


def add_bg_from_url():
     st.markdown(
          f"""
         <style>
          .stApp {{
              background-image: url("image.jpg");
              background-attachment: fixed;
              background-size: cover
          }}
         </style>
          """,
          unsafe_allow_html=True
      )

# add_bg_from_url() 

# import base64
# def add_bg_from_local(image_file):
#     with open(image_file, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read())
#     st.markdown(
#     f"""
#     <style>
#     .stApp {{
#         background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
#         background-size: cover
#     }}
#     </style>
#     """,
#     unsafe_allow_html=True
#     )
# add_bg_from_local('image.jpg')    
#load the models

diabetes_model=pickle.load(open("trained_model02.sav",'rb'))
heart_model=pickle.load(open("trained_model01.sav",'rb'))
parkinson_model=pickle.load(open("trained_model03.sav","rb"))
with st.sidebar:
    selected=option_menu('MULTIPLE DISEASE PREDICTION WEB APP',
                         ['Diabetic Prediction',
                         'Heart Prediction',
                         'parkinson prediction'],
                         icons=['activity','heart','person'],
                         default_index=0)

if (selected=='Diabetic Prediction'):
    st.title('DIABETES DISEASE PREDICTION')
    col11,col12,col13=st.columns(3)
    with col11:
        Pregnancies=st.text_input('Pregnancies')
    with col12:
        Glucose=st.text_input('Glucose Level')
    with col13:
         BloodPressure=st.text_input('BloodPressure Level')
    with col11:
        SkinThickness=st.text_input('SkinThickness')
    with col12:
        Insulin=st.text_input('Insulin Level')
    with col13:
        BMI=st.text_input('BMI')
    with col11:
        DiabetesPedigreeFunction=st.text_input('DiabetesPedigreeFunction Value')
    with col12:
        Age=st.text_input('Age of the Person')

    dia_diagonsis=''

    if st.button('Diabetic disease result'):
        dia_pred=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])

        if (dia_pred[0]==0):
            dia_diagonsis='the person does not have diabetic disease'
        else:
            dia_diagonsis='the person have diabetic disease'
        st.success(dia_diagonsis)

#heart disease prediction section
if (selected=='Heart Prediction'):
    st.title('HEART DISEASE PREDICTION')
    col11,col12,col13=st.columns(3)
    with col11:
        age=st.number_input('Age of the person')
    with col12:
        sex=st.number_input('sex')
    with col13:
        cp=st.number_input('cp value')
    with col11:
        trestbps=st.number_input(' trestbps Value')
    with col12:
        chol=st.number_input('chol Value')
    with col13:
        fbs=st.number_input('fbs Value')
    with col11:
        restecg=st.number_input('restecg Value')
    with col12:
        thalach=st.number_input('thalach Value')
    with col13:
        exang=st.number_input('exang Value')
    with col11:
        oldpeak=st.number_input('oldpeak Value')
    with col12:
        slope=st.number_input('slope Value')
    with col13:
        ca=st.number_input('ca Value')
    with col11:
        thal=st.number_input('thal Value')

    heart_diagonsis=''

    if st.button('Heart disease result'):
        heart_pred=heart_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])

        if (heart_pred[0]==0):
               heart_diagonsis='the person does not have heart disease'
        else:
            heart_diagonsis='the person have heart disease'
        st.success(heart_diagonsis)
    
if (selected=='parkinson prediction'):
    st.title('PARKINSON DISEASE PREDICTION')
    col11,col12,col130,col140=st.columns(4)
    with col11:
        col1=st.number_input('MDVP Fo(Hz)')
    with col12:
        col2=st.number_input('MDVP Fhi(Hz)')
    with col130:
        col3=st.number_input('MDVP Flo(Hz)')
    with col140:
        col4=st.number_input('MDVP Jitter(%)')
    with col11:
        col5=st.number_input('MDVP Jitter(Abs)')
    with col12:
        col6=st.number_input('MDVP RAP')
    with col130:
        col7=st.number_input('MDVP PPQ')
    with col140:
        col8=st.number_input('Jitter DDP')
    with col11:
        col9=st.number_input('MDVP Shimmer')
    with col12:
        col10=st.number_input('MDVP Shimmer(dB)')
    with col130:
        col111=st.number_input('Shimmer APQ3')
    with col140:
        col122=st.number_input('Shimmer APQ5')
    with col11:
        col13=st.number_input('MDVP APQ')
    with col12:
        col14=st.number_input('Shimmer DDA')
    with col130:
        col15=st.number_input('NHR')
    with col140:
        col16=st.number_input('HNR')
    with col11:
        col17=st.number_input('RPDE')
    with col12:
        col18=st.number_input('DFA')
    with col130:
        col19=st.number_input('spread1')
    with col140:
        col20=st.number_input('spread2')
    with col11:
        col21=st.number_input('D2')
    with col12:
        col22=st.number_input('PPE')

    parkinson_diagonsis=''

    if st.button('Parkinson disease result'):
        parkinson_pred=parkinson_model.predict([[col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19,col20,col21,col22]])
        if (parkinson_pred[0]==0):
               parkinson_diagonsis='the person does not have heart disease'
        else:
            parkinson_diagonsis='the person have heart disease'
        st.success(parkinson_diagonsis)

















































    