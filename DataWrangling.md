#Data Wrangling in Machine Learning

CSV is the most important format in regards to Machine Learning with Python as it's the most common. 

##Things to look out for

####Does your data have a file header:
If it does it can help with automatically assigning names to each column of data. Otherwise you'll be attributing them manually. 

When loading data it's always a good idea to specify whether or not the CSV file has a file header when loading. 

####Comments
Comments in CSV are denoted with the #(hash) at the start of the line. Some methods require you to annotate if there are any comments in your file and what character to expect. 

####Delimiter
The standard in CSV (comma-separated values) files is the ,(comma) character. Now there are other ways such as a tab or white space. If this is the case you should specify it in the uploading process. 

####Quotes
When field values have spaces the values often are quoted. The default quote character is the double quotation mark("). Other characters can be used and so it's best to specify the quote character used in your file. 

#Demo Data Set
The data set that will be used is the Pima Indians data set. The data is freely available from the UCI Machine Learning Repository. [https://archive.ics.uci.edu/ml/datasets/Pima+Indians+Diabetes]()

#Load CSV Files
The python api provides a module CSV and the function reader() which then can be converted into NumPy Array. 

```
import csv
import numpy
fileName = 'pima-indians-diabetes.data.csv'
raw_data = open(fileName, 'rb')
reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
x = list(reader)
data = numpy.array(x).astype('float')
print(data.shape)
```
This should return:
```
(768,9)
```

The example above loads an object that iterates over each row of the data an dcan easilly be converted into a NumPy array. Then it prints the shape of the array. 
