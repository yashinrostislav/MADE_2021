import numpy as np
from sklearn.base import BaseEstimator


def entropy(y):  
    """
    Computes entropy of the provided distribution. Use log(value + eps) for numerical stability
    
    Parameters
    ----------
    y : np.array of type float with shape (n_objects, n_classes)
        One-hot representation of class labels for corresponding subset
    
    Returns
    -------
    float
        Entropy of the provided subset
    """
    EPS = 0.0005

    freqs = np.sum(y, axis=0) / y.shape[0]
    probas = np.sum(-freqs * np.log(freqs + EPS))

    return probas

    
def gini(y):
    """
    Computes the Gini impurity of the provided distribution
    
    Parameters
    ----------
    y : np.array of type float with shape (n_objects, n_classes)
        One-hot representation of class labels for corresponding subset
    
    Returns
    -------
    float
        Gini impurity of the provided subset
    """

    freqs = np.sum(y, axis=0) / y.shape[0]
    probas = 1 - np.sum(freqs**2)

    return probas
    
def variance(y):
    """
    Computes the variance the provided target values subset
    
    Parameters
    ----------
    y : np.array of type float with shape (n_objects, 1)
        Target values vector
    
    Returns
    -------
    float
        Variance of the provided target vector
    """
    var = np.mean((y - np.mean(y))**2)

    return var

def mad_median(y):
    """
    Computes the mean absolute deviation from the median in the
    provided target values subset
    
    Parameters
    ----------
    y : np.array of type float with shape (n_objects, 1)
        Target values vector
    
    Returns
    -------
    float
        Mean absolute deviation from the median in the provided vector
    """
    median = np.mean(np.abs(y - np.median(y)))
    return median


def one_hot_encode(n_classes, y):
    y_one_hot = np.zeros((len(y), n_classes), dtype=float)
    y_one_hot[np.arange(len(y)), y.astype(int)[:, 0]] = 1.
    return y_one_hot


def one_hot_decode(y_one_hot):
    return y_one_hot.argmax(axis=1)[:, None]


class Node:
    """
    This class is provided "as is" and it is not mandatory to it use in your code.
    """
    def __init__(self, feature_index=None, threshold=None, proba=0):
        self.feature_index = feature_index
        self.value = threshold
        self.proba = proba
        self.left_child = None
        self.right_child = None
        
        
class DecisionTree(BaseEstimator):
    all_criterions = {
        'gini': (gini, True), # (criterion, classification flag)
        'entropy': (entropy, True),
        'variance': (variance, False),
        'mad_median': (mad_median, False)
    }

    def __init__(self, n_classes=None, max_depth=np.inf, min_samples_split=2, 
                 criterion_name='gini', debug=False):

        assert criterion_name in self.all_criterions.keys(), 'Criterion name must be on of the following: {}'.format(self.all_criterions.keys())
        
        self.n_classes = n_classes
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.criterion_name = criterion_name

        self.depth = 0
        self.root = None # Use the Node class to initialize it later
        self.debug = debug

        
        
    def make_split(self, feature_index, threshold, X_subset, y_subset):
        """
        Makes split of the provided data subset and target values using provided feature and threshold
        
        Parameters
        ----------
        feature_index : int
            Index of feature to make split with

        threshold : float
            Threshold value to perform split

        X_subset : np.array of type float with shape (n_objects, n_features)
            Feature matrix representing the selected subset

        y_subset : np.array of type float with shape (n_objects, n_classes) in classification 
                   (n_objects, 1) in regression 
            One-hot representation of class labels for corresponding subset
        
        Returns
        -------
        (X_left, y_left) : tuple of np.arrays of same type as input X_subset and y_subset
            Part of the providev subset where selected feature x^j < threshold
        (X_right, y_right) : tuple of np.arrays of same type as input X_subset and y_subset
            Part of the providev subset where selected feature x^j >= threshold
        """

        X_left = X_subset[X_subset[:, feature_index] < threshold]
        X_right = X_subset[X_subset[:, feature_index] >= threshold]

        y_left = y_subset[X_subset[:, feature_index] < threshold]
        y_right = y_subset[X_subset[:, feature_index] >= threshold]

        return (X_left, y_left), (X_right, y_right)

    
    def make_split_only_y(self, feature_index, threshold, X_subset, y_subset):
        """
        Split only target values into two subsets with specified feature and threshold
        
        Parameters
        ----------
        feature_index : int
            Index of feature to make split with

        threshold : float
            Threshold value to perform split

        X_subset : np.array of type float with shape (n_objects, n_features)
            Feature matrix representing the selected subset

        y_subset : np.array of type float with shape (n_objects, n_classes) in classification 
                   (n_objects, 1) in regression 
            One-hot representation of class labels for corresponding subset
        
        Returns
        -------
        y_left : np.array of type float with shape (n_objects_left, n_classes) in classification 
                   (n_objects, 1) in regression 
            Part of the provided subset where selected feature x^j < threshold

        y_right : np.array of type float with shape (n_objects_right, n_classes) in classification 
                   (n_objects, 1) in regression 
            Part of the provided subset where selected feature x^j >= threshold
        """

        y_left = y_subset[X_subset[:, feature_index] < threshold]
        y_right = y_subset[X_subset[:, feature_index] >= threshold]
        
        return y_left, y_right


    def choose_best_split(self, X_subset, y_subset):
        """
        Greedily select the best feature and best threshold w.r.t. selected criterion
        
        Parameters
        ----------
        X_subset : np.array of type float with shape (n_objects, n_features)
            Feature matrix representing the selected subset

        y_subset : np.array of type float with shape (n_objects, n_classes) in classification 
                   (n_objects, 1) in regression 
            One-hot representation of class labels or target values for corresponding subset
        
        Returns
        -------
        feature_index : int
            Index of feature to make split with

        threshold : float
            Threshold value to perform split

        """
        best_reduction = -np.inf
        best_feature_index = -1
        best_threshold = -1

        n_features = X_subset.shape[1]

        for feature_index in range(n_features):
            for threshold in self.threshholds[feature_index]:
                y_left, y_right = self.make_split_only_y(feature_index,
                                                    threshold,
                                                    X_subset,
                                                    y_subset)
                if y_left.shape[0] == 0 or y_right.shape[0] == 0:
                    continue
                reduction = self.criterion(y_subset) - self.criterion(y_left) * y_left.shape[0] / y_subset.shape[0] - self.criterion(y_right) * y_right.shape[0] / y_subset.shape[0]
                if reduction > best_reduction:
                    best_reduction = reduction
                    best_threshold = threshold
                    best_feature_index = feature_index

        return best_feature_index, best_threshold
    
    def make_tree(self, X_subset, y_subset, depth=1):
        """
        Recursively builds the tree
        
        Parameters
        ----------
        X_subset : np.array of type float with shape (n_objects, n_features)
            Feature matrix representing the selected subset

        y_subset : np.array of type float with shape (n_objects, n_classes) in classification 
                   (n_objects, 1) in regression 
            One-hot representation of class labels or target values for corresponding subset
        
        Returns
        -------
        root_node : Node class instance
            Node of the root of the fitted tree
        """

        new_node = Node()

        if depth == self.max_depth or X_subset.shape[0] < \
                    self.min_samples_split or self.criterion(y_subset) == 0:
            if self.classification:
                freqs = np.sum(y_subset, axis = 0)
                new_node.probs = freqs / np.sum(freqs)
                new_node.value = np.argmax(new_node.probs)
            else:
                new_node.value = np.mean(y_subset)
            return new_node

        feature_index, threshold = self.choose_best_split(X_subset, y_subset)
        new_node.feature_index = feature_index
        new_node.threshold = threshold

        (X_left, y_left), (X_right, y_right) = self.make_split(feature_index, threshold, X_subset, y_subset)
        if y_left.shape[0] == 0 or y_right.shape[0] == 0:
            if self.classification:
                freqs = np.sum(y_subset, axis = 0)
                new_node.probs = freqs / np.sum(freqs)
                new_node.value = np.argmax(new_node.probs)
            else:
                new_node.value = np.mean(y_subset)
        else:
            new_node.left_child = self.make_tree(X_left, y_left, depth + 1)
            new_node.right_child = self.make_tree(X_right, y_right, depth + 1)

        return new_node
        
    def fit(self, X, y):
        """
        Fit the model from scratch using the provided data
        
        Parameters
        ----------
        X : np.array of type float with shape (n_objects, n_features)
            Feature matrix representing the data to train on

        y : np.array of type int with shape (n_objects, 1) in classification 
                   of type float with shape (n_objects, 1) in regression 
            Column vector of class labels in classification or target values in regression
        
        """
        assert len(y.shape) == 2 and len(y) == len(X), 'Wrong y shape'
        self.criterion, self.classification = self.all_criterions[self.criterion_name]
        if self.classification:
            if self.n_classes is None:
                self.n_classes = len(np.unique(y))
            y = one_hot_encode(self.n_classes, y)

        self.threshholds = []
        n_features = 40
        for i in range(X.shape[1]):
            thresholds = np.sort(list(set(X[:, i])))
            if len(thresholds) >= n_features:
                thresholds = [thresholds[int(i * len(thresholds) / n_features)] for i in range(n_features)]
            self.threshholds.append(thresholds)
        self.root = self.make_tree(X, y)
    
    def predict(self, X):
        """
        Predict the target value or class label  the model from scratch using the provided data
        
        Parameters
        ----------
        X : np.array of type float with shape (n_objects, n_features)
            Feature matrix representing the data the predictions should be provided for

        Returns
        -------
        y_predicted : np.array of type int with shape (n_objects, 1) in classification 
                   (n_objects, 1) in regression 
            Column vector of class labels in classification or target values in regression
        
        """

        n_objects = X.shape[0]
        y_predicted = np.zeros(n_objects)
        for obj_idx in range(n_objects):
            obj = X[obj_idx, :].reshape(-1)
            cur_node = self.root
            while cur_node.left_child and cur_node.right_child:
                if obj[cur_node.feature_index] < cur_node.threshold:
                    cur_node = cur_node.left_child
                else:
                    cur_node = cur_node.right_child
            y_predicted[obj_idx] = cur_node.value

        return y_predicted.reshape((n_objects, 1))
        
    def predict_proba(self, X):
        """
        Only for classification
        Predict the class probabilities using the provided data
        
        Parameters
        ----------
        X : np.array of type float with shape (n_objects, n_features)
            Feature matrix representing the data the predictions should be provided for

        Returns
        -------
        y_predicted_probs : np.array of type float with shape (n_objects, n_classes)
            Probabilities of each class for the provided objects
        
        """
        assert self.classification, 'Available only for classification problem'

        n_objects = X.shape[0]
        n_classes = self.n_classes
        y_predicted_probs = np.zeros((n_objects, n_classes))
        for obj_idx in range(n_objects):
            obj = X[obj_idx, :].reshape(-1)
            cur_node = self.root
            while cur_node.left_child != None and cur_node.right_child != None:
                if obj[cur_node.feature_index] < cur_node.threshold:
                    cur_node = cur_node.left_child
                else:
                    cur_node = cur_node.right_child
            y_predicted_probs[obj_idx, :] = cur_node.probs

        return y_predicted_probs
