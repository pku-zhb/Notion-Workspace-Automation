
import requests
import secrets
import json
import time

def decoder(x):
    return [i for i in x]

def clearCheckbox(block_id):
    url = "https://api.notion.com/v1/blocks/" + block_id
    payload = {
        "to_do": {
            "checked":False
        }
    }
    header = {
        'Authorization':secrets.NOTION_TOKEN,
        'Accept':"application/json",
        'Notion-Version': "2022-06-28",
        'Content-Type': "application/json"
    }
    requests.patch(url, json=payload, headers=header)
    time.sleep(0.4) # 每个requests后面停0.4s，防止超notion的请求频率

def get_blockContent(block_id):
    url = "https://api.notion.com/v1/blocks/" + block_id
    header = {
        'Authorization':secrets.NOTION_TOKEN,
        'Notion-Version': "2022-06-28",
        'Content-Type': "application/json"
    }
    response = requests.get(url,headers=header)
    time.sleep(0.4) 
    return response.json()['to_do']['rich_text']

def retrieve_db(database_id):
    url = "https://api.notion.com/v1/pages/"
    url += "ee68f7cd5ca340e29c06136d8b6e0a33" 
    # url += "/children"
    header = {
        'Authorization':secrets.NOTION_TOKEN,
        'Notion-Version': "2022-06-28",
        'Content-Type': "application/json"
    }
    response = requests.get(url,headers=header)
    time.sleep(0.4)
    # print(response)
    print(json.dumps(response.json(), indent=4))

def test(database_id):
    url = "https://api.notion.com/v1/pages/" + database_id
    # url += "/children"
    header = {
        'Authorization':secrets.NOTION_TOKEN,
        'Notion-Version': "2021-05-13",
        # 'Content-Type': "application/json"
    }
    response = requests.get(url,headers=header)
    time.sleep(0.4)
    # print(response)
    return response.json()['properties']

def test_post(block_id, prop):
    url = "https://api.notion.com/v1/pages/"
    header = {
        'Authorization':secrets.NOTION_TOKEN,
        'Notion-Version': "2021-05-13",
        'Accept': "application/json",
        'Content-Type': "application/json"
    }
    payload = {
        "parent":{
            "type": "database_id",
            "database_id": block_id
            },
        # "properties": prop
    }
    response = requests.post(url,headers=header, json = payload)
    time.sleep(0.4)
    # print(response)
    print(json.dumps(response.json(), indent=4))


def main():

    # url =  BLOCK_ID
    # retrieve(url)
    # update(url)
    with open('../appData/dailyCheck.json','r') as f:
        config = json.load(f)
    # for job in config['configurations']:
        # clearCheckbox(job['block_id'])
        # content = get_blockContent(job['block_id'])
        # retrieve_db(job['database_id'])
    
    prop = test('96d6614a7e9e4a9ea52b5574e7e8a811')
    test_post('57e061fe4b3547d0928fb354978fea2f', prop)


    

if __name__ == '__main__':
    main()
