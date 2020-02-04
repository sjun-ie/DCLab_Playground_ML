from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.externals.six import StringIO
import numpy as np
import pandas as pd
import graphviz

# This code is originally acquired from https://towardsdatascience.com/decision-tree-in-python-b433ae57fb93


def main():
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y = pd.Categorical.from_codes(iris.target, iris.target_names)
    # X.head()
    y = pd.get_dummies(y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
    dt = tree.DecisionTreeClassifier()
    dt.fit(X_train, y_train)
    dot_data = tree.export_graphviz(dt, out_file=None, feature_names=iris.feature_names, class_names=iris.target_names,
                                    filled=True, rounded=True, special_characters=True)
    graph = graphviz.Source(dot_data)
    graph
    print("End of Program")


if __name__ == '__main__':
    main()
