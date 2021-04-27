import yaml
import pprint

with open("C:\\Users\\vesna\\Programming\\DnDcc\\raceMods.yaml") as f:
    someVar = 0
    try:
        dict = yaml.load(f, Loader=yaml.FullLoader)
        dict = dict['races']['name']['Dwarf']['Bonus']
        for item in dict:
            someVar += dict[item]
        print(someVar)
    except yaml.YAMLError as e:
        print(e)