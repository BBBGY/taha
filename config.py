## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME      =      getenv ( " SESSION_NAME"     ،     "AgC36LMX0RNmFoJ90gWpoSvh-EJcUxwrrGcPtghcdjQhMZ3QCgHVXysFTs4dqdnkxOOwmRuFpKsuneQcQ7E_w1btF6tQoknPkBRYNtxyyN6_n03ylmD2HCnzKIkzuecitVrnW9_c_A8bQSIvMupRknK6Py9U8tTr7o7jrQDNViM6fUVc4-qVkMtPdpQnWtxVSit_QqgVxIeHBfEPX7qMeFOqVMbixcHR0LxPExteeLYlXIXtmWdWtZTDn1ICqJJkgb2vOZ_leFrX-1wJkTE37i19GZ4qrZwxAydJ3fy6IHcp2qISjoZYWiygZKda0n7ZnEsoqqL-vOA81kWh-sTrHsNJAAAAATtJ9AIA")
BOT_TOKEN = getenv("BOT_TOKEN", "5156913565:AAH0HeV5dvMVTpuQht0XEFemIuv11MKHNwc")
BOT_NAME = getenv("BOT_NAME", "Nelover")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "Taha")
OWNER_USERNAME = getenv("OWNER_USERNAME", "TTTTZ9")
ALIVE_NAME = getenv("ALIVE_NAME", "Taha")
BOT_USERNAME = getenv("BOT_USERNAME", "EN_9BoT")
OWNER_ID = getenv("OWNER_ID", "5564738618")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "EEN6E")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "TTTP9")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "TTTP9")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5564738618").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/466de30ee0f9383c8e09e.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/d70bb6fa92728763c671f.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/46fa55b49b85c084159ce.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/a282c460a7f98aedbe956.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/8fe190a2a52986bd29dc5.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
