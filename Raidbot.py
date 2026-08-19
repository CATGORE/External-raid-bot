import discord
from discord import app_commands

class BotClient(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()
        pass

client = BotClient()

@client.tree.command(name="say")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def say(interaction: discord.Interaction, message: str):
    await interaction.response.send_message(".", ephemeral=True)
    await interaction.followup.send(message, ephemeral=False)


@client.tree.command(name="spam")
@app_commands.allowed_installs(guilds=True, users=True)
@app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
async def fl00d(interaction: discord.Interaction, message: str):
    await interaction.response.send_message(".", ephemeral=True)
    for _ in range(5):
        await interaction.followup.send(message, ephemeral=False)


client.run("")
