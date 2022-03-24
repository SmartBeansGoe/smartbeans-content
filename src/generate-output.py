import json
import os

PATH = "material/outfits"


def load_data_from_json(path):
    if not os.path.exists(f"{path}/meta.json"):
        print(f"ERR: Meta JSON file not found for \"{path}\"")
        return []
    with open(f"{path}/meta.json", "r") as fp:
        return json.load(fp)
        
def deleteSVGEntry(loadedJSONItem):
    svg = loadedJSONItem.pop('svg', None)
    with open(f"out/assets/{loadedJSONItem['svgPath']}", "w") as file:
        file.write(svg)

    return loadedJSONItem


if __name__ == '__main__':
    if not os.path.exists("out/assets/"):
        os.makedirs("out/assets")

    output = []
    outfits = [name for name in os.listdir(
        PATH) if os.path.isdir(os.path.join(PATH, name))]
    for outfit in outfits:
        loaded = load_data_from_json(f"{PATH}/{outfit}")
        loaded = filter(lambda x: x["svg"] != "", loaded)

        loaded = map(lambda x: deleteSVGEntry(x), loaded)
        
        output += loaded
        
    
    ids = [asset["id"] for asset in output]
    print(ids)


    with open('out/assets-backend.json', 'w') as fp:
        json.dump(output, fp)