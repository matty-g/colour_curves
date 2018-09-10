import json


class Profile(object):

    def __init__(self, profile_dict):
        self._name = next(iter(profile_dict))
        self._curves = profile_dict[self._name]
        self._samples = len(self._curves)

        # print self._name
        # print self._curves
        # print self._samples

    def getCurveForChannel(self, channel='r'):
        """ returns an ordered list of samples @ time """
        result = []
        for sample in range (1, self._samples + 1):
            result.append(self._curves[str(sample)][channel])
        return result

    def getName(self):
        return self._name


def get_json(path):
    """ retrieves json file from disk and saves it as a dict """

    f = open(path, 'r')
    profiles_dict = json.load(f)

    return profiles_dict

data = get_json('data/ocio_aces.json')


