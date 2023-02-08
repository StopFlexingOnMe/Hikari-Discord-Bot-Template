import hikari
import lightbulb
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("token")
guild_id = int(os.getenv("guild_id"))
prefix = os.getenv("prefix")
owner_id = int(os.getenv("owner_id"))


bot = lightbulb.BotApp(
    token=token,
    prefix=prefix,
    owner_ids=owner_id,
    default_enabled_guilds=guild_id,
    ignore_bots=True,
    intents=hikari.Intents.ALL
)


bot.load_extensions_from("./extensions")
bot.run()