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