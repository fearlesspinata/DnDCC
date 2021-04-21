import yaml
import pprint

with open("C:\\Users\\vesna\\Programming\\DnDcc\\raceMods.yaml") as f:
    try:
        dict = yaml.load(f, Loader=yaml.FullLoader)
        pprint.pprint(dict['races']['name']['Dwarf']['Bonus'])
    except yaml.YAMLError as e:
        print(e)