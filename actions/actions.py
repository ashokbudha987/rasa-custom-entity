from typing import Dict, Text, Any, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionGatherPreferences(Action):
    def name(self) -> Text:
        return "action_gather_preferences"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        preference = tracker.get_slot("preference")
        metric = tracker.get_slot("metric")

        # Accessing the stored preferences dictionary from the tracker
        preferences_dict = {"sales":[]}

        # Check if metric exists in the preferences_dict
        if metric in preferences_dict:
            # Check if preference is not already in the list, then add it
            if preference not in preferences_dict[metric]:
                preferences_dict[metric].append(preference)
        else:
            # If metric doesn't exist, create a new entry
            preferences_dict[metric] = [preference]


        # You can access this dictionary in subsequent actions or use it as needed
        print("Updated Preferences Dictionary:", preferences_dict)

        dispatcher.utter_message(template="utter_acknowledge_preferences", preference=preference, metric=metric)
        return []
