#ChauhanMahesh/Vasusen/COL/DroneBots

from telethon import events
import asyncio
from .. import Drone

async def clone(bot, source, destination, msg_id, media_only=True):
    async for msg in bot.iter_messages(int(source), min_id=int(msg_id), reverse=True):
        try:
            await asyncio.sleep(3)
            if media_only == False:
                try:
                    await bot.send_message(destination, msg)
                    return
                except Exception as exc:
                    print(str(exc))
                    return
            if msg.poll:
                return
            if msg.photo:
                photo=msg.media.photo
                await bot.send_file(
                    destination, photo, caption=msg.text, link_preview=False
                )
            elif msg.media:
                try:
                    if msg.media.webpage:
                        await bot.send_message(
                            destination, msg.text, link_preview=False
                        )
                except Exception:
                    media=msg.media.document
                    await bot.send_file(
                        destination, media, caption=msg.text, link_preview=False
                    )
                finally:
                    return
            else:
                return
        except Exception as exc:
            print(str(exc))

@Drone.on(events.NewMessage(outgoing=True, pattern="^/run (.*)"))
async def run(event):
    c = (event.text).split(" ")
    if not len(c) == 5 :
        await event.edit("Incorrect format")
        return
    if c[4] == "True":
        media==True
    else:
        media==False 
    await clone(event.client, int(c[1]), int(c[2]), int(c[3]), media_only=media)
