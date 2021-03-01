from MLalgorithms.Classification._DecisionTreeClassifier import DecisionTreeClassifier
from MLalgorithms.Metrics._confusion_matrix import confusion_matrix
from MLalgorithms.Metrics._classification_report import classification_report
from MLalgorithms.Metrics._hinge_loss import hinge_loss
from MLalgorithms.Metrics._jaccard_score import jaccard_score
from MLalgorithms.Metrics._log_loss import log_loss

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


def test():
    """ Example for decision tree classifier."""
    # Step 1: Load the dataset.
    X, y = load_iris(return_X_y=True)

    # Step 2: Split the dataset into train and test.
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

    # Step 3: Create object of an adapter with default DecisionTreeClassifier.
    adapterObj = DecisionTreeClassifier()

    # Step 4: Call the fit method the adapter.
    adapterObj.fit(X_train, y_train)

    # Step 5: Call the predict method of the adapter.
    y_pred = adapterObj.predict(X_test)

    """ Step 6: In this example, we apply confusion matrix. Create an object of the confusion_matrix class.
        Please don't rely on parameter positions, as the code is autogenerated. 
        Instead always pass the arguments like below.
    """
    metricsAdapterObj = confusion_matrix(y_true=y_test, y_pred=y_pred)

    # Step 7: The result of the metrics can be accessed by adapterobj.value
    print(metricsAdapterObj.value)

    """ Step 8: To access other methods defined in scikit which are not part of adapter.
        these methods can be called like below.
    """
    print("Tree depth: ", adapterObj.model.get_depth())


if __name__ == "__main__":
    test()
