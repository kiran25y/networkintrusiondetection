import streamlit as st
import xgboost as xgb
import numpy as np
# from xgboost.sklearn import XGBClassifier
import pickle


st.title("Network Intrusion prediction using ML")
st.subheader("This is an interactive dashboard which utilizes ML algorithms to predict if there is any attack.")

with st.form("form1",clear_on_submit=True):

    # col1,col2 = st.columns(2)

    st.write("Select the destination host server rerror rate")
    feature_1 = st.slider('',0.0,1.0,0.77,key='val_1')

    st.write("Select the  server rerror rate")
    feature_2 = st.slider('',0.0,1.0,0.77,key='val_2')
    #---------------------------

    st.write("Enter service")
    feature_3 = (st.text_input('',key='val_3'))

    st.write("Select protocol type ")
    feature_4 = st.selectbox('',(0,1,2),key='val_4')

    st.write("Enter destination host count ")
    feature_5 = (st.text_input('',key='val_5'))

    st.write("Enter count ")
    feature_6 = (st.text_input('',key='val_6'))

    st.write("Select flag type ")
    feature_7 = st.selectbox('',(0,1,2,3,4,5,6,7,8,9,10),key='val_7')

    st.write("Select the server serror rate")
    feature_8 = st.slider('',0.0,1.0,0.77,key='val_8')

    st.write("Select the serror rate")
    feature_9 = st.slider('',0.0,1.0,0.77,key='val_9')

    st.write("Select the destination host serror rate")
    feature_10 = st.slider('',0.0,1.0,0.77,key='val_10')

    st.write("Select the destination srv host serror rate")
    feature_11 = st.slider('',0.0,1.0,0.77,key='val_11')

    st.write("Check if logged in")
    feature_12 = st.selectbox('',(0,1),key='val_12')

    st.write("Select the destination host same serror rate")
    feature_13 = st.slider('',0.0,1.0,0.77,key='val_13')

    st.write("Select destination host srv count ")
    feature_14 = st.text_input('',key='val_14')

    st.write("Select same srv rate")
    feature_15 = st.slider('',0.0,1.0,0.77,key='val_15')


    submit = st.form_submit_button("\n\nSubmit this form")

    if submit:
        loaded_model = pickle.load(open('rf_model.pkl', 'rb'))
        X = np.array([[feature_1,feature_2,int(feature_3),feature_4,int(feature_5),int(feature_6),feature_7,feature_8,feature_9,feature_10,feature_11,feature_12,feature_13,int(feature_14),feature_15]])
        
        val = loaded_model.predict(X)[0]
        if val==0:
            st.write("Normal :) ")
        else:
            st.error("Warning ! Possible chances of attack")
        
    








