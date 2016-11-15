#Train and Test
from sklearn import datasets
iris = datasets.load_iris()

# calling features x and labels y, f(x) = y
X = iris.data
Y = iris.target

#partition into train or test
#this will split the group into two different sets, the test_size is what will be randomly split, roughly half for this exmaple

from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = .5)