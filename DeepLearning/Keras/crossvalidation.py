#10-fold cross validation via sklearn example
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.cross_validation import StratifiedKFold
from sklearn.cross_validation import cross_val_score
import numpy

#function to create model, required for the KerasClassifier we're going to rock later
def create_model():
	#create the model
	model = Sequential()
	model.add(Dense(12, input_dim=8, init='uniform', activation='relu'))
	model.add(Dense(8, init='uniform', activation='relu'))
	model.add(Dense(1, init='uniform', activation='sigmoid'))
	#compile model
	model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
	return model

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
#create th emodel
model = KerasClassifier(build_fn=create_model, nb_epoch=150, batch_size=10, verbose=0)
#evaluate using 10-fold cross validation
kfold = StratifiedKFold(y=Y, n_folds=10, shuffle=True, random_state=seed)
results = cross_val_score(model, X, Y, cv=kfold)
print(results.mean())