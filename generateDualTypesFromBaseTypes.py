from itertools import permutations

from models.DualType import DualType
from models.TypeRelationships import Relationships


def calculate_defenses(permutation):
    type1defenses = permutation[0].defending
    type2defenses = permutation[1].defending
    defending_relationships = Relationships(normal=type1defenses.normal * type2defenses.normal,
                                            fire=type1defenses.fire * type2defenses.fire,
                                            water=type1defenses.water * type2defenses.water,
                                            electric=type1defenses.electric * type2defenses.electric,
                                            grass=type1defenses.grass * type2defenses.grass,
                                            ice=type1defenses.ice * type2defenses.ice,
                                            fighting=type1defenses.fighting * type2defenses.fighting,
                                            poison=type1defenses.poison * type2defenses.poison,
                                            ground=type1defenses.ground * type2defenses.ground,
                                            flying=type1defenses.flying * type2defenses.flying,
                                            psychic=type1defenses.psychic * type2defenses.psychic,
                                            bug=type1defenses.bug * type2defenses.bug,
                                            rock=type1defenses.rock * type2defenses.rock,
                                            ghost=type1defenses.ghost * type2defenses.ghost,
                                            dragon=type1defenses.dragon * type2defenses.dragon,
                                            dark=type1defenses.dark * type2defenses.dark,
                                            steel=type1defenses.steel * type2defenses.steel,
                                            fairy=type1defenses.fairy * type2defenses.fairy)

    return defending_relationships


def generate_dual_type(permutation):
    dual_type = DualType(_type1name=permutation[0].name, _type2name=permutation[1].name, _defenses=Relationships(
                                                                                                       normal=-1,
                                                                                                       fire=-1,
                                                                                                       water=-1,
                                                                                                       electric=-1,
                                                                                                       grass=-1,
                                                                                                       ice=-1,
                                                                                                       fighting=-1,
                                                                                                       poison=-1,
                                                                                                       ground=-1,
                                                                                                       flying=-1,
                                                                                                       psychic=-1,
                                                                                                       bug=-1,
                                                                                                       rock=-1,
                                                                                                       ghost=-1,
                                                                                                       dragon=-1,
                                                                                                       dark=-1,
                                                                                                       steel=-1,
                                                                                                       fairy=-1
                                                                                                   )
                         )

    dual_type._defenses = calculate_defenses(permutation)

    return dual_type


def get_base_type_permutations(base_types):
    type_permutations = list()

    for n in range(1, 3):
        type_permutations += list(permutations(base_types, n))

    return type_permutations


def get_dual_types(base_types):
    type_permutations = get_base_type_permutations(base_types)
    dual_types = list()

    for permutation in type_permutations:
        if len(permutation) == 1:
            dual_type = DualType(_type1name=permutation[0].name, _type2name='', _defenses=permutation[0].defending)
        else:
            dual_type = generate_dual_type(permutation)

        dual_types.append(dual_type)

    return dual_types
