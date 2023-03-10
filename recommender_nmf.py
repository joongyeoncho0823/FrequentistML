# -*- coding: utf-8 -*-
"""recommender_nmf.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ko4zDVh-2Z9ARzn5NV4m_ndFNrs_CGS7
"""

#!pip install scikit-surprise

import surprise
from surprise import Dataset
from surprise.prediction_algorithms.matrix_factorization import NMF
from surprise.model_selection import GridSearchCV

# Use movielens-100K
# rating (1-5) from 943 users on 1682 movies.
data = Dataset.load_builtin("ml-100k")

param_grid = {"n_factors": [5, 10, 20, 40], "reg_pu": [0.01, 0.05, 0.08, 0.1], "reg_qi": [0.01, 0.05, 0.08, 0.1]}
gs = GridSearchCV(NMF, param_grid, measures=["rmse", "mae"], cv=5)

gs.fit(data)

# best RMSE score
print(gs.best_score["rmse"])

# combination of parameters that gave the best RMSE score
print(gs.best_params["rmse"])

model = gs.best_estimator['rmse']
model.fit(data.build_full_trainset())

"""Sample outputs"""

model.predict('1', '1682')