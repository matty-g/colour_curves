"""
using Nuke to sample and retrieve the data
"""

import nuke


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
    node_dict[name] = frames

    return node_dict

