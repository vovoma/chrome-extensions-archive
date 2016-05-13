import json
import urllib.request
import os.path
import sys

DOWNLOAD_URL = "https://clients2.google.com/service/update2/crx?response=redirect&prodversion=49.0.2623.108&x=id%3D{ID}%26uc"
DESTINATION = "crx/{ID}.crx"


def down(ext_id, filename):
    urllib.request.urlretrieve(DOWNLOAD_URL.format(ID=ext_id), filename)


def down_protected(ext_id):
    print('down', ext_id)
    filename = DESTINATION.format(ID=ext_id)
    if not os.path.isfile(filename) or os.path.getsize(filename) == 0:
        try:
            down(ext_id, filename)
        except Exception as e:
            print('paid extension ?', e)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        down_protected(sys.argv[1])
    else:
        for url in json.load(open('extension_list.json')):
            ext_id = url.split('/')[-1]
            down_protected(ext_id)