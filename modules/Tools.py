import imp


import json

def de_id_char(ID):
    return ID.replace('-','')

def decoder(x):
    return [i for i in x]

def print_dic_json_style(dic):
    print(json.dumps(dic,indent=4))

def generate_payload(config,content=""):
    json_str = json.dumps(config)
    if json_str.__contains__("update_me"):
        res = json_str.replace("update_me",content)
    else:
        res = json_str
    return json.loads(res)
