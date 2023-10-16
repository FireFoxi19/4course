import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import random

column_names = ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal", "target"]
clf = pd.read_csv('heart_data.csv', header=None, names=column_names)
clf = clf.replace("?", None)

clf = clf.apply(pd.to_numeric, errors='ignore')

x = clf.iloc[1:, 0:13]  
y = clf.iloc[1:, 13]    

clf = tree.DecisionTreeClassifier(random_state=0, max_depth=12, max_leaf_nodes=2)

train_accuracy = []
test_accuracy = []

print('N \t На обучающей ', 'На тестовой ', sep=" ")
for i in range(10):
    random_seed = random.randint(1, 1000)  
    X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.3, random_state=random_seed)
    clf.fit(X_train, Y_train)
    train_acc = clf.score(X_train, Y_train)
    test_acc = clf.score(X_test, Y_test)
    train_accuracy.append(train_acc)
    test_accuracy.append(test_acc)
    print(f'{(i + 2):2}\t {train_acc:.6f}\t {test_acc:.6f}')

plt.figure(figsize=(8, 6))
plt.plot(range(2, 12), train_accuracy, label='Обучающая')
plt.plot(range(2, 12), test_accuracy, label='Тестовая')
plt.xlabel('Номер итерации')
plt.ylabel('Точность')
plt.legend()
plt.title('Точность и номер итерации')
plt.show()