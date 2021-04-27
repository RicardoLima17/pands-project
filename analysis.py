# Author Ricardo

import pandas as pd
import seaborn as sns
import numpy as np 
import matplotlib.pyplot as plt
import sys


# Read in file
iris_df = pd.read_csv("https://raw.githubusercontent.com/RicardoLima17/pands-project/main/iris.csv")

# show the names of column
iris_df.columns = ["sepal length", "sepal width", "petal length", "petal width", "variety"]

# Creating a text file called Iris Analysis to print output results of comparing the species
sys.stdout = open("Iris Analysis", "w", newline='\n') # Using 'w' for read mode. 

# Show first and last 5 rows
print(iris_df.head())

# Show number of rows and columns
print(iris_df.shape)

# Show numerical summary of each attribute through describe and round 4
summary = iris_df.describe().round(4)
print(summary)


# Show numerical summary grouped by each attribute through describe
setosa = iris_df[iris_df["variety"] =="Iris-setosa"]
versicolor = iris_df[iris_df["variety"] =="Iris-versicolor"]
virginica = iris_df[iris_df["variety"] =="Iris-virginica"]

# Show setosa correlation table
print ("Setosa Correlation")
SetCorr = setosa.corr()
print (SetCorr)

# Show versicolor correlation table
print ("Versicolor Correlation")
VerCorr = versicolor.corr()
print (VerCorr)

# Show virginica correlation correlation
print ("Virginica Correlation")
VirCorr = virginica.corr()
print (VirCorr)

# Show setosa numerical summary grouped by each attribute through describe round 4
print("Iris setosa:")
summary1 = (setosa.describe()).round(4)
print(summary1)

# Show versicolor numerical summary grouped by each attribute through describe round 4
print("Iris versicolor:")
summary2 = (versicolor.describe()).round(4)
print(summary2)

# Show vitginica numerical summary grouped by each attribute through describe round 4
print("Iris virginica:")
summary3 = (virginica.describe()).round(4)
print(summary3)


# Show row count per species
iris_df.groupby("variety").size()


# Graphics 


# show how many groupby 50, 50, 50.
ax = plt.axes()
# Bar is black
plt.hist(iris_df["variety"], color = "black")
# Title
plt.title("Group lenght Histogram")
plt.grid(True)
# color the back of the chart
ax.set_facecolor("lightyellow")
# save picture
plt.savefig(fname="groupby.png")


# Show the summary of 4 graphics with linewidth=1 and each graphic in the position and color
distplot, axes = plt.subplots(2,2, figsize=(11,11), sharex=False)
sns.histplot( iris_df["sepal length"] , kde = True, stat="density", linewidth=1, color="blue"  , ax=axes[0, 0])
sns.histplot( iris_df["sepal width" ] , kde = True, stat="density", linewidth=1, color="yellow"  ,ax=axes[0, 1]) 
sns.histplot( iris_df["petal length"] , kde = True, stat="density", linewidth=1, color="purple", ax=axes[1, 0]) 
sns.histplot( iris_df["petal width" ] , kde = True, stat="density", linewidth=1, color="green" , ax=axes[1, 1])
plt.suptitle ("Summary Iris dataset in centimeter")
plt.savefig(fname="summary.png")


# Show the setosa summary of 4 graphics with linewidth=1 and each graphic in the position and color
distplot, axes = plt.subplots(2,2, figsize=(11,11), sharex=False)
sns.histplot( setosa["sepal length"] , kde = True, stat="density", linewidth=1, color="blue"  , ax=axes[0, 0])
sns.histplot(setosa["sepal width" ] , kde = True, stat="density", linewidth=1, color="yellow"  ,ax=axes[0, 1]) 
sns.histplot(setosa["petal length"] , kde = True, stat="density", linewidth=1, color="purple", ax=axes[1, 0]) 
sns.histplot(setosa["petal width" ] , kde = True, stat="density", linewidth=1, color="green" , ax=axes[1, 1])
plt.suptitle ("Setosa Iris dataset in centimeter")
plt.savefig(fname="setosa.png")


# Show the versicolor summary of 4 graphics with linewidth=1 and each graphic in the position and color
distplot, axes = plt.subplots(2,2, figsize=(11,11), sharex=False)
sns.histplot( versicolor["sepal length"] , kde = True, stat="density", linewidth=1, color="blue"  , ax=axes[0, 0])
sns.histplot(versicolor["sepal width" ] , kde = True, stat="density", linewidth=1, color="yellow"  ,ax=axes[0, 1]) 
sns.histplot(versicolor["petal length"] , kde = True, stat="density", linewidth=1, color="purple", ax=axes[1, 0]) 
sns.histplot(versicolor["petal width" ] , kde = True, stat="density", linewidth=1, color="green" , ax=axes[1, 1])
plt.suptitle ("Versicolor Iris dataset in centimeter")
plt.savefig(fname="versicolor.png")


# Show the virginica summary of 4 graphics with linewidth=1 and each graphic in the position and color
distplot, axes = plt.subplots(2,2, figsize=(11,11), sharex=False)
sns.histplot( virginica["sepal length"] , kde = True, stat="density", linewidth=1, color="blue"  , ax=axes[0, 0])
sns.histplot(virginica["sepal width" ] , kde = True, stat="density", linewidth=1, color="yellow"  ,ax=axes[0, 1]) 
sns.histplot(virginica["petal length"] , kde = True, stat="density", linewidth=1, color="purple", ax=axes[1, 0]) 
sns.histplot(virginica["petal width" ] , kde = True, stat="density", linewidth=1, color="green" , ax=axes[1, 1])
plt.suptitle ("Virginical Iris dataset centimeter")
plt.savefig(fname="virginica.png")


# Show Heatmap summary correlation
fig = plt.figure(figsize = (12,10))
sns.heatmap(iris_df.corr(), cmap = "Blues", annot = True)
plt.suptitle ("Summary Heatmap")
plt.savefig(fname="Summary_Correlation.png")

# Show setosa Heatmap setosa correlation
fig = plt.figure(figsize = (12,10))
sns.heatmap(setosa.corr(), cmap = "Greens", annot = True)
plt.title("Setosa Heatmap")
plt.savefig(fname="Setosa_Correlation.png")

# Show versicolor Heatmap versicolor correlation
fig = plt.figure(figsize = (12,10))
sns.heatmap(versicolor.corr(), cmap = "Greys", annot = True)
plt.title("Versicolor Heatmap")
plt.savefig(fname="Versicolor_Correlation.png")

# Show virginica Heatmap virginica correlation
fig = plt.figure(figsize = (12,10))
sns.heatmap(virginica.corr(), cmap = "Reds", annot = True)
plt.title(" Virginica Heatmap")
plt.savefig(fname="Virginica_Correlation.png")


# Show PairGrid "histograma and scatter" with legend 
a = sns.PairGrid(iris_df, hue="variety", palette = "nipy_spectral")
a.map_diag(sns.histplot)
a.map_offdiag(sns.scatterplot)
a.add_legend()
plt.savefig(fname="scatterplot.png")


#Display plot
plt.show()


# References
# https://web.microsoftstream.com/video/ee296187-6469-4481-b28d-aed28af38ea4?list=studio
# https://web.microsoftstream.com/video/958c5886-bc34-4bd1-8bf2-78c85b1dba49?list=studio
# https://web.microsoftstream.com/video/31b9d1db-d72c-4ba2-97e3-03208b057ce6?list=studio&referrer=https:%2F%2Flearnonline.gmit.ie%2F
# https://web.microsoftstream.com/video/46aca21f-2b47-4ad1-9a83-8ac8b554202c?list=studio
# https://web.microsoftstream.com/video/2dd501ea-cd0b-4a1a-9a47-0dda9a304143?list=studio
# https://towardsdatascience.com/how-to-export-pandas-dataframe-to-csv-2038e43d9c03
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.tail.html
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html
# https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html
# https://stackoverflow.com/questions/67150094/how-can-i-condense-a-series-of-seaborn-scatterplots-using-for-loops
# https://seaborn.pydata.org/generated/seaborn.set.html
# https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/
# https://www.geeksforgeeks.org/python-pandas-dataframe-describe-method/
# https://www.python.org/
