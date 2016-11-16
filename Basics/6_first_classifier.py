from scipy.spatial import distance

def euc(a, b):
    return distance.euclidean(a, b)


class ScrappyKNN():
    """
    Barebones KNN
    """

    def fit(self, X_train, y_train):

        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):

        predictions = []
        for row in X_test:
            # label = random.choice(self.y_train)  # Random decision
            label = self.closest(row)
            predictions.append(label)

        return predictions

    def closest(self, row):
        # Distance from test point to first training point
        best_distance = euc(row, self.X_train[0])  # Shortest distance found so far
        best_index = 0  # index of closest training point
        for i in xrange(1, len(self.X_train)):  # Iterate over all other training points
            distance = euc(row, self.X_train[i])
            if distance < best_distance:  # Found closer, update
                best_distance = distance
                best_index = i
        return self.y_train[best_index]  # closest example

#Train and Test
from sklearn import datasets
iris = datasets.load_iris()

# calling features x and labels y, f(x) = y
X = iris.data
Y = iris.target

#partition into train or test
#this will split the group into two different sets, the test_size is what will be randomly split,half for this exmaple

from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = .5)

#lets make a decision tree
#from sklearn import tree
my_classifier = ScrappyKNN()

#then like the other examples train the classifier with the training data
my_classifier.fit(X_train, Y_train)
#create the predictions of all the test data
predictions = my_classifier.predict(X_test)

#check accuracy
from sklearn.metrics import accuracy_score
print accuracy_score(Y_test, predictions)
