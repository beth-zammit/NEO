"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # TODO: Load NEO data from the given CSV file.
    neo_list = []
    with open(neo_csv_path) as infile:
        reader = csv.DictReader(infile)
        for elem in reader:
            pdes = elem.get('pdes')
            name = elem.get('name')
            diameter = elem.get('diameter')
            pha = elem.get('pha')

            neo = NearEarthObject(pdes, name, diameter, pha)
            neo_list.append(neo)
    return neo_list


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.
    ca_list = []
    with open(cad_json_path) as infile:
        close_approach = json.load(infile)
        for elem in close_approach['data']:
            _designation = elem[0]
            time = elem[3]
            distance = elem[4]
            velocity = elem[7]
            
            ca_name = CloseApproach(_designation, time, distance, velocity)
            ca_list.append(ca_name)
            
    return ca_list
