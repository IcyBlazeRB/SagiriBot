import discord
import qrcode
from discord.ext import commands
import os
import time
import json
import random
import ast
from gtts import gTTS


def insert_returns(body):
    # insert return stmt if the last expression is a expression statement
    if isinstance(body[-1], ast.Expr):
        body[-1] = ast.Return(body[-1].value)
        ast.fix_missing_locations(body[-1])

    # for if statements, we insert returns into the body and the orelse
    if isinstance(body[-1], ast.If):
        insert_returns(body[-1].body)
        insert_returns(body[-1].orelse)

    # for with blocks, again we insert returns into the body
    if isinstance(body[-1], ast.With):
        insert_returns(body[-1].body)




class useful(commands.Cog):

        def __init__(self, client):
                self.client = client

        @commands.command()
        async def ping(self, ctx):
                await ctx.send(f'Pong! In {round(self.client.latency * 1000)}ms!')
                
        @commands.command()
        async def say(self, ctx, *, arg):
                await ctx.send(arg)
        
        @commands.command()
        async def tts(self, ctx, *, arg):
                tts = gTTS(arg)
                tts.save('TTS.mp3')
                audio = discord.File("TTS.mp3")
                await ctx.send(
                        "Here is what you said!",
                        file=audio
                )
                os.remove("TTS.mp3")


        @commands.command()
        async def avatar(self, ctx, member: discord.Member=None):  
                if not member:
                        member = ctx.message.author
                show_avatar = discord.Embed(description="[Avatar URL](%s)" % member.avatar_url)
                show_avatar.set_image(url="{}".format(member.avatar_url))
                show_avatar.set_footer(text=f'{member}')
                await ctx.send(embed=show_avatar)


        @commands.command()
        async def qrcode(self, ctx, *, arg):
                qr = qrcode.QRCode(
                        version=1,
                        box_size=15,
                        border=5
                        )
                data = arg
                qr.add_data(data)
                qr.make(fit=True)
                img = qr.make_image(fill="black", back_color="white")
                img.save("qrcode.png")
                embed=discord.Embed(title="QRCode for "+arg)
                embed.set_image(
                url="attachment://qrcode.png"
                )
                image = discord.File("qrcode.png")
                await ctx.send(
                        embed=embed,
                        file=image
                )
                os.remove("qrcode.png")
        
        @commands.command()
        async def membercount(self, ctx):
                embed=discord.Embed(title="Member Count for " + ctx.message.guild.name, description=ctx.message.guild.member_count, color=0xf143e0)
                embed.set_thumbnail(url=ctx.message.guild.icon_url)
                await ctx.send(embed=embed)

        @commands.command()
        @commands.has_permissions(administrator=True) 
        async def setprefix(self, ctx, prefix):
                with open("prefixes.json","r") as f:
                        prefixes = json.load(f)
                
                prefixes[str(ctx.guild.id)] = prefix

                with open("prefixes.json","w") as f:
                        json.dump(prefixes, f, indent=4)

                embed=discord.Embed(title="The servers prefix has been changed to: " + "``" + prefix + "``", color=0xae00d1)
                await ctx.send(embed=embed)


        @commands.command()
        async def prefix(self, ctx):
                with open("prefixes.json","r") as f:
                        prefixes = json.load(f)

                embed=discord.Embed(title="Current prefix for the server is: " + "``"+prefixes[str(ctx.guild.id)]+"``", color=0xae00d1)
                await ctx.send(embed=embed)

        @commands.command()
        async def invite(self, ctx):
                embed=discord.Embed(title="Click here to invite me!", url="https://discord.com/oauth2/authorize?client_id=566852738345074689&scope=bot&permissions=8")
                await ctx.send(embed=embed)

        
        

        @commands.command()
        async def help(self, ctx):
                embed1=discord.Embed(title="Moderation Commands", color=0xd100ca)
                embed1.add_field(name="Warn [member] [reason]", value="Will warn the player.", inline=False)
                embed1.add_field(name="Kick [member] [reason]", value="Will kick the player.", inline=False)
                embed1.add_field(name="Ban [member] [reason]", value="Will ban the player.", inline=False)
                embed1.add_field(name="Purge [num]", value="Will bulk delete messages.", inline=False)
                embed1.add_field(name="Setprefix [prefix]", value="Will server prefix.", inline=False)
                embed1.add_field(name="Reload [cog]", value="Dev use only.", inline=False)
                embed1.set_footer(text="Note: Most of these commands require permissions")
                embed2=discord.Embed(title="Useful Commands", color=0xd100ca)
                embed2.add_field(name="QRcode [link]", value="Will return a qrcode.", inline=False)
                embed2.add_field(name="Ping", value="Will return bot's latency.", inline=False)
                embed2.add_field(name="Avatar [user]", value="Will return users avatar.", inline=False)
                embed2.add_field(name="MemberCount", value="Will return servers member count.", inline=False)
                embed2.add_field(name="Prefix", value="Will return servers prefix.", inline=False)
                embed2.add_field(name="Say [arg]", value="Will repeat anything you type.", inline=False)
                embed2.add_field(name="Help", value="I think you know.", inline=False)
                embed2.add_field(name="Invite", value="Will give you bots invite link.", inline=False)
                embed2.set_footer(text="Note: Most of these commands require permissions!")
                embed3=discord.Embed(title="Fun Commands", color=0xd100ca)
                embed3.add_field(name="Die", value="Will role a die.", inline=False)
                embed3.add_field(name="Flip", value="Will flip a coin.", inline=False)
                embed3.add_field(name="Fortune", value="Will tell your fortune.", inline=False)
                embed3.add_field(name="Cat", value="Kawaii Neko Images!!! 😸", inline=False)
                embed3.set_footer(text="Note: Most of these commands require permissions!")
                embed4=discord.Embed(title="Anime Commands", color=0xd100ca)
                embed4.add_field(name="Anime", value="Will search MAL database for specified anime.", inline=False)
                embed4.add_field(name="Doujin", value="Will return doujin of specified ID.", inline=False)
                embed4.add_field(name="rDoujin", value="Will return a random doujin from NHentai.", inline=False)
                embed4.set_footer(text="Note: Some of these commands are restricted to NSFW channels.")
                await ctx.message.author.send(embed=embed1)
                await ctx.message.author.send(embed=embed2)
                await ctx.message.author.send(embed=embed3)
                await ctx.message.author.send(embed=embed4)
                await ctx.send("📫 **Check your dms!**")

def setup(client):
        client.add_cog(useful(client))
