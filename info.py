import re
from os import environ, getenv
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', "29127726"))
API_HASH = environ.get('API_HASH', "b25483bdec0d64a73899ee8ede66cd40")
BOT_TOKEN = environ.get('BOT_TOKEN', "7033757994:AAHtN9NiibNpziLYFClMUkfaft7CBljaFJA")
TIMEZONE = environ.get("TIMEZONE", "Asia/Kolkata")
# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = is_enabled((environ.get('USE_CAPTION_FILTER', 'True')), True)

PICS = (environ.get('PICS', 'https://telegra.ph/file/0ed351c8605c23e8cae79.jpg https://telegra.ph/file/6524270c008b60f81f30a.jpg https://telegra.ph/file/848ed57090fd5111ce64d.jpg https://telegra.ph/file/5fe959d96fcc33d1b9dc9.jpg https://telegra.ph/file/ec5f5a031b7826e28360c.jpg https://telegra.ph/file/aa4b77441bb41cfce12d7.jpg https://telegra.ph/file/00ed60e2c89d564d850ef.jpg https://telegra.ph/file/a5d518f6020976bc45264.jpg https://telegra.ph/file/650191ad1f813ca8f41cb.jpg https://telegra.ph/file/c6042704a1bc0a2b52996.jpg https://telegra.ph/file/9d68211fa9dcb208200be.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://telegra.ph/file/c6042704a1bc0a2b52996.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://telegra.ph/file/451f038b4e7c2ddd10dc0.mp4")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/5e2d4418525832bc9a1b9.jpg")
SUBSCRIPTION = (environ.get('SUBSCRIPTION', 'https://graph.org/file/12adf3a7451bf2a72b454.jpg'))
CODE = (environ.get('CODE', 'https://vault.pictures/p/0ce73492b6cb43c4aa5bea288545bd35')) # Scanner Code image 

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1985196029').split()]
OWNER_USER_NAME = environ.get("OWNER_USER_NAME", "Titanoboa_team") # widout 👉 @
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001572383457').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL', "-1001430858047")
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID')
reqst_channel = environ.get('REQST_CHANNEL_ID', "-1002067624859")
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = is_enabled((environ.get("NO_RESULTS_MSG", 'True')), False)

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://bossjk:jkboss@cluster0.uywmvse.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Raaz")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

#refer time, or user count
REFERAL_USER_TIME = int(environ.get('REFERAL_USER_TIME', "2592000")) # set in seconds | already seted 1 month premium
USERS_COUNT = int(environ.get('USERS_COUNT', "2")) # Set Referel User Count
INVITED_USER_TRAIL = int(environ.get('INVITED_USER_TRAIL', "86400")) #set in seconds, free trail invites users in 1 day, 

#stream link shortner
STREAM_SITE = (environ.get('STREAM_SITE', 'urlshortx.com'))
STREAM_API = (environ.get('STREAM_API', '8afa8fbc218cc0791c62495f2c510c92524503ce'))
STREAMHTO = (environ.get('STREAMHTO', 'https://t.me/Hoe/69'))
STREAM_LINK_MODE = is_enabled((environ.get('STREAM_LINK_MODE', "False")), False)

#premium Users Satuts
premium = environ.get('PREMIUM_LOGS', '-1001998895377')
PREMIUM_LOGS = int(premium) if premium and id_pattern.search(premium) else None

#files link shortnet
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'instantearn.in')
SHORTLINK_API = environ.get('SHORTLINK_API', 'fe42ad11c5d8487b19d045dfe7402a4db13bdd80')
IS_SHORTLINK = is_enabled((environ.get('IS_SHORTLINK', 'False')), False)

# verify link shortner
IS_VERIFY = is_enabled((environ.get('IS_VERIFY', 'True')), False)
HOW_TO_VERIFY = environ.get('HOW_TO_VERIFY', "https://t.me/link_Streaam_Movies/16")
VERIFY2_URL = environ.get('VERIFY2_URL', "instantearn.in")
VERIFY2_API = environ.get('VERIFY2_API', "fe42ad11c5d8487b19d045dfe7402a4db13bdd80")

DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '-1001998895377').split()]
MAX_B_TN = environ.get("MAX_B_TN", "7")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/Mix_Cinema_Box')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/Latest_movies_freeOnNet')
MSG_ALRT = environ.get('MSG_ALRT', 'Wʜᴀᴛ Aʀᴇ Yᴏᴜ Lᴏᴏᴋɪɴɢ Aᴛ ?')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', -1001801990402))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'Titanoboa_team')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "Falsd")), False)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
PM_FILTER = is_enabled((environ.get('PM_FILTER', "False")), True)
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/Mix_Cinema_Box')
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', True))
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

# Streaming
BIN_CHANNEL = environ.get("BIN_CHANNEL", "-1001801990402")
if len(BIN_CHANNEL) == 0:
    logging.error('BIN_CHANNEL is missing, exiting now')
    exit()
else:
    BIN_CHANNEL = int(BIN_CHANNEL)

PORT = int(environ.get('PORT', 8080))
NO_PORT = bool(environ.get('NO_PORT', False))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
    "https://{}:{}/".format(FQDN, PORT)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'LusiBot'))
MULTI_CLIENT = False
name = str(environ.get('name', 'Lusifilms'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))

else:
    ON_HEROKU = False
HAS_SSL=bool(getenv('HAS_SSL',False))
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "https://{}/".format(FQDN)
REPO_OWNER = "Titanoboa_team"

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

