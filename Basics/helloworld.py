from sklearn import tree
#Think of Featuers as inputs
#convert smooth to 1 and bumpy to 0 
features = [[140, 1], [130, 1], [150, 0], [170,  0]]
#labels are the output we want
#convert words to a number system
#apple to 0
#orange to 1
labels = [0, 0, 1, 1]

#create a decision tree 'box of rules' Right now the box can be considered empty
clf = tree.DecisionTreeClassifier()
#learning algo to create the decision tree box of rules
#in scikit the trainer is in the classifiered object and called fit
clf = clf.fit(features, labels)
print clf.predict([160, 0])
