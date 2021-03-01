
from sklearn.tree import DecisionTreeRegressor as DTR
from MLalgorithms._Regression import Regression


class DecisionTreeRegressor(Regression):
	
	def predict(self, X, check_input=True):
		return self.model.predict(X=X,
			check_input=check_input)

	def __init__(self, criterion='mse', splitter='best', max_depth=None, min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features=None, random_state=None, max_leaf_nodes=None, min_impurity_decrease=0.0, min_impurity_split=None, ccp_alpha=0.0):
		self.min_samples_split = min_samples_split
		self.ccp_alpha = ccp_alpha
		self.random_state = random_state
		self.max_features = max_features
		self.splitter = splitter
		self.criterion = criterion
		self.min_impurity_decrease = min_impurity_decrease
		self.min_impurity_split = min_impurity_split
		self.max_leaf_nodes = max_leaf_nodes
		self.max_depth = max_depth
		self.min_samples_leaf = min_samples_leaf
		self.min_weight_fraction_leaf = min_weight_fraction_leaf
		self.model = DTR(splitter = self.splitter,
			min_samples_split = self.min_samples_split,
			max_features = self.max_features,
			min_impurity_decrease = self.min_impurity_decrease,
			random_state = self.random_state,
			ccp_alpha = self.ccp_alpha,
			criterion = self.criterion,
			min_impurity_split = self.min_impurity_split,
			max_depth = self.max_depth,
			min_samples_leaf = self.min_samples_leaf,
			max_leaf_nodes = self.max_leaf_nodes,
			min_weight_fraction_leaf = self.min_weight_fraction_leaf)

	def fit(self, X, y, sample_weight=None, check_input=True, X_idx_sorted='deprecated'):
		return self.model.fit(X=X,
			check_input=check_input,
			y=y,
			sample_weight=sample_weight,
			X_idx_sorted=X_idx_sorted)

