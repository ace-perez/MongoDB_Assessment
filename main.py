
import json


with open(r"myjson.json", encoding="utf-8") as unflat_json:
    json_object = json.load(unflat_json)


def flatten_json(y):

    out = {}

    def flatten(x, name=''):

        if type(x) is dict:

            for a in x:
                flatten(x[a], name + a + '_')

        elif type(x) is list:

            i = 0

            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


print(flatten_json(json_object))
