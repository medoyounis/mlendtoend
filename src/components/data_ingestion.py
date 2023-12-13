import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass 
#this is a decorator: you can use it when you only are defining variables in the calss,if you have other functions it is not recommended

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")#the training data will be saved here
    test_data_path: str=os.path.join('artifacts',"test.csv")#the testing data will be saved here
    raw_data_path: str=os.path.join('artifacts',"data.csv")#the raw data will be saved here

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig() #the three variables above will be stored in ingestion_config

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the dataset as dataframe')#so we can know if an exception happens, we can know where it happens

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)#to create the artifacts folder, exist_ok=True: if it there no need to delete and recreate

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)#saving the training data after the split

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)#saving the testing data after the split

            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()