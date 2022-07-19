import requests
import json
import time

class Client:
    def __init__(self, api_key) -> None:
        self.api_key = api_key

def rest(func):
    def sleep_first(*args, **kw):
        time.sleep(0.35)
        func(*args, **kw)
    return sleep_first

class Database(Client):
    def __init__(self, api_key, db_id) -> None:
        super().__init__(api_key)
        self.id = db_id
    
    @rest
    def get_elements_text(self, attribute):
        url =  url = f"https://api.notion.com/v1/databases/{self.id}/query"
        payload = {"page_size": 100}
        headers = {
            "Accept": "application/json",
            "Notion-Version": "2021-08-16",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        response = requests.post(url, json=payload, headers=headers)
        arr = []
        for result in response.json()["results"]:
            arr.append(result["properties"]
                       [f"{attribute}"]["title"][0]["plain_text"])
        return arr
    
    @rest
    def get_json(self):
        url =  url = f"https://api.notion.com/v1/databases/{self.id}/query"
        payload = {"page_size": 100}
        headers = {
            "Accept": "application/json",
            "Notion-Version": "2021-08-16",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        response = requests.post(url, json=payload, headers=headers)
        return response.json()
    
    @rest
    def new_record(self):
        url =  url = f"https://api.notion.com/v1/pages/"
        payload = {
            "parent":{
                "type":"database_id",
                "database_id":self.id
            },
            "properties": {
                "Name": {
                    'title':[{
                        'text': {
                            'content': ''
                        }
                    }]
                }
            }
        }
        headers = {
            "Accept": "application/json",
            "Notion-Version": "2021-08-16",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        response = requests.post(url, json=payload, headers=headers)
        return response.json()

class Page(Client):
    def __init__(self, api_key, pg_id) -> None:
        super().__init__(api_key)
        self.id = pg_id
    
    @rest
    def get_json(self):
        url =  url = f"https://api.notion.com/v1/pages/{self.id}"
        payload = {"page_size": 100}
        headers = {
            "Accept": "application/json",
            "Notion-Version": "2021-08-16",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        response = requests.get(url, headers=headers)
        return response.json()
    
    @rest
    def modify_text_prop(self, prop, content):
        url =  url = f"https://api.notion.com/v1/pages/{self.id}"
        payload = {
            "properties": {
                prop: {
                    'title':[{
                        'text': {
                            'content': content
                        }
                    }]
                }
            }
        }
        headers = {
            "Accept": "application/json",
            "Notion-Version": "2021-08-16",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        response = requests.patch(url, headers=headers, json=payload)
        return response.json()