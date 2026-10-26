
import logging
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
log_folder = project_folder / "logs"

log_folder.mkdir(exist_ok=True)

log_file = log_folder / "pipeline.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

