
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import datetime
import joblib 

st.set_page_config(
    page_title="Stream",
    page_icon="😊"
)

st.header("😊 Input something please")

# User-defined inputs
st.subheader("Define the question here")

# Here you can read in some pretrained model or parameters as you want
#scaler = joblib.load('folder_path/scaler.save')
#model = joblib.load('folder_path/lgbm_reg.joblib')

# First row of inputs
col1, col2, col3, col4 = st.columns(4)

feature_01 = col1.date_input('Date', min_value=datetime.date(2019,1,1), max_value=datetime.date(2024,1,1), value=datetime.date(2020, 1, 1), key="date")

# Read in some external data if necessary
#data = pd.read_json('map_postal_codes.json')

feature_02 = col2.text_input("The postal codes", value = "75002", max_chars=5, placeholder="e.g. 75002")
feature_03 = col3.text_input("The section codes", value = "AI", max_chars=2, placeholder="e.g. CE")

# Second row of inputs
col5, col6, col7, col8 = st.columns(4)

feature_4 = col4.number_input('Parameter 4', min_value = 0, value=1, step=1) #
feature_5 = col5.number_input('Parameter 5', value=3, min_value = 0, step=1, help="Add some examples here")
feature_6 = col6.slider('Parameter 6', min_value=9, max_value=250, value=33, step=1)
feature_7 = col7.number_input('Parameter 7', value=1, min_value=0, step=1, help="Add some examples here")



# User-defined inputs
st.subheader("Here is the output of your expected results")

# You can define the model prediction you trained here if needed
if st.button("Predict"):
    print('Bingo!')
else:
    pass
'''
@st.experimental_memo
def modelpredict(feature_1, feature_2, feature_3, feature_4, feature_5, feature_6, feature_7):
    dict_features = {'A': [feature_1], 
    'B': [feature_2],
    'C': [feature_7],
    'D': [feature_6],
    'E': [feature_3],
    'F': [feature_4],
    'G': [feature_5]}

    
    X_test = pd.DataFrame(dict_features)
    
    # Scale our training data to the [min, max] range
    X_test_scaled = scaler.transform(X_test)

    # Make the prediction
    prediction = model.predict(X_test_scaled)
    return prediction

if st.button("Predict"):
    # Predict the result with the model
    modelpredict.clear()
    prediction = modelpredict(feature_1, feature_2, feature_3, feature_4, feature_5, feature_6, feature_7)

    # Output the prediction result
    st.write("The prediction result is: ")
    st.markdown(
    f"""
    <div 
        style="
            background-color: #f9f9f9; 
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 10px;
        "
    >
        {prediction[0]}
    </div>
    """,
    unsafe_allow_html=True
    )

    # Plot the trend of median house price per m2 in the past 90 days
    # Disable the warning
    st.set_option('deprecation.showPyplotGlobalUse', False)
    traindir = "path/csvs"

    # get the list of all CSV files in the directory
    csv_files = [f for f in os.listdir(traindir) if f.endswith('.csv')]

    # You can define a new function here to plot the result
'''
