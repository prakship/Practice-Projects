
## 1. Pipeline projects:

### (a) Titanic Classification

1. Used Logistic Regression as the baseline model for classification.

2. Created function for evaluating statistical significance(p-value).

3. Built separate pipelines for Numerical and categorical features.

4. Built the machine learning model in systematic method using pipelines.

5. Built multiple classifiers and carried out Hyperparameter tuning and results were:

6. Logistic regression[BASELINE] : Test accuracy = 79.9, p-value = 0.05

7. KNN algorithm : Test accuracy = 83.2, p-value = 0.03 

8. Naive Bayes : Test accuracy = 77.1, p-value = 0.00017

9. Support vector : Test accuracy = 81.6, p-value = 0.00

10. Stochastic Gradient : Test accuracy = 79.9 , p-value = 0.2953

11. Random forest : Test accuracy = 81.6, p-value = 0.007

12. Thus, we choose the best model as Support Vector Machine taking into consideration both test accuracy and the p-value. Closely follows Random Forest classifier.
