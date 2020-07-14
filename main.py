import discord
import os
import json
from discord.ext import commands



def get_prefix(client, message):
        if not message.guild:
                return commands.when_mentioned_or("uwu ")(client, message)

        with open("prefixes.json","r") as f:
                prefixes = json.load(f)
        
        return prefixes[str(message.guild.id)]

client = commands.Bot(command_prefix=get_prefix and commands.when_mentioned_or("owo ")) 
client.remove_command("help")

@client.event
async def on_guild_join(guild):
        with open("prefixes.json","r") as f:
                prefixes = json.load(f)
        
        prefixes[str(guild.id)] = "uwu "

        with open("prefixes.json","w") as f:
                json.dump(prefixes, f, indent=4)

@client.event
async def on_guild_remove(guild):
        with open("prefixes.json","r") as f:
                prefixes = json.load(f)
        
        prefixes.pop(str(guild.id))

        with open("prefixes.json","w") as f:
                json.dump(prefixes, f, indent=4)

@client.command()
async def reload(ctx, extension):
        if ctx.message.author.id == 261249219812261888:
                client.unload_extension(f'cogs.{extension}')
                client.load_extension(f'cogs.{extension}')
                await ctx.send("Cog Reloaded!")
        else:
                await ctx.send("Unable to do that, as you're not the bot owner!")

@client.command()
async def load(ctx, extension):
        if ctx.message.author.id == 261249219812261888:
                client.load_extension(f'cogs.{extension}')
                await ctx.send("Cog Loaded!")
        else:
                await ctx.send("Unable to do that, as you're not the bot owner!")

@client.command()
async def unload(ctx, extension):
        if ctx.message.author.id == 261249219812261888:
                client.unload_extension(f'cogs.{extension}')
                await ctx.send("Cog Unloaded!")
        else:
                await ctx.send("Unable to do that, as you're not the bot owner!")


for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
                client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv("TOKEN"))

