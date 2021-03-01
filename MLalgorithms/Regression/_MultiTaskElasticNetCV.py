
from sklearn.linear_model import MultiTaskElasticNetCV as MTENCV
from MLalgorithms._Regression import Regression


class MultiTaskElasticNetCV(Regression):
	
	def __init__(self, l1_ratio=0.5, eps=0.001, n_alphas=None, alphas=None, fit_intercept=True, normalize=False, max_iter=100, tol=0.0001, cv=None, copy_X=True, verbose=0, n_jobs=None, random_state=None, selection='cyclic'):
		self.n_alphas = n_alphas
		self.l1_ratio = l1_ratio
		self.random_state = random_state
		self.selection = selection
		self.verbose = verbose
		self.fit_intercept = fit_intercept
		self.tol = tol
		self.alphas = alphas
		self.copy_X = copy_X
		self.eps = eps
		self.cv = cv
		self.max_iter = max_iter
		self.normalize = normalize
		self.n_jobs = n_jobs
		self.model = MTENCV(normalize = self.normalize,
			copy_X = self.copy_X,
			random_state = self.random_state,
			fit_intercept = self.fit_intercept,
			eps = self.eps,
			alphas = self.alphas,
			max_iter = self.max_iter,
			n_alphas = self.n_alphas,
			selection = self.selection,
			verbose = self.verbose,
			l1_ratio = self.l1_ratio,
			cv = self.cv,
			tol = self.tol,
			n_jobs = self.n_jobs)

	def predict(self, X):
		return self.model.predict(X=X)

	def fit(self, X, y):
		return self.model.fit(y=y,
			X=X)

