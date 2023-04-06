#ChauhanMahesh/Vasusen/DroneBots/COL

from telethon.sessions import StringSession
from telethon import TelegramClient
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Basics
API_ID = 
API_HASH = 
SESSION = 

Drone = TelegramClient(StringSession(SESSION) , API_ID, API_HASH)
