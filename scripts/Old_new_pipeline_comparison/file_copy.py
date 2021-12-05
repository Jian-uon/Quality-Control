import os
import shutil
import csv


def obtain_subjects(subject_list_path):
    subjects_path = []
    subjects_ids = []
    base_path = "/gpfs01/share/TILDA/Raw_nii_files_for_MC_pCASL_T1_B0_M0/"

    #subjects_path = os.listdir(subject_list_path)
    with open(subject_list_path, "r+", ) as file:
        lines = file.readlines()
        for line in lines:
            subjects_ids.append(line.strip())
            #subjects_path.append(base_path + line.strip())
    #print(subjects_path)

    index = 1
    data_map = []
    total_subjects = os.listdir(base_path)
    for id in subjects_ids:
        for subject in total_subjects:
            if id in subject:
                path = base_path+subject
                subjects_path.append(path)
                data_map.append({"id":id, "path":path, "index":index})
                index += 1

    with open("subjects_map.csv", "w+") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["subject_id", "path", "new_index"])
        for i in data_map:
            writer.writerow(i["id"], i["path"], i["index"])
    #for subject_path in subjects_path:
    #    data_map[""]
    pass

    with open("subjects_path.txt", "w+") as file:
        for line in subjects_path:
            file.write(line)



if __name__ == '__main__':
    subject_list_path = "E:\\temp\\subjects_ids.txt"
    obtain_subjects(subject_list_path)