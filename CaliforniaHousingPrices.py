import os
import tarfile
import urllib
from tarfile import TarFile
from typing import Any, Union

import matplotlib.pyplot as plt

download_root="https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH="datasets/housing"
HOUSING_URL= download_root + HOUSING_PATH + "/housing.tgz"


def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
    # tgz_path=os.path.join(housing_path + "/housing.tgz")
    tgz_path: Union[bytes, str]=os.path.join("20190302/data/housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz: Union[TarFile, Any] = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()

    housing_tgz.hist(bins=50, figsize=(20,15))
    plt.show()
