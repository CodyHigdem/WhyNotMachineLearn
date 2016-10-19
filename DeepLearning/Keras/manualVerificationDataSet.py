
# train_test_split() from scikit-learn to train and test datasets. 
# this requires determining percenategs of training vs testing
# manual verification of datasets
from keras.models import Sequential
from keras.layers import Dense
from sklearn.cross_validation import train_test_split
import numpy
import urllib
#fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
#load pima indians dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
raw_data = urllib.urlopen(url)
dataSet = numpy.loadtxt(raw_data, delimiter=",")
#lets split the data into the 8 input variables and then assign a single output
X = dataSet[:,0:8]
Y = dataSet[:,8]
#split into 67 and 33% for training and test
X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size=0.33, random_state=seed)
#create model
model = Sequential()
model.add(Dense(12, input_dim=8, init="uniform", activation='relu'))
model.add(Dense(8, init='uniform', activation='relu'))
model.add(Dense(1, init='uniform', activation='sigmoid'))
#complie model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
#fit the model
model.fit(X_train, y_train, validation_data=(X_test, y_test), nb_epoch=150, batch_size=10)