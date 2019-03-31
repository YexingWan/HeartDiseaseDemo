import glob
import os

import config


def get_default_year():
    """
        get default prediction year if not selected
    """
    files = glob.glob(os.path.join(config.OUTPUT_DIR, "pred_result*"))
    if len(files) == 0:
        print("file not found")
        pred_year = -1
    else:
        latest_file = max(files, key=os.path.getmtime)
        pred_year = int(os.path.splitext(latest_file)[0].split('_')[-1])
        print('default year: ', pred_year)
    return pred_year
