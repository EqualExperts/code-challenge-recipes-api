import json
import logging

import jsonllm
from templates import Templates

logger = logging.getLogger(__file__)

class RecipeGenerator:
    units_of_measurement = None

    def __init__(self, theme) -> None:
        self.templates = Templates(theme)
        self.units_of_measurement = self.generateUnitsOfMeasurement()

        logger.info(f"Recipe Generator is ready: {json.dumps(self.units_of_measurement)}")

    def generateUnitsOfMeasurement(self):
        return jsonllm.complete(
            self.templates.promptGetUnitsOfMeasurement(), 
            expected_output_format=self.templates.outputFormatUnitsOfMeasurement())
        

    def generateSingleRecipe(self):
        return jsonllm.complete(
            self.templates.promptGetSingleRecipe(self.units_of_measurement),
            expected_output_format=self.templates.outputFormatSingleRecipe()
        )
    
    def generateRecipes(self, num:int):
        return jsonllm.complete(
            self.templates.promptGetRecipes(self.units_of_measurement, num),
            expected_output_format=f"[{self.templates.outputFormatSingleRecipe()}]"
        )