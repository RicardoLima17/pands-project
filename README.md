 "![gmit](https://user-images.githubusercontent.com/77755223/115528889-56c6fc80-a28a-11eb-8f36-2d7004e6ece6.PNG)  
 
## Ricardo Oliveira Lima Rodrigues - G00398291 

<h1>Pandas-Project 2021 - Iris Dataset Analysis</h1> 

## Table of contents
                                
1. Summary
2. Introduction
3. Dataset Analysis 
  3.1 Codes and Table
  3.2 Graphics
5. Conclusion
6. References

## 1- Summary of Pands-Project
<p>This repository contains my programming and scripting pands-project 2021. In this project, was developed skills in, github, csv, Matplolib, NumPy, Pandas and Seaborn.</p>

## 2- Introduction
<p>The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician, eugenicist, and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis. It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. Two of the three species were collected in the Gaspé Peninsula "all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus".

The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.</p>

1. Iris Setosa
2. Iris Virginica
3. Iris Versicolor

Four features are were measured from each sample:

1. Sepal length (cm)
2. Sepal width (cm)
3. Petal length (cm)
4. Petal width (cm)

![Iris flower](https://user-images.githubusercontent.com/77755223/115158575-bbb20500-a086-11eb-877d-059237278e12.png)

## 3- Dataset Analysis
This is an example to demonstrate concepts of Data Science. In this example we will do some exploratory data analysis on the famous Iris dataset.

<p>The Iris Dataset contains four features (length and width of sepals and petals) of 50 samples of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). These measures were used to create a linear discriminant model to classify the species. The dataset is often used in data mining, classification and clustering examples and to test algorithms.</p>

#### ----------------------------------------------------------------------------------------------------------------------------

### 3.1- Code and Tables

#### Imported libraries and modules
<p>Python Libraries are a set of useful functions that eliminate the need for writing codes from scratch. There are over 137,000 python libraries present today. Python libraries play a vital role in developing machine learning, data science, data visualization, image and data manipulation applications and more</p>
![image](https://user-images.githubusercontent.com/77755223/115998743-9f5f1c80-a5e0-11eb-85dc-0993c6148d15.png)
#### ----------------------------------------------------------------------------------------------------------------------------
The head() function is used to get the first n rows. This function returns the first n rows for the object based on position. It is useful for quickly testing if your object has the right type of data in it.

![image](https://user-images.githubusercontent.com/77755223/115613768-beaa3100-a2e4-11eb-9363-a5545eb946a3.png)
#### ----------------------------------------------------------------------------------------------------------------------------
The function "shape" returns the shape of an array. The shape is a tuple of integers. These numbers denote the lengths of the corresponding array dimension. In other words: The "shape" of an array is a tuple with the number of elements per axis (dimension).

![image](https://user-images.githubusercontent.com/77755223/115613936-f44f1a00-a2e4-11eb-9aa6-d52a89ea535b.png)
#### ----------------------------------------------------------------------------------------------------------------------------
The describe() method is used for calculating some statistical data like percentile, mean and std of the numerical values of the Series or DataFrame. It analyzes both numeric and object series and also the DataFrame column sets of mixed data types.

![image](https://user-images.githubusercontent.com/77755223/115614151-39734c00-a2e5-11eb-851a-b55e3d3c1008.png)
#### ----------------------------------------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/77755223/115614314-75a6ac80-a2e5-11eb-8016-a50787615b6f.png)
#### ----------------------------------------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/77755223/115615149-7d1a8580-a2e6-11eb-9733-a2de9e3de35e.png)
#### ----------------------------------------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/77755223/115615174-87d51a80-a2e6-11eb-942f-36a3a3c67509.png)
#### ----------------------------------------------------------------------------------------------------------------------------
groupby() function is used to split the data into groups based on some criteria. pandas objects can be split on any of their axes.

![image](https://user-images.githubusercontent.com/77755223/115615453-e601fd80-a2e6-11eb-83dc-d177414c2d5d.png)
#### ----------------------------------------------------------------------------------------------------------------------------
Correlation coefficients quantify the association between variables or features of a dataset. These statistics are of high importance for science and technology, and Python has great tools that you can use to calculate them. SciPy, NumPy, and Pandas correlation methods are fast, comprehensive, and well-documented.

![setosaCorr](https://user-images.githubusercontent.com/77755223/115971934-56a55600-a543-11eb-8047-9956d7a2e80b.PNG)
#### ----------------------------------------------------------------------------------------------------------------------------
![versicolorCarr](https://user-images.githubusercontent.com/77755223/115972132-8e60cd80-a544-11eb-93b0-490e6a5230bc.PNG)
#### ----------------------------------------------------------------------------------------------------------------------------
![virginicaCorr](https://user-images.githubusercontent.com/77755223/115972150-97ea3580-a544-11eb-9440-a941beabeb6e.PNG)
#### ----------------------------------------------------------------------------------------------------------------------------

### 3.1- Graphics
![image](https://user-images.githubusercontent.com/77755223/116291995-218c4400-a78d-11eb-8aed-1f48678092a7.png)
#### ----------------------------------------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/77755223/116289932-d8d38b80-a78a-11eb-85ae-58b43282a1cc.png)
![image](https://user-images.githubusercontent.com/77755223/116286836-99577000-a787-11eb-911d-d1d9c41ccc61.png)
#### ----------------------------------------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/77755223/116291436-7a0f1180-a78c-11eb-9ead-4d4816d663b8.png)
![image](https://user-images.githubusercontent.com/77755223/116290564-8181eb00-a78b-11eb-8589-b3b34128f77f.png)
#### ----------------------------------------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/77755223/116293748-1d612600-a78f-11eb-8853-a94f545c23fb.png)
![image](https://user-images.githubusercontent.com/77755223/116293834-2c47d880-a78f-11eb-91c5-a7f3bbeff7b6.png)
#### ----------------------------------------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/77755223/116294266-b1cb8880-a78f-11eb-98c0-0cd16c603dd8.png)
![image](https://user-images.githubusercontent.com/77755223/116294343-c6a81c00-a78f-11eb-9a07-79a156f0e275.png)
#### ----------------------------------------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/77755223/116295533-19ce9e80-a791-11eb-8f43-10dd5ffc52ab.png)
![image](https://user-images.githubusercontent.com/77755223/116295586-281cba80-a791-11eb-95f0-fc2996402750.png)
#### ----------------------------------------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/77755223/116296252-e7717100-a791-11eb-860f-f4a94736f976.png)
![image](https://user-images.githubusercontent.com/77755223/116296115-bdb84a00-a791-11eb-9800-829f94f8df3f.png)

#### ----------------------------------------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/77755223/116296749-7e3e2d80-a792-11eb-9aa3-e5beabb80b81.png)
![image](https://user-images.githubusercontent.com/77755223/116296798-8e560d00-a792-11eb-89c5-9ba2e14fe139.png)

#### ----------------------------------------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/77755223/116297167-e856d280-a792-11eb-9f27-f66e82f4cec7.png)
![image](https://user-images.githubusercontent.com/77755223/116297229-f4db2b00-a792-11eb-8f1a-70ec4de1fe51.png)

#### ----------------------------------------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/77755223/116298315-34564700-a794-11eb-87bd-b11da95974f6.png)
![image](https://user-images.githubusercontent.com/77755223/116298474-65cf1280-a794-11eb-9131-73e6d4cf703f.png)
#### ----------------------------------------------------------------------------------------------------------------------------
![image](https://user-images.githubusercontent.com/77755223/116298771-c8c0a980-a794-11eb-971f-08475f367d27.png)

## 4- Conclusion
In this project, we've introduced and analysed the Iris Flower Dataset. We've used the various helpful codes from the panda's package for our analysis, and then we proceeded to create some interesting visualisations using pandas and seaborn on top of matplotlib. 
## 5- References
<https://web.microsoftstream.com/video/ee296187-6469-4481-b28d-aed28af38ea4?list=studio>
<https://web.microsoftstream.com/video/958c5886-bc34-4bd1-8bf2-78c85b1dba49?list=studio>
<https://web.microsoftstream.com/video/31b9d1db-d72c-4ba2-97e3-03208b057ce6?list=studio&referrer=https:%2F%2Flearnonline.gmit.ie%2F>
<https://web.microsoftstream.com/video/46aca21f-2b47-4ad1-9a83-8ac8b554202c?list=studio>
<https://web.microsoftstream.com/video/2dd501ea-cd0b-4a1a-9a47-0dda9a304143?list=studio>
<https://towardsdatascience.com/how-to-export-pandas-dataframe-to-csv-2038e43d9c03>
<https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.tail.html>
<https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html>
<https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html>
<https://stackoverflow.com/questions/67150094/how-can-i-condense-a-series-of-seaborn-scatterplots-using-for-loops>
<https://seaborn.pydata.org/generated/seaborn.set.html>
<https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/>
<https://www.geeksforgeeks.org/python-pandas-dataframe-describe-method/>
<https://www.python.org/>



