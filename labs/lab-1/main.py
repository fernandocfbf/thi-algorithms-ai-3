import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import random
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV, ShuffleSplit
random.seed(42)

from sklearn import svm
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

from src.utils.database import get_database
df = get_database()
df.columns
df.head()
df.describe()
df.Potability.value_counts(True)

### a) Display yhe histogram of all attibutes including Y
plt.style.use('seaborn-darkgrid')
df.hist(figsize=(20,15), color='#607c8e')
plt.suptitle("Histogram of all variables", fontsize=20, fontweight='bold')
plt.xlabel("Value", fontsize=14)
plt.ylabel("Frequency", fontsize=14)
plt.legend(df.columns, loc='upper right')
plt.show()

### b) Display histogram of each attribute regarding Y=0 and Y=1. What is your conclusion regarding the expected performance of the classifier? Also explain why you came to this conclusion.
grouped = df.groupby('Potability')
num_cols = len(df.columns) - 1
num_rows = num_cols // 3 + (num_cols % 3 > 0)

fig, axes = plt.subplots(nrows=num_rows, ncols=3, figsize=(10, 5*num_rows))
for i, col in enumerate(df.columns[:-1]):
    row_idx, col_idx = divmod(i, 3)
    for key, group in grouped:
        group[col].hist(alpha=0.5, bins=10, ax=axes[row_idx][col_idx], label=f'y={key}')
    axes[row_idx][col_idx].set_xlabel(col)
    axes[row_idx][col_idx].set_ylabel('Frequency')
    axes[row_idx][col_idx].legend(title='Class')

for i in range(num_cols, num_rows*3):
    fig.delaxes(axes.flat[i])

plt.tight_layout()
plt.show()

### c) Perform serval runs employing the SVM with different C and gamma parameter using cross validation. (no shuffle). Vary n_splits parameter between 10 and 50. Display the confusion matrix of the test data for each run. Calculate the obtained average Accuracy of the test data after 5 runs.
x = df.copy().drop('Potability', axis=1)
y = df.copy()["Potability"]
x = StandardScaler().fit_transform(x)
c_values = [random.uniform(0.01, 10) for i in range(0, 5)]
gamma_values = [random.uniform(0, 50) for i in range(0, 5)]
n_splits_values = [random.randint(10, 50) for i in range(0, 5)]
n_splits_values
c_values
acc_list = list()
for i in range(len(c_values)):
    c = c_values[i]
    gamma = gamma_values[i]
    n_splits = n_splits_values[i]
    clf = svm.SVC(C=c, gamma=gamma) #creates the classifier
    y_pred = cross_val_predict(clf, x, y, cv=n_splits)
    conf_mat = confusion_matrix(y, y_pred)
    accuracy = np.diag(conf_mat).sum() / conf_mat.sum()
    acc_list.append(accuracy)
    sns.heatmap(conf_mat, annot=True, fmt="d", cmap="Blues")
    plt.xlabel("Predicted labels")
    plt.ylabel("True labels")
    plt.title("C: {:.3f}, gamma: {:.3f}, n_splits: {:.0f}".format(c, gamma, n_splits))
    plt.show()
    print(f"Accuracy: {round(accuracy*100,2)}%")
    
avg_acc = np.mean(acc_list)
print(f"Avarege Accuracy: {round(avg_acc*100,2)}%")
### d) Perform 5 runs employing SVM with the gridsearch. Display best hyperparameter results obtained for each run. Display the confusion matrix of the test data for each run. Calculate the obtained average Accuracy of the test data after 5 runs.

from sklearn.model_selection import train_test_split
param_grid = {
    'gamma': [0.1, 1, 2, 4, 8, 10],
    'C': [1, 5, 25, 50, 100]
}
for i in range(5):
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=i)
    svm_model = svm.SVC()
    shuffle_split = ShuffleSplit(n_splits=5, test_size=0.2, random_state=42)
    grid_search = GridSearchCV(svm_model, param_grid, cv=shuffle_split, scoring='accuracy')
    grid_search.fit(X_train, y_train)
    y_pred = grid_search.predict(X_test)
    conf_mat = confusion_matrix(y_test, y_pred)
    y_pred_train = grid_search.predict(X_train)
    acc = accuracy_score(y_train, y_pred_train)
    sns.heatmap(conf_mat, annot=True, fmt="d", cmap="Blues")
    plt.xlabel("Predicted labels")
    plt.ylabel("True labels")
    plt.title(f"{grid_search.best_params_}")
    plt.show()
    print(f"Test best score: {round(grid_search.best_score_*100,2)}%")
    print(f"Train best score: {round(acc*100,2)}%")