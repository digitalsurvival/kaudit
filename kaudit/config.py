__author__ = 'mmarchese'

# This library includes functions to test for and extract the Linix kernel's .config file
# It should be able to parse regular text files and compressed .config files

import os.path
# For reading compressed files
import bz2
import gzip
import lzma
import zipfile
#
import logging

# Tests to see if .config file exists (defaults to /proc/config.gz).
def config_permission_check( conf_file_path ):

    if conf_file_path == '':
        conf_file_path = '/proc/config.gz'


    # Properly handle exceptions/logging for all file formats
    try: conf_file = open(str(conf_file_path), 'w')

    except IOError:

        if os.path.getsize(conf_file):
            print("Found configuration file: " + conf_file)
        else:
            print(".config file does not exist or no read access")

    return True