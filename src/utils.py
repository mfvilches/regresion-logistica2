from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd

# load the .env file variables
load_dotenv()


def db_connect():
    import os
    engine = create_engine(os.getenv('DATABASE_URL'))
    engine.connect()
    return engine

def transformar_columnas_object(df):
    for column in df.columns:
        if df[column].dtype == 'object':
            df[column+'_n'] = pd.factorize(df[column])[0]
    return df
