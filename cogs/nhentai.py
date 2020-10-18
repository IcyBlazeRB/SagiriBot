import discord
from discord.ext import commands
from hentai import Hentai, Format, Utils, Sort

class nhentai(commands.Cog):

        def __init__(self, client):
                self.client = client


        @commands.command(aliases=['douj','d'])
        async def doujin(self, ctx, *, args):
                if ctx.channel.is_nsfw():
                        doujin = Hentai(int(args))


                        title = doujin.title(Format.Pretty)

                        artist = doujin.artist
                        artl = []
                        for i in artist: 
                                artl.append(i.name + " (" + str(i.count) + ")")

                        alan = str(artl)[1:-1]
                        alan2 = alan.replace("'","")
                        alan3 = alan2.replace(",","\n")

                        uploaddate = doujin.upload_date
                        utags = str([tag.name for tag in doujin.tag])[1:-1] 
                        tags = utags.replace("'","")
                        pages = doujin.num_pages
                        languages = doujin.language
                        lanlist = []
                        for i in languages: 
                                lanlist.append(i.name + " (" + str(i.count) + ")")

                        flan = str(lanlist)[1:-1]
                        flan2 = flan.replace("'","")
                        flan3 = flan2.replace(",","\n")




                        
                        embed=discord.Embed(title=title, url=doujin.url, color=0xff0095)
                        embed.set_image(url="{}".format(doujin.thumbnail))
                        embed.add_field(name="Artist:", value=alan3, inline=True)
                        embed.add_field(name="Pages:", value=pages, inline=True)
                        embed.add_field(name="Languages:", value=flan3, inline=True)
                        embed.add_field(name="Uploaded on:", value=str(uploaddate)[:-9], inline=True)
                        embed.add_field(name="Tags:", value=tags, inline=False)
                        embed.set_footer(text="All Doujin are sourced from nhentai.to!", icon_url="https://i.imgur.com/uLAimaY.png")
                        await ctx.send(embed=embed)

                else:
                        embed=discord.Embed(color=0xf50000)
                        embed.add_field(name="ERROR:", value="Unable to use this commad in non NSFW channels.\nPlease use this command in NSFW channels.", inline=False)
                        await ctx.send(embed=embed)

        @doujin.error
        async def doujin_error(self, ctx, error):
                if isinstance(error, commands.MissingRequiredArgument):
                        embed=discord.Embed(color=0xf50000)
                        embed.add_field(name="ERROR:", value="You are missing required argments.\nCorrect Ussage: ``uwu doujin [doujin number]``!", inline=False)
                        await ctx.send(embed=embed)   

        @commands.command(aliases=['rdouj','rd'])
        async def randomdoujin(self, ctx):
                if ctx.channel.is_nsfw():
                        rid = Utils.get_random_id()
                        print(rid)
                        doujin = Hentai(rid)

                        title = doujin.title(Format.Pretty)

                        artist = doujin.artist
                        artl = []
                        for i in artist: 
                                artl.append(i.name + " (" + str(i.count) + ")")

                        alan = str(artl)[1:-1]
                        alan2 = alan.replace("'","")
                        alan3 = alan2.replace(",","\n")

                        uploaddate = doujin.upload_date
                        utags = str([tag.name for tag in doujin.tag])[1:-1] 
                        tags = utags.replace("'","")
                        pages = doujin.num_pages
                        languages = doujin.language
                        lanlist = []
                        for i in languages: 
                                lanlist.append(i.name + " (" + str(i.count) + ")")

                        flan = str(lanlist)[1:-1]
                        flan2 = flan.replace("'","")
                        flan3 = flan2.replace(",","\n")
                        
                        embed=discord.Embed(color=0xff0095)
                        embed=discord.Embed(title=title, url=doujin.url, color=0xff0095)
                        embed.set_image(url="{}".format(doujin.thumbnail))
                        embed.add_field(name="Artist:", value=alan3, inline=True)
                        embed.add_field(name="Pages:", value=pages, inline=True)
                        embed.add_field(name="Languages:", value=flan3, inline=True)
                        embed.add_field(name="Uploaded on:", value=str(uploaddate)[:-9], inline=True)
                        embed.add_field(name="Tags:", value=tags, inline=False)
                        embed.set_footer(text="All Doujin are sourced from nhentai.to!", icon_url="https://i.imgur.com/uLAimaY.png")
                        await ctx.send(embed=embed)
                else:
                        embed=discord.Embed(color=0xf50000)
                        embed.add_field(name="ERROR:", value="Unable to use this commad in non NSFW channels.\nPlease use this command in NSFW channels.", inline=False)
                        await ctx.send(embed=embed)
      
        

        

def setup(client):
        client.add_cog(nhentai(client))