import yaml

with open('raceMods.yaml') as f:
    try:
        dict = yaml.load(f, Loader=yaml.FullLoader)
        print(dict)
    except yaml.YAMLError as e:
        print(e)