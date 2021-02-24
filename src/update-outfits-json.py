# Updates only the svg-string in all json files.

from lxml import etree
import re
import json
import os

PATH = "material/outfits"
SHIRTS = 'shirts'
PANTS = 'pants'
HATS = 'hats'


def extract_layers(path):
    layers = []
    with open(f'{path}/original.svg', 'rb') as src_file:
        my_xml_file = src_file.read()
        root = etree.fromstring(my_xml_file)
        for attribute in root:
            attrib = dict(attribute.attrib)
            if '{http://www.inkscape.org/namespaces/inkscape}label' in attrib.keys():
                category = attrib['{http://www.inkscape.org/namespaces/inkscape}label']
                # Skip body and face
                if category in ['Body', 'Face', 'Gesicht']:
                    continue
                # For empty layers svg is empty string
                if len(list(attribute)) == 0:
                    layers.append((category, ""))
                else:
                    svg = str(etree.tostring(attribute)).replace(r"\n", "")
                    svg = re.sub('> +<', '><', svg)
                    svg = svg[2:-1]
                    svg = re.sub("\"", "\'", svg)
                    layers.append((category, svg))
    return layers


def add_svg_to_json(path, category, svg):
    meta = None
    if not os.path.exists(f"{path}/meta.json"):
        print(f"ERR: Meta JSON file not found for \"{path}\"")
        return
    with open(f"{path}/meta.json", "r") as fp:
        meta = json.load(fp)
        match = [(i, x) for (i, x) in enumerate(
            meta) if x["category"] == category]
        meta[match[0][0]]["svg"] = svg

    with open(f"{path}/meta.json", "w") as fp:
        json.dump(meta, fp, indent=2)


def add_all_svgs_to_json(path):
    layers = extract_layers(path)

    for category, svg in layers:
        category_constant = None
        if category in ["Shirt"]:
            category_constant = SHIRTS
        if category in ["Hose", "Pants"]:
            category_constant = PANTS
        if category in ["Hat", "Hut"]:
            category_constant = HATS
        if category_constant != None:
            add_svg_to_json(path, category_constant, svg)
        else:
            print(f"ERR: Cannot find category label: {category}")


if __name__ == '__main__':
    outfits = [name for name in os.listdir(
        PATH) if os.path.isdir(os.path.join(PATH, name))]
    for outfit in outfits:
        add_all_svgs_to_json(f"{PATH}/{outfit}")
