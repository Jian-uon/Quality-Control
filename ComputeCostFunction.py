import os
import numpy as np
import nibabel as nib
import argparse
import csv
import warnings
import pandas as pd
from sklearn.metrics.cluster import normalized_mutual_info_score, mutual_info_score
from nibabel.testing import data_path
warnings.filterwarnings('ignore')
#python ComputeCostFunction.py --filepath=E:\Projects\code\python\CostFunction\imagelist.txt


Image_path = []#subjects' pathes named in the provided file
Nimages = []
Subjects = []
COST_FUNCTIONS = ["PCC", "CC", "NMI", "SSD", "MI", "CR"]

parser = argparse.ArgumentParser(description='Calculate cost functions.')
parser.add_argument('--filepath', )
parser.add_argument('--costfunc', choices=["PCC", ""] )
args = parser.parse_args()
#print(args)
#print(args.filepath)


def data_read():

    print('Reading local images.')
    with open(args.filepath, "r") as file:
        image_pathes = file.readlines()
        for path in image_pathes:
            Image_path.append(path.strip())
        #print(image_pathes)

    for img_path in Image_path:
        #print(img_path)
        img = nib.load(img_path)
        #print(img.shape)
        nimg = img.get_fdata()
        img_index = img_path.split('\\')[-1][4:-7]
        #print(img_index)
        Subjects.append({"id":img_index, "nimg":nimg.flatten()})
        Nimages.append(nimg)
    print('Reading done.')

def cost_calculator(Subject_A, Subject_B, function_name):
    if function_name == 'PCC':
        cost = np.corrcoef(Subject_A, Subject_B)
    elif function_name == 'SSD':
        diff = Subject_A - Subject_B
        cost = np.dot(diff, diff)
    elif function_name == 'CC':
        cost = np.correlate(Subject_A, Subject_B)
    elif function_name == 'NMI':
        cost = normalized_mutual_info_score(Subject_A, Subject_B)
    elif function_name == 'MI':
        cost = mutual_info_score(Subject_A, Subject_B)
    elif function_name == 'CR':
        cost = np.correlate(Subject_A, Subject_B)/np.var([Subject_A, Subject_B])
    else:
        raise TypeError('{0} does not exist.'.format(function_name))
    return cost

def get_cost(method):

    print("Start computing cost function {0}.".format(method))
    if method in COST_FUNCTIONS:
        for subject in Subjects:
            total_cost = []
            for sub in Subjects:
                cost = cost_calculator(subject['nimg'], sub['nimg'], method)
                total_cost.append(cost)
            subject[method] = np.mean(total_cost)
    else:
        raise TypeError("{0} doesn't exist.".format(method))

    print('Start saving results.')
    with open('asl_reg\\' + method + ".csv", "w+", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["ID", method])
        for subject in Subjects:
            writer.writerow([subject['id'], subject[method]])
    print("{0} saved.".format(method))

def filename_generator():
    pre = "E:\Projects\\a_project\\asl_instd\sub-"
    suf = ".nii.gz"
    pathes = ""
    for i in range(1, 97):
        pathes += (pre+str(i)+suf+'\n')

    with open("temp.txt", "w+") as file:
        file.write(pathes)

def data_check():
    data = []
    for sub in Subjects:
        data.append(sub['nimg'])
    df = pd.DataFrame(data)
    #print(df.head())
    print(df.describe())



if __name__ == '__main__':
    data_read()
    #data_check()
    get_cost('PCC')
    get_cost('CC')
    get_cost('NMI')
    get_cost('MI')
    get_cost('CR')
    get_cost('SSD')
    #PCC()

