import os
import zipfile
import sys
import gdown
from src.Kidney_CTScan import logger
from src.Kidney_CTScan.utils.utility import get_size
from src.Kidney_CTScan import CustomException
from src.Kidney_CTScan.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config = config
    
    def download_data(self) -> str:
        try:
            dataset_url = self.config.source_url
            zip_download_dir = self.config.local_data_file
            os.makedirs(self.config.root_dir, exist_ok=True)
            logger.info(f'Downloading dataset from {dataset_url} to local directory {zip_download_dir}')

            file_id = dataset_url.split('/')[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id, zip_download_dir)
            logger.info(f'Downloaded dataset from {dataset_url} to local directory {zip_download_dir}')

        except Exception as e:
            raise CustomException(e,sys)
    
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,"r") as f:
            f.extractall(unzip_path)