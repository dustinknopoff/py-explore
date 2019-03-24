from glob import glob
import requests
from zipfile import ZipFile
import os
import shutil


def extract_picks(globbed):
    with open("./sickpicks.md", "w+") as out:
        for fname in globbed:
            with open(fname, 'r') as f:
                contents = f.read()
                can_add = False
                for line in contents.split("\n"):
                    if "## Sick Picks" in line:
                        can_add = True
                    elif "## ××× SIIIIICK ××× PIIIICKS ×××" in line:
                        can_add = True
                    elif "##" in line and can_add is True:
                        can_add = False
                    elif can_add is True and line is not '':
                        out.write(line)
                        out.write("\n")


def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
                    # f.flush()
    return local_filename


def get_path_root(zip_file):
    zip_ref = ZipFile(zip_file, 'r')
    zip_ref.extractall('./')
    zip_ref.close()
    return zip_ref.namelist()[0]


def cleanup(zip_path, repo):
    os.remove(zip_path)
    shutil.rmtree(repo)


if __name__ == '__main__':
    zip_path = download_file('https://github.com/wesbos/Syntax/archive/master.zip')
    root = get_path_root(zip_path)
    pattern = glob(f'./{root}shows/*.md')
    extract_picks(pattern)
    cleanup(zip_path, root)
