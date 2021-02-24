# Generates the initial json file for all outfits that don't have one yet.
import os
import json

PATH = "material/outfits"
SHIRTS = 'shirts'
PANTS = 'pants'
HATS = 'hats'


def sample_json(outfit_name_id, category):
    id = f"{outfit_name_id}-{category}"
    return {
        "id": id,
        "name": "change-me",
        "outfit-id": outfit_name_id,
        "category": category,
        "precondition": {
            "task-id": None,
            "achievement-id": None,
        },
        "attributes": [],
        "svg": ""}


def generate_json(path, output_folder):
    outfit_name_id = output_folder.lower()
    sample = [sample_json(outfit_name_id, x) for x in [SHIRTS, PANTS, HATS]]
    if not os.path.exists(f'{path}/{output_folder}/meta.json'):
        with open(f'{path}/{output_folder}/meta.json', 'w') as fp:
            json.dump(sample, fp, indent=2)


if __name__ == '__main__':
    outfits = [ name for name in os.listdir(PATH) if os.path.isdir(os.path.join(PATH, name)) ]
    for outfit in outfits:
        generate_json(PATH, outfit)
