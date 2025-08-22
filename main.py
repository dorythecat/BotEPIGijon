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


@bot.event
async def on_raw_reaction_add(payload: discord.RawReactionActionEvent) -> None:
    user = payload.member
    if user.bot or payload.message_id not in [1408560477151432706, 1408560559531753623]:
        return

    if str(payload.emoji) not in ["🖥️", "📊", "📡", "🌉", "📋", "🔧", "⚡", "🔬", "💡", "🇪🇸", "🇬🇧"]:
        return

    match str(payload.emoji):
        case "️🖥️":
            await user.add_roles(discord.utils.get(user.guild.roles, id=869949213348356116))
        case "📊":
            await user.add_roles(discord.utils.get(user.guild.roles, id=869951347158569041))
        case "📡":
            await user.add_roles(discord.utils.get(user.guild.roles, id=869951429979279401))
        case "🌉":
            await user.add_roles(discord.utils.get(user.guild.roles, id=869951533658292294))
        case "📋":
            await user.add_roles(discord.utils.get(user.guild.roles, id=869951838328328253))
        case "🔧":
            await user.add_roles(discord.utils.get(user.guild.roles, id=869952186560442478))
        case "⚡":
            await user.add_roles(discord.utils.get(user.guild.roles, id=869955325078417500))
        case "🔬":
            await user.add_roles(discord.utils.get(user.guild.roles, id=869955417302781993))
        case "💡":
            await user.add_roles(discord.utils.get(user.guild.roles, id=869955514547724358))
        case "🇪🇸":
            await user.add_roles(discord.utils.get(user.guild.roles, id=756149958276677683))
        case "🇬🇧":
            await user.add_roles(discord.utils.get(user.guild.roles, id=756149959434436680))

    await user.send("Rol añadido correctamente")


@bot.event
async def on_raw_reaction_remove(payload: discord.RawReactionActionEvent) -> None:
    guild = bot.get_guild(payload.guild_id)
    user = guild.get_member(payload.user_id)
    if payload.message_id not in [1408560477151432706, 1408560559531753623]:
        return

    if str(payload.emoji) not in ["🖥️", "📊", "📡", "🌉", "📋", "🔧", "⚡", "🔬", "💡", "🇪🇸", "🇬🇧"]:
        return

    match str(payload.emoji):
        case "️🖥️":
            await user.remove_roles(discord.utils.get(guild.roles, id=869949213348356116))
        case "📊":
            await user.remove_roles(discord.utils.get(guild.roles, id=869951347158569041))
        case "📡":
            await user.remove_roles(discord.utils.get(guild.roles, id=869951429979279401))
        case "🌉":
            await user.remove_roles(discord.utils.get(guild.roles, id=869951533658292294))
        case "📋":
            await user.remove_roles(discord.utils.get(guild.roles, id=869951838328328253))
        case "🔧":
            await user.remove_roles(discord.utils.get(guild.roles, id=869952186560442478))
        case "⚡":
            await user.remove_roles(discord.utils.get(guild.roles, id=869955325078417500))
        case "🔬":
            await user.remove_roles(discord.utils.get(guild.roles, id=869955417302781993))
        case "💡":
            await user.remove_roles(discord.utils.get(guild.roles, id=869955514547724358))
        case "🇪🇸":
            await user.remove_roles(discord.utils.get(guild.roles, id=756149958276677683))
        case "🇬🇧":
            await user.remove_roles(discord.utils.get(guild.roles, id=756149959434436680))

    await user.send("Rol quitado correctamente")

dotenv.load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
if BOT_TOKEN is None:
    raise Exception("BOT_TOKEN not found in .env")

if __name__ == "__main__":
    bot.run(BOT_TOKEN)  # Start the bot up