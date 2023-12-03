# KidneyCNN

## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
10. Update app.py

# How to run?

### STEPS:
Clone the repository
```bash
https://github.com/VishalChandru/KidneyCNN
```

### STEP 01- Create a conda environment after opening the repository
```bash 
conda create -p venv python=3.11 -y
```

```bash
conda activate venv
```

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


# MLFlow
[Documentation](https://mlflow.org/docs/latest/index.html)

##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/VishalChandru/KidneyCNN.mlflow \
MLFLOW_TRACKING_USERNAME=VishalChandru \
MLFLOW_TRACKING_PASSWORD=db7fb84a8a680ae7d4b6ee54f6ad4bf9e542dc0f \
python script.py

Run this to export as env variables:

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/VishalChandru/KidneyCNN.mlflow

export MLFLOW_TRACKING_USERNAME=VishalChandru

export MLFLOW_TRACKING_PASSWORD=db7fb84a8a680ae7d4b6ee54f6ad4bf9e542dc0f
```

### DVC

1. dvc init
2. dvc repro
3. dvc dag

