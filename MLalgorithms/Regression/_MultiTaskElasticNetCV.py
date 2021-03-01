
from sklearn.linear_model import MultiTaskElasticNetCV as MTENCV
from MLalgorithms._Regression import Regression


class MultiTaskElasticNetCV(Regression):
	
	def predict(self, X):
		return self.model.predict(X=X)

	def fit(self, X, y):
		return self.model.fit(y=y,
			X=X)

	def __init__(self, l1_ratio=0.5, eps=0.001, n_alphas=None, alphas=None, fit_intercept=True, normalize=False, max_iter=100, tol=0.0001, cv=None, copy_X=True, verbose=0, n_jobs=None, random_state=None, selection='cyclic'):
		self.normalize = normalize
		self.tol = tol
		self.fit_intercept = fit_intercept
		self.verbose = verbose
		self.copy_X = copy_X
		self.eps = eps
		self.selection = selection
		self.l1_ratio = l1_ratio
		self.max_iter = max_iter
		self.n_alphas = n_alphas
		self.n_jobs = n_jobs
		self.random_state = random_state
		self.cv = cv
		self.alphas = alphas
		self.model = MTENCV(l1_ratio = self.l1_ratio,
			copy_X = self.copy_X,
			alphas = self.alphas,
			max_iter = self.max_iter,
			cv = self.cv,
			verbose = self.verbose,
			random_state = self.random_state,
			tol = self.tol,
			n_alphas = self.n_alphas,
			n_jobs = self.n_jobs,
			eps = self.eps,
			fit_intercept = self.fit_intercept,
			selection = self.selection,
			normalize = self.normalize)

