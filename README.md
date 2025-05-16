# Stock Price Prediction Project

## Project Overview
This project uses historical stock price data to predict future prices using machine learning models, including LSTM.

## Folder Structure
- `data_collection.py`: Script to fetch stock data using Yahoo Finance API.
- `data_preprocessing.py`: Data cleaning and scaling.
- `feature_engineering.py`: Feature creation like moving averages and lag features.
- `model_training.ipynb`: Jupyter notebook for training the LSTM model.
- `model_evaluation.py`: Model evaluation and visualization.
- `app_streamlit.py`: Streamlit app for interactive prediction UI.
- `requirements.txt`: Required Python libraries.

## Setup Instructions
1. Create a virtual environment and activate it.
2. Install dependencies with:
```bash
pip install -r requirements.txt
```
3. Run individual scripts or launch the Streamlit app:
```bash
streamlit run app_streamlit.py
```
