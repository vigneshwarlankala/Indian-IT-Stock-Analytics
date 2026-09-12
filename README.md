# Indian IT Stock Analytics & ML-Based Price Prediction

## Introduction

**Indian IT Stock Analytics** is an end-to-end data analytics and
machine learning project focused on analyzing historical stock-market
data of major Indian IT companies and generating data-driven
closing-price predictions.

The project combines **Python for data collection, preprocessing,
feature engineering and machine learning**, **MySQL for structured data
storage**, and **Tableau for interactive visualization and
dashboard-based analysis**.

The project covers five major Indian IT companies:

-   Tata Consultancy Services (TCS)
-   Infosys
-   Wipro
-   HCLTech
-   Tech Mahindra

> **Purpose:** This project is developed for academic, analytical, and
> portfolio demonstration purposes. Stock predictions are model outputs
> and should not be considered financial advice.

------------------------------------------------------------------------

## Project Objectives

-   Collect and organize historical stock-market data.
-   Clean and preprocess financial time-series data.
-   Create useful technical and statistical features.
-   Store and manage processed data using MySQL.
-   Train machine learning models for stock closing-price prediction.
-   Compare model performance using standard regression metrics.
-   Analyze stock trends, returns, volatility, and company-level
    performance.
-   Build interactive Tableau dashboards for communicating insights.

------------------------------------------------------------------------

## Key Features

### 1. Data Collection

Historical stock data is collected and prepared for analysis, including
market variables such as:

-   Date
-   Open price
-   High price
-   Low price
-   Close price
-   Adjusted close
-   Trading volume

### 2. Data Preprocessing

The project prepares the raw data for analysis by handling data-quality
requirements and creating a consistent dataset for downstream analytics
and machine learning.

### 3. Feature Engineering

Financial and technical features are generated from historical price
data. These features help the machine learning models learn
relationships between previous market observations and future closing
prices.

Examples include:

-   Daily returns
-   Moving averages
-   RSI
-   Bollinger Bands
-   Rolling volatility
-   Volume-related indicators
-   Previous-day price features

### 4. Machine Learning-Based Prediction

The project uses regression-based machine learning models to estimate
stock closing prices from engineered historical features.

The repository contains model-comparison and prediction-result datasets,
allowing the performance of different approaches to be evaluated and the
resulting predictions to be analyzed.

### 5. MySQL Data Storage

MySQL is used as the relational database layer for storing and managing
processed stock data and prediction-related information.

### 6. Tableau Visualization

Tableau is used to convert analytical results into interactive
dashboards for:

-   Market overview
-   Company comparison
-   Technical analysis
-   Risk and portfolio analysis
-   Actual vs. predicted stock prices

------------------------------------------------------------------------

## Tech Stack

  -----------------------------------------------------------------------
  Technology                          Purpose
  ----------------------------------- -----------------------------------
  **Python**                          Data collection, preprocessing,
                                      feature engineering and ML

  **Pandas**                          Data manipulation and analysis

  **NumPy**                           Numerical operations

  **Scikit-learn**                    Machine learning model development
                                      and evaluation

  **MySQL**                           Relational database storage

  **Tableau**                         Interactive dashboards and
                                      visualization

  **Jupyter Notebook**                Exploratory analysis and
                                      experimentation

  **Git & GitHub**                    Version control and project hosting
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## Machine Learning & Stock Price Prediction

The prediction workflow follows a time-series-oriented process:

``` text
Historical Stock Data
        ↓
Data Collection
        ↓
Data Cleaning & Preprocessing
        ↓
Feature Engineering
        ↓
Train/Test Data Preparation
        ↓
Machine Learning Models
        ↓
Model Evaluation & Comparison
        ↓
Closing Price Prediction
        ↓
Tableau Visualization
```

The project compares regression models and evaluates their predictions
using metrics such as:

-   **MAE (Mean Absolute Error)** --- measures the average absolute
    difference between actual and predicted values.
-   **RMSE (Root Mean Squared Error)** --- gives greater weight to
    larger prediction errors.
-   **R² (Coefficient of Determination)** --- indicates how well the
    model explains variation in the target variable.

The generated files `models/model_comparison.csv` and
`models/stock_predictions.csv` contain the project's model-comparison
and prediction outputs.

> Machine learning predictions are based on historical patterns and do
> not guarantee future stock-market performance.

------------------------------------------------------------------------

## Repository Structure

``` text
Indian-IT-Stock-Analytics/
│
├── data/
│   ├── stock_data_raw.csv
│   └── stock_data_processed.csv
│
├── models/
│   ├── model_comparison.csv
│   └── stock_predictions.csv
│
├── src/
│   ├── data_collection.py
│   ├── feature_engineering.py
│   ├── ml_prediction.py
│   ├── mysql_loader.py
│   └── prediction_loader.py
│
├── dashboard/
├── sql/
│
├── .gitignore
└── README.md
```

### Folder Description

**`data/`**\
Contains the raw and processed stock datasets used by the project.

**`models/`**\
Contains model-comparison results and generated stock-prediction
outputs.

**`src/`**\
Contains the Python source code for data collection, feature
engineering, machine learning, MySQL loading, and prediction loading.

**`dashboard/`**\
Reserved for Tableau/dashboard-related project assets.

**`sql/`**\
Contains SQL/database-related project files.

------------------------------------------------------------------------

## Installation

### Prerequisites

Install the following before running the project:

-   Python 3.x
-   MySQL Server
-   MySQL client/tool such as MySQL Workbench
-   Tableau Desktop or Tableau Public
-   Git

### 1. Clone the Repository

``` bash
git clone https://github.com/vigneshwarlankala/Indian-IT-Stock-Analytics.git
cd Indian-IT-Stock-Analytics
```

### 2. Create a Virtual Environment

Windows:

``` bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Python Dependencies

If a `requirements.txt` file is present, run:

``` bash
pip install -r requirements.txt
```

If dependencies need to be installed individually, the project uses
common data-science packages such as:

``` bash
pip install pandas numpy scikit-learn yfinance mysql-connector-python
```

### 4. Configure MySQL

Create the required MySQL database and tables using the SQL files
available in the `sql/` directory.

Update the database connection settings in the relevant Python
configuration/code before running the database-loading scripts.

**Do not commit real database passwords, API keys, or other credentials
to GitHub.**

------------------------------------------------------------------------

## Usage

### Step 1 --- Collect Stock Data

Run the data-collection script:

``` bash
python src/data_collection.py
```

This prepares the historical stock data used by the project.

### Step 2 --- Generate Features

Run:

``` bash
python src/feature_engineering.py
```

This prepares analytical and technical features for downstream modeling.

### Step 3 --- Load Data into MySQL

Run:

``` bash
python src/mysql_loader.py
```

Use your local MySQL configuration when connecting to the database.

### Step 4 --- Train Prediction Models

Run:

``` bash
python src/ml_prediction.py
```

This performs the machine-learning prediction workflow and generates
prediction/model-evaluation outputs.

### Step 5 --- Load Prediction Results

Run:

``` bash
python src/prediction_loader.py
```

This supports loading prediction results for further analysis or
visualization.

### Step 6 --- Open the Tableau Dashboard

Open the Tableau workbook/dashboard associated with the project and
connect it to the prepared data sources.

Use the dashboards to explore:

-   Stock-price trends
-   Company comparisons
-   Technical indicators
-   Risk and portfolio information
-   Actual vs. predicted prices
-   Model performance

------------------------------------------------------------------------

## Project Workflow

``` text
              ┌──────────────────────┐
              │ Historical Stock Data│
              └──────────┬───────────┘
                         ↓
              ┌──────────────────────┐
              │ Python Data Pipeline │
              └──────────┬───────────┘
                         ↓
              ┌──────────────────────┐
              │ Feature Engineering  │
              └──────────┬───────────┘
                         ↓
              ┌──────────────────────┐
              │      MySQL DB        │
              └──────────┬───────────┘
                         ↓
              ┌──────────────────────┐
              │ Machine Learning     │
              │ Price Prediction     │
              └──────────┬───────────┘
                         ↓
              ┌──────────────────────┐
              │ Tableau Dashboards    │
              └──────────────────────┘
```

------------------------------------------------------------------------

## Skills Demonstrated

This project demonstrates practical experience in:

-   Python programming
-   Data cleaning and preprocessing
-   Exploratory data analysis
-   Feature engineering
-   Time-series data handling
-   Machine learning
-   Regression-model evaluation
-   SQL and MySQL database operations
-   Data visualization
-   Tableau dashboard development
-   Git and GitHub version control

------------------------------------------------------------------------

## Future Enhancements

Possible extensions include:

-   Adding more Indian and global stocks.
-   Incorporating additional market and macroeconomic features.
-   Testing additional time-series and machine-learning approaches.
-   Automating regular data updates.
-   Improving dashboard interactivity.
-   Adding live or near-real-time market-data pipelines.
-   Deploying the analytics application as a web application.

------------------------------------------------------------------------

## Disclaimer

This project is intended for **educational, analytical, and portfolio
purposes**. The machine learning predictions are generated from
historical data and selected features. They are not guaranteed forecasts
of future market prices and should not be used as a substitute for
professional financial advice.

------------------------------------------------------------------------

## Contact

**L. Vigneshwar Reddy**

GitHub: <https://github.com/vigneshwarlankala>

Project Repository:
<https://github.com/vigneshwarlankala/Indian-IT-Stock-Analytics>

------------------------------------------------------------------------
