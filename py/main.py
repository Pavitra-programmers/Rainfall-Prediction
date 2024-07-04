import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score
import pickle


#reading the csv dataset
df = pd.read_csv('datasets\weatherAUS.csv')
#removed useless columns
x = df.iloc[:,[1,2,3,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]].values
Y = df.iloc[:,[-1]].values
y = Y.reshape(-1,1)

#imputing the data
imputer = SimpleImputer(missing_values=np.nan, strategy="most_frequent")
x = imputer.fit_transform(x)
y = imputer.fit_transform(y)

#encoding
lb1 = LabelEncoder()
x[:,0] = lb1.fit_transform(x[:,0])
lb2 = LabelEncoder()
x[:,4] = lb2.fit_transform(x[:,4])
lb3 = LabelEncoder()
x[:,6] = lb2.fit_transform(x[:,6])
lb4 = LabelEncoder()
x[:,7] = lb2.fit_transform(x[:,7])
lb5 = LabelEncoder()
x[:,-1] = lb5.fit_transform(x[:,-1])
lb6 = LabelEncoder()
y = lb6.fit_transform(y)



#feature scaling
sc = StandardScaler()
x = sc.fit_transform(x)

# splitting training and testing data 
x_train, x_test, y_train ,y_test = train_test_split(x,y,test_size=0.85,random_state=0)

#training the model

rf = RandomForestClassifier()
rf.fit(x_train,y_train)
res = rf.predict(x_test)
print(accuracy_score(y_test,res), recall_score(y_test,res), precision_score(y_test,res), f1_score(y_test,res))

# saving the model
pick = open('RFCrainfallmodel.sav','wb')
pickle.dump(rf,pick)
pick.close()





