# secondly data transformation i.e numeric to str etc.
import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from src.exception import CustomException
from src.logger import logging
import os

class DataTransformation_config:
    preprocessor_obj_file_path = os.path.join('artifacts',"preprocessor.pkl")
    
class DataTransformer:
    def __init__(self):
        self.data_transformation_config = DataTransformation_config()
    
    def get_transformer_object(self):
        try:
            numerical_features = ["writing_score","reading_score"]
            categorical_features = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
                ]
            
            num_pipeline = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scaler",StandardScaler())
                ]
            )
            
            cat_pipeline = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder",OneHotEncoder()),
                    ("scaler",StandardScaler())
                ]
            )
            logging.info("Numerical cols scaling completed")
            logging.info("categorical cols encoding completed")
            
            preprocessor = ColumnTransformer([
                ("num_pipeline",num_pipeline,numerical_features),
                ("cat_pipeline",cat_pipeline,categorical_features)
            ])
            
            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)
        

    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            
            logging.info("read train and test data completed")
            
            logging.info("obtaining preprocessing object")
            preprocessing_obj = self.get_transformer_object()
            target_column_name = "math_score"
            numerical_features = ["writing_score","reading_score"]
            
            input_feature_train_df = train_df.drop(columns=[target_column_name],axis=1)
            
            

        except:
            pass
        