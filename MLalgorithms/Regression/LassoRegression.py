


from sklearn.linear_model import Lasso


class LassoRegression(Regression):
    
    def __init__(self, copy_X, n_jobs, normalize, fit_intercept, max_iter):
        self.max_iter = max_iter
		Regression.__init__(self, copy_X, n_jobs, normalize, fit_intercept)
		self.model = Lasso(max_iter = self.max_iter,
			n_jobs = self.n_jobs,
			fit_intercept = self.fit_intercept,
			copy_X = self.copy_X,
			normalize = self.normalize)

    