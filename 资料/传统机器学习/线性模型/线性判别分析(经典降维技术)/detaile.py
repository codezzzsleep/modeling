import numpy as np
from scipy.linalg import eig

class LinearDiscriminantAnalysis:
    def __init__(self, n_components=None):
        self.n_components = n_components
        self.w = None
        self.class_labels = None
        self.class_means = None

    def fit(self, X, y):
        classes = np.unique(y)
        n_features = X.shape[1]
        if self.n_components is None or self.n_components > len(classes) - 1:
            self.n_components = len(classes) - 1

        self.class_labels = classes

        # 计算类别均值向量
        class_means = []
        for c in classes:
            class_means.append(np.mean(X[y == c], axis=0))
        self.class_means = np.array(class_means)

        # 计算类内散度矩阵
        within_scatter_matrix = np.zeros((n_features, n_features))
        for c, class_mean in zip(classes, self.class_means):
            class_samples = X[y == c]
            scatter_matrix = np.cov(class_samples.T)
            within_scatter_matrix += scatter_matrix

        # 计算类间散度矩阵
        total_mean = np.mean(X, axis=0)
        between_scatter_matrix = np.zeros((n_features, n_features))
        for c, class_mean in zip(classes, self.class_means):
            n_samples = X[y == c].shape[0]
            mean_diff = (class_mean - total_mean).reshape(-1, 1)
            between_scatter_matrix += n_samples * mean_diff.dot(mean_diff.T)

        # 计算广义特征值和特征向量
        eigenvalues, eigenvectors = eig(np.linalg.inv(within_scatter_matrix).dot(between_scatter_matrix))

        # 选择前n_components个特征向量
        idx = np.argsort(eigenvalues)[::-1]
        self.w = eigenvectors[:, idx[:self.n_components]]

    def transform(self, X):
        if self.w is None:
            raise ValueError("LDA has not been fitted.")
        return X.dot(self.w)

    def fit_transform(self, X, y):
        self.fit(X, y)
        return self.transform(X)

    def predict(self, X):
        if self.w is None:
            raise ValueError("LDA has not been fitted.")
        X_proj = self.transform(X)
        y_pred = []
        for x in X_proj:
            distances = [np.linalg.norm(x - class_mean) for class_mean in self.class_means]
            y_pred.append(self.class_labels[np.argmin(distances)])
        return np.array(y_pred)
