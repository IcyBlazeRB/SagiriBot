import discord
import qrcode
from discord.ext import commands
import os
import time
import json



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

def setup(client):
        client.add_cog(useful(client))