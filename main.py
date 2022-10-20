from loadSingleTypeJSON import load_json
from itertools import combinations


def generate_dual_type(combo):
    pass


def get_dual_types(base_types):
    type_combinations = get_base_type_combinations(base_types)
    dual_types = list()

    for combo in type_combinations:
        dual_type = generate_dual_type(combo)
        dual_types.append(dual_type)

    return dual_types


def get_base_type_combinations(base_types):
    type_combinations = list()

    for n in range(1, 3):
        type_combinations += list(combinations(base_types, n))

    return type_combinations


def main():
    base_types = load_json()

    dual_types = get_dual_types(base_types)

    pass


if __name__ == '__main__':
    main()
