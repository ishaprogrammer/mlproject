# for logging the data i.e every info should be there

import logging
import os
from datetime import datetime

# Use single quotes or escape double quotes within double quotes
log_file = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"  # Fixed date format string
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

log_file_path = os.path.join(logs_path, log_file)  # Variable name corrected to lowercase

logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


#for testing
# if __name__ == "__main__":
#     logging.info("Logging has started..")
