import discord
from discord.ext import commands
import robloxapi, asyncio
import random
import json
sart = robloxapi.Client()
    



class roblox(commands.Cog):

        def __init__(self, client):
                self.client = client

        @commands.command()
        async def robloxinfo(self, ctx, *, args):
                ira = await sart.get_user_by_username(args)
                rig = "Guest"
                members = []
                grape = await sart.get_group(6814798)
                async for member in grape.get_members():
                        members.append(member.name)
                if args in members:
                        rig = await ira.get_role_in_group(6814798)
                        rig = rig.name
                embed=discord.Embed(title="Roblox Info")
                embed.set_thumbnail(url="http://www.roblox.com/Thumbs/Avatar.ashx?x=150&y=150&Format=Png&username="+args)
                embed.add_field(name="Username", value=str(ira.name), inline=True)
                embed.add_field(name="UserID", value=str(ira.id), inline=True)
                embed.add_field(name="Group Role", value=rig, inline=True)
                embed.add_field(name="Discord", value="Not Found", inline=True)
                await ctx.send(embed=embed)

def setup(client):
        client.add_cog(roblox(client))
