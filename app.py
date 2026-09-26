from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():

    # =========================================
    # LOAD PREDICTION DATA
    # =========================================

    predictions = pd.read_csv(
        "models/stock_predictions.csv"
    )


    # =========================================
    # LOAD MODEL COMPARISON DATA
    # =========================================

    model_comparison = pd.read_csv(
        "models/model_comparison.csv"
    )


    # =========================================
    # LOAD HISTORICAL STOCK DATA
    # =========================================

    historical_data = pd.read_csv(
        "data/stock_data_processed.csv"
    )


    # =========================================
    # GET COMPANY NAMES
    # =========================================

    companies = sorted(
        predictions["Company"].unique()
    )


    # =========================================
    # CLEAN HISTORICAL DATA
    # =========================================

    historical_data["Date"] = pd.to_datetime(
        historical_data["Date"]
    )


    # Convert dates back to strings
    # so Flask can send them to JavaScript

    historical_data["Date"] = (
        historical_data["Date"]
        .dt.strftime("%Y-%m-%d")
    )


    # =========================================
    # SEND DATA TO HTML
    # =========================================

    return render_template(

        "index.html",

        predictions=
            predictions.to_dict(
                orient="records"
            ),

        model_comparison=
            model_comparison.to_dict(
                orient="records"
            ),

        historical_data=
            historical_data.to_dict(
                orient="records"
            ),

        companies=companies

    )


if __name__ == "__main__":

    app.run(
        debug=True
    )