import numpy as np
from scipy.linalg import eigh


class LinearDiscriminantAnalysis:
    def __init__(self):
        self.weights = None

    # 计算均值向量
    def _compute_mean_vectors(self, X, y):
        n_classes = np.unique(y)
        mean_vectors = []
        for cls in n_classes:
            mean_vectors.append(np.mean(X[y == cls], axis=0))

        return np.array(mean_vectors)

    # 计算类内散布矩阵和类间散布矩阵
    def _compute_scatter_matrices(self, X, y, mean_vectors):
        n_classes = np.unique(y)
        n_features = X.shape[1]

        # 类内散布矩阵
        S_W = np.zeros((n_features, n_features))
        for cls, mean_vector in zip(n_classes, mean_vectors):
            cls_scatter = np.zeros((n_features, n_features))
            for row in X[y == cls]:
                row, mean_vector = row.reshape(n_features, 1), mean_vector.reshape(n_features, 1)
                cls_scatter += (row - mean_vector).dot((row - mean_vector).T)
            S_W += cls_scatter

        # 类间散布矩阵
        overall_mean = np.mean(X, axis=0)
        S_B = np.zeros((n_features, n_features))
        for cls, mean_vector in zip(n_classes, mean_vectors):
            n = X[y == cls, :].shape[0]
            mean_vector, overall_mean = mean_vector.reshape(n_features, 1), overall_mean.reshape(n_features, 1)
            S_B += n * (mean_vector - overall_mean).dot((mean_vector - overall_mean).T)

        return S_W, S_B

    def fit(self, X, y, n_components=None):
        mean_vectors = self._compute_mean_vectors(X, y)
        S_W, S_B = self._compute_scatter_matrices(X, y, mean_vectors)

        # 计算逆矩阵和特征值、特征向量
        inv_S_W = np.linalg.pinv(S_W)
        eigvals, eigvecs = eigh(inv_S_W.dot(S_B))

        # 选择最大特征值的特征向量作为LDA子空间的基
        idx = np.argsort(eigvals)[::-1]
        eigvals, eigvecs = eigvals[idx], eigvecs[:, idx]

        # 选择指定数量的特征向量
        if n_components is not None:
            eigvecs = eigvecs[:, :n_components].real

        self.weights = eigvecs
        self.class_means = mean_vectors @ self.weights
        self.classes = np.unique(y)

        return self.weights

    def transform(self, X):
        return X.dot(self.weights)

    def predict(self, X):
        X_lda = self.transform(X)
        y_pred = np.array(
            [self.classes[np.argmin(np.linalg.norm(self.class_means - point, axis=1))] for point in X_lda])
        return y_pred
