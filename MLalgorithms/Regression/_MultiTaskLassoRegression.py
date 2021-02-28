
from sklearn.linear_model import MultiTaskLasso as MLTR
from MLalgorithms._Regression import Regression


class MultiTaskLassoRegression(Regression):
	
	def __init__(self, alpha=1.0, fit_intercept=True, normalize=False, copy_x=True, max_iter=None, tol=0.001, warm_start=False, random_state=None, selection='cyclic'):
		self.selection = selection
		self.max_iter = max_iter
		self.tol = tol
		self.warm_start = warm_start
		self.alpha = alpha
		self.random_state = random_state
		Regression.__init__(self, fit_intercept=fit_intercept, normalize=normalize, copy_x=copy_x)
		self.model = MLTR(random_state = self.random_state,
			max_iter = self.max_iter,
			tol = self.tol,
			selection = self.selection,
			warm_start = self.warm_start,
			copy_x = self.copy_x,
			alpha = self.alpha,
			fit_intercept = self.fit_intercept,
			normalize = self.normalize)

	def predict(self, X):
		return self.model.predict(X=X)

	def fit(self, X, y):
		return self.model.fit(y=y,
			X=X)
