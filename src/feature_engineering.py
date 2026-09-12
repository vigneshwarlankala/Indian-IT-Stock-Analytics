import pandas as pd

# ==========================================
# 1. LOAD RAW STOCK DATA
# ==========================================

data = pd.read_csv("data/stock_data_raw.csv")

data["Date"] = pd.to_datetime(data["Date"])

# Sort company-wise and date-wise
data = data.sort_values(["Company", "Date"]).reset_index(drop=True)


# ==========================================
# 2. DAILY PRICE CHANGE
# ==========================================

data["Price_Change"] = (
    data.groupby("Company")["Close"].diff()
)


# ==========================================
# 3. DAILY PERCENTAGE RETURN
# ==========================================

data["Daily_Return"] = (
    data.groupby("Company")["Close"].pct_change()
)


# ==========================================
# 4. MOVING AVERAGES
# ==========================================

data["MA_20"] = (
    data.groupby("Company")["Close"]
    .transform(lambda x: x.rolling(20).mean())
)

data["MA_50"] = (
    data.groupby("Company")["Close"]
    .transform(lambda x: x.rolling(50).mean())
)

data["MA_200"] = (
    data.groupby("Company")["Close"]
    .transform(lambda x: x.rolling(200).mean())
)


# ==========================================
# 5. 20-DAY VOLATILITY
# ==========================================

data["Volatility_20"] = (
    data.groupby("Company")["Daily_Return"]
    .transform(lambda x: x.rolling(20).std())
)


# ==========================================
# 6. RSI
# ==========================================

def calculate_rsi(series, period=14):

    delta = series.diff()

    gain = delta.clip(lower=0)

    loss = -delta.clip(upper=0)

    average_gain = gain.rolling(period).mean()

    average_loss = loss.rolling(period).mean()

    rs = average_gain / average_loss

    rsi = 100 - (100 / (1 + rs))

    return rsi


data["RSI_14"] = (
    data.groupby("Company")["Close"]
    .transform(calculate_rsi)
)


# ==========================================
# 7. BOLLINGER BANDS
# ==========================================

rolling_mean = (
    data.groupby("Company")["Close"]
    .transform(lambda x: x.rolling(20).mean())
)

rolling_std = (
    data.groupby("Company")["Close"]
    .transform(lambda x: x.rolling(20).std())
)

data["BB_Middle"] = rolling_mean

data["BB_Upper"] = (
    rolling_mean + (2 * rolling_std)
)

data["BB_Lower"] = (
    rolling_mean - (2 * rolling_std)
)


# ==========================================
# 8. VOLUME ANALYSIS
# ==========================================

data["Volume_MA_20"] = (
    data.groupby("Company")["Volume"]
    .transform(lambda x: x.rolling(20).mean())
)

data["Volume_Ratio"] = (
    data["Volume"] / data["Volume_MA_20"]
)

data["Volume_Change"] = (
    data.groupby("Company")["Volume"].pct_change()
)


# ==========================================
# 9. MA CROSSOVER SIGNAL
# ==========================================

def generate_ma_signal(group):

    signal = []

    for ma20, ma50 in zip(group["MA_20"], group["MA_50"]):

        if pd.isna(ma20) or pd.isna(ma50):
            signal.append("HOLD")

        elif ma20 > ma50:
            signal.append("BUY")

        elif ma20 < ma50:
            signal.append("SELL")

        else:
            signal.append("HOLD")

    return pd.Series(signal, index=group.index)


data["MA_Signal"] = (
    data.groupby("Company", group_keys=False)
    .apply(generate_ma_signal, include_groups=False)
    .reset_index(level=0, drop=True)
)


# ==========================================
# 10. RSI SIGNAL
# ==========================================

def rsi_signal(rsi):

    if pd.isna(rsi):
        return "HOLD"

    elif rsi < 30:
        return "OVERSOLD"

    elif rsi > 70:
        return "OVERBOUGHT"

    else:
        return "NEUTRAL"


data["RSI_Signal"] = data["RSI_14"].apply(rsi_signal)


# ==========================================
# 11. CUMULATIVE MAXIMUM PRICE
# ==========================================

data["Peak_Price"] = (
    data.groupby("Company")["Close"]
    .cummax()
)


# ==========================================
# 12. DRAWDOWN
# ==========================================

data["Drawdown"] = (
    (data["Close"] - data["Peak_Price"])
    / data["Peak_Price"]
)


# ==========================================
# 13. RISK CATEGORY
# ==========================================

def risk_category(volatility):

    if pd.isna(volatility):
        return "UNKNOWN"

    elif volatility < 0.015:
        return "LOW"

    elif volatility < 0.03:
        return "MEDIUM"

    else:
        return "HIGH"


data["Risk_Category"] = (
    data["Volatility_20"].apply(risk_category)
)


# ==========================================
# 14. SAVE PROCESSED DATA
# ==========================================

data.to_csv(
    "data/stock_data_processed.csv",
    index=False
)


# ==========================================
# 15. DISPLAY RESULTS
# ==========================================

print("\nFeature engineering completed!")

print("Rows:", len(data))

print("\nColumns:")
print(data.columns.tolist())

print("\nLast 10 rows:")
print(data.tail(10))

print("\nMA Signal counts:")
print(data["MA_Signal"].value_counts())

print("\nRSI Signal counts:")
print(data["RSI_Signal"].value_counts())

print("\nRisk Category counts:")
print(data["Risk_Category"].value_counts())