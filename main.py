from src.Kidney_CTScan import logger
from src.Kidney_CTScan import CustomException
from src.Kidney_CTScan.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.Kidney_CTScan.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from src.Kidney_CTScan.pipeline.stage_03_model_training import TrainingPipepline
from src.Kidney_CTScan.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline
import sys


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx============x\n\n")
except Exception as e:
        logger.exception(e)
        raise CustomException(e,sys)


STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = PrepareBaseModelPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx============x\n\n")
except Exception as e:
        logger.exception(e)
        raise CustomException(e,sys)

STAGE_NAME = "Model Training"
try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    obj = TrainingPipepline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx============x\n\n")
except Exception as e:
    logger.exception(e)
    raise CustomException(e,sys)

STAGE_NAME = "Model Evaluation"
try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx============x\n\n")
except Exception as e:
    logger.exception(e)
    raise CustomException(e, sys)