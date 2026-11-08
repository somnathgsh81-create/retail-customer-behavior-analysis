import pandas as pd
import numpy as np
import urllib
from sqlalchemy import create_engine

def run_data_pipeline():
    raw_path = r'E:\SOM PERSONAL\Project\customer_shopping_behavior.csv'
    df = pd.read_csv(raw_path)
    
    df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))
    
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(' ', '_')
    
    df = df.rename(columns={'purchase_amount_(usd)': 'purchase_amount'})
    
    labels = ['Young Adult', 'Adult', 'Middle-aged', 'Senior']
    df['age_group'] = pd.qcut(df['age'], q=4, labels=labels)
    
    frequency_mapping = {
        'Fortnightly': 14,
        'Weekly': 7,
        'Monthly': 30,
        'Quarterly': 90,
        'Bi-Weekly': 14,
        'Annually': 365,
        'Every 3 Months': 90
    }
    df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)
    
    df = df.drop('promo_code_used', axis=1)
    
    server = r'localhost\SQLEXPRESS'
    database = 'customer_behavior'
    
    params = urllib.parse.quote_plus(
        f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'
    )
    engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")
    
    df.to_sql('customer_analysis_table', con=engine, if_exists='replace', index=False)
    print("Table successfully exported to MS SQL Server")

if __name__ == "__main__":
    run_data_pipeline()
