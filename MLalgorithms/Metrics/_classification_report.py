
from sklearn.metrics import classification_report as CR
from MLalgorithms._Metrics import Metrics


class classification_report(Metrics):
	
	def __init__(self, y_true, y_pred, labels=None, target_names=None, sample_weight=None, digits=2, output_dict=False, zero_division='warn'):
		self.y_pred = y_pred
		self.zero_division = zero_division
		self.target_names = target_names
		self.output_dict = output_dict
		self.digits = digits
		Metrics.__init__(self, y_true=y_true, sample_weight=sample_weight, labels=labels)
		self.value = CR(output_dict = self.output_dict,
			digits = self.digits,
			target_names = self.target_names,
			y_true = self.y_true,
			labels = self.labels,
			y_pred = self.y_pred,
			sample_weight = self.sample_weight,
			zero_division = self.zero_division)

