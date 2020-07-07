import discord
from discord.ext import commands
import json

class moderation(commands.Cog):

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
        

        @commands.command()
        @commands.has_permissions(kick_members=True)
        async def kick(self, ctx, member: discord.Member=None, *, args):  
                if not member:
                        await ctx.send("``Failed to provide user.``")
                embed=discord.Embed(title="You have been kicked from " + ctx.message.guild.name, color=0xeb0000)
                embed.add_field(name="Kicked by:", value=ctx.message.author, inline=True)
                embed.add_field(name="Reason:", value=args, inline=True)
                embed.set_thumbnail(url=ctx.message.guild.icon_url)
                await ctx.send(f'**<@!{member.id}>' + " has been kicked!**")
                await member.send(embed=embed)
                await member.kick()

        @kick.error
        async def kick_error(self, ctx, error):
                if isinstance(error, commands.MissingRequiredArgument):
                        await ctx.send("**You are missing an argument. Correct format ``'uwu warn [user] [reason]'``.**")
                if isinstance(error, commands.MissingPermissions):
                        await ctx.send("**You are missing the required permissions, or the user you are attempting to kick is higher then me.**")

        @commands.command()
        @commands.has_permissions(ban_members=True)
        async def ban(self, ctx, member: discord.Member=None, *, args):  
                if not member:
                        await ctx.send("``Failed to provide user.``")
                embed=discord.Embed(title="You have been banned from " + ctx.message.guild.name, color=0xeb0000)
                embed.add_field(name="Banned by:", value=ctx.message.author, inline=True)
                embed.add_field(name="Reason:", value=args, inline=True)
                embed.set_thumbnail(url=ctx.message.guild.icon_url)
                await ctx.send(f'**<@!{member.id}>' + " has been banned!**")
                await member.send(embed=embed)
                await member.ban()

        @ban.error
        async def ban_error(self, ctx, error):
                if isinstance(error, commands.MissingRequiredArgument):
                        await ctx.send("**You are missing an argument. Correct format ``'uwu warn [user] [reason]'``.**")
                if isinstance(error, commands.MissingPermissions):
                        await ctx.send("**You are missing the required permissions, or the user you are attempting to kick is higher then me.**")


                        

                


        

def setup(client):
        client.add_cog(moderation(client))
