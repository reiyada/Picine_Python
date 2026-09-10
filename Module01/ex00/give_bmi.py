def parse_height_and_weight(height: list[int | float], weight: list[int | float]):
    """This parse the given values and flag erros if needed"""

    for h in height:
        assert isinstance(h, int) or isinstance(h, float), "Height needs to be int or float."
    for w in weight:
            assert isinstance(w, int) or isinstance(w, float), "Weight needs to be int or float."
    assert len(height) == len(weight), "2 lists need to have the same amout of values."
    for h in height:
        assert h > 0, "Height needs to be more than 0."
    for w in weight:
        assert w > 0, "Weight needs to be more than 0."


def calcul_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """This calculate bmis based on the given values and
        returns the list of them"""

    bmis = list()

    for h, w in zip(height, weight):
        bmi = w / h**2
        bmis.append(bmi)

    return bmis


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """This returns the list of bmis"""

    try:
        parse_height_and_weight(height, weight)
        return calcul_bmi(height, weight)
    except AssertionError as ex:
        print(f"Error: {ex}")


def parse_limit(limit: int):
    assert isinstance(limit, int), "Limit needs to be an integers."
    assert limit > 0, "Limit needs to be a positive value."


def check_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """This checks if the given mbis are greater than the given limit,
            and it returns the list of boolean."""
    
    limit_list = list()
    for b in bmi:
        limit_list.append(b > limit)

    return limit_list


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """This returns the list of boolean."""

    try:
        parse_limit(limit)
        return check_limit(bmi, limit)
    except AssertionError as ex:
        print(f"Error: {ex}")