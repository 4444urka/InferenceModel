import pandas as pd

from fastapi import File, UploadFile
from src.config.Config import load_config_by_path
from src.lib.Features.Features import Features
from src.lib.PredictionModel.PredictionModel import PredictionModel
from src.lib.logger.logger import get_logger

cfg = load_config_by_path("config/config.yaml")

logger = get_logger(__name__, cfg.env, "logs/app.log")

model_instance = PredictionModel()

def predict(features: Features):
    try:
        logger.debug(f"Trying to predict price for features: {features}")
        prediction = model_instance.predict([features.totsp, features.livesp, features.kitsp, features.dist,
                                         features.metrdist, features.walk, features.brick, features.floor])
    except Exception as e:
        logger.error(f"Prediction failed: {e}")
        return e
    
    logger.info(f"Predicted successfully")
    return {"predicted_price": prediction}


def upload_data(file: UploadFile = File(...)):
    try:
        logger.debug(f"Trying to read file: {file.filename}")
        df = pd.read_csv(file.file)
    except Exception as e:
        logger.error(f"Failed to read file: {e}")
        return {"error": str(e)}

    logger.debug(f"File read successfully")

    try:
        logger.debug(f"Trying to train model")
        model_instance.train(df)
    except Exception as e:
        logger.error(f"Failed to train model: {e}")
        return {"error": str(e)}
    logger.info(f"Model trained successfully")
