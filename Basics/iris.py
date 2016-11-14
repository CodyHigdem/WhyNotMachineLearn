import numpy as np
#Decision trees are easy to visualize
from sklearn.datasets import load_iris
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