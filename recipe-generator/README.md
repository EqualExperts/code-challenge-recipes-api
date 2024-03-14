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

By default the script will output to ./recipes.

```
python src/main/python/cli.py --theme "Healthy Recipes" --num 10
```

**Note** The num property is passed to GPT, too large a number may cause it to cut off prematurily, you're better off doing batches in a bash loop, or if you have the time, build it into the script.
