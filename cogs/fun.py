import discord
from discord.ext import commands
import random

class fun(commands.Cog):

        def __init__(self, client):
                self.client = client

        @commands.command()
        async def fortune(self, ctx):
                responses = [
                        'It is certain.',
                        'It is decidedly so.',
                        'As I see it, yes.',
                        'Ask again later.',
                        'Better not tell you now.',
                        'Cannot predict now.',
                        'Concentrate and ask again',
                        'It is certain.',
                        "Don't count on it.",
                        "Most likely.",
                        "My reply is no.",
                        "My sources say no.",
                        "Outlook not so good.",
                        "Outlook good.",
                        "Reply hazy, try again.",
                        "Signs point to yes.",
                        "Very Doubtful!",
                        "Without a doubt!",
                        "Yes.",
                        "Yes - definitely.",
                        "You may rel on it."
                ]
                choice = random.choice(responses)
                embed=discord.Embed(title="Fortune Teller", description=choice, color=0xa700bd)
                embed.set_thumbnail(url="https://www.emojibase.com/resources/img/emojis/apple/1f52e.png")
                embed.set_footer(text="Fortune Teller Sagiri 🔮")
                await ctx.send(embed=embed)

        @commands.command()
        async def die(self, ctx, *num):
                if num:
                        if num.isnumeric():
                                die = random.randint(1,int(num))
                                await ctx.send("I rolled a " + str(die))
                        else:
                                await ctx.send("Failed to provide a valid argument!")

                elif not num:
                        die = random.randint(1,6)
                        await ctx.send("I rolled a " + str(die))

        @commands.command()
        async def flip(self,ctx):
                options = ["The coin landed on Heads!","The coin landed on Tails!","Wow, whats the chances? The coin landed it on its side!"]
                distirbution = [0.495, 0.495, 0.01]
                choice = str(random.choices(options, distirbution))
                schoice = choice[2:-2:]
                embed=discord.Embed(title="Results of the coinflip:", description=schoice, color=0xa700bd)
                await ctx.send(embed=embed)





def setup(client):
        client.add_cog(fun(client))