#ChauhanMahesh/Vasusen/DroneBots/COL

from telethon.sessions import StringSession
from telethon import TelegramClient
import logging
import time
import sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Basics
API_ID = 2992000
API_HASH = "235b12e862d71234ea222082052822fd"
SESSION = "1BJWap1wBu36XUBjHZOusMjLi28oQH36uaTo9SRxRFE1zvMn6WSrcpTzJqlXOQXM5576wwq6_uS_OFV38-M3cntmcd8lbPVS0EHZxpQL_KG8g193jt6OuQ8e6obcpK6tjPjaBzyBfjcFRviRQ_z6cirRCfGZWOU9Dfgz72aG6_hJ0DiFbhl-zTDgB2JGORaM5wIyTIUJNuc7x9qgn0WVVKQR8ak46GpdO5d8pt_vJEFCg5DS-ut9m3RWnHY7eOKAnOCvpIlqN1kCPH38w6mNui__uWoRQeI8Wv0ASBHgtyZydbJ8WGahRHduHyAwPsyb27LCSyuRJffDg472_30Dw3NRzikItbLc="

Drone = TelegramClient(StringSession(SESSION) , API_ID, API_HASH)

try:
    Drone.start()
except Exception:
    print("Userbot Error ! Have you added a SESSION in deploying??")
    sys.exit()
