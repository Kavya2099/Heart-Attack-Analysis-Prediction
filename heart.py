import pickle
import streamlit as st
import pandas as pd
import xgboost

#from streamlit_option_menu import option_menu

# loading the saved model

price_model = pickle.load(open('finalized_model_classification.sav', 'rb'))


# page title
st.title('Heart Attack Prediction using ML')

st.markdown(
    """
    <style>
    .reportview-container {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .main .block-container {
        flex: 1;
        max-width: 800px;
        padding-top: 5rem;
        padding-right: 2rem;
        padding-left: 2rem;
        padding-bottom: 5rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f'<div style="display: flex; justify-content: center;"><img src="https://media.tenor.com/91scJf-xrKEAAAAi/emoji-coraz%C3%B3n-humano.gif" width="200"></div>', 
    unsafe_allow_html=True,
)

#st.image("https://media.tenor.com/91scJf-xrKEAAAAi/emoji-coraz%C3%B3n-humano.gif", width=200)

age = st.number_input('Enter age',step=1)
sex = st.selectbox('Enter sex', ('Male', 'Female'))
sex = 1 if sex == 'Male' else 0
st.write("Chest Pain type \n\n Value 0: typical angina \n\n Value 1: atypical angina \n\n Value 2: non-anginal pain \n\n Value 3: asymptomatic trtbps : resting blood pressure (in mm Hg)")
#cp = st.number_input('Enter Chest Pain type',step=1)
cp = st.selectbox('Enter Chest Pain type', (0,1,2,3))
#cp = 1 if cp == '1' else 0
trtbps = st.number_input('Enter resting blood pressure value',step=1)
chol = st.number_input('Enter cholestoral value(cholestoral in mg/dl fetched via BMI sensor)',step=1)
fbs = st.selectbox('Is fasting blood sugar > 120 mg/dl', ('Yes', 'No'))
fbs = 1 if fbs == 'Yes' else 0
#fbs = st.number_input('Enter fbs value((fasting blood sugar > 120 mg/dl) (1 = true; 0 = false))',step=1)
st.write("Resting Electrocardiographic Results \n\nValue 0: normal \n\n Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV) \n\nValue 2: showing probable or definite left ventricular hypertrophy by Estes' criteria thalach : maximum heart rate achieved)")
restecg = st.selectbox('Enter Resting Electrocardiographic Results value', (0,1, 2))
#restecg = st.number_input("Enter restecg value(resting electrocardiographic results: Value 0: normal Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV) Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria thalach : maximum heart rate achieved)",step=1)
thalachh = st.number_input("The person's maximum heart rate achieved",step=1)
exng=st.selectbox('Enter exercise induced angina value', ('Yes', 'No'))
exng = 1 if exng == 'Yes' else 0
oldpeak = st.number_input('Enter oldpeak(ST depression caused by activity compared to rest) value')
st.write("the slope of the peak exercise ST segment — \n\n 0: downsloping; \n\n 1: flat; \n\n 2: upsloping")
slp = st.selectbox('Enter slope of the peak exercise ST segment value',(0,1,2))
caa = st.selectbox('Enter caa(coronary artery anomaly) value(number of major vessels (0-3))',(0,1,2,3))
thall = st.selectbox('Enter thalassemia value',(0,1,2,3))


features=['thall','caa','cp','oldpeak','exng','chol','thalachh']

if st.button('Predict'):

    data_1 = pd.DataFrame({'thall': [thall],
            'caa': [caa],
            'cp': [cp],
            'oldpeak': [oldpeak],
            'exng': [exng],
            'chol': [chol],
            'thalachh': [thalachh]
        })


    prediction = price_model.predict(data_1)
    if prediction == 0:
        #st.write('Patient has no risk of Heart Attack')
        st.markdown("<h2 style='text-align: center; color: green;'>Patient has no risk of Heart Attack</h2>", unsafe_allow_html=True)
    else:
        #st.write('Patient has risk of Heart Attack')
        st.markdown("<h2 style='text-align: center; color: red;'>Patient has risk of Heart Attack</h2>", unsafe_allow_html=True)
