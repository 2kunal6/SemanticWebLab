
from sklearn.linear_model import Ridge
from MLalgorithms._Regression import Regression


class RidgeRegression(Regression):
	
	def __init__(self, alpha=1.0, fit_intercept=True, normalize=False, copy_X=True, max_iter=None, tol=0.001, solver='auto', random_state=None):
		self.random_state = random_state
		self.max_iter = max_iter
		self.solver = solver
		self.alpha = alpha
		self.tol = tol
		Regression.__init__(self, normalize=normalize, copy_X=copy_X, fit_intercept=fit_intercept)
		self.model = Ridge(fit_intercept = self.fit_intercept,
			copy_X = self.copy_X,
			random_state = self.random_state,
			normalize = self.normalize,
			solver = self.solver,
			alpha = self.alpha,
			tol = self.tol,
			max_iter = self.max_iter)

