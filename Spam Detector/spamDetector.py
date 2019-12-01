import pandas as pd
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import AdaBoostClassifier

data = pd.read_csv('spambase.data').as_matrix()

np.random.shuffle(data)

#Dataset
X= data[:, :48]
Y= data[:, -1]

#Division of dataset
Xtrain = X[:-100,]
Ytrain = Y[:-100,]
Xtest = X[-100:,]
Ytest = Y[-100:,]

#fitting the model 1 --- Naive Bayes Classifier
model = MultinomialNB()
model.fit(Xtrain, Ytrain)
print ("Classification rate for NB:", model.score(Xtest, Ytest))

#fitting the model 2 --- AdaBoost Classifier
model1 = AdaBoostClassifier()
model.fit(Xtrain, Ytrain)
print ("Classification rate for Adaboost:", model.score(Xtest, Ytest))
