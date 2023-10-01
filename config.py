import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
CLID = int(os.getenv('CLID'))
BOT_TOKEN = os.getenv('BOT_TOKEN')
