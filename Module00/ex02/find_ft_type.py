from typing import Any


def all_thing_is_obj(object: Any) -> int:

    inputObjType = type(object)
    output = list()

    objList = [list, tuple, set, dict, str]

    if (inputObjType in objList):
        if (inputObjType is str):
            output.append(f"{object} is in the kitchen :")
        else:
            output.append(f"{inputObjType.__name__.capitalize()} :")

        output.append(f"<class '{inputObjType.__name__}'>")

    else:
        output.append(f"Type not found")

    print(*output)

    return 42