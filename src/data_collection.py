import yfinance as yf
import pandas as pd

companies = {
    "TCS": "TCS.NS",
    "INFOSYS": "INFY.NS",
    "WIPRO": "WIPRO.NS",
    "HCLTECH": "HCLTECH.NS",
    "TECHM": "TECHM.NS"
}

all_data = []

for company, ticker in companies.items():

    print("Downloading:", company)

    data = yf.download(
        ticker,
        start="2015-01-01",
        end="2026-01-01",
        auto_adjust=False
    )

    # Convert multi-level columns to normal columns
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    data = data.reset_index()

    # Add company name
    data["Company"] = company

    all_data.append(data)

final_data = pd.concat(all_data, ignore_index=True)

# Save cleaned structure
final_data.to_csv(
    "data/stock_data_raw.csv",
    index=False
)

print("\nData collection completed!")
print("Rows:", len(final_data))
print("\nColumns:")
print(final_data.columns.tolist())

print("\nFirst 5 rows:")
print(final_data.head())