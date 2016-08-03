#Getting Up with Statistic Descriptives...?

##View Data in the Raw
Pandas has a slick little function called head() that allows you to glance at your data briefly. 
```
import pandas
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names=names)
peek = data.head(20)
print(peek)
```

##Rows of data

Reviewing your shape and size of your dataset can be done by printing shape property of the pandas dataframe. 

```
import pandas
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names=names)
shape = data.shape
print(shape)
```
Printing shape will let you see there are 768 rows and 9 columns. 
```
(768, 9)
```

##Data Type Attributes

datatypes can become a pain as strings may need to be converted to integers or floating point. So you can get `dtypes` property in Pandas DataFrame

```
import pandas
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
name = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names=names)
types = data.dtypes
print(types)
```

You will see that there are integers and floating point types. 

```
preg       int64
plas       int64
pres       int64
skin       int64
test       int64
mass     float64
pedi     float64
age        int64
class      int64
dtype: object
```

##Stats 

The describe() function on Pandas DataFrame focuses on 8 properties: 
Count
Mean
Standard Deviation (STD)
Minimum Value
25th Percentile
50th Percentile (Median)
75th Percentile
Maximum Value

```
import pandas
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names=names)
pandas.set_option('display.width', 100)
pandas.set_option('precision', 3)
description = data.describe()
print(description)
```

classification problems you need to know how balances the class values are. Highly imbalanced problems (more observations for one class than another) are common and may need special handling in data preparation stage of you rproject. 

```
import pandas
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names=names)
class_counts = data.groupby('class').size()
print(class_counts)
```

returning

```
class
0 500
1 268
```
There are way more class 0 (no onset of diabetes) than there are of class 1 (onset)

##Correlations

Is the relationship between two variables and how they may or may not change together. A commong method for calculating is Pearson's Correlatoin Coefficient, that assumes a normal distribution of attributes. -1 or 1 shows a full negative or positive correlation respectively and a 0 shows no correlation at all. 

some machine learning algorithms can suffer from poor performance if there ar ehighly correlated attributes in the dataset (linear & logistic regression)

So try to review the pair-wise correlations of attributes in your dataset. You can use the cor() function from Pandas Framework to calculate a correlation matrix. 

```
import pandas
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names=names)
pandas.set_option('display.width', 100)
pandas.set_option('precision', 3)
correlations = data.corr(methods='pearson')
print(correlations)
```

Will return:
```
        preg   plas   pres   skin   test   mass   pedi    age  class
preg   1.000  0.129  0.141 -0.082 -0.074  0.018 -0.034  0.544  0.222
plas   0.129  1.000  0.153  0.057  0.331  0.221  0.137  0.264  0.467
pres   0.141  0.153  1.000  0.207  0.089  0.282  0.041  0.240  0.065
skin  -0.082  0.057  0.207  1.000  0.437  0.393  0.184 -0.114  0.075
test  -0.074  0.331  0.089  0.437  1.000  0.198  0.185 -0.042  0.131
mass   0.018  0.221  0.282  0.393  0.198  1.000  0.141  0.036  0.293
pedi  -0.034  0.137  0.041  0.184  0.185  0.141  1.000  0.034  0.174
age    0.544  0.264  0.240 -0.114 -0.042  0.036  0.034  1.000  0.238
class  0.222  0.467  0.065  0.075  0.131  0.293  0.174  0.238  1.000
```

##univariate Distributions

When a bell curve distribution is skewed data is shifted or squashed to one side. Many machine learning algorithms assume a normal Gaussian distribution and knowing that an attribute has a skew may allow you to perform data preparation to correct the skew and later improve the accuracy of you rmodels. Using skew() can help. 

```
import pandas
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names=names)
skew = data.skew()
print(skew)
```

The closer to 0 you receive the less skew there is. 

```
preg     0.902
plas     0.174
pres    -1.844
skin     0.109
test     2.272
mass    -0.429
pedi     1.920
age      1.130
class    0.635
```



