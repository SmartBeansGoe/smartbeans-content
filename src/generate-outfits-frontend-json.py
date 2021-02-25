import json
import os

PATH = "material/outfits"

def load_data_from_json(path):
    if not os.path.exists(f"{path}/meta.json"):
        print(f"ERR: Meta JSON file not found for \"{path}\"")
        return []
    with open(f"{path}/meta.json", "r") as fp:
        return json.load(fp)

def filter_for_empty_svg(meta):
    return [asset for asset in meta if asset["svg"] != ""]
        

if __name__ == '__main__':
    output = []
    outfits = [name for name in os.listdir(
        PATH) if os.path.isdir(os.path.join(PATH, name))]
    for outfit in outfits:
        output += load_data_from_json(f"{PATH}/{outfit}")
    output = filter_for_empty_svg(output)
    ids = [asset["id"] for asset in output]
    print(ids)


    with open('out/assets-frontend.json', 'w') as fp:
        json.dump(output, fp)