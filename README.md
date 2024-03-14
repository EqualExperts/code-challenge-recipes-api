This repo hosts the recipes API on which the [AI Assist coding challenge](https://github.com/EqualExperts/code-challenge-recipe-finder) depends.

The (mock) API is just a set of static JSON files.

It also contains code to generate new recipes:

- Generate unique recipes around a theme

# AI Assist Study - Recipe Generator

## Prerequisites

- Python 3.11
- pip

## Get your environment ready

- Install Virtualenv:

```
pip3 install virtualenv
```

- Create a virtual env and install the requirements

```
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r ./requirements.txt
```

- Create a .env file and set your OpenAI API Key:

_.env_

```
OPENAI_API_KEY=...
```

## Running the tests

```
pytest
```

## Creating some recipes

By default the script will output to data/recipes.

```
python src/main/python/cli.py --theme "Healthy Recipes" --num 10
```

**Note** The num property is passed to GPT, too large a number may cause it to cut off prematurily, you're better off doing batches in a bash loop, or if you have the time, build it into the script.

- Create a fake database by slicing single recipes into multiple files/folders:

```bash
cd recipe-splitter
python3 src/main/python/cli.py
```

- Run the mock API

```bash
cd recipe-api
python3 src/main/python/cli.py
```

- Start up the recipe finder application

* Open Intellij IDEA,
* File | New Project from Existing Sources
    - Select the recipe-finder directory
    - Select _Import project from existing sources_
    - Select Maven
* Create a run configuration to run src/main/java/RecipeFinderApplication

- You can "import" the recipes from the mock api by issuing a GET request to http://localhost:8080/admin/import.
- You can search for recipes by navigating to http://localhost:8080/recipes

