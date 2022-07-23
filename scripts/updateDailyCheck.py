
import imp


import sys
import os
import time
sys.path.append(".")

import json
from modules.KEY import NOTION_TOKEN
from modules.notionClients import Block, Database, Page
from modules.Tools import generate_payload, de_id_char

def main():

    with open("./data/dailyCheck.json",'r') as f:
        task_json = json.load(f)
    
    for task in task_json["configurations"]:
        database_id = task['target_database_id']
        database = Database(NOTION_TOKEN,database_id)
        new_record_response = database.new_record()

        record_page_id = de_id_char(new_record_response["id"])
        record_page = Page(NOTION_TOKEN,record_page_id)

        today_str = time.strftime("%Y-%m-%d")
        record_page_init_payload = task["new_record_init_payload"]
        record_page_init_payload = generate_payload(record_page_init_payload,today_str)
        
        init_rew_record_response = record_page.modify_content(record_page_init_payload)
        
        target_block_id = task['target_block_id']
        block = Block(NOTION_TOKEN,target_block_id)

        block_update_payload = task["target_block_update_payload"]
        herf = "/" + record_page_id
        payload = generate_payload(block_update_payload, herf)

        update_response = block.modify_content(payload)


    

if __name__ == '__main__':
    main()