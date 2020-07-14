import numpy as np 
import pandas as pd 
import pickle

from sklearn.neighbors import KNeighborsClassifier


# Read the csv file and convert it to numpy array
df_train = pd.read_csv('app/model/mnist_train.csv')
df_train = df_train.sample(30000, replace=False)
X_train = df_train.iloc[:, 1:].values.astype('float32')
y_train = df_train['label'].values

print("The shape of X_train: ", X_train.shape)
print("The shape of y_train: ", y_train.shape)

# Read the csv file and convert it to numpy array
df_test = pd.read_csv('app/model/mnist_test.csv')
X_test = df_test.iloc[:, 1:].values.astype('float32')
y_test = df_test['label'].values

print("The shape of X_test: ", X_test.shape)
print("The shape of y_test: ", y_test.shape)

# Normalize the data
X_train /= 255
X_test /= 255

# Train the model
model = KNeighborsClassifier(n_neighbors=5, weights='distance', n_jobs=-1).fit(X_train, y_train)

# Score evaluation
score = model.score(X_test, y_test)
print("The score on testset: ", score)

# Save the model
filename = 'app/model/finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))