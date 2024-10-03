import pandas as pd
import numpy as np
from pandas.tseries.offsets import DateOffset

class OptionFinder:
    def __init__(self, ticker):
        self.ticker = ticker
        self.df = self._load_data()

    def _load_data(self):
        df = pd.read_pickle(f"Data/{self.ticker}.pkl")
        df.dropna(inplace=True)
        df = df.sort_values(by="date")
        df = df[["date", "Sym", "BestBid", "BestOffer", "CallPut", "Expiry", "ID", "Strike",
                 "ImpliedVolatility", "Delta", "PV", "Gamma", "Theta", "Vega", "UnderRef"]]
        return df

    def find_option(self, maturity, callput, delta):
        """
        Find the closest option based on maturity and delta.
        
        :param maturity: Maturity in months
        :param callput: 'C' for Call, 'P' for Put
        :param delta: Target delta value
        :return: DataFrame row with the closest matching option
        """
        df = self.df[self.df["CallPut"] == callput]
        return df.groupby("date").apply(self._find_closest_expiry_and_delta, d=delta, exp=maturity).reset_index(drop=True)

    def _find_closest_expiry_and_delta(self, group, d, exp):
        target_date = group["date"].iloc[0] + DateOffset(months=exp)
        expiry_diff = (pd.to_datetime(group["Expiry"]) - target_date).abs()
        closest_expiry_row = group.loc[expiry_diff.idxmin()]
        closest_expiry_date = closest_expiry_row["Expiry"]
        closest_expiry_group = group[group["Expiry"] == closest_expiry_date]
        closest_delta_row = closest_expiry_group.loc[(closest_expiry_group["Delta"] - d).abs().idxmin()]
        return closest_delta_row

    def get_option_data(self, maturity, callput, delta):
        """
        Get option data for a specific maturity, call/put type, and delta.
        
        :param maturity: Maturity in months
        :param callput: 'C' for Call, 'P' for Put
        :param delta: Target delta value
        :return: DataFrame with option data
        """
        return self.find_option(maturity, callput, delta)

# Usage example:
# finder = OptionFinder("SPX")
# option_data = finder.get_option_data(3, 'C', 0.5)
# print(option_data)
