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