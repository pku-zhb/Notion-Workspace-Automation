import requests
import json
import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    print(os.getenv("NOTION_TOKEN"))


if __name__ == '__main__':
    main()
