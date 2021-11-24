import csv
import xlrd

def csv_comp(csv1, csv2):

    csv1_list = []
    with open(csv1, "r", encoding='ISO-8859-1') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            #print(row)
            csv1_list.append(row[0][:7])
            #print(row)

    csv2_list = []
    with open(csv2, "r", encoding='ISO-8859-1') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            # print(row)
            csv2_list.append(row[0][:7])
            # print(row)

    unique_csv1 = []
    unique_csv2 = []
    common_subjects = []
    l1 = list(set(csv1_list))
    l2 = list(set(csv2_list))

    for s in l1:
        if s not in l2:
            unique_csv1.append(s)

    for s in l2:
        if s not in l1:
            unique_csv2.append(s)

    print("original length:")
    print("subjects in csv1:", len(unique_csv1))
    print("subjects in csv2:", len(unique_csv2))
    # print(baseline_list)
    print("unique subjects in csvq:", len(l1))
    print("unique subjects in csv2:", len(l2))


    with open("unqiue_" + csv1, "w+",newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Subject ID"])
        for i in unique_csv1:
            writer.writerow([i])


    with open("unqiue_" + csv2, "w+",newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Subject ID"])
        for i in unique_csv2:
            writer.writerow([i])


def fetch_commments(csv1, excel):
    csv_list = []
    with open(csv1, "r", encoding='ISO-8859-1') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            # print(row)
            csv_list.append(row[0][:7])
            # print(row)

    comments = []
    #excel = xlrd.open_workbook("TILDA_ASL_Exclusions_1_10_21.xls")
    #excel = xlrd.open_workbook("CaoiASLmapscreening_SK.xlsx", "r")
    excel = xlrd.open_workbook(excel, "r")
    sheet = excel.sheet_by_index(0)
    for s in range(1, sheet.nrows):
        id = str(sheet.cell(s, 0).value)[:7]
        artefact = sheet.cell(s, 1).value
        c = sheet.cell(s, 2).value
        caoi = sheet.cell(s, 3).value
        mc = sheet.cell(s, 4).value
        if id in csv_list:
            comments.append([id, artefact,c, caoi, mc])
        #exclusions.append(str(sheet.cell(s, 0).value)[:7])

    with open("comments_"+csv1, "w+",newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Subject ID", "N.B. artefact", "Video", "Caoi comments", "MC comments"])
        for i in comments:
            writer.writerow([i[0], i[1], i[2], i[3], i[4]])

if __name__ == '__main__':
    #csv_comp("baseline.csv", "raw.csv")
    fetch_commments("unqiue_baseline.csv", "../pipeline_analysis/CaoiASLmapscreening_SK.xlsx")



