import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """This reads the csv file and prints the dimention, then returns it."""

    try:
        if not isinstance(path, str) or not path.endswith(".csv"):
            raise ValueError("path must be a string ending with .csv")

        data = pd.read_csv(path)
        # data_dimention = data.shape
        # first_column = data.iloc[:1]

        # print(f"Loading dataset of dimensions {data_dimention}")
        # print(first_column)
        return data
    except Exception as ex:
        print(f"Error: {ex}")
