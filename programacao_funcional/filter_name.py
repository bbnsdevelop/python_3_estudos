#!/usr/bin/python3
# coding: utf-8

def get_name(list_names):
    name = filter(lambda n: n['name'] == 'jackie', list_names)
    return name


if __name__ == '__main__':
    aquarium_creatures = [
        {"name": "sammy", "species": "shark", "tank number": 11, "type": "fish"},
        {"name": "ashley", "species": "crab", "tank number": 25, "type": "shellfish"},
        {"name": "jo", "species": "guppy", "tank number": 18, "type": "fish"},
        {"name": "jackie", "species": "lobster", "tank number": 21, "type": "shellfish"},
        {"name": "charlie", "species": "clownfish", "tank number": 12, "type": "fish"},
        {"name": "olly", "species": "green turtle", "tank number": 34, "type": "turtle"}
    ]
    name = get_name(aquarium_creatures)
    print(list(name))
