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
