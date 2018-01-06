import csv
from datetime import date
i = 1
with open('/Users/Dustin/Downloads/report1515112378821.csv', 'rt', encoding='ISO-8859-1') as csv_file:
    reader = csv.reader(csv_file)
    row_count = len(list(reader))
    numFiles = int(row_count / 2500)

    # for row in reader:
    #     with open(date.today() + ' Contact Ownership P' + str(i)+ '.csv', 'a') as new:
    #         i+=1
    #         writer = csv.writer(new)
    #         if reader.line_num < 2500:
    #             writer.writerow(row)
    #         else
    for i in range (0, numFiles):
        f = open(date.today() + ' Contact Ownership P' + str(i)+ '.csv', 'a')

print(numFiles)