import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load


def to_number(value) -> float:
    """Convert a population value like '3.28M' or '28.3k' to a float."""

    if isinstance(value, str):
        units = {"k": 1e3,
                 "M": 1e6,
                 "B": 1e9}
        if value[-1] in units:
            return float(value[:-1]) * units[value[-1]]
    return float(value)


def generate_graph(life_expectancy_data: pd.DataFrame,
                   gdp_data: pd.DataFrame, year: str):
    """Plot life expectancy against GDP per capita
        for the given year."""

    try:
        life_expectancy_df = life_expectancy_data[year]
        gdp_df = gdp_data[year]

        merged = pd.concat([gdp_df, life_expectancy_df],
                           axis=1, join="inner").dropna()
        merged.columns = ["gdp", "life_expectancy"]
        merged = merged.map(to_number)

        plt.scatter(merged["gdp"], merged["life_expectancy"])
        plt.xscale("log")
        plt.xlim(300, 10000)
        plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])

        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.title(year)
        plt.show()
    except Exception as ex:
        print(f"Error: {ex}")


def main():
    life_expectancy_data = load("life_expectancy_years.csv")
    gdp_data =\
        load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    if life_expectancy_data is None or gdp_data is None:
        return
    generate_graph(life_expectancy_data, gdp_data, "1900")


if (__name__ == "__main__"):
    main()
