from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("23513526"))
API_HASH = getenv("8e0771f3d5d048cbf3b601b8ed152c0d")

BOT_TOKEN = getenv("7635831190:AAEubbqTyxeGVqJ0rdlNvAXhOBcYLjlbAKw", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("7125448912"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/84819fc115cb0eff32b2b.jpg")

SESSION = getenv("BQFmybYAkwBaOWoXVxynkUndCEmRcxueU-VZD4bPzhQfUWZixKJiHiCAk2-rkbMBxdJ5lFROVX62BzP16Wruj-xwlFtp9RmPlRfNdoFOZKMk4xt_jCiLgjXuP6Nhp69rxvuISoqmjyOGVbNo29ZiNJ_Y1c3x1xNFCYySKxhjqY5mK_OzZcHrpmnPrWfY-0BPF5vIwsgFWY6mlD2D5CIB6yqnKFGO_AdydgDSYIG7dtLUa19DXiD1zPtC24n9nvfKrEL-hFYmky9JtZiqEpcMlId7TrZvQOHfxf8vOtnVbZ2UicktHj5FODBptogUScXelapRZexyxnZibLE8MGVUv2TU4Yi6vwAAAAGotbjQAA", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/tbcbotschat")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/tbc_bots")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5090817443").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
