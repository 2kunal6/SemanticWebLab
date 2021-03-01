
from sklearn.cluster import DBSCAN as DBSCANClustering
from MLalgorithms._Clustering import Clustering


class DBSCAN(Clustering):
	
	def __init__(self, eps=0.5, min_samples=5, metric='euclidean', metric_params=None, algorithm='auto', leaf_size=30, p=None, n_jobs=None):
		self.leaf_size = leaf_size
		self.eps = eps
		self.n_jobs = n_jobs
		self.min_samples = min_samples
		self.metric_params = metric_params
		self.algorithm = algorithm
		self.p = p
		self.metric = metric
		self.model = DBSCANClustering(eps = self.eps,
			p = self.p,
			leaf_size = self.leaf_size,
			n_jobs = self.n_jobs,
			algorithm = self.algorithm,
			metric_params = self.metric_params,
			min_samples = self.min_samples,
			metric = self.metric)

	def fit(self, X, y, sample_weight=None):
		return self.model.fit(X=X,
			sample_weight=sample_weight,
			y=y)

