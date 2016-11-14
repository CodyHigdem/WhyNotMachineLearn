import numpy as np
#Decision trees are easy to visualize
from sklearn.datasets import load_iris
from sklearn import tree
#sklearn has slick adoptions of classic machine learning data sets
iris = load_iris()
print iris.feature_names
print iris.target_names
print iris.data[0]
print iris.target[0]

#Establish your testing data
# You will have to remove a part of your data into a testing set. This is what will be used to check the accuracy

test_iris = [0, 50, 100]

#set u the training data
#remove test data from training dataset
train_target = np.delete(iris.target, text_iris)
#establish training data
train_data = np.delete(iris.data, text_iris, axis=0)

#testing data, just the three examples above
test_target = iris.target[test_iris]
test_data = iris.data[test_iris]

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

print test_target