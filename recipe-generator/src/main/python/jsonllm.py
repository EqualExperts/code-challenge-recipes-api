import os
import logging
import traceback
import json

from typing import Union

from openai import OpenAI

MODEL = "gpt-3.5-turbo-16k"
MAX_FAILURES = 3

logger = logging.getLogger(__file__)

if not os.environ['OPENAI_API_KEY']:
    raise Exception("OpenAI API key was not set, please set the OPENAI_API_KEY environmental variable")

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

def message(role: str, message: str) -> str:
    return { "role": role, "content": message }

def complete(msg: str, expected_output_format: str) -> list:
    failures = 0
    try:    
        messages = [message("system", "You are a REST API, which responds in only valid JSON, in the formats given."),
            message("system", f"Your output format should be precisely aligned with the following JSON template: {expected_output_format}"),
            message("user", msg)]
        
        logging.info(f"Start Attempt ({failures+1}/{MAX_FAILURES}): {msg}")
        logging.debug(f"   GPT Request={messages}")
        output = client.chat.completions.create(model=MODEL, messages=messages).choices[0].message.content
        logging.debug(f"    GPT Response={output}")
        result = json.loads(output)
        logging.info("    Success")
        return result
    except:
        failures += 1
        logging.info(f"    Failure {traceback.format_exc()}")
        if failures == MAX_FAILURES:
            raise Exception("Max failures in parsing valid JSON reached, cowardly giving up.")
