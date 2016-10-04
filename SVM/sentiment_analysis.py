__author__ = 'arathi'

import csv

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import BernoulliNB
from sklearn.svm import SVC
from sklearn.svm import SVR
from sklearn import cross_validation
from sklearn.metrics import classification_report
import numpy as np
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

# review.csv contains two columns
# first column is the review content (quoted)
# second column is the assigned sentiment (positive or negative)
def load_file():
    with open('comments.csv') as csv_file:
        reader = csv.reader(csv_file,delimiter=",",quotechar='"')
        reader.__next__()
        data =[]
        target = []
        for row in reader:
            # skip missing data
            if row[0] and row[1]:
                data.append(row[0])
                target.append(row[1])

        return data,target

# preprocess creates the term frequency matrix for the review data set
def preprocess():
    data,target = load_file()
    count_vectorizer = CountVectorizer(binary='true')
    data = count_vectorizer.fit_transform(data)
    tfidf_data = TfidfTransformer(use_idf=False).fit_transform(data)

    return tfidf_data

def learn_model(data,target):
    # preparing data for split validation. 60% training, 40% test
    # X, y = make_classification(n_features=2, n_redundant=0, n_informative=2,
    #                            random_state=1, n_clusters_per_class=1)
    data_train,data_test,target_train,target_test = cross_validation.train_test_split(data,target,test_size=0.4,random_state=43)
    # classifier = BernoulliNB().fit(data_train,target_train)
    classifier = SVC(gamma=.01, C=100.)
    # classifier = SVR(gamma=1, C=10.)
    classifier.fit(data_train,target_train)
    predicted = classifier.predict(data_test)
    evaluate_model(target_test,predicted)

    # Create and fit an AdaBoosted decision tree
    bdt = AdaBoostClassifier(DecisionTreeClassifier(max_depth=4),
                             algorithm="SAMME",
                             n_estimators=200)
    #bdt = AdaBoostClassifier(SVC(gamma=.01, C=100.), algorithm="SAMME",n_estimators=200)

    bdt.fit(data_train, target_train)
    predicted = bdt.predict(data_test)
    evaluate_model(target_test, predicted)

    num_folds = 10
    # num_instances = len(data_train)
    seed = 7
    num_trees = 100
    max_features = 3
    # kfold = cross_validation.KFold(n=num_instances, n_folds=num_folds, random_state=seed)
    model = RandomForestClassifier(n_estimators=num_trees, max_features=max_features)
    model.fit(data_train, target_train)
    predicted = model.predict(data_test)
    evaluate_model(target_test, predicted)


# read more about model evaluation metrics here
# http://scikit-learn.org/stable/modules/model_evaluation.html
def evaluate_model(target_true,target_predicted):
    print (classification_report(target_true,target_predicted))
    print ("The accuracy score is {:.2%}".format(accuracy_score(target_true,target_predicted)))

def main():
    data,target = load_file()
    tf_idf = preprocess()
    learn_model(tf_idf,target)


main()

