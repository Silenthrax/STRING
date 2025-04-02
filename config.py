from os import environ

# Telegram Account Api Id And Api Hash
API_ID = int(environ.get("API_ID", "29991343"))
API_HASH = environ.get("API_HASH", "89d05e3d07989acb31ce596397e87897")

# Your Main Bot Token 
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Owner ID For Broadcasting 
OWNER_ID = int(environ.get("OWNER_ID", "6890400066")) # Owner Id or Admin Id

# Give Your Force Subscribe Channel Id Below And Make Bot Admin With Full Right.
F_SUB = environ.get("F_SUB", "1002413084281")

# Mongodb Database Uri For User Data Store 
MONGO_DB_URI = environ.get("MONGO_DB_URI", "")

# Port To Run Web Application 
PORT = int(environ.get('PORT', 8080))
