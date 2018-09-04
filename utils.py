"""
using Nuke to sample and retrieve the data
"""

import nuke
import json


def get_sampled_data(node):
    # get name from label
    name = node.knob('label').evaluate()
    node_dict = {}
    chans = ['r', 'g', 'b']
    frames = {}
    for i in range(1, 257):
        results = {}
        for colour in chans:
            colour_idx = chans.index(colour)
            results[colour] = node.knob('intensitydata').getValueAt(i, colour_idx)
        frames[i] = results
    node_dict[name.strip()] = frames

    return node_dict


def retrieve_data():
    data = {}
    for node in nuke.selectedNodes():
        result = get_sampled_data(node)
        for key, value in result.iteritems():
            data[key] = value

    return data


def write_json(data_dict, destination):
    """ write a dict out to disk as json data """
    json_file = json.dumps(data_dict)
    f = open(destination, 'w')
    f.write(json_file)
    f.close()


def get_json(path):
    """ retrieves json file from disk and saves it as a dict """

    f = open(path, 'r')
    profiles_dict = json.load(f)

    return profiles_dict

data = get_json('data/ocio_aces.json')

print data
