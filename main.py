from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys

if __name__=='__main__':
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestinoconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestinoconfig)
        logging.info("Initiate the data ingestion")
        dataingestinoartifact=data_ingestion.initiate_data_ingestion()
        print(dataingestinoconfig)
    except Exception as e:
           raise NetworkSecurityException(e,sys)