#Feature Selection

It's best to do feature selection before you begin modeling data so that you can help reduce overfitting, improve the accuracy of your model and can reduce training time. 

##Univariate Selection

There is a SelectKBest class that can be used with a suite of different statistical tests to select a specified number of features. 
```
import pandas
import numpy
from sklearn.feature_selection import SelectKBest
from skelearn.feature_selection import chi2
#load the data
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataFrame = pandas.read_csv(url, names=names)
array = dataFrame.values
X = array[:,0:8]
Y = array[:,8]
#feature extraction
test = SelectKBest(precision=3)
fit = test.fit(X,Y)
#summary of scores
numpy.set_printoptions(precision=3)
print(fit.scores_)
features = fit.transform(X)
print(features[0:5,:])
```
