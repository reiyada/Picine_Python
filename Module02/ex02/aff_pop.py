import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load
from matplotlib.ticker import FuncFormatter


def to_number(value) -> float:
    """Convert a population value like '3.28M' or '28.3k' to a float."""

    if isinstance(value, str):
        units = {"k": 1e3,
                 "M": 1e6,
                 "B": 1e9}
        if value[-1] in units:
            return float(value[:-1]) * units[value[-1]]
    return float(value)


def generate_graph(data: pd.DataFrame, country1: str, country2: str):
    """This generates the graph about the given data,
        comparing the value of Contry 1 and Country 2."""

    try:
        subset = data.set_index("country").loc[:, "1800": "2050"]
        subset = subset.map(to_number)
        years = subset.columns.astype(int)

        plt.plot(years, subset.loc[country1], color='g', label=country1)
        plt.plot(years, subset.loc[country2], color='b', label=country2)

        plt.gca().yaxis.set_major_formatter(
            FuncFormatter(lambda y, _: f"{int(y / 1e6)}M")
        )

        plt.title(f"Population Projections {country1} vs {country2}")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.legend()
        plt.show()
    except Exception as ex:
        print(f"Error: {ex}")


def main():
    data = load("population_total.csv")
    if data is None:
        return
    generate_graph(data, "France", "Japan")


if (__name__ == "__main__"):
    main()
