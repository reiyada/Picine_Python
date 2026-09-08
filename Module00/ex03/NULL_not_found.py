from typing import Any
import math

def NULL_not_found(object: Any) -> int:

    if (object == None):
        print(f"Nothing: {object} {type(None)}")
        return 0
    elif isinstance(object, float) and math.isnan(object):
        print(f"Cheese: {object} {type(object)}")
        return 0
    elif (object == 0):
        print(f"Zero: {object} {type(object)}")
        return 0
    elif (object == ""):
        print(f"Empty: {object} {type(object)}")
        return 0
    elif (object == False):
        print(f"Fake: {object} {type(object)}")
        return 0
    else:
        print("Type not Found")
        return 1
