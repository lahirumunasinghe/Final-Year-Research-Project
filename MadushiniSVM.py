# Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading dataset and view a few records.
dataset = pd.read_csv('/home/lahiru/Documents/FYP Madushini/finalMadushini.csv')
dataset.shape

dataset.head()

dataset.describe()

dataset.info()

dataset.hist(figsize=(10,8))

dataset.plot(kind= 'box' , subplots=True, layout=(8,8), sharex=False, sharey=False, figsize=(10,8))

# Correlation plot
Corr=dataset[dataset.columns].corr()
sns.heatmap(Corr, annot=True)

# Split into Input and Output.
attributes = list(dataset.columns[:46])
X = dataset[attributes].values
y= dataset['Label'].values

# Scale input dataset.
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X = sc_X.fit_transform(X)

from sklearn import preprocessing
X = preprocessing.normalize(X)

# Split into train and test sets.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state =0)

# Import suite of algorithms.
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression, RidgeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis, QuadraticDiscriminantAnalysis
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, BaggingClassifier, GradientBoostingClassifier
from sklearn.calibration import CalibratedClassifierCV

models = []
models.append(("SVM Linear",SVC(kernel="linear")))
models.append(("SVM RBF",SVC(kernel="rbf")))
models.append(("LinearSVC",LinearSVC()))

# Find accuracy of models.
results = []
for name,model in models:
    kfold = KFold(n_splits=10, random_state=0)
    cv_result = cross_val_score(model,X_train,y_train, cv = kfold,scoring = "accuracy")
    results.append(tuple([name,cv_result.mean(), cv_result.std()]))

results.sort(key=lambda x: x[1], reverse = True)
for i in range(len(results)):
    print('{:20s} {:2.2f} (+/-) {:2.2f} '.format(results[i][0] , results[i][1] * 100, results[i][2] * 100))

from sklearn.model_selection import GridSearchCV
model = SVC()
paramaters = [
             {'C' : [0.01, 0.1, 1, 10, 100, 1000], 'kernel' : ['linear']}
             ]
grid_search = GridSearchCV(estimator = model,
                           param_grid = paramaters,
                           scoring = 'accuracy',
                           cv = 10,
                           n_jobs = -1)
grid_search = grid_search.fit(X_train, y_train)
best_accuracy = grid_search.best_score_
best_parameters = grid_search.best_params_

print('Best accuracy : ', grid_search.best_score_)
print('Best parameters :', grid_search.best_params_  )

# Predict output for test set.
final_model = SVC(C = 1, kernel = 'linear')
final_model.fit(X_train, y_train)
y_pred = final_model.predict(X_test)

from sklearn.metrics import confusion_matrix, accuracy_score
cf = confusion_matrix(y_test, y_pred)
print(cf)
print(accuracy_score(y_test, y_pred) * 100)

#Update. 19Jun2017. Included classiifcation report.
from sklearn.metrics import classification_report
report = classification_report(y_test, y_pred)
print(report)

import pickle
filename = 'finalized_modelMadushini.sav'
pickle.dump(final_model, open(filename, 'wb'))

# load the model from disk
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, y_test)
print(result)
