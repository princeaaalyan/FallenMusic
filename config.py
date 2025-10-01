from os import getenv
from dotenv import load_dotenv

load_dotenv()

# API credentials
API_ID = int(getenv("API_ID", "28142579"))
API_HASH = getenv("API_HASH", "f3dcd1e8dedf35e513b59c0ad01f33be")
BOT_TOKEN = getenv("BOT_TOKEN", "8238506745:AAGoZtm2kceFcJAPC0VkFzzvL5kx4MiXBVI")
SESSION = getenv("SESSION", "AQFk39kAhjZcHuD4YJmtD6IhgTwq_5YXw7zDpsDZevtzQgoRtdNDR2tysPwnMIpZ09jC9mBWZ_7msws_gclXvBuziE9WzA3yGBMUkf99O3YnTb_6BhdCf91K5uDNZIlr8mgmzr7C8rQTk3jUzQQVPv_BKGSSZszRGoxarfOR11kAr7hi8H8-SmWqdBSp9Aj7tr1xXxJLHMk2m_6OmRVwPiYFWOFLb_s26PSk9E05DVB9GLYKGsops4JHeCZ6eYgroCSfpNtASV_dObxqon0qKCq8JhTycmEqMSF4yOp39RfLJ3wP0cAWCfp0-aCJD4StzVY7XXVZtvGFMrTBO02Y9M_BTVAqeQAAAAHGGy28AA")

# Bot settings
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

# Owner and Sudo users
OWNER_ID = int(getenv("OWNER_ID", "7618637244"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))

# Media links
PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")
FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"

# Support links
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FallenAssociation")
