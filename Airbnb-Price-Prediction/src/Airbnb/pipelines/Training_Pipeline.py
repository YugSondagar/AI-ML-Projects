from src.Airbnb.components.Data_ingestion import DataIngestion
from src.Airbnb.components.Data_transformation import DatTransformation
from src.Airbnb.components.Model_trainer import ModelTrainer

obj = DataIngestion()
train_data_path, test_data_path = obj.initiate_data_ingestion()

data_transformation = DatTransformation()
train_arr,test_arr = data_transformation.initialize_data_transformation(train_data_path,test_data_path)

model_trainer_obj = ModelTrainer()
model_trainer_obj.initiate_model_training(train_arr,test_arr)