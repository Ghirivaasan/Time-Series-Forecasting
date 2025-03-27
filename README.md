# Time Series Forecasting Web Application

## Overview

This project is a web application for time series forecasting using Python and Flask. It allows users to analyze and forecast temperature data from a global weather repository, providing various statistical tests, visualizations, and forecasting models.

## Features

- Load and process global weather data
- Perform time series analysis including:
  - Stationarity tests (ADF and KPSS)
  - ACF and PACF plots
  - Moving average calculations (SMA, CMA, EMA)
- Generate forecasts using ARIMA and SARIMA models
- Visualize time series data and forecasts
- Calculate forecast accuracy metrics (MAE, RMSE, MAPE)

## Installation

1. Clone the repository
2. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the Flask application:

```bash
python app.py
```

2. Open a web browser and navigate to `http://localhost:8000`
3. Select a country or location and specify the forecast period
4. View the analysis results and forecasts

## Project Structure

- `app.py`: Main Flask application
- `stationarity_tests.py`: Functions for ADF and KPSS tests
- `visualization.py`: Time series plotting functions
- `interpretations.py`: ACF and PACF interpretation
- `acf_pacf.py`: ACF and PACF plotting
- `metrics.py`: Forecast accuracy metric calculations
- `moving_averages.py`: Moving average calculations and plotting
- `templates/`: HTML templates for the web interface

## Dependencies

- Flask
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- statsmodels

## Future Improvements

- Add support for more forecasting models
- Implement data upload functionality
- Enhance visualization options
- Add user authentication and data persistence

