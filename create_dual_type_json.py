from dataclasses import asdict
import json


def create_dual_type_json(dual_types):
    for dual_type in dual_types:
        y = asdict(dual_type)
        json_object = json.dumps(y)

        filename = dual_type._type1name

        if dual_type._type2name != '':
            filename += '_' + dual_type._type2name

        filename += '.json'

        path = "./data/typesJSON/dualTypes/"

        with open(path + filename, "w") as outfile:
            outfile.write(json_object)
        pass
    pass