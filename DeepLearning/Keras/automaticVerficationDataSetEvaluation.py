#Best way to design models is through small experiments and empircally evaluating using real data. 
#Think of changing the number, size and type of layers in the network
# and choices of loss functions, activation functions, optimizatoin procedures and number of epochs

#ROBUST testing that can estimate the performance of a given config on unseen data

#ust automatic datasets
#validatin_split argument on the fit() function with Keras
from keras.models import Sequential
from keras.layers import Dense
import numpy
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

#create the model
model = Sequential()
model.add(Dense(12, input_dim=8, init="uniform", activation="relu"))
model.add(Dense(8, init="uniform", activation="relu"))
model.add(Dense(1, init="uniform", activation="sigmoid"))
#compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
#fit the model
model.fit(X,Y,validation_split=0.33, nb_epoch=150, batch_size=10)
