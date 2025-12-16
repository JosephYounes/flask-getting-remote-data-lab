import requests
import json

class PeopleAPI:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def get_response_body(self):
        response = requests.get(self.endpoint)
        return response.text

    def load_json(self):
        response_body = self.get_response_body()
        return json.loads(response_body)

endpoint = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
api = PeopleAPI(endpoint)

people_data = api.load_json()
print(people_data)