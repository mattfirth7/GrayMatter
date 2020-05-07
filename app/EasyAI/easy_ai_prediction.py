import os
import numpy as np
from sklearn import preprocessing, neighbors, svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
import pickle
from app.EasyAI import easy_validation

def prediction(input_filename, model_name):
    clf = pickle.load(open('C:/Users/Matt/Documents/graymatter-flask/assets/models/' + model_name, 'rb'))
    dataset = np.genfromtxt('C:/Users/Matt/Documents/graymatter-flask/assets/tempdata/'+input_filename, delimiter = ',', skip_header = 1)
    predictions = clf.predict(dataset)
    return predictions