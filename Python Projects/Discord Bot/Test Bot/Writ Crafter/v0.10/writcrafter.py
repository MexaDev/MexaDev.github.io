import discord
from discord.ext import commands
import discord.ui
from discord.ui import View, Button, Select

BOT_TOKEN = "MTI2NTcyNjA4NzcyODU5NTAyNQ.GW4i4d.8AtSxs98zZxye_B6zOhLDc0dbLRDZ7T9-R95bE"
CHANNEL_ID = 1265711359736287263
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Hello, Test bot is ready!")
    channel = bot.get_channel(CHANNEL_ID)
    # await channel.send("Hello, Test bot is ready!")

@bot.command()
async def check(ctx):
    await ctx.send(f"Crafting bot is ready to go!")

@bot.command()
async def info(ctx):
    await ctx.send(f"```Here will be a possible list of commands.\n/info For all commands.\n/writ To open a crafting writ.\n/report To report bugs to the developer.```")

@bot.command()
async def writ(ctx):
    await ctx.send(f"Writ crafting system is work in progress.")

@bot.command()
async def report(ctx):
    await ctx.send(f"Bug reporting is work in progress")

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Help", description="Shows all bot commands replacing the info function.", color=0x6B4E90)
    embed.add_field(name="/info", value="Gives basic info regarding the bot, it's features and development.", inline=False)
    embed.add_field(name="/writ", value="Command to start this crafting writ ticket system.(WIP)", inline=False)
    embed.add_field(name="/report", value="Please use this option to report bugs and submit suggestions.", inline=False)
    embed.set_footer(text="Made by Semper")
    await ctx.send(embed=embed)

# Remember to create "Crafters" role on discord and assign to crafters
async def ticketcallback(interaction):
    guild = interaction.guild
    role = discord.utils.get(guild.roles, name="Crafters")
    role2 = discord.utils.get(guild.roles, name="Dev")
    overwrites = {
        guild.default_role : discord.PermissionOverwrite(view_channel=False),
        interaction.user : discord.PermissionOverwrite(view_channel=True),
        role : discord.PermissionOverwrite(view_channel=True),
        role2 : discord.PermissionOverwrite(view_channel=True)
    }

    select = Select(options=[
        discord.SelectOption(label="Crafting Writ", value="01", emoji="✔️", description="This will open a crafting ticket."),
        discord.SelectOption(label="Bug Report", value="02", emoji="❌", description="Use this to report bugs with the ticket bot."),
    ])

    async def my_callback(interaction):
        if select.values[0] == "01":
            category = discord.utils.get(guild.categories, name="Crafting Writs")
            channel = await interaction.guild.create_text_channel(f"{interaction.user.name}-writ", category=category, overwrites=overwrites)
            await interaction.response.send_message(f"Created a crafting writ - <#{channel.id}>", ephemeral=True)
            # await interaction.response.send_message(f"Created a crafting writ", ephemeral=True)
            await channel.send(f"Hi {interaction.user.name} what sets would you like to have crafted?")
        elif select.values[0] == "02":
            category = discord.utils.get(guild.categories, name="Bugs Reports")
            channel = await interaction.guild.create_text_channel(f"{interaction.user.name}-report", category=category, overwrites=overwrites)
            await interaction.response.send_message(f"Created bug report - <#{channel.id}>", ephemeral=True)
            # await interaction.response.send_message(f"Created bug report", ephemeral=True)
            await channel.send(f"Hi {interaction.user.name} what bug would you like to report, please supply as much info as possible.?")


    select.callback = my_callback
    view = View(timeout=None)
    view.add_item(select)
    await interaction.response.send_message("Choose an option below", view=view, ephemeral=True)

@bot.command()
async def ticket(ctx):
    button = Button(label="📥 Create Ticket", style=discord.ButtonStyle.green)
    button.callback = ticketcallback
    view = View(timeout=None)
    view.add_item(button)
    await ctx.send("Open a crafting writ or bug report below.", view=view, embed=embed)

bot.run(BOT_TOKEN)