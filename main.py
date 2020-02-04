from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.externals.six import StringIO
from sklearn.tree import export_graphviz
import numpy as np
import pandas as pd
import graphviz


# This code is origianlly acquired from https://towardsdatascience.com/decision-tree-in-python-b433ae57fb93
def decision_tree():
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y = pd.Categorical.from_codes(iris.target, iris.target_names)
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
    dt = DecisionTreeClassifier()
    dt.fit(X_train, y_train)
    dot_data = DecisionTreeClassifier.export_graphviz(dt, out_file=None)
    graph = graphviz.Source(dot_data)
    graph.render("iris")


def main():
    print("End of Program")


if __name__ == '__main__':
    main()
