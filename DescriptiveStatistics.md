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


