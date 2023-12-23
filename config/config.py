from os import getenv
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = getenv("BOT_TOKEN")
ADMINS = getenv("ADMINS")

# sql litedan boshqa database kerak bo'lmasa shart emas
DATABASE = getenv("DATABASE")
USER = getenv("USER")
PASSWORD = getenv("PASSWORD")
HOST = getenv("HOST")
IP = getenv("IP")