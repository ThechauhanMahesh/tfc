#ChauhanMahesh/Vasusen/DroneBots/COL

from telethon.sessions import StringSession
from telethon import TelegramClient
import logging
import time
import sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Basics
API_ID = 
API_HASH = 
SESSION = 

Drone = TelegramClient(StringSession(SESSION) , API_ID, API_HASH)

try:
    Drone.start()
except Exception:
    print("Userbot Error ! Have you added a SESSION in deploying??")
    sys.exit()
