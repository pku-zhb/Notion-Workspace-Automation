
TASK_DB_ID = "2274e92348464e65b1eb6d4054ac32f2"

from modules.KEY import NOTION_TOKEN
from modules.notionClients import Block, Database, Page
from modules.Tools import generate_payload, de_id_char

def main():
    database = Database(NOTION_TOKEN,TASK_DB_ID)
    query_payload = {
        "filter":{
            "and":[
                {
                    "property":"[All] Status",
                    "select":{
                        "equals":"Done"
                    }
                },
                {
                    "property":"[End] Feedback Done",
                    "formula":{
                        "checkbox":{
                            "equals":True
                        }
                    }
                },
                {
                    "property":"[End] If today",
                    "checkbox":{
                        "equals":True
                    }
                }
            ]
        }
    }

    query_result = database.get_json(query_payload)
    for record in query_result['results']:
        page_id = de_id_char(record['id'])
        page = Page(NOTION_TOKEN,page_id)
        modify_payload ={
                "properties":{
                    "[End] If today":{
                        "checkbox":False
                    }
                }
            }
        page.modify_content(modify_payload)

if __name__ == '__main__':
    main()
