import pandas as pd
from sklearn.datasets import fetch_openml
from pathlib import Path
from pyprojroot import here

FREQ_ID = 41214
SEV_ID = 41215
DATA_PATH = here("data")


def load_openml_as_frame(data_id: int, data_path: Path | None = None) -> pd.DataFrame:
    """
    Loads any OpenML dataset as a dataframe and optionally caches the data in a specified
    path.

    Arguments:
        id (int): the OpenML data ID.
        data_path (Path | None): the path where the downloaded dataset is cached.
        Defaults to None.

    Returns: 
        pd.DataFrame: the OpenML dataset as a dataframe.

    """ 
    return fetch_openml(data_id=data_id, data_home=data_path, as_frame=True).frame

def load_freq(data_path : Path | None = None) -> pd.DataFrame:
    """
    Fetches the frequency dataset with OpenML ID `FREQ_ID` and caches it under
    `DATA_PATH`.
    
    Arguments:
        data_path (Path | None): the path where the downloaded dataset is cached.

    Returns:
        freq_df (pd.DataFrame): The frequency dataset as a dataframe.
    """

    data_path = data_path if data_path else DATA_PATH

    freq_df = load_openml_as_frame(FREQ_ID, data_path)

    return freq_df

def load_sev(data_path : Path | None = None) -> pd.DataFrame:
    """
    Fetches the severity dataset with OpenML ID `SEV_ID` and caches it under
    `DATA_PATH`.
    
    Arguments:
        data_path (Path | None): the path where the downloaded dataset is cached.

    Returns:
        sev_df (pd.DataFrame): The severity dataset as a dataframe.
    """

    data_path = data_path if data_path else DATA_PATH

    sev_df = load_openml_as_frame(SEV_ID, DATA_PATH)

    return sev_df