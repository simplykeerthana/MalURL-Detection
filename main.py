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

# now get a list of malwaare urls to test. 
X_predict = ['google.com/search=jcharistech',
'google.com/search=faizanahmad',
'pakistanifacebookforever.com/getpassword.php/', 
'www.radsport-voggel.de/wp-admin/includes/log.exe', 
'ahrenhei.without-transfer.ru/nethost.exe',
'www.itidea.it/centroesteticosothys/img/_notes/gum.exe']

X_predict = vectorizer.transform(X_predict)
New_predict = logic.predict(X_predict)
print(New_predict)

X_predict1 = ['www.buyfakebillsonlinee.blogspot.com', 
'www.unitedairlineslogistics.com',
'www.stonehousedelivery.com',
'www.silkroadmeds-onlinepharmacy.com' ]

X_predict1 = vectorizer.transform(X_predict1)
New_predict1 = logic.predict(X_predict1)
print(New_predict1)


