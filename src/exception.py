# for handling exceptions

import sys
from src.logger import logging # this is because to save the exception in logging files

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in Python script name: {0}, line number: {1}, error message: {2}".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)
        
    def __str__(self):
        return self.error_message
    
#for testing
# if __name__ == "__main__":
#     try:
#         a = 1 / 0  # Intentional division by zero to trigger the exception
#     except Exception as e:
#         logging.info("Divide operation failed.")
#         raise CustomException(e, sys)
