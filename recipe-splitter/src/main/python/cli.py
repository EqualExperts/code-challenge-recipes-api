"""
A basic utility to create a directory structure to mimic a very convulated API.
"""
import argparse
import shutil
import os
import json
import logging.config

logging.config.fileConfig("log.ini")
logger = logging.getLogger(__file__)

SLICES = {
    "summary": ['name', 'description', 'servings', 'preparationTimeMin', 'cookingTimeMin', 'estimatedCostDollars', 'id'],
    "ingredients": ['ingredients'],
    "method": ['method'],
    "diets": ['diets']
}


def run(inputdir, outputdir):
    list = []
    for filename in os.listdir(inputdir):
        file_path = os.path.join(inputdir, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as df:
                recipe = json.load(df)
                recipe['id'] = filename.split('.')[0]
                list.append({
                    'id': recipe['id'],
                    'name': recipe['name'],
                    'description': recipe['description']
                })

                recipe_dir = str(os.path.join(outputdir, recipe['id']))
                os.makedirs(recipe_dir)

                for slice in SLICES:
                    data = {k: recipe[k] for k in SLICES[slice] if k in recipe}
                    with open(os.path.join(recipe_dir, f"{slice}.json"), 'w') as output:
                        json.dump(data, output)

    with open(os.path.join(outputdir, "list.json"), 'w') as output:
        json.dump(list, output)
    logger.info(f"Split {len(list)} recipes.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="AI Assist Study - Recipe Splitter")
    parser.add_argument('--inputdir', type=str, help='Directory containing the raw recipes', default="../data/recipes")
    parser.add_argument('--outputdir', type=str, help='An output directory', default="../data/split-recipes")
    args = parser.parse_args()

    if os.path.exists(args.outputdir):
        shutil.rmtree(args.outputdir)
    os.makedirs(args.outputdir)

    run(args.inputdir, args.outputdir)
