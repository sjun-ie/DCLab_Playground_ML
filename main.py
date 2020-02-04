from sklearn.datasets import load_iris
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn import metrics
from sklearn.externals.six import StringIO
import numpy as np
import pandas as pd
import graphviz
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

# This code is originally acquired from https://towardsdatascience.com/decision-tree-in-python-b433ae57fb93


def wine():
    wine = load_wine()
    X = pd.DataFrame(wine.data, columns=wine.feature_names)
    y = pd.Categorical.from_codes(wine.target, wine.target_names)
    y = pd.get_dummies(y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
    dt = tree.DecisionTreeClassifier()
    dt.fit(X_train, y_train)

    y_pred = dt.predict(X_test)
    print("Accuracy:", metrics.accuracy_score(y_test, y_pred))


def iris():
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y = pd.Categorical.from_codes(iris.target, iris.target_names)
    # X['ratio'] = X[['sepal length (cm)', 'sepal width (cm)']].apply(lambda row: row['sepal length (cm)'] < row['sepal width (cm)'], axis=1)
    # X['sepal ratio'] = X['sepal length (cm)'] / X['sepal width (cm)']
    # X['petal ratio'] = X['petal length (cm)'] / X['petal width (cm)']
    y = pd.get_dummies(y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
    dt = tree.DecisionTreeClassifier(max_depth=2, max_leaf_nodes=4)
    dt.fit(X_train, y_train)

    y_pred = dt.predict(X_test)
    print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
    # dot_data = tree.export_graphviz(dt, out_file=None, feature_names=iris.feature_names, class_names=iris.target_names,filled=True, rounded=True, special_characters=True)
    # graph = graphviz.Source(dot_data)
    # graph.render()


def main():
    wine()
    iris()
    print("End of Program")


if __name__ == '__main__':
    main()