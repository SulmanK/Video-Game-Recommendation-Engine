#--------------------- Packages
from model.tf_idf import tf_idf_inputs, tf
from sklearn.decomposition import TruncatedSVD

#--------------------- SVD
"""Function to run and store the Singular Value Decomposition (model parameters and transformation of dataframe)."""
tsv = TruncatedSVD(n_components = 335, algorithm = 'randomized', n_iter = 5, random_state = 7)
svd_inputs = tsv.fit_transform(tf_idf_inputs)