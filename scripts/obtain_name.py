import os, csv

RAW_PATH = "/share/TILDA/Raw_nii_files_for_MC_pCASL_T1_B0_M0"
CO2OCT_path = '/share/TILDA/Processed_pCASL/co2oct'
BASELINE_PATH = '/share/TILDA/Processed_pCASL/Baseline'



list1 = os.listdir(RAW_PATH)
list2 = os.listdir(CO2OCT_path)
list3 = os.listdir(BASELINE_PATH)

with open("raw.csv", "w+") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow("Subject ID")
    for i in list1:
        writer.writerow(i)


with open("co2oct.csv", "w+") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow("Subject ID")
    for i in list2:
        writer.writerow(i)

with open("baseline.csv", "w+") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow("Subject ID")
    for i in list3:
        writer.writerow(i)

raw = set(list1)
co2oct = set(list2)
baseline = set(list3)

raw_co2oct_diff = {}
co2oct_raw_diff = {}
raw_baseline_diff = {}
baseline_raw_diff = {}
co2oct_baseline_diff = {}
baseline_co2oct_diff = {}

for x in raw:
    if x not in co2oct:
        raw_co2oct_diff.add(x)

    if x not in baseline:
        raw_baseline_diff.add(x)

for x in co2oct:
    if x not in raw:
        co2oct_raw_diff.add(x)

    if x not in baseline:
        co2oct_baseline_diff.add(x)

for x in baseline:
    if x not in raw:
        baseline_raw_diff.add(x)

    if x not in co2oct:
        baseline_co2oct_diff.add(x)

print(raw.difference(co2oct))





