import pandas as pd
import glob
import os
from pandas.io.json import json_normalize as jn
import itertools
import json
import requests
import bz2

path = '/Users/henry/code/freelance/upwork/04.03_betfair_download/data'

files = glob.glob(os.path.join(path + '/**/*.bz2'), recursive=True)

test_files = files[10000:10010]

test_file = test_files[0]

# Read as text > JSON
with bz2.open(test_file, "rt") as f:
    testlist = [line.rstrip('\n') for line in f]

f.close()

json_list = [json.loads(x) for x in testlist]
