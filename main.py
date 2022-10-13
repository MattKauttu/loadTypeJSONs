# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import os

from models.BaseType import BaseType
from models.TypeRelationships import Relationships


def load_json():
    path = "./data/typesJSON/baseTypes"
    ls = os.listdir(path)

    base_types = []

    for jsonFile in ls:
        with open(path + jsonFile) as f:
            lines = ""
            for line in f:
                lines += line.strip()
            parsed_json = json.loads(lines)

            type_name = parsed_json['name']

            attacking_relationships = Relationships(normal=parsed_json['attacking']['normal'],
                                                    fire=parsed_json['attacking']['fire'],
                                                    water=parsed_json['attacking']['water'],
                                                    electric=parsed_json['attacking']['electric'],
                                                    grass=parsed_json['attacking']['grass'],
                                                    ice=parsed_json['attacking']['ice'],
                                                    fighting=parsed_json['attacking']['fighting'],
                                                    poison=parsed_json['attacking']['poison'],
                                                    ground=parsed_json['attacking']['ground'],
                                                    flying=parsed_json['attacking']['flying'],
                                                    psychic=parsed_json['attacking']['psychic'],
                                                    bug=parsed_json['attacking']['bug'],
                                                    rock=parsed_json['attacking']['rock'],
                                                    ghost=parsed_json['attacking']['ghost'],
                                                    dragon=parsed_json['attacking']['dragon'],
                                                    dark=parsed_json['attacking']['dark'],
                                                    steel=parsed_json['attacking']['steel'],
                                                    fairy=parsed_json['attacking']['fairy'])

            defending_relationships = Relationships(normal=parsed_json['defending']['normal'],
                                                    fire=parsed_json['defending']['fire'],
                                                    water=parsed_json['defending']['water'],
                                                    electric=parsed_json['defending']['electric'],
                                                    grass=parsed_json['defending']['grass'],
                                                    ice=parsed_json['defending']['ice'],
                                                    fighting=parsed_json['defending']['fighting'],
                                                    poison=parsed_json['defending']['poison'],
                                                    ground=parsed_json['defending']['ground'],
                                                    flying=parsed_json['defending']['flying'],
                                                    psychic=parsed_json['defending']['psychic'],
                                                    bug=parsed_json['defending']['bug'],
                                                    rock=parsed_json['defending']['rock'],
                                                    ghost=parsed_json['defending']['ghost'],
                                                    dragon=parsed_json['defending']['dragon'],
                                                    dark=parsed_json['defending']['dark'],
                                                    steel=parsed_json['defending']['steel'],
                                                    fairy=parsed_json['defending']['fairy'])

            base_type = BaseType(name=type_name, attacking=attacking_relationships, defending=defending_relationships)

            base_types.append(base_type)
        pass

    return base_types


def main():

    base_types = load_json()

    pass


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
