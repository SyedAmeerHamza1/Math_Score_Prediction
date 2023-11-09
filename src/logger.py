import logging
import os
from datetime import datetime

LOG_FILE= f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.logs"

log_path= os.path.join(os.getcwd(), "logs", LOG_FILE)

os.makedirs(log_path, exist_ok=True)

log_file_path= os.path.join(log_path, LOG_FILE)

logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s], %(lineno)s, %(name)s, %(levelname)s, %(message)s",
    level=logging.INFO
    )


if __name__ == "__main__":
    logging.info("Logging is working")