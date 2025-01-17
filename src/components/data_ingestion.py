# first data ingestion will happen means data from database 
import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

#this class saves the train,test,raw modular code to the specified files
@dataclass
class Data_Ingestion_Config:
    train_data_path : str = os.path.join('artifacts',"train.csv")
    test_data_path : str = os.path.join('artifacts',"test.csv")
    raw_data_path : str = os.path.join('artifacts',"raw.csv")
    
class DataIngestion:
    def __init__(self):
        self.ingestion_config = Data_Ingestion_Config() #here the ingestion_config is a variable which will have sub_variables of Data_Ingestion()
    
    def initiate_data_ingestion(self):
        logging.info("entered the data ingestion method")
        try:
            df = pd.read_csv(r'C:\Users\isha\Downloads\mlproject\notebook\data\stud.csv')
            logging.info("Read the dataframe")
            
            #now we will make files for the artifacts
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            
            #converted raw data to csv file
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("train test split initiated")
            train_set, test_set = train_test_split(df,test_size=0.2,random_state=42)
            
            #save the train and test files
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("ingestion of the data completed")
            
            return (
                self.ingestion_config.train_data_path, 
                self.ingestion_config.test_data_path,
            )
        except Exception as e:
            raise CustomException(e,sys)
            
            
if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
        



