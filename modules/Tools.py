import imp


import json

def de_id_char(ID):
    return ID.replace('-','')

def generate_payload(config,content=""):
    json_str = json.dumps(config)
    if json_str.__contains__("update_me"):
        res = json_str.replace("update_me",content)
    else:
        res = json_str
    return json.loads(res)
