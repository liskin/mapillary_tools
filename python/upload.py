#!/usr/bin/python

import sys
import os
from lib.uploader import upload_file_list
from lib.sequence import Sequence
from lib.exif import verify_mapillary_tag

'''
Script for uploading images taken with the Mapillary
iOS or Android apps.

Intended use is for cases when you have multiple SD cards
or for other reasons have copied the files to a computer
and you want to bulk upload.

NB: DO NOT USE THIS ON OTHER IMAGE FILES THAN THOSE FROM
THE MAPILLARY APPS, WITHOUT PROPER TOKENS IN EXIF, UPLOADED
FILES WILL BE IGNORED SERVER-SIDE.
'''


if __name__ == '__main__':
    '''
    Use from command line as: python upload.py path
    '''

    if sys.version_info >= (3, 0):
        raise IOError("Incompatible Python version. This script requires Python 2.x, you are using {0}.".format(sys.version_info[:2]))

    if len(sys.argv) > 2:
        print("Usage: python upload.py path")
        raise IOError("Bad input parameters.")

    path = sys.argv[1]

    s = Sequence(path, skip_folders=['success'], check_exif=False)

    num_image_file = len(s.file_list)

    file_list = [f for f in s.file_list if verify_mapillary_tag(f)]

    print ("Uploading {} images with valid mapillary tags (Skipping {})".format(len(file_list), num_image_file-len(file_list)))

    upload_file_list(file_list)

    print("Done uploading {} images.".format(len(file_list)))
