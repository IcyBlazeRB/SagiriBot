import discord
from discord.ext import commands
import json

class onready(commands.Cog):

        def __init__(self, client):
                self.client = client

        @commands.command()
        @commands.has_permissions(manage_messages=True)
        async def warn(self, ctx, member: discord.Member=None, *, args):  
                if not member:
                        await ctx.send("``Failed to provide user.``")
                embed=discord.Embed(title="You have recieved a warning on " + ctx.message.guild.name, color=0xeb0000)
                embed.add_field(name="Warned by:", value=ctx.message.author, inline=True)
                embed.add_field(name="Reason:", value=args, inline=True)
                embed.set_thumbnail(url=ctx.message.guild.icon_url)
                await ctx.send(f'**<@!{member.id}>' + " has been warned!**")
                await member.send(embed=embed)

        @warn.error
        async def warn_error(self, ctx, error):
                if isinstance(error, commands.MissingRequiredArgument):
                        await ctx.send("**You are missing an argument. Correct format ``'uwu warn [user] [reason]'``.**")
                if isinstance(error, commands.MissingPermissions):
                        await ctx.send("**You are missing the required permissions.**")
        
        

                


        

def setup(client):
        client.add_cog(onready(client))