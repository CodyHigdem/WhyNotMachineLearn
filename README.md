# WhyNotMachineLearn

Machine Learning and Python notes, recipes and mini-projects. 

##Predictive Machine Learning Modeling Steps

1. **Define Problem**: Investigate and characterize the problem in order to better understand the goals of the project.2. **Analyze Data:** Use descriptive statistics and visualization to better understand the data you have available.3.**Prepare Data:** Use data transforms in order to better expose the structure of the prediction problem to modeling algorithms.4. **Evaluate Algorithms:** Design a test harness to evaluate a number of standard algorithms on the data and select the top few to investigate further.5. **Improve Results:** Use algorithm tuning and ensemble methods to get the most out of well-performing algorithms on your data.6. **Present Results:** Finalize the model, make predictions and present results.



## Python Machine Learning Environment

The environment consists of several modules/libraries. SciPy is used for large swaths of mathematics, science and engineering. To use SciPy effectively you'll also want to have a handful of other modules like Numpy, which works with data in arrays. Matplotlib, provides 2d charts and plots from data sets. Pandas which helps organize and analyze data.

so in summary you'll create plots in Matplolib, manipulate arrays in NumPy and Panda to load and gain clarity on your data sets. 

###sciKit-learn

SciKit-Learn is a python library that is dependent on SciPy. It is a base set for exploring machine learning with Python with a large set of tools for clustering, regression, classification and more. It's helpful for pre-processing data as well as tuning it. 

### Getting Started with SciPy

Let's install python if you don't have it and at a minimum the following:

  1. scipy  2. numpy  3. matplotlib 
  4. pandas
  5. SciKitLearn

  ####Checking Versions
  `
  python --version`
  
  Will Check for your python version. 
  
```# scipy
import scipyprint('scipy: {}'.format(scipy.__version__)) # numpyimport numpyprint('numpy: {}'.format(numpy.__version__))
 # matplotlibimport matplotlibprint('matplotlib: {}'.format(matplotlib.__version__)) # pandasimport pandasprint('pandas: {}'.format(pandas.__version__))
# scikit-learnimport sklearnprint('sklearn: {}'.format(sklearn.__version__))
```

If you do not have any of these installed a quick Google search with the name of the module and install will provide you with the official installation instructions. 

You coud also use Anaconda or another packaging system manager to help install everything for python.
https://www.continuum.io/downloads

# Getting to know Python

A quick look at Python for those who know a programming language or two. 
##Strings
```
#Strings
data = 'hello world'
print(data[0])
print(len(data))
print(data)
```

This should print out


```
h 
11 
hello world
```

##Numbers
```
# Numbersvalue = 343.5print(value)value = 10print(value)
```
You should get: 

```
343.5 
10
```
##Boolean

```
# Booleana = Trueb = Falseprint(a, b)
```

Gives you ```(True, False)```

##Multiple Assignments

```
# Multiple Assignmenta, b, c = 1, 2, 3print(a, b, c)
```

Gives you back ```(1,2,3)```

##No Value

When a value is not provided None will print. 

## If-Then

```
speed = 30if speed == 30:	print 'Cheetah'
elif speed > 1000:	print 'Rocket' 
else:	print 'Running'
```
Notice the tabbing with the code. Python is sensitive to how you tab which is why some people enjoy coding in Python. Also take a look at the colon (:) at the end of the conditions. Knowing these two pieces of information will help you resolve early headaches if you're not used to coding in python. 

## For-Loop

```
for i in range(10):
	print i
```
returns
```0
1
2
3
4
5
6
7
8
9
10
```
## While-Loop

```
i = 0
while i < 10:
	print i
	i += 1
```

Returns
```
0
1
2
3
4
5
6
7
8
9
```

#Data Structures

##Tuples
A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists. The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets. - [http://www.tutorialspoint.com/python/python_tuples.htm](Read More)

So like the above notes say. Tuples are read-only collections of items.

```
a = (1,3,4)
print a
```

Returns
```
(1,2,4)
```

##List
Lists are square bracket notations and can be indexed using array notation. 

```
myList = [1,2,3]
print("Zeroth value: %d") % myList[0]
myList.append(4)
print("list Lenght: %d") % len(myList)
for value in myList:
	print value
```
Returns:
```
Zeroth Value: 1
List Length: 4
1
2
3
4
```

##Dictionary

Is kind of like a json data set. They ar emapped with names to values so very similiar to key value pairs. 

```
myDict = {'a':1, 'b':2, 'c':3}
print("A vlaue: %d") % myDict['a']
myDict['a'] = 11
print("A value: %d") % myDict['a']
print("Keys: %s") % myDict.keys()
print("Values: %s") % myDict.values()
for key in myDict.keys():
	print myDict[key]
```

returns
```
A value: 1
A value: 11
Keys: ['a','c','b']
values: [11,3,2]
11
3
2
```

##Functions
Don't forget about white spacing when it comes to Python that's the easiest hangup for people new to it. Functions and loops will be a pain if you're not aware of it. 
```
def mysum(x,y):
	return x+y
#test the function
result = mysum(1,3)
print(result)
```

returns:
``` 4 ```

#NumPy Crash Course
NumPy is the foundation for all of the data structures and operations that you'll be using in SciPy. 

##Create Array
```
import numpy
myList = [1,2,3]
myArray = numpy.array(myList)
print(myArray)
print(myArray.shape)
```

Returns
```
[1,2,3]
(3)
```

##Access Data
Array notations and ranges can be used to access data in NumPy arrays

```
#access values
import numpy
myList = [[1,2,3], [3,4,5]]
myArray = numpy.array(myList)
print(myArray)
print(myArray.shape)
print("First row: %s") % myArray[0]
print("Last row: %s") % myArray[-1]
print("Specific row and col: %s") % myArray[0,2]
print("Whole col: %s") % myArray[:,2]
```

Returns the following:
```
[[1 2 3]
 [3 4 5]]
(2,3)
First row: [1 2 3]
Last row: [3 4 5]
Specific row and col: 3
Whole col: [3 5]
```
##Math

NumPy arrays can be used in all adding

```
import numpy
myArray1 = numpy.array([2,2,2])
myArray2 = numpy.array([5,5,5])
print("Addition: %s") % (myArray1 + myArray2)
print("Multiplication: %s) % (myArray1 * myArray2)
```
Returns:
```
Addition: [7 7 7]
Multiplication: [10 10 10]
```

#Matplotlib Crash Course


