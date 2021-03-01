
from sklearn.ensemble import AdaBoostRegressor as ABR
from MLalgorithms._Regression import Regression


class AdaBoostRegressor(Regression):
	
	def predict(self, X):
		return self.model.predict(X=X)

	def fit(self, X, y, sample_weight=None):
		return self.model.fit(y=y,
			sample_weight=sample_weight,
			X=X)

	def __init__(self, base_estimator=None, n_estimators=50, learning_rate=1.0, random_state=None):
		self.n_estimators = n_estimators
		self.base_estimator = base_estimator
		self.learning_rate = learning_rate
		self.random_state = random_state
		self.model = ABR(n_estimators = self.n_estimators,
			random_state = self.random_state,
			base_estimator = self.base_estimator,
			learning_rate = self.learning_rate)

