import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.utils import check_array
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

# Python program to convert a list to strin

from model_methods import predict
classes = {0:'url',1:'label'}
class_labels = list(classes.values())
st.title("MalURL Dectection")


st.markdown('**Objective** : Given details about the url')
st.markdown('The model can predict if a url is malicious or not ')
def predict_class():
    scaler.fit([[user_list]])
    data = scaler.transform([[url]])
    result = predict(data)
    st.write("The predicted class is ",result)
st.markdown("**Please enter the url link that you want to check if it's malicios or not")
url = st.text_input('Enter elements of a list separated by space ')
print("\n")
user_list = url.split()
print('list: ', user_list)

# print('list: ', user_list)
if st.button("Predict"):
    predict_class()

# # data = st.text_input("Enter the url", "")
# input_string = st.text_input('Enter elements of a list separated by space ')
# print("\n")
# user_list = input_string.split()
# # print list
# print('list: ', user_list)

# # data = data.lower()

# # output = []
# # for character in data:
# #     number = ord(character) - 96
# #     output.append(number)

# # print(output)
# # # Driver code	

# # # print(listToString(output))

# sampledata = ['100', '20', '30']



# if(st.button('Submit')):
#     result = predict([[user_list]])
#     print(type(result))
#     st.success(result)

