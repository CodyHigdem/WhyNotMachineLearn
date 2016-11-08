import numpy
import pandas
import urllib
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import pipeline

#fix random seed
seed = 7
numpy.random.seed(seed)

#load dataset
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
raw_data = urllib.urlopen(url)
dataSet = numpy.loadtxt(raw_data, delimiter=",")
#lets split the data into the 8 input variables and then assign a single output
X = dataSet[:,0:4].astype(float)
Y = dataSet[:,4]

#encode class values as integerss
encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)
# convert integers to dummy variables (I think this ws hot coding)
dummy_y = np_utils.to_categorical(encoded_Y)

#define baseline model
def baseline_model():
	#create the model
	model = Sequential()
	model.add(Dense(4, input_dim=4, init='normal', activation='relu'))
	model.add(Dense(3, init='normal', activation='sigmoid'))
	#compile model
	model.compile(loss='categorical_crossentropy', optimizer="adam", metrics=['accuracy'])
	return model

estimator = KerasClassifier(build_fn=baseline_model, nb_epoch=200, batch_size=5, verbose=0)

kfold = KFold(n=len(X), n_folds=10, shuffle=True, random_state=seed)
results = cross_val_score(estimator, X, dummy_y, cv=kfold)
print("Accuracy: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))