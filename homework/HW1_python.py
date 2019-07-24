
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import requests
import io
import zipfile

def getZIP(zip_file_name):
    r = (requests.get(zip_file_name)).content
    s = io.BytesIO(r)
    zip_file_ = zipfile.ZipFile(s, 'r')
    return zip_file_

zip_file = getZIP('http://seanlahman.com/files/database/lahman-csv_2014-02-14.zip')