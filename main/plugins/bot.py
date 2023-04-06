#ChauhanMahesh/Vasusen/COL/DroneBots

import asyncio

async def clone(bot, source, destination):
    async for msg in bot.iter_messages(int(source), reverse=True):
        try:
            await asyncio.sleep(3)
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

