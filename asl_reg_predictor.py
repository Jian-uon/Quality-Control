from sklearn.svm import SVC
import os, csv, random
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

Classifier = SVC(kernel='linear')


def data_augment(X, y):

    print(len(X), len(y))
    print(X[0].shape)
    '''
    for i in range(5):
        X = np.row_stack((X, X[78]))
        y = np.append(y, y[78])
        print(len(X), len(y))
        X = np.row_stack((X, X[80]))
        y = np.append(y, y[80])
        X = np.row_stack((X, X[47]))
        y = np.append(y, y[47])
    '''
    print(len(X), len(y))
    X = pd.DataFrame(X)
    y = pd.Series(y)
    print(X.head())
    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=0.2,
                                                        random_state=1)
    print('Data augmentation done.')
    return X_train, y_train, X_test, y_test

def get_features():
    cost_list = ['PCC', 'SSD', 'CC', 'NMI', 'MI', 'CR']
    features = []
    for cost in cost_list:
        feature = []
        cost_path = './' + cost + '.csv'
        if os.path.exists(cost_path):
            print('{0}.csv exists.'.format(cost))

        with open('asl_reg\\' + cost_path, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                feature.append(float(row[1]))
        features.append(feature)
    features = np.array(features)
    features = np.transpose(features)
    #print(features)
    #print(features.shape)

    label = [1 for i in range(102)]
    label[78] = 0
    label[80] = 0
    label[47] = 0
    label[67] = 0
    label[96] = 0
    label[97] = 0
    label[98] = 0
    label[99] = 0
    label[100] = 0
    label[101] = 0

    print('Data imported.')
    return features, label

def train_classifier(X, y):
    print(X.shape)
    print(y.shape)
    print(len(X), len(y))
    Classifier.fit(X, y)
    print('Classifier training done.')

def predict(test_X, test_y):

    prediction = Classifier.predict(test_X)
    prediction = pd.DataFrame(prediction, index=test_y.index)
    #print(prediction)
    print('ID Prediciton True')
    result = pd.concat([test_y, prediction], axis=1)
    #print(pd.merge(test_y,pd.DataFrame(prediction), how="left"))
    print(result)
    #for idx in range(len(X)):
    #    y_ = classifier.predict(X[idx])
    #    print("True label is {0}, predicted label is {1}".format(y[idx], y_) )

if __name__ == '__main__':

    X, y = get_features()
    train_X, train_y, test_X, test_y = data_augment(X, y)
    train_classifier(train_X, train_y)
    predict(test_X, test_y)


