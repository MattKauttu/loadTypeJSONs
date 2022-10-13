import os
import json
from models.BaseType import BaseType
from models.TypeRelationships import Relationships


def load_json():
    # TODO - Make paths file
    path = "./data/typesJSON/baseTypes/"
    ls = os.listdir(path)

    base_types = []

    for jsonFile in ls:
        with open(path + jsonFile) as f:
            lines = ""
            for line in f:
                lines += line.strip()
            parsed_json = json.loads(lines)

            type_name = parsed_json['name']

            relationships = set_relationships(parsed_json)

            base_type = BaseType(name=type_name, attacking=relationships[0], defending=relationships[1])

            base_types.append(base_type)
        pass

    return base_types


def set_relationships(parsed_json):
    relationships = []

    for i in range(len(parsed_json)):

        for i in range(2):

            if i == 0:
                action = 'attacking'
            else:
                action = 'defending'

            relationships.append(
                Relationships(normal=parsed_json[action]['normal'],
                              fire=parsed_json[action]['fire'],
                              water=parsed_json[action]['water'],
                              electric=parsed_json[action]['electric'],
                              grass=parsed_json[action]['grass'],
                              ice=parsed_json[action]['ice'],
                              fighting=parsed_json[action]['fighting'],
                              poison=parsed_json[action]['poison'],
                              ground=parsed_json[action]['ground'],
                              flying=parsed_json[action]['flying'],
                              psychic=parsed_json[action]['psychic'],
                              bug=parsed_json[action]['bug'],
                              rock=parsed_json[action]['rock'],
                              ghost=parsed_json[action]['ghost'],
                              dragon=parsed_json[action]['dragon'],
                              dark=parsed_json[action]['dark'],
                              steel=parsed_json[action]['steel'],
                              fairy=parsed_json[action]['fairy'])
            )

        return relationships

    pass