import tensorflow as tf
import mlflow
import mlflow.keras
from Kidney_CTScan.components import *
from Kidney_CTScan.config.configuration import ModelEvaluationConfig
from Kidney_CTScan.utils.utility import save_json
from pathlib import Path
from urllib.parse import urlparse

class Evaluation:
    def __init__(self, config = ModelEvaluationConfig):
        self.config = config

    def _valid_generator(self):
        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split = 0.30
        )

        dataflow_kwargs = dict(
            target_size = self.config.params_image_size[:-1],
            batch_size = self.config.params_batch_size,
            interpolation = "bilinear"
        )

        #generate validation data
        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(**datagenerator_kwargs)

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory = self.config.training_data,
            subset = "validation",
            shuffle = False,
            **dataflow_kwargs
        )
    
    def evaluate(self):
        self.model = self.load_model(self.config.path_of_model)
        self._valid_generator()
        self.score = self.model.evaluate(self.valid_generator)
        self.save_score()
    
    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(file_path = Path("scores.json"), data= scores)
    
    def log_into_mlflow(self):
        mlflow.set_tracking_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            mlflow.log_params(self.config.all_param)
            mlflow.log_metrics(
                {"loss": self.score[0], "accuracy": self.score[1]}
            )
            if tracking_url_type_store != "file":
                mlflow.log_artifact(self.config.path_of_model, "model")
            else:
                mlflow.log_artifact(self.config.path_of_model, "model")

    @staticmethod
    def load_model(path:Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)