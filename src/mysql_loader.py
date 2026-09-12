import pandas as pd
import numpy as np
from sqlalchemy import create_engine


# ==========================================
# 1. MYSQL CONNECTION DETAILS
# ==========================================

DB_USER = "root"
DB_PASSWORD = "Bumrah93"
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "it_stock_analytics"


# ==========================================
# 2. CREATE MYSQL CONNECTION
# ==========================================

connection_string = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(connection_string)


# ==========================================
# 3. LOAD PROCESSED CSV
# ==========================================

print("Loading processed stock data...")

data = pd.read_csv(
    "data/stock_data_processed.csv"
)

print("Original rows:", len(data))


# ==========================================
# 4. CONVERT DATE
# ==========================================

data["Date"] = pd.to_datetime(
    data["Date"]
).dt.date


# ==========================================
# 5. REMOVE ID COLUMN IF PRESENT
# ==========================================

if "id" in data.columns:
    data = data.drop(columns=["id"])


# ==========================================
# 6. REPLACE INFINITY VALUES
# ==========================================

print("Checking for infinity values...")

numeric_columns = data.select_dtypes(
    include=[np.number]
).columns

infinity_count = np.isinf(
    data[numeric_columns]
).sum().sum()

print(
    "Infinity values found:",
    infinity_count
)

# Replace +inf and -inf with NaN
data = data.replace(
    [np.inf, -np.inf],
    np.nan
)


# ==========================================
# 7. CHECK MISSING VALUES
# ==========================================

missing_values = data.isna().sum().sum()

print(
    "Missing values after cleaning:",
    missing_values
)


# ==========================================
# 8. UPLOAD TO MYSQL
# ==========================================

print("\nUploading data to MySQL...")

data.to_sql(
    "stock_data",
    con=engine,
    if_exists="append",
    index=False,
    chunksize=500
)


# ==========================================
# 9. COMPLETION MESSAGE
# ==========================================

print("\n================================")
print("DATA UPLOAD COMPLETED")
print("================================")

print("Rows uploaded:", len(data))

print("\nCompanies uploaded:")

print(
    data["Company"].value_counts()
)