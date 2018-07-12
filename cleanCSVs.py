import csv
import glob
import os
import subprocess
import sys
import time


def main():
    """
    Cleans csv file if found.
    """
    try:
        clean(7, 3000, 'y')
    except IOError:
        print("Downloads folder does not contain a .csv file.")


def clean(last, length, delete):
    """
    Strips csv of last 7 lines, splits by 3000 rows and then deletes after 5 minutes.
    """
    file = str(get_download_path()) + str(getFile())
    with open(file, 'r') as f:
        reader = csv.reader(f)
        counter = 0
        rows = []
        for row in reader:
            if counter == 0:
                header = row
            else:
                rows.append(row)
            counter += 1
        rows = rows[:-last]
        if counter <= length:
            with open(str(get_download_path()) + 'out.csv', 'w+') as fout:
                writer = csv.writer(fout)
                writer.writerow(header)
                for row in rows:
                    writer.writerow(row)
        else:
            def fn(A, n): return [A[i:i + n] for i in range(0, len(A), n)]
            arrays = fn(rows, 3000)
            count = 1
            for array in arrays:
                with open(str(get_download_path()) + 'out' + str(count) + '.csv', 'w+') as fwrite:
                    writer = csv.writer(fwrite)
                    writer.writerow(header)
                    for row in array:
                        writer.writerow(row)
                    count += 1
        print('Your report has been reformatted for dataloader uploading.')
        cmd = "cd " + get_download_path()
        opn = "open ."
        subprocess.Popen(cmd.split())
        subprocess.Popen(opn.split())
        if 'y' in delete:
            time.sleep(300)
            os.chdir(get_download_path())
            for file in glob.glob("*.csv"):
                os.remove(file)
            print("Files have been removed from your Downloads Folder.")


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
