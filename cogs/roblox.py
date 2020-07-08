import discord
from discord.ext import commands
import robloxapi, asyncio
import random
import json
sart = robloxapi.Client()
import sqlite3

        

#def commit():




class roblox(commands.Cog):

        def __init__(self, client):
                self.client = client

        @commands.command()
        async def robloxinfo(self, ctx, *, args):
                ira = await sart.get_user_by_username(args)     
                dbid = ira.id

                connect = sqlite3.connect("roblox.db")
                c = connect.cursor()
                c.execute("SELECT * FROM users WHERE robloxid = ?", (dbid,))
                data = c.fetchall()
                
                drid = "No Bind"

                for row in data:
                        drid=str(row[1])
                
                detailed = await ira.get_detailed_user()
                friends = await ira.get_friends()
                fira = await sart.get_user_by_username(ira.name)

                rig = "Guest"
                members = []
                grape = await sart.get_group(6814798)
                async for member in grape.get_members():
                        members.append(member.name)
                if args in members:
                        rig = await fira.get_role_in_group(6814798)
                        rig = rig.name
                embed=discord.Embed(title="Roblox Info", color=0xd90d0d)
                embed.set_thumbnail(url="http://www.roblox.com/Thumbs/Avatar.ashx?x=150&y=150&Format=Png&username="+args)
                embed.add_field(name="Username", value=str(ira.name), inline=True)
                embed.add_field(name="UserID", value=str(ira.id), inline=True)
                embed.add_field(name="Group Role", value=rig, inline=True)
                embed.add_field(name="Join Date", value=detailed.join_date, inline=True)
                embed.add_field(name="Friends", value=str(len(friends)), inline=True)
                embed.add_field(name="Discord", value="<@!"+drid+">", inline=True)

                await ctx.send(embed=embed)

        @commands.command()
        async def bind(self, ctx):
                #Important Variables
                user = ctx.message.author
                uid = user.id
                channel = ctx.message.channel

                connect = sqlite3.connect("roblox.db")
                c = connect.cursor()
                c.execute("SELECT * FROM users WHERE discordid = ?", (uid,))
                data = c.fetchall()

                if len(data,) == 0:
                        embed=discord.Embed(title="Hello, too continue please enter your roblox username!", color=0xd90d0d)
                        

                        verification_codes = [
                                "donkey monkey donkey donkey",
                                "moon sun moon mars",
                                "cars trucks boats cars",
                                "goats are goats which goats are not"
                        ]

                        verifier = random.choice(verification_codes)

                        #send embed
                        await ctx.send(embed=embed)
                        
                        #check command
                        def check(m):
                                return m.author == user and m.channel == channel

                        #message checker function
                        try:
                                msg = await self.client.wait_for('message', check=check, timeout=60.0)
                        except asyncio.TimeoutError:
                                return await ctx.message.author.dm_channel.send("Sorry you took too long. Try again.")

                        #confirmation embed
                        ira = await sart.get_user_by_username(msg.content)

                        c.execute("SELECT * FROM users WHERE robloxid = ?", (ira.id,))
                        rdata = c.fetchall()

                        if len(rdata) > 0:
                                await ctx.send("**Error:** You are already in the system.")
                        else:
                                embed2 = discord.Embed(title="Is this the roblox account?", description="If so reply, ``yes``. Else reply, ``no``.",  url="https://www.roblox.com/users/"+str(ira.id)+"/profile")
                                embed2.set_image(url="http://www.roblox.com/Thumbs/Avatar.ashx?x=150&y=150&Format=Png&username="+ira.name)
                                await ctx.send(embed=embed2)
                        
                        #confirmation check
                        try:
                                msg = await self.client.wait_for('message', check=check, timeout=30.0)
                        except asyncio.TimeoutError:
                                return await ctx.message.author.dm_channel.send("Sorry you took too long. Try again.")
                        
                        #confirmation continue
                        if msg.content == "yes":
                                embed3 = discord.Embed(title="Please add the following to your blurb, so we can verify your account.", description="``"+verifier+"`` then type ``done`` when you are done.")
                                await ctx.send(embed=embed3)
                                try:
                                        dmsg = await self.client.wait_for('message', check=check, timeout=120.0)
                                except asyncio.TimeoutError:
                                        return await ctx.message.author.dm_channel.send("Sorry you took too long. Try again.")
                                
                                if dmsg.content == "done":
                                        detailed = await ira.get_detailed_user()
                                        if detailed.blurb == verifier:
                                                await ctx.send("Awesome, you are now verified!")
                                                c.execute("INSERT INTO users (discordid,robloxid) VALUES (?,?)", (uid, ira.id),)
                                                connect.commit()
                                                connect.close()
                                                
                                        else:
                                                await ctx.send("Failed to find the verification code in your about section, please try again.")        

                        elif msg.content == "no":
                                await ctx.send("**Please try again.**")
                else:
                        ctx.send("**Error:** ``Found in database!``")


def setup(client):
        client.add_cog(roblox(client))
