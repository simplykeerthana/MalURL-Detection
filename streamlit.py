#Detecting malicious URL with hML

#Importing packages
import pandas as pd
import numpy as np
import streamlit as st
import random 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


#Loading URL Data
data = pd.read_csv("urldata.csv")
#check the type of data
type(data)

#check what the data contains
print(data.head())

#now let's vectorize using tfidVectorizer
## we have to create a token 

def createTokens(f):
    tkns_BySlash = str(f.encode('utf-8')).split('/')	# make tokens after splitting by slash
    total_Tokens = []
    for i in tkns_BySlash:
        tokens = str(i).split('-')	# make tokens after splitting by dash
        tkns_ByDot = []
        for j in range(0,len(tokens)):
            temp_Tokens = str(tokens[j]).split('.')	# make tokens after splitting by dot
            tkns_ByDot = tkns_ByDot + temp_Tokens
        total_Tokens = total_Tokens + tokens + tkns_ByDot
    total_Tokens = list(set(total_Tokens))	#remove redundant tokens
    if 'com' in total_Tokens:
        total_Tokens.remove('com')	#removing .com since it occurs a lot of times and it should not be included in our features
    return total_Tokens

#now we need to label 
y = data["label"]

#select feature
url_list = data["url"]

#custpm tokenizer
vectorizer = TfidfVectorizer(tokenizer=createTokens)

# Store vectors into X variable as Our XFeatures
x = vectorizer.fit_transform(url_list)

#the training and testing dataset is split by 80/20 ratio
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#now we need to build the model usinf regression logistic
logic = LogisticRegression(max_iter=3000)
logic.fit(x_train, y_train)

pickle.dump(logic, open('final_model.pkl', 'wb'))

#get the accuracy
print("Accuracy ", logic.score(x_test, y_test))
#now let's predict with our model
st.title("MalURL Dectection")


st.markdown('**Objective** : Given details about the url')
st.markdown('The model can predict if a url is malicious or not ')
st.markdown("**Please enter the url link that you want to check if it's malicios or not")
# def predict_class():
    
url = st.text_input('Enter url ')
# input_string = input('Enter elements of a list separated by space ')
print("\n")
user_list = url.split()
# print list
print('list: ', user_list)
# print('list: ', user_list)
if st.button("Predict"):
    X_predict1 = user_list
    print(list(X_predict1))
    X_predict1 = vectorizer.transform(X_predict1)
    New_predict1 = logic.predict(X_predict1)
    print(New_predict1)
    st.write("The predicted class is ",New_predict1)
    st.write("The accuracy is ",logic.score(x_test, y_test))




