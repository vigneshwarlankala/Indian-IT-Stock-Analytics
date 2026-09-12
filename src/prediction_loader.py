import pandas as pd
from sqlalchemy import create_engine

DB_USER = "root"
DB_PASSWORD = "Bumrah93"
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "it_stock_analytics"

connection_string = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(connection_string)

print("Loading ML prediction data...")

data = pd.read_csv("models/stock_predictions.csv")

print("Rows found:", len(data))

data["Date"] = pd.to_datetime(data["Date"]).dt.date

print("\nUploading predictions to MySQL...")

data.to_sql(
    "stock_predictions",
    con=engine,
    if_exists="append",
    index=False,
    chunksize=500
)

print("\n================================")
print("PREDICTION DATA UPLOAD COMPLETED")
print("================================")

print("Rows uploaded:", len(data))

print("\nCompanies:")
print(data["Company"].value_counts())

print("\nBest Models:")
print(data["Best_Model"].value_counts())