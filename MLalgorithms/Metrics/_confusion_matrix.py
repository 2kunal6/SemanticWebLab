
from sklearn.metrics import confusion_matrix as CM
from MLalgorithms._Metrics import Metrics


class confusion_matrix(Metrics):
	
	def __init__(self, y_true, y_pred, labels=None, sample_weight=None, normalize=None):
		self.y_pred = y_pred
		self.normalize = normalize
		Metrics.__init__(self, labels=labels, y_true=y_true, sample_weight=sample_weight)
		self.value = CM(y_pred = self.y_pred,
			y_true = self.y_true,
			sample_weight = self.sample_weight,
			normalize = self.normalize,
			labels = self.labels)

