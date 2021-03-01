
import numpy as np
from sklearn.cluster import KMeans as KMeansClustering
from MLalgorithms._Clustering import Clustering


class KMeans(Clustering):
	
	def __init__(self, n_clusters=8, n_init=10, max_iter=300, tol=0.0001, precompute_distances='auto', verbose=0, random_state=None, copy_x=True, n_jobs=None, algorithm='auto'):
		self.random_state = random_state
		self.max_iter = max_iter
		self.algorithm = algorithm
		self.tol = tol
		self.verbose = verbose
		self.n_clusters = n_clusters
		self.copy_x = copy_x
		self.precompute_distances = precompute_distances
		self.n_jobs = n_jobs
		self.n_init = n_init
		self.model = KMeansClustering(max_iter = self.max_iter,
			verbose = self.verbose,
			n_clusters = self.n_clusters,
			tol = self.tol,
			precompute_distances = self.precompute_distances,
			n_init = self.n_init,
			random_state = self.random_state,
			n_jobs = self.n_jobs,
			copy_x = self.copy_x,
			algorithm = self.algorithm)

	def fit(self, X, y, sample_weight=None):
		return self.model.fit(X=X,
			y=y,
			sample_weight=sample_weight)

	def predict(self, X, sample_weight=None):
		return self.model.predict(X=X,
			sample_weight=sample_weight)

