import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LassoCV

if __name__ == '__main':

    white_wine = 0
    clf = pd.read_csv('winequalityN.csv', header=0).fillna(0).values
    for i in clf:
        if i[0] == 'white':
            i[0] = 0
            white_wine += 1
        else:
            i[0] = 1
    x = clf[:, 0:12]
    y = clf[:, 12]

    
    print(f'Все вина:')
    result = 0
    for _ in range(10):
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
        model = LassoCV(cv=5, normalize=False)
        model.fit(x_train, y_train)
        predict = model.predict(x_test)

        success = 0
        for i in range(len(x_test)):
            if abs(y_test[i] - predict[i]) < 1:
                success += 1
        print(f'Точность: {success / len(x_test) * 100:.4}%')
        result += success / len(x_test) * 100
    print(f'Средняя точность: {result / 10:.4}%\n')

    x1 = clf[0:white_wine, 0:12]
    y1 = clf[0:white_wine, 12]
    print(f'Белые вина:')
    result = 0
    for _ in range(10):
        x_train, x_test, y_train, y_test = train_test_split(x1, y1, test_size=0.3)
        model = LassoCV(cv=5, normalize=False)
        model.fit(x_train, y_train)
        predict = model.predict(x_test)

        success = 0
        for i in range(len(x_test)):
            if abs(y_test[i] - predict[i]) < 1:
                success += 1
        print(f'Точность: {success / len(x_test) * 100:.4}%')
        result += success / len(x_test) * 100
    print(f'Средняя точность: {result / 10:.4}%\n')

    x2 = clf[white_wine:, 0:12]
    y2 = clf[white_wine:, 12]
    print(f'Красные вина:')
    result = 0
    for _ in range(10):
        x_train, x_test, y_train, y_test = train_test_split(x2, y2, test_size=0.3)
        model = LassoCV(cv=5, normalize=False)
        model.fit(x_train, y_train)
        predict = model.predict(x_test)

        success = 0
        for i in range(len(x_test)):
            if abs(y_test[i] - predict[i]) < 1:
                success += 1
        print(f'Точность: {success / len(x_test) * 100:.4}%')
        result += success / len(x_test) * 100
    print(f'Средняя точность: {result / 10:.4}%\n')
