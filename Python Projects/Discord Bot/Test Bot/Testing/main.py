import discord
from discord.ext import commands
import discord.ui
from discord.ui import View, Button, Select

BOT_TOKEN = ""

CHANNEL_ID = 1265711359736287263
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Trader bot loaded successfully")
    channel = bot.get_channel(CHANNEL_ID)
    # await channel.send("Hello, Test bot is ready!")

@bot.command()
async def check(ctx):
    await ctx.send(f"Trader is online!")


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
        discord.SelectOption(label="Weapons", value="01", emoji="⚔️", description="Select the Weapons category."),
        discord.SelectOption(label="Apparel", value="02", emoji="🛡️", description="Select the Apparel category."),
        discord.SelectOption(label="Jewelry", value="03", emoji="💍", description="Select the Jewelry category."),
        discord.SelectOption(label="Consumables", value="04", emoji="🍗", description="Select the Consumables category."),
        discord.SelectOption(label="Materials", value="05", emoji="💎", description="Category for all enchanting & crafting materials."),
        discord.SelectOption(label="Glyphs", value="06", emoji="✨", description="Select the Glyphs category."),
        discord.SelectOption(label="Furnishings", value="07", emoji="🛋️", description="Select the Furnishings category."),
        discord.SelectOption(label="Companion Equipment", value="08", emoji="⚔️", description="Select the Companion Equipment category."),
        discord.SelectOption(label="Miscellaneous", value="09", emoji="🔮", description="Select the Miscellaneous category."),
        discord.SelectOption(label="Motifs", value="10", emoji="📖", description="Select the Motifs category."),
    ])

    async def trader_listing_callback(interaction):
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
        elif select.values[0] == "03":
            category = discord.utils.get(guild.categories, name="Crafting Writs")
            channel = await interaction.guild.create_text_channel(f"{interaction.user.name}-writ", category=category, overwrites=overwrites)
            await interaction.response.send_message(f"Created a crafting writ - <#{channel.id}>", ephemeral=True)
            # await interaction.response.send_message(f"Created a crafting writ", ephemeral=True)
            await channel.send(f"Hi {interaction.user.name} what sets would you like to have crafted?")
        elif select.values[0] == "04":
            category = discord.utils.get(guild.categories, name="Bugs Reports")
            channel = await interaction.guild.create_text_channel(f"{interaction.user.name}-report", category=category, overwrites=overwrites)
            await interaction.response.send_message(f"Created bug report - <#{channel.id}>", ephemeral=True)
            # await interaction.response.send_message(f"Created bug report", ephemeral=True)
            await channel.send(f"Hi {interaction.user.name} what bug would you like to report, please supply as much info as possible.?")
        elif select.values[0] == "05":
            category = discord.utils.get(guild.categories, name="Crafting Writs")
            channel = await interaction.guild.create_text_channel(f"{interaction.user.name}-writ", category=category, overwrites=overwrites)
            await interaction.response.send_message(f"Created a crafting writ - <#{channel.id}>", ephemeral=True)
            # await interaction.response.send_message(f"Created a crafting writ", ephemeral=True)
            await channel.send(f"Hi {interaction.user.name} what sets would you like to have crafted?")
        elif select.values[0] == "06":
            category = discord.utils.get(guild.categories, name="Bugs Reports")
            channel = await interaction.guild.create_text_channel(f"{interaction.user.name}-report", category=category, overwrites=overwrites)
            await interaction.response.send_message(f"Created bug report - <#{channel.id}>", ephemeral=True)
            # await interaction.response.send_message(f"Created bug report", ephemeral=True)
            await channel.send(f"Hi {interaction.user.name} what bug would you like to report, please supply as much info as possible.?")
        elif select.values[0] == "07":
            category = discord.utils.get(guild.categories, name="Crafting Writs")
            channel = await interaction.guild.create_text_channel(f"{interaction.user.name}-writ", category=category, overwrites=overwrites)
            await interaction.response.send_message(f"Created a crafting writ - <#{channel.id}>", ephemeral=True)
            # await interaction.response.send_message(f"Created a crafting writ", ephemeral=True)
            await channel.send(f"Hi {interaction.user.name} what sets would you like to have crafted?")
        elif select.values[0] == "08":
            category = discord.utils.get(guild.categories, name="Bugs Reports")
            channel = await interaction.guild.create_text_channel(f"{interaction.user.name}-report", category=category, overwrites=overwrites)
            await interaction.response.send_message(f"Created bug report - <#{channel.id}>", ephemeral=True)
            # await interaction.response.send_message(f"Created bug report", ephemeral=True)
            await channel.send(f"Hi {interaction.user.name} what bug would you like to report, please supply as much info as possible.?")
        elif select.values[0] == "09":
            category = discord.utils.get(guild.categories, name="Crafting Writs")
            channel = await interaction.guild.create_text_channel(f"{interaction.user.name}-writ", category=category, overwrites=overwrites)
            await interaction.response.send_message(f"Created a crafting writ - <#{channel.id}>", ephemeral=True)
            # await interaction.response.send_message(f"Created a crafting writ", ephemeral=True)
            await channel.send(f"Hi {interaction.user.name} what sets would you like to have crafted?")
        elif select.values[0] == "10":
            category = discord.utils.get(guild.categories, name="Bugs Reports")
            channel = await interaction.guild.create_text_channel(f"{interaction.user.name}-report", category=category, overwrites=overwrites)
            await interaction.response.send_message(f"Created bug report - <#{channel.id}>", ephemeral=True)
            # await interaction.response.send_message(f"Created bug report", ephemeral=True)
            await channel.send(f"Hi {interaction.user.name} what bug would you like to report, please supply as much info as possible.?")


    select.callback = trader_listing_callback
    view = View(timeout=None)
    view.add_item(select)
    await interaction.response.send_message("Select yout", view=view, ephemeral=True)

@bot.command()
async def ticket(ctx):
    button = Button(label="📥 Create Ticket", style=discord.ButtonStyle.green)
    button.callback = ticketcallback
    view = View(timeout=None)
    view.add_item(button)
    await ctx.send("Open a crafting writ or bug report below.", view=view)

# Trading Bot
# # Listing Template
    # Username (Automate)
        # user_id
    # Item Category
        # category_id
    # Item Name
        # item_id
    # Item Quantity
        # quantity_id
    # Payment
        # payment_id
# Commands
    # Show all Listings
    # Search Listing
    # Create Listing
bot.run(BOT_TOKEN)