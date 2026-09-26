# Indian IT Stock Analytics & ML-Based Price Prediction

An end-to-end **data analytics and machine learning project** for analyzing major Indian IT stocks, engineering technical indicators, storing analytical data in MySQL, comparing ML regression models, generating stock-price predictions, and presenting insights through interactive dashboards.

The project covers five major Indian IT companies:

* **Tata Consultancy Services (TCS)**
* **Infosys**
* **Wipro**
* **HCLTech**
* **Tech Mahindra**

> **Purpose:** This project is developed for academic, analytical, and portfolio demonstration purposes. Stock predictions are model outputs based on historical data and should not be considered financial advice.

---

## Project Overview

The project follows a complete data-to-insight pipeline:

```text
Historical Stock Data
        ↓
Data Collection
        ↓
Data Cleaning & Preprocessing
        ↓
Feature Engineering
        ↓
MySQL Data Storage
        ↓
Machine Learning
        ↓
Model Evaluation
        ↓
Stock Price Prediction
        ↓
Prediction Error Analysis
        ↓
Interactive Visualization
        ↓
Dashboard / Deployment
```

The project combines:

* **Python** for data collection, preprocessing, feature engineering, and machine learning
* **MySQL** for structured data storage
* **Tableau** for analytical visualization
* **HTML, CSS and JavaScript** for the interactive web dashboard
* **Plotly.js** for interactive charts
* **Git & GitHub** for version control and project hosting

---

# Project Objectives

* Collect historical stock-market data for major Indian IT companies.
* Clean and preprocess financial time-series data.
* Generate technical and statistical indicators.
* Store processed data using MySQL.
* Develop machine-learning models for closing-price prediction.
* Compare regression models using standard evaluation metrics.
* Analyze actual vs. predicted stock prices.
* Perform prediction-error analysis.
* Analyze stock trends, returns, volatility, and risk.
* Build interactive dashboards for communicating analytical results.
* Develop a portfolio-ready end-to-end data analytics project.

---

# Key Features

## 1. Historical Stock Data Collection

Historical market data is collected for five Indian IT companies.

The dataset includes:

* Date
* Open Price
* High Price
* Low Price
* Close Price
* Adjusted Close
* Trading Volume
* Company

The data collection pipeline prepares the historical dataset for subsequent preprocessing and analysis.

---

## 2. Data Preprocessing

The collected stock data is processed before machine-learning and analytical operations.

The preprocessing workflow includes:

* Handling missing values
* Detecting invalid numerical values
* Preparing time-series data
* Maintaining company-wise records
* Creating a consistent dataset for feature engineering
* Preparing data for machine-learning models

---

## 3. Feature Engineering

Technical and statistical features are generated from historical stock prices.

The project includes indicators such as:

* Daily Price Change
* Daily Return
* 20-Day Moving Average
* 50-Day Moving Average
* 200-Day Moving Average
* Rolling Volatility
* RSI
* Bollinger Bands
* Volume Moving Average
* Volume Ratio
* Volume Change
* Moving Average Signal
* RSI Signal
* Peak Price
* Drawdown
* Risk Category
* Previous-day price features

These features provide additional information about price movement, momentum, volatility, trading volume, and risk.

---

# 4. MySQL Database Integration

MySQL is used as the relational database layer of the project.

Processed stock data and prediction-related results are loaded into MySQL for structured storage and querying.

The database layer allows the project to demonstrate practical:

* SQL operations
* Database design
* Data loading
* Data retrieval
* Relational data management
* Python-to-MySQL integration

The project uses Python database connectors to transfer analytical datasets into MySQL.

> Database credentials should always be stored locally and should never be committed to GitHub.

---

# 5. Machine Learning-Based Stock Price Prediction

The project uses regression-based machine-learning models to estimate stock closing prices.

The prediction workflow includes:

```text
Processed Stock Data
        ↓
Feature Selection
        ↓
Train/Test Split
        ↓
Model Training
        ↓
Prediction
        ↓
Evaluation
        ↓
Model Comparison
```

The project compares multiple regression approaches, including:

* **Linear Regression**
* **Random Forest Regression**
* **Gradient Boosting Regression**

The models are evaluated using:

### MAE — Mean Absolute Error

Measures the average absolute difference between actual and predicted prices.

```text
Lower MAE → Smaller average prediction error
```

### RMSE — Root Mean Squared Error

Measures prediction error while giving greater importance to larger errors.

```text
Lower RMSE → Smaller large-error impact
```

### R² — Coefficient of Determination

Measures how much of the variation in the target variable is explained by the model.

```text
Higher R² → Greater explained variation
```

Model-comparison results are stored in:

```text
models/model_comparison.csv
```

Prediction results are stored in:

```text
models/stock_predictions.csv
```

---

# 6. Prediction Error Analysis

The project also includes **prediction-error analysis** to examine how closely the machine-learning predictions follow the actual stock prices.

The analysis compares:

```text
Actual Price
     vs.
Predicted Price
     ↓
Prediction Error
     ↓
Error Analysis
```

Prediction error can be examined using the difference between actual and predicted values.

This helps identify:

* Periods with larger prediction errors
* Differences between actual and predicted prices
* Model prediction behavior
* Companies where prediction errors vary over time
* Areas where the model may require improvement

The interactive dashboard provides visual analysis of prediction performance rather than relying only on numerical evaluation metrics.

---

# 7. Interactive Web Dashboard

In addition to Tableau, the project includes an interactive web-based dashboard for presenting analytical results.

The dashboard is designed to provide an accessible visual interface for exploring the stock analytics project.

It includes interactive visualizations for areas such as:

* Stock price trends
* Company comparison
* Historical performance
* Technical indicators
* Actual vs. predicted prices
* Prediction errors
* Model performance
* Risk analysis

The dashboard uses **Plotly.js** to create interactive charts.

Users can interact with the visualizations to explore different aspects of the stock data.

---

# 8. Tableau Dashboard

Tableau is used for interactive business-intelligence visualization and analytical storytelling.

The Tableau dashboards provide analysis of:

### Market Overview

* Overall stock-price trends
* Company-level performance
* Historical price movements

### Company Comparison

* Comparison of major Indian IT companies
* Price trends
* Returns
* Trading activity

### Technical Analysis

* Moving averages
* RSI
* Bollinger Bands
* Volatility
* Trading signals

### Risk Analysis

* Volatility
* Drawdown
* Risk categories
* Company-level risk comparison

### ML Prediction Analysis

* Actual vs. predicted prices
* Model results
* Prediction performance
* Prediction-error analysis

---

# Technology Stack

| Technology           | Purpose                                                    |
| -------------------- | ---------------------------------------------------------- |
| **Python**           | Data collection, preprocessing, feature engineering and ML |
| **Pandas**           | Data manipulation and analysis                             |
| **NumPy**            | Numerical computation                                      |
| **Scikit-learn**     | Machine-learning model development                         |
| **yfinance**         | Historical stock-market data collection                    |
| **MySQL**            | Relational database storage                                |
| **SQL**              | Data querying and database operations                      |
| **Tableau**          | Interactive analytics and dashboards                       |
| **HTML**             | Web dashboard structure                                    |
| **CSS**              | Dashboard styling                                          |
| **JavaScript**       | Dashboard functionality                                    |
| **Plotly.js**        | Interactive data visualization                             |
| **Jupyter Notebook** | Exploratory analysis                                       |
| **Git**              | Version control                                            |
| **GitHub**           | Project hosting and collaboration                          |

---

# Machine Learning Workflow

```text
                  Historical Stock Data
                           │
                           ▼
                  Data Collection
                           │
                           ▼
                Data Preprocessing
                           │
                           ▼
                  Feature Engineering
                           │
                           ▼
                     MySQL DB
                           │
                           ▼
                 Train/Test Preparation
                           │
                           ▼
                  Machine Learning
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
       Linear Regression  Random Forest  Gradient Boosting
              │            │            │
              └────────────┼────────────┘
                           ▼
                  Model Evaluation
                           │
                           ▼
                  Price Predictions
                           │
                           ▼
                Prediction Error Analysis
                           │
                           ▼
             Tableau / Web Visualization
```

---

# Repository Structure

```text
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
│   └── index.html
│
├── sql/
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

# Folder Description

### `data/`

Contains the raw and processed stock-market datasets.

```text
stock_data_raw.csv
stock_data_processed.csv
```

### `models/`

Contains machine-learning evaluation and prediction results.

```text
model_comparison.csv
stock_predictions.csv
```

### `src/`

Contains the main Python data and machine-learning pipeline.

```text
data_collection.py
feature_engineering.py
ml_prediction.py
mysql_loader.py
prediction_loader.py
```

### `dashboard/`

Contains web-dashboard assets used to present the analytical results.

### `sql/`

Contains SQL scripts and database-related files.

---

# Installation

## Prerequisites

Install:

* Python 3.x
* MySQL Server
* Git
* Tableau Desktop or Tableau Public
* Modern web browser

---

## 1. Clone the Repository

```bash
git clone https://github.com/vigneshwarlankala/Indian-IT-Stock-Analytics.git
cd Indian-IT-Stock-Analytics
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3. Install Dependencies

If `requirements.txt` is available:

```bash
pip install -r requirements.txt
```

Otherwise:

```bash
pip install pandas numpy scikit-learn yfinance mysql-connector-python
```

Additional database libraries may be required depending on the database-loading implementation.

---

# Running the Project

## Step 1 — Collect Stock Data

```bash
python src/data_collection.py
```

This collects and prepares the historical stock dataset.

---

## Step 2 — Generate Features

```bash
python src/feature_engineering.py
```

This generates the technical and statistical indicators required for analysis and machine learning.

---

## Step 3 — Load Data into MySQL

```bash
python src/mysql_loader.py
```

Configure the local MySQL connection before running the script.

---

## Step 4 — Train ML Models

```bash
python src/ml_prediction.py
```

This trains the regression models and generates model-evaluation and prediction outputs.

---

## Step 5 — Load Prediction Results

```bash
python src/prediction_loader.py
```

This loads prediction results into the database for further analysis.

---

## Step 6 — Open the Web Dashboard

Open:

```text
dashboard/index.html
```

in a modern web browser.

The dashboard provides interactive visualizations of the project's analytical and machine-learning results.

---

## Step 7 — Open the Tableau Dashboard

Open the associated Tableau workbook and connect it to the prepared datasets.

The Tableau dashboard can be used to explore:

* Stock trends
* Company comparisons
* Technical indicators
* Risk analysis
* Actual vs. predicted prices
* Prediction errors
* Model performance

---

# Project Results

The machine-learning pipeline produces model evaluation results for each company.

The project evaluates models using:

```text
MAE
RMSE
R²
```

The generated prediction dataset contains the actual and predicted values required for further analysis.

Example output files:

```text
models/model_comparison.csv
models/stock_predictions.csv
```

These outputs can be used by both the visualization layer and the prediction-error analysis.

---

# Analytical Insights

The project enables analysis of:

### Stock Performance

* Historical closing-price movement
* Company-level trends
* Price changes
* Returns

### Technical Indicators

* Moving averages
* RSI
* Bollinger Bands
* Trading signals

### Risk

* Rolling volatility
* Drawdown
* Risk categorization
* Volume behavior

### Machine Learning

* Model performance comparison
* Actual vs. predicted prices
* Prediction errors
* Company-level prediction behavior

---

# Skills Demonstrated

This project demonstrates practical experience in:

* Python programming
* Pandas and NumPy
* Data collection
* Data cleaning
* Data preprocessing
* Exploratory data analysis
* Feature engineering
* Financial time-series analysis
* Machine learning
* Regression modeling
* Model evaluation
* Prediction-error analysis
* SQL
* MySQL database integration
* Tableau
* Interactive data visualization
* HTML
* CSS
* JavaScript
* Plotly.js
* Git and GitHub
* End-to-end data analytics workflows

---

# Future Enhancements

Possible future improvements include:

* Adding additional Indian and international stocks
* Incorporating macroeconomic indicators
* Adding news and sentiment analysis
* Testing advanced time-series models
* Automating daily data updates
* Improving prediction-error diagnostics
* Adding real-time or near-real-time market data
* Adding user-selectable companies and date ranges
* Deploying the dashboard as a web application
* Adding cloud database integration
* Creating an automated data pipeline

---

# Disclaimer

This project is intended for **educational, analytical, and portfolio purposes**.

Machine-learning predictions are generated using historical market data and selected features. Historical patterns do not guarantee future stock-market performance.

This project should **not** be considered financial advice or a recommendation to buy or sell any security.

---

# Author

**L. Vigneshwar Reddy**

GitHub:
https://github.com/vigneshwarlankala

Project Repository:
https://github.com/vigneshwarlankala/Indian-IT-Stock-Analytics
