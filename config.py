import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID","22457436"))
API_HASH = getenv("API_HASH","c071b6a3575ca36614df86249576e310")

BOT_TOKEN = getenv("BOT_TOKEN")

MONGO_DB_URI = getenv("MONGO_DB_URI", "")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID","-1001885729197"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "乂D ᴍᴜꜱɪᴄ")

OWNER_ID = list(map(int, getenv("OWNER_ID", "6545714937").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/rocks143014/Saket_music/")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/XD_BOTSS")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/XD_SPAM")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "10012"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7f92897a59464ddbbf00f06cd6bda7fc")

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "BQAbqXH9v5TWIpVy574alGsqb-iIUEg8AVxGKbo8inRAOIEa2zzlmZFaxuJ9SfO7ULLBdwuvLWk1WZ_egVAGFhFQyTGAt7I7BgKF030RJaIGNU0lSk3Z9dtU3Cq8Ih2qXiDj54q20fOxJ0zr83U98CHF2H0lQQ11-MIFf90hhJYiMApLQ17JSOv-aILkQ0zPZGycdGGQQlnQ9cvPzUVo2CJ2-9YSJePX2s6YpzpjLXcr3QMU0kv11qleqb-_GVadY6KTcmcNWRwvTZxUiXTCygXRePKq1v0TZ7sbBAVUO5XA9Ujpf1uc3MJYJQfYgeNeQjuPdBv6NE9mPlMFPk_0FC_iAAAAAYIGbIAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://graph.org/file/4bcbafaa4e73c0e550177.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://graph.org/file/97ec679cd7e3e146cd230.jpg",
)

PLAYLIST_IMG_URL = "https://graph.org/file/b013f7ca79dab967c83e0.jpg"

GLOBAL_IMG_URL = "https://graph.org/file/471f5efc4676676c469b8.jpg"

STATS_IMG_URL = "https://graph.org/file/471f5efc4676676c469b8.jpg"

TELEGRAM_AUDIO_URL = "https://graph.org/file/2369dd282146c7dda1e4e.jpg"

TELEGRAM_VIDEO_URL = "https://graph.org/file/2369dd282146c7dda1e4e.jpg"

STREAM_IMG_URL = "https://graph.org/file/32eb0f7d1cf8b7e9dc73b.jpg"

SOUNCLOUD_IMG_URL = "https://graph.org/file/32eb0f7d1cf8b7e9dc73b.jpg"

YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/32eb0f7d1cf8b7e9dc73b.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/32eb0f7d1cf8b7e9dc73b.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://graph.org/file/471f5efc4676676c469b8.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://graph.org/file/471f5efc4676676c469b8.jpg"
