#stratifiedKfold calss attempts to balance the number of instances of each class in k-fold. 
#you can turn on or off the verbose output by passing verbose=0 to the fite and evaluate functions of the model
#MLP for Pima Indians Dataset with 10-fold cross validation
from keras.models import Sequential
from keras.layers import Dense
from sklearn.cross_validation import stratifiedKfold
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
#define 10-fold cross validation test harness as kfold
kfold = stratifiedKfold(y=Y, n_folds=10, shuffle=true, random_state=seed)
cvsscores = []
for i, (trian,test) in enumerate(kfold):
	#create the model 
	model = Sequential()
	model.add(Dense(12, input_dim=8, init='uniform', activation='relu'))
	model.add(Dense(8, init='uniform', activation='relu'))
	model.add(Dense(1, init='uniform', activation='relu'))
	#Compile Model
	model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
	#Fit the model
	model.fit(X[train], Y[train], nb_epoch=150, batch_size=10, verbose=0)
	#evaluate the model
	scores = model.evaluate(X[test], Y[test], verbose=0)
	print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
	cvsscores.append(scores[1] * 100)
print("%.2f%% (+/- %.2f%%)" % (numpy.mean(cvsscores), numpy.std(cvsscores)))