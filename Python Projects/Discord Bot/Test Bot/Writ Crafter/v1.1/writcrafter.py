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
    print("Writ crafter is ready to go!")
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
async def craftingcallback(interaction):
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
        discord.SelectOption(label="Crafting Writ", value="01", emoji="🔨", description="This will open a crafting writ."),
        discord.SelectOption(label="Enchantment Writ", value="02", emoji="✨", description="This will create an enchantment writ."),
        discord.SelectOption(label="Provisioning Writ", value="03", emoji="🍗", description="This will create an provision writ."),
        discord.SelectOption(label="Bug Report", value="04", emoji="❌", description="Use this to report bugs with the ticket bot."),
    ])

    async def my_callback(interaction):
        if select.values[0] == "01":
            category = discord.utils.get(guild.categories, name="Crafting Writs")
            channel = await interaction.guild.create_text_channel(f"{interaction.user.name}-writ", category=category, overwrites=overwrites)
            await interaction.response.send_message(f"Created a crafting writ - <#{channel.id}>", ephemeral=True)
            # await interaction.response.send_message(f"Created a crafting writ", ephemeral=True)
            await channel.send(f"Hi {interaction.user.name} what sets would you like to have crafted?")
            await channel.send(f"Please consult link on which set you'd like to have crafted..")
            await channel.send(f"https://eso-sets.com/sets/type/craftable")
            await channel.send("Please note all gear will only be crafted at *Superior (Blue)* Quality.")
            await channel.send(f"For higher quality crafting, please request it directly from the appointed Guild Crafter and supply them with the appropriate mats.")
        elif select.values[0] == "02":
            category = discord.utils.get(guild.categories, name="Crafting Writs")
            channel = await interaction.guild.create_text_channel(f"{interaction.user.name}-enchantment", category=category, overwrites=overwrites)
            await interaction.response.send_message(f"Created a enchantment writ - <#{channel.id}>", ephemeral=True)
            # await interaction.response.send_message(f"Created a crafting writ", ephemeral=True)
            await channel.send(f"Hi {interaction.user.name} which enchantments do you need?")
            await channel.send("Please note all gear will only be crafted at *Superior (Blue)* Quality.")
            await channel.send(f"For higher quality crafting, please request it directly from the appointed Guild Crafter and supply them with the appropriate mats.")
        elif select.values[0] == "03":
            category = discord.utils.get(guild.categories, name="Crafting Writs")
            channel = await interaction.guild.create_text_channel(f"{interaction.user.name}-provision", category=category, overwrites=overwrites)
            await interaction.response.send_message(f"Created a provision writ - <#{channel.id}>", ephemeral=True)
            # await interaction.response.send_message(f"Created a crafting writ", ephemeral=True)
            await channel.send(f"Hi {interaction.user.name} which provisions do you need?")
            await channel.send("Please note all gear will only be crafted at *Superior (Blue)* Quality.")
            await channel.send(f"For higher quality crafting, please request it directly from the appointed Guild Crafter and supply them with the appropriate mats.")
        elif select.values[0] == "04":
            category = discord.utils.get(guild.categories, name="Crafting Writs")
            channel = await interaction.guild.create_text_channel(f"{interaction.user.name}-alchemy", category=category, overwrites=overwrites)
            await interaction.response.send_message(f"Created a alchemy writ - <#{channel.id}>", ephemeral=True)
            # await interaction.response.send_message(f"Created a crafting writ", ephemeral=True)
            await channel.send(f"Hi {interaction.user.name} which potions/poisens do you need?")
            await channel.send("Please note all gear will only be crafted at *Superior (Blue)* Quality.")
            await channel.send(f"For higher quality crafting, please request it directly from the appointed Guild Crafter and supply them with the appropriate mats.")
        elif select.values[0] == "05":
            category = discord.utils.get(guild.categories, name="Bugs Reports")
            channel = await interaction.guild.create_text_channel(f"{interaction.user.name}-report", category=category, overwrites=overwrites)
            await interaction.response.send_message(f"Created bug report - <#{channel.id}>", ephemeral=True)
            # await interaction.response.send_message(f"Created bug report", ephemeral=True)
            await channel.send(f"Hi {interaction.user.name} what bug would you like to report or do you have suggestions?")
            await channel.send(f"Any and all suggestions and reports are appreciated.")


    select.callback = my_callback
    view = View(timeout=None)
    view.add_item(select)
    await interaction.response.send_message("Choose an option below", view=view, ephemeral=True)

async def farmingcallback(interaction):
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
        discord.SelectOption(label="Work In Progress", value="01", emoji="🔨", description="This will open a crafting writ.", disabled=True),
        discord.SelectOption(label="Work In Progress", value="02", emoji="✨", description="This will create an enchantment writ.", disabled=True),
        discord.SelectOption(label="Work In Progress", value="03", emoji="🍗", description="This will create an provision writ.", disabled=True),
        discord.SelectOption(label="Bug Report", value="04", emoji="❌", description="Use this to report bugs with the ticket bot.", disabled=True),
    ])

    async def my_callback(interaction):
        if select.values[0] == "01":
            category = discord.utils.get(guild.categories, name="Crafting Writs")
            channel = await interaction.guild.create_text_channel(f"{interaction.user.name}-writ", category=category, overwrites=overwrites)
            await interaction.response.send_message(f"Created a crafting writ - <#{channel.id}>", ephemeral=True)
            # await interaction.response.send_message(f"Created a crafting writ", ephemeral=True)
            await channel.send(f"Hi {interaction.user.name} what sets would you like to have crafted?")
            await channel.send(f"Please consult link on which set you'd like to have crafted..")
            await channel.send(f"https://eso-sets.com/sets/type/craftable")
            await channel.send("Please note all gear will only be crafted at *Superior (Blue)* Quality.")
            await channel.send(f"For higher quality crafting, please request it directly from the appointed Guild Crafter and supply them with the appropriate mats.")
        elif select.values[0] == "02":
            category = discord.utils.get(guild.categories, name="Crafting Writs")
            channel = await interaction.guild.create_text_channel(f"{interaction.user.name}-enchantment", category=category, overwrites=overwrites)
            await interaction.response.send_message(f"Created a enchantment writ - <#{channel.id}>", ephemeral=True)
            # await interaction.response.send_message(f"Created a crafting writ", ephemeral=True)
            await channel.send(f"Hi {interaction.user.name} which enchantments do you need?")
            await channel.send("Please note all gear will only be crafted at *Superior (Blue)* Quality.")
            await channel.send(f"For higher quality crafting, please request it directly from the appointed Guild Crafter and supply them with the appropriate mats.")
        elif select.values[0] == "03":
            category = discord.utils.get(guild.categories, name="Crafting Writs")
            channel = await interaction.guild.create_text_channel(f"{interaction.user.name}-provision", category=category, overwrites=overwrites)
            await interaction.response.send_message(f"Created a provision writ - <#{channel.id}>", ephemeral=True)
            # await interaction.response.send_message(f"Created a crafting writ", ephemeral=True)
            await channel.send(f"Hi {interaction.user.name} which provisions do you need?")
            await channel.send("Please note all gear will only be crafted at *Superior (Blue)* Quality.")
            await channel.send(f"For higher quality crafting, please request it directly from the appointed Guild Crafter and supply them with the appropriate mats.")
        elif select.values[0] == "04":
            category = discord.utils.get(guild.categories, name="Crafting Writs")
            channel = await interaction.guild.create_text_channel(f"{interaction.user.name}-alchemy", category=category, overwrites=overwrites)
            await interaction.response.send_message(f"Created a alchemy writ - <#{channel.id}>", ephemeral=True)
            # await interaction.response.send_message(f"Created a crafting writ", ephemeral=True)
            await channel.send(f"Hi {interaction.user.name} which potions/poisens do you need?")
            await channel.send("Please note all gear will only be crafted at *Superior (Blue)* Quality.")
            await channel.send(f"For higher quality crafting, please request it directly from the appointed Guild Crafter and supply them with the appropriate mats.")
        elif select.values[0] == "05":
            category = discord.utils.get(guild.categories, name="Bugs Reports")
            channel = await interaction.guild.create_text_channel(f"{interaction.user.name}-report", category=category, overwrites=overwrites)
            await interaction.response.send_message(f"Created bug report - <#{channel.id}>", ephemeral=True)
            # await interaction.response.send_message(f"Created bug report", ephemeral=True)
            await channel.send(f"Hi {interaction.user.name} what bug would you like to report or do you have suggestions?")
            await channel.send(f"Any and all suggestions and reports are appreciated.")


    select.callback = my_callback
    view = View(timeout=None)
    view.add_item(select)
    await interaction.response.send_message("Choose an option below", view=view, ephemeral=True)

@bot.command()
async def ticket(ctx):
    button1 = Button(label="🔨Crafting Writs", style=discord.ButtonStyle.green)
    button2 = Button(label="📥 Reserved", style=discord.ButtonStyle.grey, disabled=True)
    button3 = Button(label="📥 Reserved", style=discord.ButtonStyle.grey, disabled=True)
    button1.callback = craftingcallback
    button2.callback = farmingcallback
    # button3.callback = ticketcallback
    view = View(timeout=None)
    view.add_item(button1)
    view.add_item(button2)
    # view.add_item(button3)
    await ctx.send("**\nGraaf Gesigte Gemeenskap Paneel\n\n**", view=view)

bot.run(BOT_TOKEN)