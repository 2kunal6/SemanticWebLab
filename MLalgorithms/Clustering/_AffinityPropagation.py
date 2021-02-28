
import numpy as np
from sklearn.cluster import AffinityPropagation as APClustering
from MLalgorithms._Clustering import Clustering


class AffinityPropagation(Clustering):
	
	def __init__(self, damping=0.5, max_iter=200, convergence_iter=15, copy=True, preference=None, affinity='euclidean', verbose=False, random_state='warn'):
		self.copy = copy
		self.convergence_iter = convergence_iter
		self.max_iter = max_iter
		self.verbose = verbose
		self.damping = damping
		self.random_state = random_state
		self.preference = preference
		self.affinity = affinity
		self.model = APClustering(preference = self.preference,
			random_state = self.random_state,
			max_iter = self.max_iter,
			affinity = self.affinity,
			convergence_iter = self.convergence_iter,
			copy = self.copy,
			verbose = self.verbose,
			damping = self.damping)

	def predict(self, X):
		return self.model.predict(X=X)

	def fit(self, X, y):
		return self.model.fit(y=y,
			X=X)
