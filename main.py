from generateDualTypesFromBaseTypes import get_dual_types
from loadSingleTypeJSON import load_json
import json
from dataclasses import dataclass, asdict


def create_dual_type_json(dual_types):
    for type in dual_types:
        y = asdict(type)
        json_object = json.dumps(y)

        filename = type._type1name

        if type._type2name != '':
            filename += '_' + type._type2name

        filename += '.json'

        path = "./data/typesJSON/dualTypes/"

        with open(path + filename, "w") as outfile:
            outfile.write(json_object)
        pass
    pass


def main():
    base_types = load_json()
    dual_types = get_dual_types(base_types)
    create_dual_type_json(dual_types)
    print('Execution has ended successfully')


if __name__ == '__main__':
    main()
