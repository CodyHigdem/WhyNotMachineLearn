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

#encode class values as integers