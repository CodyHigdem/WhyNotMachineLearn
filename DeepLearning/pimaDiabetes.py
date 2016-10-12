from keras.models import Sequential
from keras.layers import Dense
import numpy
#fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
#load  pima indians data sets
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
raw_data = urllib.urlopen(url)
dataSet = numpy.loadtxt(raw_data, delimiter=",")
#lets split the data into the 8 input variables and then assign a single output
X = dataset[:,0:8]
Y = dataset[:,8]
#the output has 1 neuro layer whether diabetes gonna happen or not
#Then second layer has 8 neurons
#then 12 neuroes with 8 input variables to said 12
#create the model mentioned above
model = Sequential()
model.add(Dense(12, input_dim=8, init="uniform", activation="relu"))
model.add(Dense(8, init="uniform", activation="relu"))
model.add(Dense(1, init="uniform", activation="sigmoid"))

#When you compile lets Theano use numerical libraries to effeciently 'crunch'
#compile model
# Adam is a gradient descent algorithm that is very popular. 
model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
#nb_epoch isnumber of iterations for training
#batch_size number of instances that are evaluated before a weight update
#Fit the Model
model.fit(X, Y, nb_epoch=150, batch_size=10)
#evaluate the model
scores = model.evaluate(X,Y)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

