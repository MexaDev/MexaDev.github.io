import discord
from discord.ext.commands import Bot
from discord import app_commands, utils
# BOT_TOKEN = "MTI2NTcyNjA4NzcyODU5NTAyNQ.GYCo1s.TMEH88EHI_5yE064DEjsYGJ82VuwisL1zjdFFY"
CHANNEL_ID = 1265711359736287263

class ticket_launcher(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout = None)

    @discord.ui.button(label = "Create a Crafting Writ", style = discord.ButtonStyle.blurple, custom_id = "ticket_button")
    async def ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
        ticket = utils.get(interaction.guild.text_channels, name = f"crafting-writ-for-{interaction.user.name}-{interaction.user.discrimination}")
        if ticket is not None: await interaction.response.send_message(f"You already have a crafting writ open at {ticket.mention}!", ephemeral = True)
        else:
            overwrites = {
                interaction.guild.default_role: discord.PersmissionOverwrite(view_channel = False),
                interaction.user: discord.PermissionOverwrite(view_channel = True, send_messages = True, attach_files = True, embed_links = True),
                interaction.guild.me: discord.PermissionOverwrite(view_channel = True, send_messages = True, read_message_history = True)
            }
            channel = await interaction.guild.create_text_channel(name = f"crafting-writ-for-{interaction.user.name}-{interaction.user.discriminator}", overwrites = overwrites, reason = f"Crafting Writ for {interaction.user}")
            await channel.send(f"{interaction.user.mention} created a crafting writ!")
            await interaction.response.send_message(f"Crafting writ created for you at {channel.mention}!", ephemeral = True)

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False #Used so bot doesn't sync commands more than once

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            #await tree.sync(guild = discord.Object(id = 1265690502947147827))
            self.synced = True
        if not self.added:
            self.add_view(ticket_launcher())
            self.added = True
        print(f"We have logged in as {self.user}.")

client = aclient()
tree = app_commands.CommandTree(client)

#@tree.command(name = "test", description = "testing", guild = discord.Object(id = 1265690502947147827))
@tree.command(name = "test", description = "Crafting Writ")
async def ticketing(interaction: discord.Interaction):
    embed = discord.Embed(title = "if you need to have a Gearset crafted, click th button below and create a crafting writ!", color = discord.Color.blue())
    await interaction.channel.send(embed = embed, view = ticket_launcher())
    await interaction.response.send_message(f"Crafting writ opened!", ephemeral = True)



client.run(BOT_TOKEN)
