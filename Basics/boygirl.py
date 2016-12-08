from sklearn import tree
#Think of Featuers as inputs
#convert smooth to 1 and bumpy to 0 
features = [[240, 76, 11], [205, 72, 10], [150, 65, 8], [110, 60, 7], [105, 64, 5]]
#labels are the output we want
#convert words to a number system
#girl to 0
#boy to 1
labels = [1, 1, 0, 0, 0]

#create a decision tree 'box of rules' Right now the box can be considered empty
clf = tree.DecisionTreeClassifier()

#learning algo to create the decision tree box of rules
#in scikit the trainer is in the classifiered object and called fit
clf = clf.fit(features, labels)

print clf.predict([190, 70, 9])

feature_names = ['weight', 'height (in)', 'shoe size']
label_names = ['Boy', 'Girl']
from sklearn.externals.six import StringIO
import pydot
dot_data = StringIO()
tree.export_graphviz(clf,
						out_file=dot_data,
						feature_names=feature_names,
						class_names=label_names,
						filled=True, rounded=True,
						impurity=False)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("boygirl.pdf")

