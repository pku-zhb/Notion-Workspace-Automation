
import imp


import sys
import os
import time
import datetime

sys.path.append(".")

import json
from modules.KEY import NOTION_TOKEN
from modules.notionClients import Block, Database, Page
from modules.Tools import generate_payload, de_id_char



def calculate_score(type,page_json):
    if page_json['properties']['Checked']['formula']['boolean'] == False:
        return None
    else:
        if type == 'exercise':
    
            stars = len(page_json["properties"]["Feedback"]["select"]["name"])
            if stars == 3:
                score = 8
            elif stars == 2:
                score = 6
            elif stars == 1:
                score = 3

            type_amount = len(page_json["properties"]["Type"]['multi_select']) 
            if type_amount == 1:
                multiplier = 1
            elif type_amount == 2:
                multiplier = 1.25
            elif type_amount == 3:
                multiplier = 1.5

            score = min(multiplier * score,10)
            
        elif type == 'reading':
            stars = len(page_json["properties"]["Feedback"]["select"]["name"])
            if stars == 3:
                score = 8
            elif stars == 2:
                score = 6
            elif stars == 1:
                score = 3

            if page_json['properties']['[Option] Notes']['rich_text'] == 0:
                multiplier = 1 
            else:
                multiplier = 1.5

            score = min(multiplier*score,10)
            
            
        elif type == 'meditating':
            stars = len(page_json["properties"]["Feedback"]["select"]["name"])
            if stars == 3:
                score = 10
            elif stars == 2:
                score = 6
            elif stars == 1:
                score = 2

        elif type == 'health diet':
            stars = len(page_json["properties"]["Calories"]["select"]["name"])
            if stars == 3:
                score = 8
            elif stars == 2:
                score = 6
            elif stars == 1:
                score = 3
            
            schedule = len(page_json["properties"]["Schedule"]["select"]["name"])
            if schedule == 3:
                multiplier = 1.5
            elif schedule == 2:
                multiplier = 1.25
            elif schedule == 1:
                multiplier = 1
            
            score = min(multiplier*score,10)

    return score



def main():

    with open("./data/dailyCheck.json",'r') as f:
        task_json = json.load(f)
    
    for task in task_json["configurations"]:
        database_id = task['target_database_id']
        database = Database(NOTION_TOKEN,database_id)
        query_payload = {
            "filter":{
                "and":[
                    {
                        "property":"Score",
                        "number":{
                            "is_empty":True
                        }
                    },
                    {
                        "property":"Date",
                        "date":{
                            "on_or_after":(datetime.datetime.now()-datetime.timedelta(days=3)).strftime("%Y-%m-%d")
                        }
                    }
                ]
            }
        }
        query_result = database.get_json(query_payload)
        for record  in query_result["results"]:
            page_id = de_id_char(record['id'])
            page = Page(NOTION_TOKEN,page_id)
            score = calculate_score(task["_name"],page.get_json())
            modify_payload ={
                "properties":{
                    "Score":{
                        "number":score
                    }
                }
            }
            page.modify_content(modify_payload)

    

if __name__ == '__main__':
    main()