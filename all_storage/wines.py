from keras.backend import clear_session
clear_session()
import pandas as pd

df = pd.read_csv('wines.csv')

y=df["Class"]

y_cat = pd.get_dummies(y)

print(df.columns)

#features
X=df[['Alcohol', 'Malic_acid', 'Ash', 'Alcalinity_of_ash',
'Magnesium', 'Total_phenols', 'Flavanoids', 'Nonflavanoid_phenols',
'Proanthocyanins', 'Color_intensity', 'Hue',
'OD280-OD315_of_diluted_wines', 'Proline']]



print(X.head())




from keras.models import Sequential
#model
model  =  Sequential()






from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y_cat,test_size=0.3,random_state=50)


from keras.layers import Dense

model.add(Dense(units=50 , input_shape=(13,),
activation='relu',
kernel_initializer='glorot_uniform' ))

model.summary()

model.add(Dense(units=30,
activation='relu'))

model.summary()

model.add(Dense(units=20,
activation='relu'))

model.summary()

model.add(Dense(units=3, activation='softmax'))

model.summary()

from keras.optimizers import Adam

model.compile(optimizer=Adam(lr=0.001),
loss='categorical_crossentropy',
metrics=['accuracy']
)

model.fit(X_train,y_train,epochs=50)




y_pred=model.predict(X_test)

scores=model.evaluate(X_test,y_test)
print(scores[1])
y_pred.round()

y_test.values.astype("float64")



from keras.backend import clear_session
clear_session()





#ANN_wines.py
#ANN_wines.py