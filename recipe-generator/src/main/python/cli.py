import os
import uuid
import json
import argparse
import logging.config

from dotenv import load_dotenv
load_dotenv()

from recipe_generator import RecipeGenerator

logging.config.fileConfig("log.ini")

def main():
    parser = argparse.ArgumentParser(description="AI Assist Study - Recipe Generator")
    parser.add_argument('--theme', type=str, help='A theme of the type of recipes you would like to generate.', required=True)
    parser.add_argument('--num', type=int, help='A number of recipes to generate', default=1)
    parser.add_argument('--outputdir', type=str, help='An output directory', default="../data/recipes")
    args = parser.parse_args()

    if args.outputdir is not None:
        if not os.path.exists(args.outputdir):
            os.makedirs(args.outputdir)

    recipe_generator = RecipeGenerator(args.theme)
    list_of_recipes = []
    if args.num == 1:
        recipe = recipe_generator.generateSingleRecipe()
        list_of_recipes.append(recipe)
    else:
        list_of_recipes = recipe_generator.generateRecipes(args.num)
    
    if args.outputdir is not None:
        for recipe in list_of_recipes:
            filename = f"{uuid.uuid4()}.json"
            with open(os.path.join(args.outputdir, filename), 'w') as df:
                json.dump(recipe, df)
            

if __name__ == '__main__':
    main()
