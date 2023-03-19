from sklearn.model_selection import train_test_split
#from sklearn.externals import joblib
import joblib
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
import pickle
import sklearn

# load the iris datasets as an example 
dataset = datasets.load_iris()

# make predictions
X = dataset.data 
Y = dataset.target
test_size = 0.33
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size)


# fit a logistic regression model to the data
model = LogisticRegression(max_iter=1000)
model.fit(X_train, Y_train)

# 2- Using joblib
#  - Save the model to disk using joblib
joblib_fname = 'logreg_joblib.model'
scikit_ver = sklearn.__version__
joblib.dump(model, "model_{version}.pkl".format(version = scikit_ver))

# - Load the model from disk
joblib_model = joblib.load("model_{version}.pkl".format(version = scikit_ver))

# Sanity checks: Make prediction with all the saved models on unseen data.
result_1 = model.score(X_test, Y_test) 
result_3 = joblib_model.score(X_test, Y_test) # saved using joblib

print("Result: {}".format(result_1))
assert result_1 == result_3
