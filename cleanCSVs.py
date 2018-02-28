import sys, csv
import glob, os


def main():
    file = '/Users/Dustin/Downloads/' + str(getFile())
    with open(file, 'r', encoding='latin_1') as f:
        reader = csv.reader(f)
        counter = 0
        rows = []
        for row in reader:
            if counter == 0:
                header = row
            else:
                rows.append(row)
            counter += 1
        rows = rows[:-7]
        if counter <= 3000:
            with open('/Users/Dustin/Downloads/out.csv', 'w+', encoding='latin_1') as fout:
                writer = csv.writer(fout)
                for row in rows:
                    writer.writerow(row)
        else:
            fn = lambda A, n: [A[i:i + n] for i in range(0, len(A), n)]
            arrays = fn(rows, 3000)
            count = 1
            for array in arrays:
                with open('/Users/Dustin/Downloads/out' + str(count) + '.csv', 'w+', encoding='latin_1') as fwrite:
                    writer = csv.writer(fwrite)
                    writer.writerow(header)
                    for row in array:
                        writer.writerow(row)
                    count += 1


def getFile():
    os.chdir("/Users/Dustin/Downloads")
    for file in glob.glob("*.csv"):
        return file


if __name__ == '__main__':
    main()
