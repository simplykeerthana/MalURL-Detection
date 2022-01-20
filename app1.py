import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.utils import check_array
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

from model_methods import predict
classes = {0:'url',1:'label'}
class_labels = list(classes.values())
st.title("MalURL Dectection")


st.markdown('**Objective** : Given details about the url')
st.markdown('The model can predict if a url is malicious or not ')
# def predict_class():
#     data = scaler.transform([[url]])
#     result = predict(data)
#     st.write("The predicted class is ",result)
#     # probs = [np.round(x,6) for x in probs]
#     # ax = sns.barplot(probs ,class_labels, palette="winter", orient='h')
#     # ax.set_yticklabels(class_labels,rotation=0)
#     # plt.title("Probabilities of the Data belonging to each class")
#     # for index, value in enumerate(probs):
#     #     plt.text(value, index,str(value))
#     # st.pyplot()
# st.markdown("**Please enter the url link that you want to check if it's malicios or not")
# url = st.text_input('Enter url', '')
# if st.button("Predict"):
#     predict_class()

data = st.text_input("Enter the url", '')
check_array([[data]], dtype='numeric')
data.reshape(1, -1)
print(type(data))

if(st.button('Submit')):
    result = predict([[int(data)]])
    print(type(result))
    st.success(result)

