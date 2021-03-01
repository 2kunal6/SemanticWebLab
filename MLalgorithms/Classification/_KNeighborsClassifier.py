
from sklearn.neighbors import KNeighborsClassifier as KNC
from MLalgorithms._Classification import Classification


class KNeighborsClassifier(Classification):
	
	def fit(self, X, y):
		return self.model.fit(y=y,
			X=X)

	def __init__(self, n_neighbors=5, weights='uniform', algorithm='auto', leaf_size=30, p=2, metric='minkowski', metric_params=None, n_jobs=None):
		self.n_neighbors = n_neighbors
		self.leaf_size = leaf_size
		self.metric_params = metric_params
		self.weights = weights
		self.p = p
		self.algorithm = algorithm
		self.n_jobs = n_jobs
		self.metric = metric
		self.model = KNC(n_neighbors = self.n_neighbors,
			weights = self.weights,
			leaf_size = self.leaf_size,
			metric_params = self.metric_params,
			p = self.p,
			n_jobs = self.n_jobs,
			algorithm = self.algorithm,
			metric = self.metric)

	def predict(self, X):
		return self.model.predict(X=X)

