import discord
import os
import dotenv

# Make sure we're on the proper working directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir("/".join(dname.split("/")[:-1]))

bot = discord.Bot(intents=discord.Intents.all())

@bot.event
async def on_ready() -> None:
    print(f'\nSuccessfully logged into Discord as "{bot.user}"\n')
    await bot.change_presence(status=discord.Status.online,
                              activity=discord.Activity(type=discord.ActivityType.watching,
                                                        name="sufrir a los estudiantes de la EPI"))

dotenv.load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
if BOT_TOKEN is None:
    raise Exception("BOT_TOKEN not found in .env")

if __name__ == "__main__":
    bot.run(BOT_TOKEN)  # Start the bot up