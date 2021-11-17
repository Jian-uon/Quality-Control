import os, csv


RAW_PATH = "/share/TILDA/Raw_nii_files_for_MC_pCASL_T1_B0_M0"
CO2OCT_PATH = '/share/TILDA/Processed_pCASL/co2oct'
BASELINE_PATH = '/share/TILDA/Processed_pCASL/Baseline'

def get_subject_ids():


    list1 = os.listdir(RAW_PATH)
    list2 = os.listdir(CO2OCT_PATH)
    list3 = os.listdir(BASELINE_PATH)

    with open("raw.csv", "w+") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Subject ID"])
        for i in list1:
            writer.writerow([i])


    with open("co2oct.csv", "w+") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Subject ID"])
        for i in list2:
            writer.writerow([i])

    with open("baseline.csv", "w+") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Subject ID"])
        for i in list3:
            writer.writerow([i])



def analyse_ids():
    baseline = "baseline.csv"
    co2oct = "co2oct.csv"
    raw = "raw.csv"
    baseline_list = []
    co2oct_list = []
    raw_list = []
    with open(baseline) as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)
        for row in csv_reader:
            baseline_list.append(row)

    with open(co2oct) as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)
        for row in csv_reader:
            co2oct_list.append(row)

    with open(raw) as csvfile:
        csv_reader = csv.reader(csvfile)
        header = next(csv_reader)
        for row in csv_reader:
            raw_list.append(row)

    print(len(baseline_list), len(co2oct_list), len(raw_list))



#analyse_ids()

def check_exists(dir_path, name):

    total_list = os.listdir(dir_path)
    real_subjects = []
    for subject_name in total_list:
        path = dir_path+'/'+subject_name
        sub_dir = []
        sub_files = []
        for root, dirs, files in os.walk(path):
            sub_dir.extend(dirs)
            sub_files.extend(files)
        if "oxasl" in sub_dir and "oxasl_distcorr" in sub_dir and "perfusion.hdr" in sub_files:
            #print(subject_name)
            real_subjects.append(subject_name[:7])


    #print(total_list[0])
    print(len(total_list))
    print(len(real_subjects))
    rest = []
    for s in total_list:
        flag = False
        for k in real_subjects:
            if s[:7] == k[:7]:
                flag = True
        if flag == False:
            rest.append(s[:7])
            #break
    print("-------------------------")
    print(len(rest))
    l  = list(set(real_subjects))
    print("real unique subjects:")
    print(len(l))
    #print(l)
    with open(name+"_invalied.csv", "w+") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Subject ID"])
        for i in rest:
            writer.writerow([i])

    print("size of real subjects = of " +  dir_path + ": ",  len(real_subjects))

def check_exists_raw(object_file):

    total_list = os.listdir(RAW_PATH)
    real_subjects = []
    for subject_name in total_list:
        path = RAW_PATH+'/'+subject_name
        sub_dir = []
        sub_files = []
        for root, dirs, files in os.walk(path):
            sub_dir.extend(dirs)
            sub_files.extend(files)
        flag = 0

        for i in sub_files:
            #flag = 0
            if object_file and object_file in i:
                flag +=1
            '''
            if "B0_map" in i:
                flag +=1
            '''
            if "MPR_WIP_MPRAGE_T13D" in i:
                flag += 1
            if "__WIP_MPRAGE_T13D" in i:
                flag += 1
            if "pCASL_M0" in i:
                flag += 1
            if "pCASL_Baseline" in i:
                flag += 1
            if "e2_ph_1" in i:
                flag += 1
            if "e2_ph_2" in i:
                flag += 1
            if "e2_ph_3" in i:
                flag += 1
            if "e2_ph_4" in i:
                flag += 1
                #print(subject_name)
        if object_file == "":
            flag += 1
        if flag >= 9:
            real_subjects.append(subject_name)


    #print(total_list[0])
    print(len(total_list))
    print(len(real_subjects))
    rest = []
    for s in total_list:
        flag = False
        for k in real_subjects:
            if s[:7] == k[:7]:
                flag = True
        if flag == False:
            rest.append(s[:7])
            #break
    print("-------------------------")
    print(len(rest))
    l = list(set(real_subjects))
    print("real unique subjects:")
    print(len(l))

    #print(l)
    object_file = "normal_raw"
    with open(object_file+"_invalied.csv", "w+") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Subject ID"])
        for i in rest:
            writer.writerow([i])

    with open(object_file+"_valied.csv", "w+") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Subject ID"])
        for i in real_subjects:
            writer.writerow([i])

    print("size of real subjects = of " +  RAW_PATH + ": ",  len(real_subjects))





#check_exists(CO2OCT_PATH, "co2")
#check_exists(BASELINE_PATH, "baseline")
#check_exists_raw('pCASL_withCO2')
#check_exists_raw('')

def check_unqiue():
    l1 = os.listdir(RAW_PATH)
    print(len(l1))
    l3 = []
    for i in l1:
        l3.append(i[:7])
    l2 = list(set(l3))
    print(len(l2))

check_unqiue()








