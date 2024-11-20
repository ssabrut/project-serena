import pandas as pd

def load_data(path: str = "data/bookings.csv") -> pd.DataFrame:
    """
    Load booking data from a CSV file.

    Parameters
    ----------
    path : str, optional
        The file path to the CSV file containing booking data, by default "data/bookings.csv"

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the loaded booking data.
    """
    return pd.read_csv(path)