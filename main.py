from src.Kidney_CTScan import logger
from src.Kidney_CTScan import CustomException
import sys

try:
    logger.info('the log is recorded as demo')
    a = 1/0
except Exception as e:
    raise CustomException(e,sys)