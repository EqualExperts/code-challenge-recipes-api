# AI Assist Study - Recipe Generator

## Prerequisites

- Python 3.11
- Recipes generated with recipe-generator in this parent directory.

## Running the API

```
python3 cli.py
```

## Usage

```
GET http://localhost:9113 ->
        /list.json: Provides a list of recipe ids, names and descriptions.
        /$id/summary.json: Provides recipe summary
        /$id/method.json: Provides the instructions
        /$id/diets.json: Provides the instructions
        /$id/ingredients.json: Provides the instructions
```
