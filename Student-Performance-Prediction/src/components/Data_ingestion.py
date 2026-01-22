import os
import sys
import pandas as pd
from src.logger import logging
from dataclasses import dataclass
from src.exception import CustomException
from sklearn.model_selection import train_test_split
from pathlib import Path


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('Artifacts','Train_Data.csv')
    test_data_path: str = os.path.join('Artifacts','Test_Data.csv')
    raw_data_path: str = os.path.join('Artifacts','Raw_Data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Data Ingestion Config")
        try:
            
            project_root = Path(__file__).resolve().parents[2]

            data_path = project_root / "Notebook_Experiments" / "Data" / "stud.csv"

            if not data_path.exists():
                raise FileNotFoundError(f"Dataset not found at: {data_path}")

            data = pd.read_csv(data_path)
            logging.info("Read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Created the raw data file")

            logging.info("Splitting the data into train and test")
            train_data, test_data = train_test_split(
                data, test_size=0.2, random_state=42
            )
            logging.info("Data Splitting is done")

            train_data.to_csv(self.ingestion_config.train_data_path, index=False)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False)
            logging.info("Created the train and test data files")
            logging.info("Data ingestion Completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )

        except Exception as e:
            logging.info("Exception occurred while ingesting the data")
            raise CustomException(e, sys)
