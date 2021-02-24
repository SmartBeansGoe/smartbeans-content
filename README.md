# smartbeans-content

This repository contains all vector graphics and meta information necessary for running smartBeans. Additionally it generates JSON files with the help of Python scripts, which hold the respective information for the front- and backend. The smartBeans needs for the gamification elements clothing assets (SVG), achievement images (SVG) and information about the unlock requirement (which must also be implemented in the backend).

## Folder structure

The folder structure is as follows:

```
|__material
|    |__ outfits
|    |     |__ Granny-Smith
|    |     |     |__ original.svg
|    |     |     |__ meta.json
|    |     |
|    |     |__ Knight-Armor
|    |     |     |__ original.svg
|    |     |     |__ meta.json
|    |    ...
|    |     |__ template.svg
|    |
|    |__ achievements
|          |__ Solved-Tasks-Bronze
|          |     |__ badge.svg
|          |     |__ meta.json
|          |
|          |__ Solved-Tasks-Silver
|          |     |__ badge.svg
|          |     |__ meta.json
|         ...
|          |__ template.svg
|
|__src
     |__ generate-outfits-json.py
     |__ generate-achievements-json.py
```
## Creating a new outfit

1. Copy the `material/outfits/template.svg` file. In there are the following layers:
    - Body *(do not edit)*
    - **Pants**
    - **Shirt**
    - **Hat**
    - Face *(is not tracked for now)*
    - **Shoes**
2. During the creation it is important that the body is not changed, so that all assets fit later. It is best to embed the body directly. Then you can choose the appropriate layer for each asset and create it. It is important that for example only the shirt is on the layer "Shirt" and that there are no other assets on this layer. The renaming of the layers should not be done, because then they will not be taken into account. The same applies to new layers. Layers that do not contain anything will be ignored. The layers can be reordered.

3. Save the vector graphic in `material/outfits/<name-of-your-choice>/original.svg` as SVG (Inkscape-SVG). **Make sure that the assets are in its layer.**
4. Run the script `src/generate-outfits-json.py`. (***Not implemented yet, for now skip the steps 4 and 5***)
```
python src/generate-outfits-json.py
```

5. Open the generated file `material/outfits/<name-of-your-choice>/meta.json` and edit the marked locations (`<...>`).
Here an example of an generated `meta.json` file:
```json
[
    {
        "id": "granny-smith-pants",
        "name": <string>,
        "outfit-id": "granny-smith",
        "category": "pants",
        "precondition": {
            "task-id": <int or null>,
            "achievement-id": <string or null>,
        },
        "attributes": [],
        "svg": "<g>...</g>"
    },
    {
        "id": "granny-smith-hat",
        "name": <string>,
        "outfit-id": "granny-smith",
        "category": "hats",
        "precondition": {
            "task-id": <int or null>,
            "achievement-id": <string or null>,
        },
        "attributes": [],
        "svg": "<g>...</g>"
    },
    {
        "id": "granny-smith-shirt",
        "name": <string>,
        "outfit-id": "granny-smith",
        "category": "shirts",
        "precondition": {
            "task-id": <int or null>,
            "achievement-id": <string or null>,
        },
        "attributes": [],
        "svg": "<g>...</g>"
    }
]
```
6. Make a pull request.

## Updating an existing outfit
If an outfit, i.e. the corresponding SVG file, has been changed, the following command must be executed:
```
python update-outfits-json.py
```

## Adding new Achievement
