from typing import Any


def all_thing_is_obj(object: Any) -> int:

    input_obj_type = type(object)
    output = list()

    obj_list = [list, tuple, set, dict, str]

    if (input_obj_type in obj_list):
        if (input_obj_type is str):
            output.append(f"{object} is in the kitchen :")
        else:
            output.append(f"{input_obj_type.__name__.capitalize()} :")

        output.append(f"{input_obj_type}")

    else:
        output.append(f"Type not found")

    print(*output)

    return 42