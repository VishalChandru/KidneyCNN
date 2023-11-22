import os
import logging
import sys
from datetime import datetime


LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_DIR = 'logs'
LOG_FILE_PATH = os.path.join(os.getcwd(),LOG_FILE_DIR,LOG_FILE)
os.makedirs(LOG_FILE_DIR, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format= f'[ %(asctime)s ] %(levelname)s : %(module)s - %(lineno)d - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger('KidneyCNNLogger')



def get_error_detail(error_msg, err_detail:sys):
    _,_,tb = err_detail.exc_info()
    filename = tb.tb_frame.f_code.co_filename
    error_msg = f'Error occured in python script {filename} in line no {tb.tb_lineno} with error {error_msg}'

    return error_msg

class CustomException(Exception):
    def __init__(self, error_msg, err_detail:sys):
        super().__init__(error_msg)
        self.err_msg = get_error_detail(error_msg,err_detail)

    def __str__(self):
        return self.err_msg

    
