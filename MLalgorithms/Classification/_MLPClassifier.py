
from sklearn.neural_network import MLPClassifier as MLPC
from MLalgorithms._Classification import Classification


class MLPClassifier(Classification):
	
	def predict(self, X):
		return self.model.predict(X=X)

	def __init__(self, hidden_layer_sizes=100, activation='relu', solver='adam', alpha=0.0001, batch_size='auto', learning_rate='constant', learning_rate_init=0.001, power_t=0.5, max_iter=200, shuffle=True, random_state=None, tol=0.0001, warm_start=False, momentum=0.9, nesterovs_momentum=True, early_stopping=False, validation_fraction=0.1, beta_1=0.9, beta_2=0.999, epsilon=1e-08, n_iter_no_change=10, max_fun=15000):
		self.learning_rate_init = learning_rate_init
		self.momentum = momentum
		self.alpha = alpha
		self.early_stopping = early_stopping
		self.learning_rate = learning_rate
		self.max_iter = max_iter
		self.activation = activation
		self.validation_fraction = validation_fraction
		self.beta_1 = beta_1
		self.random_state = random_state
		self.solver = solver
		self.max_fun = max_fun
		self.warm_start = warm_start
		self.hidden_layer_sizes = hidden_layer_sizes
		self.shuffle = shuffle
		self.n_iter_no_change = n_iter_no_change
		self.batch_size = batch_size
		self.beta_2 = beta_2
		self.epsilon = epsilon
		self.power_t = power_t
		self.tol = tol
		self.nesterovs_momentum = nesterovs_momentum
		self.model = MLPC(power_t = self.power_t,
			batch_size = self.batch_size,
			random_state = self.random_state,
			n_iter_no_change = self.n_iter_no_change,
			activation = self.activation,
			hidden_layer_sizes = self.hidden_layer_sizes,
			nesterovs_momentum = self.nesterovs_momentum,
			early_stopping = self.early_stopping,
			shuffle = self.shuffle,
			solver = self.solver,
			learning_rate_init = self.learning_rate_init,
			learning_rate = self.learning_rate,
			beta_1 = self.beta_1,
			alpha = self.alpha,
			tol = self.tol,
			momentum = self.momentum,
			warm_start = self.warm_start,
			epsilon = self.epsilon,
			beta_2 = self.beta_2,
			max_iter = self.max_iter,
			max_fun = self.max_fun,
			validation_fraction = self.validation_fraction)

	def fit(self, X, y):
		return self.model.fit(X=X,
			y=y)

