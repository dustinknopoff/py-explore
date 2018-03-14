import csv
import glob
import os


def main():
    """
    Strips csv of last 7 lines, splits by 3000 rows and then deletes after 5 minutes.
    """
    file = str(get_download_path()) + str(getFile())
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
            with open(str(get_download_path()) + 'out.csv', 'w+', encoding='latin_1') as fout:
                writer = csv.writer(fout)
                for row in rows:
                    writer.writerow(row)
        else:
            fn = lambda A, n: [A[i:i + n] for i in range(0, len(A), n)]
            arrays = fn(rows, 3000)
            count = 1
            for array in arrays:
                with open(str(get_download_path()) + 'out' + str(count) + '.csv', 'w+', encoding='latin_1') as fwrite:
                    writer = csv.writer(fwrite)
                    writer.writerow(header)
                    for row in array:
                        writer.writerow(row)
                    count += 1


def getFile():
    """
    :return: all csv files in the Downloads folder.
    """
    os.chdir(get_download_path())
    for file in glob.glob("*.csv"):
        return file


def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'Downloads/')


if __name__ == '__main__':
    main()
