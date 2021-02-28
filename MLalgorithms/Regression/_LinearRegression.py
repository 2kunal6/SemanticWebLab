
from sklearn.linear_model import LinearRegression as LR
from MLalgorithms._Regression import Regression


class LinearRegression(Regression):
	
	def __init__(self, fit_intercept=True, normalize=False, copy_x=True, n_jobs=None, positive=False):
		self.n_jobs = n_jobs
		self.positive = positive
		Regression.__init__(self, fit_intercept=fit_intercept, normalize=normalize, copy_x=copy_x)
		self.model = LR(n_jobs = self.n_jobs,
			positive = self.positive,
			copy_x = self.copy_x,
			fit_intercept = self.fit_intercept,
			normalize = self.normalize)

