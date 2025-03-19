#%% 

import os
import glob
from loguru import logger

# delete all files in synopse folder for clean slate
old_reports = glob.glob("synopse/*")

for report in old_reports:
    logger.info(f"Deleting old report: {report}")
    os.remove(report)

