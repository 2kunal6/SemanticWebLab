
import numpy as np
from sklearn.cluster import MeanShift as MSClustering
from MLalgorithms._Clustering import Clustering


class MeanShift(Clustering):
	
	def __init__(self, bandwidth=None, seeds=None, bin_seeding=False, min_bin_freq=1, cluster_all=True, n_jobs=None, max_iter=300):
		self.seeds = seeds
		self.cluster_all = cluster_all
		self.n_jobs = n_jobs
		self.min_bin_freq = min_bin_freq
		self.bandwidth = bandwidth
		self.bin_seeding = bin_seeding
		self.max_iter = max_iter
		self.model = MSClustering(seeds = self.seeds,
			max_iter = self.max_iter,
			bandwidth = self.bandwidth,
			n_jobs = self.n_jobs,
			min_bin_freq = self.min_bin_freq,
			cluster_all = self.cluster_all,
			bin_seeding = self.bin_seeding)

	def predict(self, X):
		return self.model.predict(X=X)

	def fit(self, X, y):
		return self.model.fit(y=y,
			X=X)
