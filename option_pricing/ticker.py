# Standard library imports
import datetime

# Third party imports
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

class Ticker:
    @staticmethod
    def get_historical_data(ticker, start_date=None, end_date=None):
        """
        Fetches stock data from yahoo finance using yfinance library.
        
        Params:
        ticker: ticker symbol
        start_date: start date for getting historical data
        end_date: end date for getting historical data
        """
        try:
            if start_date is None:
                start_date = datetime.datetime.now() - datetime.timedelta(days=365)
            if end_date is None:
                end_date = datetime.datetime.now()
            
            stock = yf.Ticker(ticker)
            data = stock.history(start=start_date, end=end_date)
            
            if data.empty:
                raise ValueError(f"No data returned for ticker {ticker}")
            return data
        except Exception as e:
            raise Exception(f"Error fetching data for ticker {ticker}: {str(e)}")

    @staticmethod
    def get_columns(data):
        """
        Gets dataframe columns from previously fetched stock data.
        
        Params:
        data: dataframe representing fetched data
        """
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame")
        return list(data.columns)

    @staticmethod
    def get_last_price(data, column_name):
        """
        Returns last available price for specified column from already fetched data.
        
        Params:
        data: dataframe representing fetched data
        column_name: name of the column in dataframe
        """
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame")
        if column_name not in data.columns:
            raise ValueError(f"Column '{column_name}' not found in the DataFrame")
        return data[column_name].iloc[-1]

    @staticmethod
    def plot_data(data, ticker, column_name):
        """
        Plots specified column values from dataframe.
        
        Params:
        data: dataframe representing fetched data
        column_name: name of the column in dataframe
        """
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame")
        if column_name not in data.columns:
            raise ValueError(f"Column '{column_name}' not found in the DataFrame")
        
        plt.figure(figsize=(10, 6))
        data[column_name].plot()
        plt.ylabel(column_name)
        plt.xlabel('Date')
        plt.title(f'Historical data for {ticker} - {column_name}')
        plt.legend(loc='best')
        return plt