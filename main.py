import discord
from discord.ext import commands
import random
from compounding import Compounding as cmp
from datetime import datetime

API_KEY = "MTI5NzgxODI4OTA2NTU1ODAxNw.GZu2DP.yY89oYlpAjqNnBCyM1Pj7cg9zTY8LARps4Mua4"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

db = dict()
dbIndex = 0

gamedb = dict()
gameDbIndex = 0

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')




#$help
@bot.command(name='compounding-help')
async def help_command(ctx):
    global dbIndex
    db[dbIndex] = {"command": "help", "user":str(ctx.author.name), "channel":str(ctx.channel.name), "time" : datetime.now()}
    dbIndex += 1
    embed = discord.Embed(
        title="Welcome to the Compounding Server!",
        description="Here are some of the starter commands:",
        color=discord.Color.blue()
    )
    embed.add_field(
        name="$simple_compounding [initial] [years] [annual_percentage]",
        value="Calculates the compounded value of an initial investment after a given number of years with a specific annual growth percentage.",
        inline=False
    )
    embed.add_field(
        name="$rule72",
        value="A little game based on fast mental approximation to get the compounded value over the years. To do it, assume the annual compound rate is 7.2%, a conservative number. The value will double in 10 years with that compound rate, making it easy for fast approximation of future value of an investment.",
        inline=False
    )
    embed.add_field(
        name="$dca",
        value="Calculates the results of Dollar Cost Averaging (DCA), taking into account an initial investment, monthly recurring investment, years elapsed, and annual growth.",
        inline=False
    )

    await ctx.send(embed=embed)

#$example
@bot.command(name='example')
async def example_command(ctx):
    global dbIndex
    db[dbIndex] = {"command": "example", "user":str(ctx.author.name), "channel":str(ctx.channel.name), "time" : datetime.now()}
    dbIndex += 1
    print(db)
    await ctx.send(f"Hello {ctx.author.name}! This message was sent in {ctx.channel.name}.")

#$calculate_compounding 1000 10 0.04
@bot.command(name='simple_compounding')
async def calculate_compounding(ctx, initial: float, years: int, annual_percentage: float):
    global dbIndex
    db[dbIndex] = {"command": "simple_compounding", "user":str(ctx.author.name), "channel":str(ctx.channel.name), "time" : datetime.now()}
    dbIndex += 1
    compounded = initial * ((1 + annual_percentage / 100) ** years)
    await ctx.send(f"After {years} years at {annual_percentage}% annual growth, your investment will be worth ${compounded:.2f}.")

#$rule72
@bot.command(name='rule72')
async def rule72(ctx):
    global dbIndex
    db[dbIndex] = {"command": "rule72", "user":str(ctx.author.name), "channel":str(ctx.channel.name), "time" : datetime.now()}
    dbIndex += 1
    again = True
    while again:
        times = [x for x in range(10, 101, 10)]
        amount = [x for x in range(1000, 10001, 1000)]
        years = random.choice(times)
        moneys = random.choice(amount)
        compounded = moneys * ((1 + 0.072) ** years)

        await ctx.send(f"You have ${moneys} which compounds over {years} years. Guess the compounded amount:")

        def check(m):
            return m.author == ctx.author and m.content.isnumeric()

        msg = await bot.wait_for('message', check=check)
        guess = float(msg.content)

        point = 0
        point = 1 if abs(int(compounded - guess)) < int(compounded)*0.05 else 0
        global gameDbIndex
        gamedb[gameDbIndex] = point
        gameDbIndex +=1
        print(gamedb)

        await ctx.send(
            f"{'You gained a point' if point == 1 else 'You didnt gain a point'} "
            f"The compounded amount was ${round(compounded, 2)}.\n"
            f"Your guess was ${guess:.2f}, which was {round(compounded - guess, 2)} off.\n"
            f"Your total amount of points is {len([1 for x in range(len(gamedb)) if gamedb[x] == 1])}"
        )

        await ctx.send(f"Do you want to continue? (y / n)")

        def check(m):
            return m.author == ctx.author and m.content.lower() in ['y', 'n']

        msg = await bot.wait_for('message', check=check)
        if msg.content.lower() != "y":
            break

@bot.command(name='dca')
async def dca_command(ctx):
    global dbIndex
    db[dbIndex] = {"command": "dca", "user":str(ctx.author.name), "channel":str(ctx.channel.name), "time" : datetime.now()}
    dbIndex += 1
    def check(m):
        return m.author == ctx.author and m.content.isnumeric()

    await ctx.send(f"What is the initial amount you invested?")
    initial_msg = await bot.wait_for('message', check=check)
    initial = int(initial_msg.content)

    await ctx.send(f"What is the recurring amount you invested per month?")
    recurring_msg = await bot.wait_for('message', check=check)
    recurring = int(recurring_msg.content)

    await ctx.send(f"How many years have elapsed since you invested the initial amount?")
    years_msg = await bot.wait_for('message', check=check)
    years = int(years_msg.content)

    await ctx.send(f"What is the average annual percentage of growth?")
    perc_msg = await bot.wait_for('message', check=check)
    perc = float(perc_msg.content) / 100

    investment = cmp(initial, recurring, years, perc)
    results = investment.string_part()

    await ctx.send(
        f"Your investment details:\n"
        f"Initial Investment: ${initial}\n"
        f"Monthly Recurring: ${recurring}\n"
        f"Duration: {years} years\n"
        f"Annual Growth Rate: {perc*100}%\n\n"
        f"**Results**:\n"
        f"Principal: ${results['principal']:.2f}\n"
        f"Final Amount: ${results['final']:.2f}\n"
        f"ROI: {results['roi']:.2f}%"
    )

bot.run(API_KEY)
