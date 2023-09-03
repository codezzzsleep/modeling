import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report

# Load dataset and split into training and testing data
iris = datasets.load_iris()
X = iris.data[:, [2, 3]]
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)

# Feature scaling
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

# Train an RBF SVM classifier
svm = SVC(kernel='rbf', C=1.0, gamma=0.2, random_state=1)
svm.fit(X_train_std, y_train)

# Make predictions
y_pred = svm.predict(X_test_std)

# Print accuracy
print(f'classification_report\n: {classification_report(y_test, y_pred)}')
