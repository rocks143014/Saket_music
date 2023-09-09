import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from AMMusic import LOGGER, app, userbot
from AMMusic.core.call import Anon
from AMMusic.plugins import ALL_MODULES
from AMMusic.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("AMMusic").error(
            "WTF Baby ! Atleast add a pyrogram string, How Cheap..."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("AMMusic").warning(
            "Sur spotify id aur secret toh daala hi nahi aapne ab toh spotify se nahi chala paaoge gaane."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("AMMusic.plugins." + all_module)
    LOGGER("AMMusic.plugins").info(
        "Necessary Modules Imported Successfully."
    )
    await userbot.start()
    await Anon.start()
    try:
        await Anon.stream_call(
            "https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("AMMusic").error(
            "[ERROR] - \n\n🇹​​🇺​​🇲​​🇦​​🇷​​🇦​ ​🇲​​🇺​​🇸​​🇮​​🇨​ ​🇧​​🇴​​🇹​ ​🇷​​🇪​​🇦​​🇩​​🇾​ ​🇭​​🇪​ ​🇦​​🇧​ ​🇵​​🇦​​🇷​​🇹​​🇾​ ​🇩​​🇪​ ​🇷 🇴 🇨 🇰 🇾 ​ ​🇰​​🇴​."
        )
        sys.exit()
    except:
        pass
    await Anon.decorators()
    LOGGER("AMMusic").info("\x54\x75\x6d\x61\x72\x61\x20\x4d\x75\x73\x69\x63\x20\x42\x6f\x74\x20\x42\x61\x6e\x6e\x67\x61\x79\x61\x20\x41\x62\x20\x50\x61\x72\x74\x79\x20\x44\x65\x20\x41\x4d\x42\x4f\x54\x20\x20\x41\x75\x72\x20\x4a\x6f\x69\x6e\x20\x4b\x61\x72\x6c\x6f\x20\x4d\x65\x72\x61\x20\x43\x68\x61\x6e\x6e\x65\x6c\xd83e\xdd7a\x20\x4a\x6f\x69\x6e\x20\x3a\x20\x40\x41\x4d\x42\x4f\x54\x59\x54")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("AMMusic").info("Stopping Music Bot...")



 
