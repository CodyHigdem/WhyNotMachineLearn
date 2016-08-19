#Prepping DATA


##Rescale Data

This is a recipe for normalizing data sets and scaling them into the range of 0 to 1. 

This is useful for gradient descent and weight inputs like regression, neural neetworks and distance measuring algorithms like K-Nearest Neighbors. MinMaxScaler is a scikit-learn class that can help with this. 

```
import pandas
import scipy
import numpy
from sklearn.preprocessing import MinMaxScaler
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataFrame = pandas.read_csv(url, names=names)
array = dataFrame.values
#seperate array into input and outpu tcomponents
X = array[:,0:8]
Y = array[:,8]
scaler = MinMaxScaler(feature_range=(0,1))
rescaledX = scaler.fit_transform(X)
#summary of transformed data
numpy.set_printoptions(precision=3)
print(rescaledX[0:5,:])
```
##Standarizing Data

Standarizing data is useful for data that we expect to be equally distributed as opposed to skewed towards one way or another. 

```
from sklearn.preprocessing import StandardScaler
import pandas
import numpy
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataFrame = pandas.read_csv(url, names=names)
array = dataFrame.values
#seperate array into input and output
X = array[:,0:8]
Y = array[:,8]
scaler = StandardScaler().fit(X)
rescaledX = scaler.transform(X)
#summary of data
numpy.set_printoptions(precision=3)
print(rescaledX[0:5,:])
```

##Normalize Data

When you normalize data it entails rescaling everything to have a max of 1. think vectors with a length of 1 in linear algebra. This can be useful for datasets with lots of zeros of extremes that need to be associated within a relative terms of features. Think when looking at housing prices there are sqft, number of baths, number of bedrooms so on. 

There is a Normalizer class in scikit-learn that can help with this. 
```
from sklearn.preprocessing import Normalizer
import pandas
import numpy
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass, 'pedi', 'age', 'class']
dataFrame = pandas.read_csv(url, names=names)
array = dataFrame.values
X = array[:,0:8]
Y = array[:,8]
scaler = Normalizer().fit(X)
normalizedX = scaler.transform(X)

numpy.set_printoptions(precision=3)
print(normalizedX[0:5,:])
```

