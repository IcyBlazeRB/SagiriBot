import discord
from discord.ext import commands
from jikanpy import AioJikan
import asyncio
from jikanpy import Jikan
import json
jikan = Jikan()

class anime(commands.Cog):

        def __init__(self, client):
                self.client = client

        @commands.command()
        async def anime(self, ctx, *, arg):
                async with AioJikan() as aio_jikan:
                        query = await aio_jikan.search(search_type='anime', query=arg)
                        
                        #Result 1
                        RS1T = query['results'][0]['title']
                        RS1ID = str(query['results'][0]['mal_id'])
                        RS1SC = str(query['results'][0]['score'])

                        #Result 2
                        RS2T = query['results'][1]['title']
                        RS2ID = str(query['results'][1]['mal_id'])
                        RS2SC = str(query['results'][1]['score'])

                        #Result 3
                        RS3T = query['results'][2]['title']
                        RS3ID = str(query['results'][2]['mal_id'])
                        RS3SC = str(query['results'][2]['score'])

                        #Result 4
                        RS4T = query['results'][3]['title']
                        RS4ID = str(query['results'][3]['mal_id'])
                        RS4SC = str(query['results'][3]['score'])

                        # Result 5
                        RS5T = query['results'][4]['title']
                        RS5ID = str(query['results'][4]['mal_id'])
                        RS5SC = str(query['results'][4]['score'])

                        embed=discord.Embed(title="Results from MAL for ``"+arg+"``!", color=0x00eeff)
                        embed.add_field(name="``#1`` - "+RS1ID, value=RS1T + " - "+RS1SC+"/10", inline=False)
                        embed.add_field(name="``#2`` - "+RS2ID, value=RS2T + " - "+RS2SC+"/10", inline=False)
                        embed.add_field(name="``#3`` - "+RS3ID, value=RS3T + " - "+RS3SC+"/10", inline=False)
                        embed.add_field(name="``#4`` - "+RS4ID, value=RS4T + " - "+RS4SC+"/10", inline=False)
                        embed.add_field(name="``#5`` - "+RS5ID, value=RS5T + " - "+RS5SC+"/10", inline=False)
                        embed.set_footer(text="All anime results are from myanimelist.net!", icon_url="https://image.myanimelist.net/ui/OK6W_koKDTOqqqLDbIoPAiC8a86sHufn_jOI-JGtoCQ")

                        Number_emojis=["1⃣","2⃣","3⃣","4⃣","5⃣"]
                        reactor = await ctx.send(embed=embed)
                        for i in Number_emojis:
                                await reactor.add_reaction(i)

                        def check(reaction, user):
                                return reaction.message.id == reactor.id and str(reaction.emoji) in Number_emojis and user == ctx.author


                        try:
                                reaction, user = await self.client.wait_for('reaction_add', timeout=60, check=check)
                        except asyncio.TimeoutError:
                                await discord.Message.delete(reactor)
                                return
                        else:
                                await discord.Message.delete(reactor)
                                if reaction.emoji == "1⃣":
                                        anime = jikan.anime(query['results'][0]['mal_id'])

                                        #Basic Information
                                        title=anime["title"]
                                        season=anime["premiered"]
                                        score=str(anime["score"])
                                        episodes=str(anime["episodes"])
                                        rank=str(anime["rank"])
                                        studio=anime["studios"][0]["name"]

                                        airing="Finished"
                                        if anime["airing"] == False:
                                                airing="Finished"
                                        else:
                                                airing="Airing"


                                        #Links
                                        Url=anime["url"]
                                        imgURL=anime["image_url"]

                                        #Genres
                                        genres = []
                                        g = anime["genres"]
                                        for i in anime["genres"]:
                                                genres.append(i["name"])
                                                

                                        g1 = str(genres)[1:-1]
                                        g2 = g1.replace("'","") 


                                        embed2=discord.Embed(title=title, url=Url, description=anime["synopsis"][:-25])
                                        embed2.set_image(url="{}".format(imgURL))
                                        embed2.add_field(name="Episodes", value=episodes, inline=True)
                                        embed2.add_field(name="Season", value=season, inline=True)
                                        embed2.add_field(name="Status", value=airing, inline=True)
                                        embed2.add_field(name="Studio", value=studio, inline=True)
                                        embed2.add_field(name="Score", value=score+"/10", inline=True)
                                        embed2.add_field(name="Rank", value=rank, inline=True)
                                        embed2.add_field(name="Genres", value=g2, inline=False)
                                        embed2.set_footer(text="All anime results are from myanimelist.net!", icon_url="https://image.myanimelist.net/ui/OK6W_koKDTOqqqLDbIoPAiC8a86sHufn_jOI-JGtoCQ")



                                        await ctx.send(embed=embed2)
                                elif reaction.emoji == "2⃣":
                                        anime = jikan.anime(query['results'][1]['mal_id'])

                                        #Basic Information
                                        title=anime["title"]
                                        season=anime["premiered"]
                                        score=str(anime["score"])
                                        episodes=str(anime["episodes"])
                                        rank=str(anime["rank"])
                                        studio=anime["studios"][0]["name"]

                                        airing="Finished"
                                        if anime["airing"] == False:
                                                airing="Finished"
                                        else:
                                                airing="Airing"


                                        #Links
                                        Url=anime["url"]
                                        imgURL=anime["image_url"]

                                        #Genres
                                        genres = []
                                        g = anime["genres"]
                                        for i in anime["genres"]:
                                                genres.append(i["name"])
                                                

                                        g1 = str(genres)[1:-1]
                                        g2 = g1.replace("'","") 


                                        embed2=discord.Embed(title=title, url=Url, description=anime["synopsis"][:-25])
                                        embed2.set_image(url="{}".format(imgURL))
                                        embed2.add_field(name="Episodes", value=episodes, inline=True)
                                        embed2.add_field(name="Season", value=season, inline=True)
                                        embed2.add_field(name="Status", value=airing, inline=True)
                                        embed2.add_field(name="Studio", value=studio, inline=True)
                                        embed2.add_field(name="Score", value=score+"/10", inline=True)
                                        embed2.add_field(name="Rank", value=rank, inline=True)
                                        embed2.add_field(name="Genres", value=g2, inline=False)
                                        embed2.set_footer(text="All anime results are from myanimelist.net!", icon_url="https://image.myanimelist.net/ui/OK6W_koKDTOqqqLDbIoPAiC8a86sHufn_jOI-JGtoCQ")



                                        await ctx.send(embed=embed2)
                                elif reaction.emoji == "3⃣":
                                        anime = jikan.anime(query['results'][2]['mal_id'])

                                        #Basic Information
                                        title=anime["title"]
                                        season=anime["premiered"]
                                        score=str(anime["score"])
                                        episodes=str(anime["episodes"])
                                        rank=str(anime["rank"])
                                        studio=anime["studios"][0]["name"]

                                        airing="Finished"
                                        if anime["airing"] == False:
                                                airing="Finished"
                                        else:
                                                airing="Airing"


                                        #Links
                                        Url=anime["url"]
                                        imgURL=anime["image_url"]

                                        #Genres
                                        genres = []
                                        g = anime["genres"]
                                        for i in anime["genres"]:
                                                genres.append(i["name"])
                                                

                                        g1 = str(genres)[1:-1]
                                        g2 = g1.replace("'","") 


                                        embed2=discord.Embed(title=title, url=Url, description=anime["synopsis"][:-25])
                                        embed2.set_image(url="{}".format(imgURL))
                                        embed2.add_field(name="Episodes", value=episodes, inline=True)
                                        embed2.add_field(name="Season", value=season, inline=True)
                                        embed2.add_field(name="Status", value=airing, inline=True)
                                        embed2.add_field(name="Studio", value=studio, inline=True)
                                        embed2.add_field(name="Score", value=score+"/10", inline=True)
                                        embed2.add_field(name="Rank", value=rank, inline=True)
                                        embed2.add_field(name="Genres", value=g2, inline=False)
                                        embed2.set_footer(text="All anime results are from myanimelist.net!", icon_url="https://image.myanimelist.net/ui/OK6W_koKDTOqqqLDbIoPAiC8a86sHufn_jOI-JGtoCQ")



                                        await ctx.send(embed=embed2)
                                elif reaction.emoji == "4⃣":
                                        anime = jikan.anime(query['results'][3]['mal_id'])

                                        #Basic Information
                                        title=anime["title"]
                                        season=anime["premiered"]
                                        score=str(anime["score"])
                                        episodes=str(anime["episodes"])
                                        rank=str(anime["rank"])
                                        studio=anime["studios"][0]["name"]

                                        airing="Finished"
                                        if anime["airing"] == False:
                                                airing="Finished"
                                        else:
                                                airing="Airing"


                                        #Links
                                        Url=anime["url"]
                                        imgURL=anime["image_url"]

                                        #Genres
                                        genres = []
                                        g = anime["genres"]
                                        for i in anime["genres"]:
                                                genres.append(i["name"])
                                                

                                        g1 = str(genres)[1:-1]
                                        g2 = g1.replace("'","") 


                                        embed2=discord.Embed(title=title, url=Url, description=anime["synopsis"][:-25])
                                        embed2.set_image(url="{}".format(imgURL))
                                        embed2.add_field(name="Episodes", value=episodes, inline=True)
                                        embed2.add_field(name="Season", value=season, inline=True)
                                        embed2.add_field(name="Status", value=airing, inline=True)
                                        embed2.add_field(name="Studio", value=studio, inline=True)
                                        embed2.add_field(name="Score", value=score+"/10", inline=True)
                                        embed2.add_field(name="Rank", value=rank, inline=True)
                                        embed2.add_field(name="Genres", value=g2, inline=False)
                                        embed2.set_footer(text="All anime results are from myanimelist.net!", icon_url="https://image.myanimelist.net/ui/OK6W_koKDTOqqqLDbIoPAiC8a86sHufn_jOI-JGtoCQ")

                                        await ctx.send(embed=embed2)
                                elif reaction.emoji == "5⃣":
                                        anime = jikan.anime(query['results'][4]['mal_id'])

                                        #Basic Information
                                        title=anime["title"]
                                        season=anime["premiered"]
                                        score=str(anime["score"])
                                        episodes=str(anime["episodes"])
                                        rank=str(anime["rank"])
                                        studio=anime["studios"][0]["name"]

                                        airing="Finished"
                                        if anime["airing"] == False:
                                                airing="Finished"
                                        else:
                                                airing="Airing"


                                        #Links
                                        Url=anime["url"]
                                        imgURL=anime["image_url"]

                                        #Genres
                                        genres = []
                                        g = anime["genres"]
                                        for i in anime["genres"]:
                                                genres.append(i["name"])
                                                

                                        g1 = str(genres)[1:-1]
                                        g2 = g1.replace("'","") 


                                        embed2=discord.Embed(title=title, url=Url, description=anime["synopsis"][:-25])
                                        embed2.set_image(url="{}".format(imgURL))
                                        embed2.add_field(name="Episodes", value=episodes, inline=True)
                                        embed2.add_field(name="Season", value=season, inline=True)
                                        embed2.add_field(name="Status", value=airing, inline=True)
                                        embed2.add_field(name="Studio", value=studio, inline=True)
                                        embed2.add_field(name="Score", value=score+"/10", inline=True)
                                        embed2.add_field(name="Rank", value=rank, inline=True)
                                        embed2.add_field(name="Genres", value=g2, inline=False)
                                        embed2.set_footer(text="All anime results are from myanimelist.net!", icon_url="https://image.myanimelist.net/ui/OK6W_koKDTOqqqLDbIoPAiC8a86sHufn_jOI-JGtoCQ")

                                        await ctx.send(embed=embed2)
                                       

        @commands.command()
        async def manga(self, ctx, *, arg):
                async with AioJikan() as aio_jikan:
                        query = await aio_jikan.search(search_type='manga', query=arg)
                        
                        #Result 1
                        RS1T = query['results'][0]['title']
                        RS1ID = str(query['results'][0]['mal_id'])
                        RS1SC = str(query['results'][0]['score'])

                        #Result 2
                        RS2T = query['results'][1]['title']
                        RS2ID = str(query['results'][1]['mal_id'])
                        RS2SC = str(query['results'][1]['score'])

                        #Result 3
                        RS3T = query['results'][2]['title']
                        RS3ID = str(query['results'][2]['mal_id'])
                        RS3SC = str(query['results'][2]['score'])

                        #Result 4
                        RS4T = query['results'][3]['title']
                        RS4ID = str(query['results'][3]['mal_id'])
                        RS4SC = str(query['results'][3]['score'])

                        # Result 5
                        RS5T = query['results'][4]['title']
                        RS5ID = str(query['results'][4]['mal_id'])
                        RS5SC = str(query['results'][4]['score'])

                        embed=discord.Embed(title="Results from MAL for ``"+arg+"``!", color=0x00eeff)
                        embed.add_field(name="``#1`` - "+RS1ID, value=RS1T + " - "+RS1SC+"/10", inline=False)
                        embed.add_field(name="``#2`` - "+RS2ID, value=RS2T + " - "+RS2SC+"/10", inline=False)
                        embed.add_field(name="``#3`` - "+RS3ID, value=RS3T + " - "+RS3SC+"/10", inline=False)
                        embed.add_field(name="``#4`` - "+RS4ID, value=RS4T + " - "+RS4SC+"/10", inline=False)
                        embed.add_field(name="``#5`` - "+RS5ID, value=RS5T + " - "+RS5SC+"/10", inline=False)
                        embed.set_footer(text="All results come from myanimelist.net!")

                        Number_emojis=["1⃣","2⃣","3⃣","4⃣","5⃣"]
                        reactor = await ctx.send(embed=embed)
                        for i in Number_emojis:
                                await reactor.add_reaction(i)


        

def setup(client):
        client.add_cog(anime(client))