
import subprocess
import sys
from logger_config import logger

try:
    logger.info("Pipeline started")

    logger.info("STEP 1: Cleaning the order data")
    subprocess.run(
        [sys.executable, "src/read_data.py"],
        check=True
    )

    logger.info("STEP 2: Loading data into PostgreSQL")
    subprocess.run(
        [sys.executable, "src/load_data.py"],
        check=True
    )

    logger.info("STEP 3: Verifying the database")
    subprocess.run(
        [sys.executable, "src/connect_db.py"],
        check=True
    )

    logger.info("Pipeline completed successfully")

except subprocess.CalledProcessError:
    logger.exception("Pipeline failed because a step returned an error")
    sys.exit(1)

except Exception:
    logger.exception("Unexpected error occurred in the pipeline")
    sys.exit(1)

