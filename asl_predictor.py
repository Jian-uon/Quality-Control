from sklearn.svm import SVC
import os, csv, random
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

Classifier = SVC(kernel='linear')
METRICS_PATH = 'asl\\'
METRICS_NAMES = ["nonpvc_perfusion_gm.csv", "nonpvc_perfusion_wm.csv",
                "pvc_perfusion_gm.csv", "pvc_perfusion_wm.csv",
                "terr_perfusion_gm_LICA.csv", "terr_perfusion_gm_RICA.csv",
                "terr_perfusion_wm_LIBA.csv", "terr_perfusion_wm_RIBA.csv",
                "terr_perfusion_LICA.csv", "terr_perfusion_RICA.csv",
                ]
#name,Nvoxels,Mean,Std,Median,IQR,Precision-weighted mean,I2
#10%+GM,67285,60.77,14.02,59.00,19.00,57.43,70
#80%+GM,11778,64.65,12.50,63.00,17.00,62.27,58
#10%+WM,54166,52.27,14.04,52.00,19.00,48.28,75
#90%+WM,17912,42.03,10.84,41.00,15.00,39.32,63

def data_augment(X, y):

    print(len(X), len(y))
    print(X[0].shape)
    for i in range(2):
        X = np.row_stack((X, X[14]))
        y = np.append(y, y[14])
        X = np.row_stack((X, X[16]))
        y = np.append(y, y[16])
        X = np.row_stack((X, X[32]))
        y = np.append(y, y[32])
        X = np.row_stack((X, X[34]))
        y = np.append(y, y[34])
        X = np.row_stack((X, X[38]))
        y = np.append(y, y[38])
        X = np.row_stack((X, X[40]))
        y = np.append(y, y[40])
        X = np.row_stack((X, X[47]))
        y = np.append(y, y[47])
        X = np.row_stack((X, X[55]))
        y = np.append(y, y[55])
        X = np.row_stack((X, X[56]))
        y = np.append(y, y[56])
        X = np.row_stack((X, X[89]))
        y = np.append(y, y[89])

    #random.shuffle()
    state = np.random.get_state()
    np.random.shuffle(X)
    np.random.set_state(state)
    np.random.shuffle(y)
    print(len(X), len(y))
    X = pd.DataFrame(X)
    y = pd.Series(y)
    print(X.head())
    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=0.2,
                                                        random_state=0)
    print('Data augmentation done.')
    return X_train, y_train, X_test, y_test

def get_features():
    features = []
    for METRICS_NAME in METRICS_NAMES:
        feature = []
        if os.path.exists(METRICS_PATH+METRICS_NAME):
            print('{0} exists.'.format(METRICS_NAME))
        else:
            raise ImportError("{0} doesn't exist.".format(METRICS_NAME))
        with open(METRICS_PATH+METRICS_NAME, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                feature.append(float(row[1]))
        features.append(feature)
    features = np.array(features)
    features = np.transpose(features)
    #print(features)
    #print(features.shape)

    label = [1 for i in range(96)]
    #15 17 33 35 39 41 48 56  57 90
    label[14] = 0
    label[16] = 0
    label[32] = 0
    label[34] = 0
    label[38] = 0
    label[40] = 0
    label[47] = 0
    label[55] = 0
    label[56] = 0
    label[89] = 0
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


