import os
import sys
import yaml
import json
import joblib
from pathlib import Path
from box import ConfigBox
from typing import Any
from ensure import ensure_annotations
import base64
from Kidney_CTScan import logger
from Kidney_CTScan import CustomException


@ensure_annotations
def read_yaml(file_path:Path) -> ConfigBox:
    try:
        with open(file_path) as f:
            content = yaml.safe_load(f)
            logger.info(f"Read the yaml file from {file_path}")
            return ConfigBox(content)
    except Exception as e:
        raise CustomException(e,sys)

@ensure_annotations
def create_directories(file_paths:list, verbose = True):
    try:
        for path in file_paths:
            os.makedirs(path,exist_ok=True)
            if verbose == True:
                logger.info(f"Created a directory on {path}")
    except Exception as e:
        raise CustomException(e,sys)

@ensure_annotations
def save_json(file_path:Path, data: dict):
    try:
        with open(file_path, "w") as f:
            json.dump(data, f, indent= 4)
        logger.info(f"Create json file at {file_path}")
    except Exception as e:
        raise CustomException(e,sys)

@ensure_annotations
def load_json(file_path:Path) -> ConfigBox:
    try:
        with open(file_path, "r") as f:
            content = json.load(f)
        logger.info(f"Loaded json file from {file_path}")
        return ConfigBox(content)
    except Exception as e:
        raise CustomException(e,sys)

@ensure_annotations
def save_bin(file_path:Path, data:Any):
    joblib.dump(value=data,filename=file_path)
    logger.info(f"Saved binary file at {file_path}")

@ensure_annotations
def load_bin(file_path:Path) -> Any:
    content = joblib.load(filename=file_path)
    logger.info(f"Loaded binary file from {file_path}")
    return content

@ensure_annotations
def get_size(file_path:Path) -> str:
    size_in_kb = round(os.path.getsize(file_path)/1024)
    return f'~ {size_in_kb} KB'

@ensure_annotations
def decodeImage(imagestring,filename):
    imgdata = base64.b64decode(imagestring)
    with open(filename, "wb") as f:
        f.write(imgdata)
        f.close

@ensure_annotations
def encodeImage(filename):
    with open(filename, "rb") as f:
        return base64.b64encode(f.read())