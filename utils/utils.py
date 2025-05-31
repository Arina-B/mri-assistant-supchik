from os import environ
from pathlib import Path
from tempfile import gettempdir
from dotenv import load_dotenv
load_dotenv()


token = environ.get('BOT_TOKEN')
admin_ids = environ.get("ADMIN_IDS")

resources_dir = Path("resources")
temp_dir = Path(gettempdir(), "codiim_bot")
temp_dir.mkdir(exist_ok=True)

