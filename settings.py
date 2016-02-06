import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

HOST = os.environ.get('HOST', '127.0.0.1')
PORT = int(os.environ.get('PORT', 3000))
DEBUG = bool(os.environ.get('DEBUG', False))

SLACK_COMMAND = os.environ.get('SLACK_COMMAND', 'frink')
SLACK_TEAM_ID = os.environ.get('SLACK_TEAM_ID')
SLACK_COMMAND_TOKEN = os.environ.get('SLACK_COMMAND_TOKEN')
