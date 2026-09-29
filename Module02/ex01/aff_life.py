import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def generate_graph(data: pd.DataFrame, country: str):
    """This generates the graph about the given data."""

    try:
        values = data.set_index("country").loc[country]
        years = values.index.astype(int)

        plt.plot(years, values)
        plt.title(f"{country} Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.show()
    except Exception as ex:
        print(f"Error: {ex}")


def main():
    data = load("life_expectancy_years.csv")
    if data is None:
        return
    generate_graph(data, "France")


if (__name__ == "__main__"):
    main()
