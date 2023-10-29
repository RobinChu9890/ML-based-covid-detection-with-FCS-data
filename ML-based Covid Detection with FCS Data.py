# %%
import pandas as pd
from glob import glob
import FlowCal as fc
import tqdm
import numpy as np
from sklearn.model_selection import KFold
from sklearn.svm import SVC
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sn

# %% retreiving data and extracting features
path = r'.\EU_label.csv'
label_table = pd.read_csv(path)

samples_info = []
for i in range(len(label_table)):
    samples_info.append({'file_flow_id': label_table.loc[i, 'file_flow_id'],
                         'label': ((1, 0)[label_table.loc[i, 'label'] ==
                                          'Healthy']),
                         'data': None,
                         'data_feature': None})

path = r'.\EU_marker_channel_mapping.csv'
mapping_table = pd.read_csv(path)
use_channel_list = []
for i in range(len(mapping_table)):
    if (mapping_table.loc[i, 'use']):
        use_channel_list.append(mapping_table.loc[i, 'PxN(channel)'])

path = r'.\dataset\\'
for i in range(len(samples_info)):
    file_path = glob(path + samples_info[i]['file_flow_id'] + '\\*.fcs')
    samples_info[i]['data'] = fc.transform.to_rfi(
        fc.io.FCSData(file_path[0])[:, use_channel_list])

progress_bar = tqdm.tqdm(range(len(samples_info)))
for i in progress_bar:
    progress_bar.set_description('Extracting features...')
    data_feature = []
    data_feature.append(fc.stats.mean(samples_info[i]['data']))
    data_feature.append(fc.stats.std(samples_info[i]['data']))
    data_feature.append(fc.stats.median(samples_info[i]['data']))
    data_feature.append(fc.stats.iqr(samples_info[i]['data']))
    data_feature.append(fc.stats.cv(samples_info[i]['data']))
    data_feature.append(fc.stats.rcv(samples_info[i]['data']))
    data_feature.append(fc.stats.mode(samples_info[i]['data']))
    samples_info[i]['data_feature'] = (
        np.hstack(data_feature)).reshape([1, -1])

# %% splitting data for training and validation
features = []
labels = []
for i in range(len(samples_info)):
    features.append(samples_info[i]['data_feature'])
    labels.append(samples_info[i]['label'])
features = np.vstack(features)
labels = np.array(labels)

k = 5
kf = KFold(n_splits=k, shuffle=True, random_state=42)

for fold_i, (training_list, validation_list) in enumerate(
        kf.split(features, labels)):
    print('\nfold ' + str(fold_i+1))
    training_feature = []
    training_label = []
    for i in training_list:
        training_feature.append(samples_info[i]['data_feature'])
        training_label.append(samples_info[i]['label'])
    training_feature = np.vstack(training_feature)
    training_label = np.array(training_label)

    validation_feature = []
    validation_label = []
    for i in validation_list:
        validation_feature.append(samples_info[i]['data_feature'])
        validation_label.append(samples_info[i]['label'])
    validation_feature = np.vstack(validation_feature)
    validation_label = np.array(validation_label)

    clf = SVC()
    clf.fit(training_feature, training_label)

    validation_prediction = clf.predict(validation_feature)

    print('Recall: ' + str(round(metrics.recall_score(
        validation_label, validation_prediction), 4)*100) + '%')
    print('Precision: ' + str(round(metrics.precision_score(
        validation_label, validation_prediction), 4)*100) + '%')
    print('Accuracy: ' + str(round(metrics.accuracy_score(
        validation_label, validation_prediction), 4)*100) + '%')

    plt.figure()
    matrix = metrics.confusion_matrix(validation_label, validation_prediction)
    sn.heatmap(matrix, cmap='coolwarm', linecolor='white',
               linewidths=1, annot=True, fmt='g')
    plt.ylabel('Truth label')
    plt.xlabel('Prediction')
    plt.plot()
    plt.show()
    plt.clf()
    plt.close()
