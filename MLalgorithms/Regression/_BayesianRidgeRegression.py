
from sklearn.linear_model import BayesianRidge
from MLalgorithms._Regression import Regression


class BayesianRidgeRegression(Regression):
	
	def predict(self, return_std=False):
		return self.model.predict(return_std=return_std)

	def __init__(self, n_iter=300, tol=0.001, alpha_1=1e-06, alpha_2=1e-06, lambda_1=1e-06, lambda_2=1e-06, alpha_init=None, lambda_init=None, compute_score=False, fit_intercept=True, normalize=False, copy_x=True, verbose=False):
		self.verbose = verbose
		self.lambda_1 = lambda_1
		self.lambda_init = lambda_init
		self.compute_score = compute_score
		self.tol = tol
		self.alpha_2 = alpha_2
		self.alpha_init = alpha_init
		self.n_iter = n_iter
		self.alpha_1 = alpha_1
		self.lambda_2 = lambda_2
		Regression.__init__(self, copy_x=copy_x, fit_intercept=fit_intercept, normalize=normalize)
		self.model = BayesianRidge(lambda_2 = self.lambda_2,
			copy_x = self.copy_x,
			compute_score = self.compute_score,
			normalize = self.normalize,
			alpha_2 = self.alpha_2,
			alpha_init = self.alpha_init,
			fit_intercept = self.fit_intercept,
			verbose = self.verbose,
			lambda_init = self.lambda_init,
			n_iter = self.n_iter,
			lambda_1 = self.lambda_1,
			alpha_1 = self.alpha_1,
			tol = self.tol)

