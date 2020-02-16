## The following datasets have been analyzed while solving the corresponding question. Also, the results have been discussed for each research question :

### 1. Iris dataset 

#### How accurately can we classify the different species of Iris flowers given the dataset with following description:
(a) The Iris dataset has 150 records

(b) The features of the flowers are : Sepal Length, Sepal Width, Petal length, Petal width

(c) We have the target variable which is the Species of the Iris flower classified into 3 classes :

  1. 0 --- Setosa

  2. 1 --- Versicolor
  
  3. 2 --- Virginica

#### RESULTS :

(a) Four models 1. Logistic regression, 2. Random forest classifier, 3. Support Vector Machine and 4. K-Nearest Neighbours were implemented.

(b) Logistic Regression is our baseline model which gives an accuracy of 88.88%. 

(c)Support Vector Machine performs the best with an accuracy of 100% followed by Random forest and KNN who both give an accuracy of 97%.


### 2. Digits classification using KNN algorithm

#### How accurately can we identify the different digits images
(a) The Digits dataset has 1797 records.

(b) The input, each image has 8x8 dimensions ie 64.

(c) We have the target variables as the following : 0,1,2,3,4,5,6,7,8,9

#### RESULTS :

(a) We achieved a test accuracy of 99.11% and training accuracy of 98.52 after carrying out 5-fold cross validation.

(b) Using gridsearch, the best accuracy was given by the hyperparameters : 

1. n(neighbours) = 1

2. p = 2

(c) This accuracy is very similar to than other hyperparamter combinations.We just choose the simpler model (which happens to be 1-neighbor solution here) as it is cheaper to compute even it was not the best performer. 
