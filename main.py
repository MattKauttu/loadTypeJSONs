from create_dual_type_json import create_dual_type_json
from generateDualTypesFromBaseTypes import get_dual_types
from loadSingleTypeJSON import load_json


def main():
    base_types = load_json()
    dual_types = get_dual_types(base_types)
    create_dual_type_json(dual_types)
    print('Execution has ended successfully')


if __name__ == '__main__':
    main()
