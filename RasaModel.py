import json
import logging
import os

from rasa.model import get_latest_model
import asyncio
from rasa.core.agent import Agent
from rasa.shared.utils.io import json_to_string

class RASAModel:
    def __init__(self) -> None:
        current_dir = os.path.dirname(os.path.realpath(__file__))  # Get the current directory of the script
        models_path = os.path.join(current_dir, "models")
        self.agent = Agent.load(get_latest_model(model_path=models_path))
        
    def message(self, message: str) -> str:
        message = message.strip()
        return json_to_string(asyncio.run(self.agent.parse_message(message)))



class EntityExtract:
    rasamodel_instance = RASAModel()
    @staticmethod
    def get_entities(msg_query):
        json_result = EntityExtract.rasamodel_instance.message(msg_query)
        result = json.loads(json_result)

        #Extracting Entities
        entities= result.get("entities",[])
        entity_list=[]
        for entity in entities:
            entity_info = {
                "entity": entity["entity"],
                "value": entity["value"],
                # "start": entity["start"],
                # "end": entity["end"],
                # "confidence": entity["confidence_entity", None],  
                # "extractor": entity["extractor"],
                # "processors": entity["processors"],
            }
            entity_list.append(entity_info)
        return entity_list


