#%% 

import os
import sys
import glob
from loguru import logger
from pathlib import Path

# Ensure BASE_DIR is correctly set
BASE_DIR = Path(__file__).resolve().parent.parent
logger.info(f"Base directory: {BASE_DIR}")

# Ensure sys.path includes BASE_DIR for module imports
sys.path.insert(0, str(BASE_DIR))

# Import settings properly
from setup import settings  # Ensure `setup.py` is not interfering

# Determine the correct folder
folder = "vintages" if settings.settings["produce_vintages"] else "synopse"

# Use an f-string for correct path formatting
old_reports = glob.glob(f"_reports_outputs/{folder}/*")

# Delete old reports
for report in old_reports:
    logger.info(f"Deleting old report: {report}")
    os.remove(report)
