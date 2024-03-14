import json

class Templates:
    def __init__(self, theme) -> None:
        self.theme = theme


    def outputFormatSingleRecipe(self) -> str:
        return """
        {
            "name": str,
            "description": str,
            "diets": List[str],
            "servings": int,
            "ingredients": List[{
                "unit_of_measurement": str,
                "quantity": int,
                "name": str
            }],
            "method": List[str],
            "preparationTimeMin": int,
            "cookingTimeMin": int,
            "estimatedCostDollars": int
        }
        """
    
    def promptGetSingleRecipe(self, units_of_measurement: dict) -> str:
        return f"""
        {self.includeTheme()}
        Create a unique, creative and humourous recipe, use any of the following units of measurement when writing the recipe: {json.dumps(units_of_measurement)},
        ensure that ingredients listed in the ingredients section are actually used in the method section.
        Estimate what you need to estimate.
        Keep in mind that the recipes don't have to be 'real', i.e. you don't have to map the units of measurement to real world ingredients.
    """
    
    def promptGetRecipes(self, units_of_measurement: dict, num_recipes: int) -> str:
        return f"""
        {self.includeTheme()}
        Create {num_recipes} unique, creative and humourous recipe, use any of the following units of measurement when writing the recipe: {json.dumps(units_of_measurement)},
        ensure that ingredients listed in the ingredients section are actually used in the method section.
        Estimate what you need to estimate.
        Keep in mind that the recipes don't have to be 'real', i.e. you don't have to map the units of measurement to real world ingredients.
    """

    def outputFormatUnitsOfMeasurement(self) -> str:
        return """
        {"units_of_measurement": ["cups", "teaspoons", "tablespoons", "ml"]}
        """

    def includeTheme(self) -> str:
        return f"""
        Recipe Theme: 
        
        {self.theme}
        
        Taking the overall theme into account, 
        """
    
    def promptGetUnitsOfMeasurement(self) -> str:
        return f"""
        {self.includeTheme()}
        Create a comprehensive list of roughly 50 creative units of measurement for ingredients used in cooking (i.e. in normal recipes we would think 'cups', 'teaspoons', 'tablespoons', 'grams', 'kilograms').
        We will use this to define an enum.
    """
