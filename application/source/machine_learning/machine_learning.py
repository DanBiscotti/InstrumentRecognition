# This module contains functions which trains learning algorithms and saves them using joblib

# Libraries
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.externals import joblib

def knn(x_training,y_training,k,distance,savename):
    classifier = KNeighborsClassifier(n_neighbors=k,metric=distance)
    classifier.fit(x_training,y_training)
    joblib.dump(classifier,"/home/dan/university/project/source/models/"+savename)
    return classifier

def svm(
