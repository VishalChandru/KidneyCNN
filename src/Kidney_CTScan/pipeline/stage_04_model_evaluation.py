from Kidney_CTScan.config.configuration import ConfigurationManager
from Kidney_CTScan.components.model_evaluation_mlflow import Evaluation
from Kidney_CTScan import logger, CustomException
import sys


STAGE_NAME = "Model Evaluation"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_model_evaluation_config()
        evaluation = Evaluation(config = eval_config)
        evaluation.evaluate()
        evaluation.log_into_mlflow()

if __name__ == '__main__':
    try:
        logger.info(f"********************")
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise CustomException(e, sys)