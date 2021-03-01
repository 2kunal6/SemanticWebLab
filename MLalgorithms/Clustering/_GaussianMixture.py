
import numpy as np
from sklearn.mixture import GaussianMixture as GMClustering
from MLalgorithms._Clustering import Clustering


class GaussianMixture(Clustering):
	
	def fit(self, X, y):
		return self.model.fit(y=y,
			X=X)

	def __init__(self, n_components=1, covariance_type='full', tol=0.001, reg_covar=1e-06, max_iter=100, n_init=1, init_params='kmeans', weights_init=None, means_init=None, precisions_init=None, random_state=None, warm_start=False, verbose=0, verbose_interval=10):
		self.init_params = init_params
		self.covariance_type = covariance_type
		self.weights_init = weights_init
		self.warm_start = warm_start
		self.tol = tol
		self.verbose = verbose
		self.verbose_interval = verbose_interval
		self.max_iter = max_iter
		self.reg_covar = reg_covar
		self.random_state = random_state
		self.n_components = n_components
		self.precisions_init = precisions_init
		self.n_init = n_init
		self.means_init = means_init
		self.model = GMClustering(max_iter = self.max_iter,
			means_init = self.means_init,
			weights_init = self.weights_init,
			warm_start = self.warm_start,
			n_init = self.n_init,
			reg_covar = self.reg_covar,
			verbose = self.verbose,
			random_state = self.random_state,
			init_params = self.init_params,
			covariance_type = self.covariance_type,
			n_components = self.n_components,
			verbose_interval = self.verbose_interval,
			tol = self.tol,
			precisions_init = self.precisions_init)

	def predict(self, X):
		return self.model.predict(X=X)

