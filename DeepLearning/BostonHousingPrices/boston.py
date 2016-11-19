import numpy
import pandas
# https://keras.io/models/sequential/
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.cross_validation import cross_val_score
from sklearn.cross_validation import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

#load data sets
datafram = pandas.read_cvs("housing.csv", delim_whitespace=True, header=None)
dataset = dataframe.values
#split into input (X) and output (Y) variables
X = dataset[:,0:13]
Y = dataset[:,13]

