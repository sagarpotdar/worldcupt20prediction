# Worldcup T-20 Score prediction

Predict the score of World T20 matches using a machine learning algorithm.
The Scikit-Learn pipeline was used to make the code reusable. 
After evaluating several regression techniques,
the XgBoost Regressor was trained on the specified features.
The model was tested in terms of the R2 score on the test data set.
The model worked really well with just a little hyperparameter modification, yielding an R2 score of 0.946 and a Mean Absolute Error of 1.67
