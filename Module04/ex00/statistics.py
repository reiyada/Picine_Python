def ft_statistics(*args: any, **kwargs: any) -> None:
    """This calculate mean, median, quartile, standard deviation
        and variance for each values of *args"""

    for key, value in kwargs.items():
        if (not args):
            print("ERROR")
        else:
            switch(value, args)


def switch(method: str, values: tuple[float]):
    """This calculates the values with each method."""

    if (method == "mean"):
        result = calcul_mean(values)
    elif (method == "median"):
        sorted_value = sorted(values)
        values_len = len(values)
        middle_index = values_len // 2
        if (values_len % 2 == 0):
            result = (sorted_value[middle_index - 1] +
                      sorted_value[middle_index]) / 2
        else:
            result = sorted_value[middle_index]
    elif (method == "quartile"):
        sorted_value = sorted(values)
        values_len = len(values)
        result = [float(sorted_value[values_len // 4]),
                  float(sorted_value[values_len // 4 * 3])]
    elif (method == "var"):
        result = calcul_variance(values)
    elif (method == "std"):
        var = calcul_variance(values)
        result = pow(var, 0.5)
    else:
        return

    print(f"{method} : {result}")


def calcul_mean(values: tuple[float]) -> float:
    """This is a helper function to calculate a mean value."""

    result = sum(values) / len(values)
    return result


def calcul_variance(values: tuple[float]) -> float:
    """This is a helper function to calculate a variance value."""

    mean = calcul_mean(values)
    mean_gaps = []
    for nb in values:
        mean_gaps.append((nb - mean) ** 2)
    result = calcul_mean(mean_gaps)
    return result
