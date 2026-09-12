import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# ==========================================
# 1. LOAD PROCESSED DATA
# ==========================================

data = pd.read_csv("data/stock_data_processed.csv")

data["Date"] = pd.to_datetime(data["Date"])

# Sort chronologically
data = data.sort_values(
    ["Company", "Date"]
).reset_index(drop=True)


# ==========================================
# 2. CREATE NEXT-DAY TARGET
# ==========================================

data["Target_Close"] = (
    data.groupby("Company")["Close"].shift(-1)
)


# ==========================================
# 3. SELECT ML FEATURES
# ==========================================

features = [
    "Close",
    "High",
    "Low",
    "Open",
    "Volume",
    "Daily_Return",
    "MA_20",
    "MA_50",
    "MA_200",
    "Volatility_20",
    "RSI_14",
    "BB_Middle",
    "BB_Upper",
    "BB_Lower",
    "Volume_MA_20",
    "Volume_Ratio",
    "Volume_Change"
]


# ==========================================
# 4. STORAGE FOR RESULTS
# ==========================================

all_predictions = []

model_results = []


# ==========================================
# 5. TRAIN MODELS FOR EACH COMPANY
# ==========================================

for company in data["Company"].unique():

    print("\n================================")
    print("Company:", company)
    print("================================")

    company_data = data[
        data["Company"] == company
    ].copy()

    # --------------------------------------
    # Replace infinity values
    # --------------------------------------

    company_data = company_data.replace(
        [np.inf, -np.inf],
        np.nan
    )

    # --------------------------------------
    # Remove rows with missing values
    # --------------------------------------

    company_data = company_data.dropna(
        subset=features + ["Target_Close"]
    )

    # Sort by date
    company_data = company_data.sort_values(
        "Date"
    )


    # ======================================
    # 6. TIME-BASED TRAIN / TEST SPLIT
    # ======================================

    split_index = int(
        len(company_data) * 0.80
    )

    train_data = company_data.iloc[
        :split_index
    ]

    test_data = company_data.iloc[
        split_index:
    ]


    X_train = train_data[features]
    y_train = train_data["Target_Close"]

    X_test = test_data[features]
    y_test = test_data["Target_Close"]


    print("Training rows:", len(train_data))
    print("Testing rows:", len(test_data))


    # ======================================
    # 7. LINEAR REGRESSION
    # ======================================

    linear_model = LinearRegression()

    linear_model.fit(
        X_train,
        y_train
    )

    linear_predictions = (
        linear_model.predict(X_test)
    )


    # ======================================
    # 8. RANDOM FOREST
    # ======================================

    rf_model = RandomForestRegressor(
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    )

    rf_model.fit(
        X_train,
        y_train
    )

    rf_predictions = (
        rf_model.predict(X_test)
    )


    # ======================================
    # 9. GRADIENT BOOSTING
    # ======================================

    gb_model = GradientBoostingRegressor(
        n_estimators=100,
        learning_rate=0.05,
        max_depth=3,
        random_state=42
    )

    gb_model.fit(
        X_train,
        y_train
    )

    gb_predictions = (
        gb_model.predict(X_test)
    )


    # ======================================
    # 10. MODEL EVALUATION
    # ======================================

    models = {
        "Linear Regression": linear_predictions,
        "Random Forest": rf_predictions,
        "Gradient Boosting": gb_predictions
    }


    for model_name, predictions in models.items():

        mae = mean_absolute_error(
            y_test,
            predictions
        )

        rmse = np.sqrt(
            mean_squared_error(
                y_test,
                predictions
            )
        )

        r2 = r2_score(
            y_test,
            predictions
        )

        model_results.append({
            "Company": company,
            "Model": model_name,
            "MAE": mae,
            "RMSE": rmse,
            "R2_Score": r2
        })

        print(
            f"{model_name}: "
            f"MAE={mae:.2f}, "
            f"RMSE={rmse:.2f}, "
            f"R2={r2:.4f}"
        )


    # ======================================
    # 11. FIND BEST MODEL
    # ======================================

    company_results = [
        result
        for result in model_results
        if result["Company"] == company
    ]

    best_model = min(
        company_results,
        key=lambda x: x["MAE"]
    )["Model"]


    # ======================================
    # 12. GET BEST MODEL PREDICTIONS
    # ======================================

    if best_model == "Linear Regression":

        best_predictions = linear_predictions

    elif best_model == "Random Forest":

        best_predictions = rf_predictions

    else:

        best_predictions = gb_predictions


    # ======================================
    # 13. CREATE PREDICTION DATASET
    # ======================================

    prediction_data = test_data[
        ["Date", "Company", "Close"]
    ].copy()

    prediction_data["Actual_Close"] = (
        test_data["Target_Close"].values
    )

    prediction_data["Predicted_Close"] = (
        best_predictions
    )

    prediction_data["Best_Model"] = (
        best_model
    )

    all_predictions.append(
        prediction_data
    )


# ==========================================
# 14. SAVE MODEL COMPARISON
# ==========================================

results_df = pd.DataFrame(
    model_results
)

results_df.to_csv(
    "models/model_comparison.csv",
    index=False
)


# ==========================================
# 15. SAVE PREDICTIONS
# ==========================================

predictions_df = pd.concat(
    all_predictions,
    ignore_index=True
)

predictions_df.to_csv(
    "models/stock_predictions.csv",
    index=False
)


# ==========================================
# 16. FINAL OUTPUT
# ==========================================

print("\n================================")
print("ML TRAINING COMPLETED")
print("================================")

print("\nModel Comparison:")
print(results_df.to_string(index=False))

print("\nPrediction file created:")
print("models/stock_predictions.csv")

print("\nModel comparison file created:")
print("models/model_comparison.csv")

print("\nBest Models:")

best_models = (
    results_df.loc[
        results_df.groupby("Company")["MAE"].idxmin()
    ]
)

print(
    best_models[
        ["Company", "Model", "MAE", "RMSE", "R2_Score"]
    ].to_string(index=False)
)