from generateDualTypesFromBaseTypes import get_dual_types
from loadSingleTypeJSON import load_json
import json
import dataclasses


def create_dual_type_json(dual_types):
    for type in dual_types:
        y = dataclasses.asdict(dual_types)
    #y = json.dumps(dual_types)

    pass


def main():
    base_types = load_json()
    dual_types = get_dual_types(base_types)
    create_dual_type_json(dual_types)
    print('Execution has ended successfully')


if __name__ == '__main__':
    main()
