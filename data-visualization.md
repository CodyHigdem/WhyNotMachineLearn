#Data visualization

##Hisograms

```
import matplotlib.pyplot as plt
import pandas
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pei', 'age', 'class']
data = pandas.read_csv(url, names=names)
data.hist()
plt.show()
```

##Density Plots

```
import matplotlib.pyplot as plt
import pandas
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pandas.read_csv(url, names=names)
data.plot(kind='density', suplots=True, layout=(3,3), sharex=False)
plt.show()
```

