from urllib import response
from numpy import deprecate
import requests
import json
import time

class Client:
    def __init__(self, api_key) -> None:
        self.api_key = api_key

def rest(func):
    def sleep_first(*args, **kw):
        time.sleep(0.35)
        res = func(*args, **kw)
        return res
    return sleep_first

class Database(Client):
    def __init__(self, api_key, database_id) -> None:
        super().__init__(api_key)
        self.id = database_id
    
    @rest
    def get_json(self, payload = {"page_size": 100}):
        url =  url = f"https://api.notion.com/v1/databases/{self.id}/query"
        headers = {
            "Accept": "application/json",
            "Notion-Version": "2021-08-16",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        response = requests.post(url, json=payload, headers=headers)
        return response.json()

    # deprecated
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
    def __init__(self, api_key, page_id) -> None:
        super().__init__(api_key)
        self.id = page_id
    
    @rest
    def get_json(self):
        url = f"https://api.notion.com/v1/pages/{self.id}"
        headers = {
            "Accept": "application/json",
            "Notion-Version": "2021-08-16",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        response = requests.get(url, headers=headers)
        return response.json()
    
    # deprecated
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

    @rest
    def modify_content(self, payload):
        url = f"https://api.notion.com/v1/pages/{self.id}"
        payload = payload
        headers = {
            'Authorization':f"Bearer {self.api_key}",
            'Accept':"application/json",
            'Notion-Version': "2022-06-28",
            'Content-Type': "application/json"
        }
        response = requests.patch(url, json=payload, headers=headers)
        return response.json()

class Block(Client):
    def __init__(self, api_key, block_id) -> None:
        super().__init__(api_key)
        self.id = block_id

    @rest
    def get_json(self):
        url = f"https://api.notion.com/v1/blocks/{self.id}"
        headers = {
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
            
        }
        response = requests.get(url, headers=headers)
        return response.json()

    @rest
    def modify_content(self, payload):
        url = f"https://api.notion.com/v1/blocks/{self.id}"
        payload = payload
        headers = {
            'Authorization':f"Bearer {self.api_key}",
            'Accept':"application/json",
            'Notion-Version': "2022-06-28",
            'Content-Type': "application/json"
        }
        response = requests.patch(url, json=payload, headers=headers)
        return response.json()
    