import discord
from discord.ext import commands
import asyncio

def is_invalid_nickname(string):
    print(f"6 Found user nick, checking rules: {string}")
    invisible_chars = set(["\u200B", "\u200C", "\u200D", "\u2060", "\u180E", "\uFEFF", "᲼"])
    if any(char in invisible_chars for char in string):
        return True
    if all(char == '.' for char in string):
        return True
    return False


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

async def check_member_nickname(member):
    await asyncio.sleep(5)  # Wait for 5 seconds before checking the nickname

    if member.nick is None:
        # If the user has cleared their nickname, set it to their original profile username
        print(f"1 Setting nickname for {member.name}#{member.discriminator}")
        if not member.name.isspace() and not is_invalid_nickname(member.name):
            await member.edit(nick=member.name)  # Set the nickname to the original profile username if it's valid
            print(f"7 Changed to profile username: {member.name}")
        else:
            no_nick_name = f"No-Nick-{member.discriminator}"
            await member.edit(nick=no_nick_name)
            print(f"8 Changed to {no_nick_name}")
    elif member.nick.isspace() or is_invalid_nickname(member.nick):
        print(f"3 Setting nickname for {member.name}#{member.discriminator}")
        if not member.name.isspace() and not is_invalid_nickname(member.name):
            await member.edit(nick=member.name)  # Set the nickname to the original profile username if it's valid
            print(f"4 Changed to profile username: {member.name}")
        else:
            no_nick_name = f"No-Nick-{member.discriminator}"
            await member.edit(nick=no_nick_name)
            print(f"5 Changed to {no_nick_name}")

    unverified_role = discord.utils.get(member.guild.roles, name="Unverified")
    if unverified_role:
        await member.remove_roles(unverified_role)


@bot.event
async def on_ready():
    print(f"{bot.user.name} is now online!")

@bot.event
async def on_member_join(member):
    await check_member_nickname(member)

@bot.event
async def on_member_update(before, after):
    if (not after.nick or after.nick.isspace() or is_invalid_nickname(after.nick)) and (before.nick != after.nick):
        await check_member_nickname(after)
        
@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        await check_member_nickname(member)


bot.run("YOUR_BOT_TOKEN")