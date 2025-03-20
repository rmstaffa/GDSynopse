import re
import sys
from loguru import logger
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

SETTINGS_FILE = str(BASE_DIR / "setup") + "/settings.py"  # Ensure correct path

def update_produce_vintages(new_value):
    try:
        with open(SETTINGS_FILE, "r") as file:
            content = file.read()

        # Replace "produce_vintages": True with False (or vice versa)
        updated_content = re.sub(
            r'("produce_vintages"\s*:\s*)(?:True|False)',
            r'\1False' if new_value == "False" else r'\1True',  # Toggle the value
            content
        )

        with open(SETTINGS_FILE, "w") as file:
            file.write(updated_content)


    except Exception as e:
        logger.error(f"Error updating settings: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No mode provided! Use 'enable' or 'disable'")
        sys.exit(1)

    mode = sys.argv[1].lower()
    new_value = "False" if mode == "disable" else "True"

    update_produce_vintages(new_value)
    logger.info(f"Updated produce_vintages to {new_value}")
